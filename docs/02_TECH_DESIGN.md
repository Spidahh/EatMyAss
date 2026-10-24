# Technical Design Document — Unreal 5.8

**Baseline provvisoria:** il template HordeTemplate è *candidato da auditare*; gli elementi qui sotto sono l'architettura obiettivo indipendente dal template effettivamente scelto. Non creare le classi duplicate se equivalenti sono già presenti e collaudate.

## 0. Version pin, dipendenze, source control

- Unreal Engine **5.8.x pin esatto al giorno del G0**; toolchain C++ corrispondente, Enhanced Input, UMG, Niagara, Navigation System; Gameplay Ability System **solo se il progetto base lo usa già o il vantaggio misurato giustifica il costo**.
- Per la versione A adottare gli `AHordeGameMode`, `AHordeGameState`, `AZedPawn`, `AZedAIController`, `UInventoryComponent`, `UQuestManager` esistenti dove il codice reale conferma le funzioni pubblicate. Introdurre un modulo proprietario `ZD` per difese e progressione senza patchare tutto il framework originale.
- Repo Git con LFS per `.uasset`/`.umap` e altri binari voluminosi; `.gitignore` per `Binaries`, `Intermediate`, `DerivedDataCache`, `Saved` salvo file di configurazione richiesti. Conservare ricevute/licenze asset in `Docs/Licenses` senza redistribuire asset sorgenti pubblicamente. Backup frequenti.
- Branch `main` sempre compilabile; feature branch brevi, PR/checklist, tag di vertical slice. Nessun engine upgrade a metà milestone.

## 1. Confronto fra basi di progetto

| Candidato | Già presente secondo documentazione pubblica | Manca per il concept | Rischio |
| --- | --- | --- | --- |
| [HordeTemplate](https://github.com/DasBander/HordeTemplate) | zombie AI, ondate, coop 4p, shooting/inventory, trader, lobby, quest; MIT del codice | build socket, torrette, energia Nucleo, sector unlock, skill classi | qualità effettiva non testata, asset inclusi non ancora licenziati uno per uno, API/integrazione |
| [Lyra](https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine) | multiplayer, weapon/equipment, abilità, feature, UI | AI zombie e director, economia, costruzione, mondo | curva di apprendimento e modularità complessa |
| [First Person Arena Shooter](https://dev.epicgames.com/documentation/unreal-engine/first-person-template-in-unreal-engine) | 3 armi sample, IA, HUD e FPS prototype | robustezza rete, wave/coop, sistemi TD | creare multiplayer a valle costa molto |

**Regola selezione (G0):** compilazione pulita 5.8, prova host+client, nessun asset senza licenza, velocità gunplay sufficiente, extension points chiari, nessun blocco su blueprint corrotti. Se fallisce A, non iniziare 3 fork in parallelo; selezionare B e aggiornare questo TDD.

## 2. Ownership e replicated state

| Stato/funzione | Proprietario server | Replicazione UI/client | Invariante |
| --- | --- | --- | --- |
| fase e contatore ondata, nemici residui, settori attivi | `GameMode` / Wave Director | `GameState` | non modificabili dal client |
| crediti personali, loadout, cooldown | `PlayerState` + abilità/inventory | owner/all when needed | anti-double-spend e server validates |
| fondi squadra, HP Nucleo, energia, level base | `GameState` + BaseCore actor | to all | una sola fonte di verità |
| difese acquistate e tier | `DefenseManager` server + replicated actors | rilevanti vicini | un socket = un device |
| HP zombie e risultato colpi | server Zombie Character | health/hit cues/anim state | il client non decide uccisioni |
| effetti grafici, audio locali | client dopo evento validato | eventi sintetici | non replicare Niagara per ogni particella |

Per partire usare la replication esistente di UE/template. Non scegliere Iris/Replication Graph per sentito dire. Epic documenta la necessità di pianificare presto il multiplayer: https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine

## 3. Moduli di gameplay (contratti piccoli)

### 3.1 `WaveDirector`

Input: `WaveDataAsset`, numero giocatori vivi, settori aperti, metriche ultime due ondate. Output: spawn commands verso `SpawnPointRegistry`, `WaveStarted`, `WaveCleared`, `WaveFailed`.

- Fasi enum: `Lobby`, `Prep`, `Spawning`, `Combat`, `Cleanup`, `Rewards`, `Completed`, `Failed`.
- Solo il server cambia fase. Lo spawn è limitato dal cap attivo; mantenere una coda con retry se slot/spawn invalidi, loggare timeout. *Nessun* timer come surrogato degli zombie rimasti.
- Preventiva regola anti-stallo: se un nemico vive ma non avanza da N secondi, ripath/telegraph/despawn con **nessuna ricompensa duplicata** e log; soglia da prova.
- Evento `WaveCleared` idempotente, una sola erogazione di ricompensa per wave ID.

### 3.2 `Damage/WeaponBridge`

Usare shooting del template quando regge; esporre `ApplyValidatedDamage(DamageContext)` con `Instigator`, `WeaponId`, `DamageType`, `HitBone`, `Distance`, `Damage`, `TxnId`. Il server ha authority sulle risorse e sui colpi; il cliente può predire VFX/hitmarker senza concedere doppio danno. Mitigazione contro RPC rapid fire con fire cadence/ammo server-side.

Interfaccia damageable per player, zombies, torri e Nucleo (resistenze differenti). VFX indirizzati da `SurfaceType`/tag (`Flesh`, `Metal`, `Stone`) e grado reazione, non da asset singoli hardcoded.

### 3.3 `DefenseManager` e `BuildSocket`

`FDefenseSpec` = `DefenseId`, `Cost`, `AllowedSocketTypes`, `TierSpecs`, `TargetPolicy`, `PowerCost`, `TeamCap`, `MeshVariant`, `AudioCue`, `EffectTags`.

`ServerRequestBuild(SocketId, DefenseId, ClientRequestId)` esegue atomicamente: validità fase → socket libero/area sbloccata → cap → fondi → spawn → affiliazione/energia → addebito → replicate. Se spawn fallisce non addebita; richieste duplicate con stesso ID ricevono lo stesso esito senza pagare due volte. Miglioramenti/riparazioni replicano tier e HP. Non lasciare che un client istanzi torri autorevoli.

Torretta: scansione target a intervallo da test (non Tick per torre+nemico), punteggio bersaglio, controllo LoS, limite rotazione, cooldown, applicazione danno server, FX/anim lato client. Offscreen ottimizzare senza alterare simulazione.

### 3.4 `BaseCore`

Un actor replicated con `MaxHP`, `HP`, `Tier`, `PowerCapacity`, `PowerUsage`, `DamagedState`. Trigger `OnCoreHPChanged`, `OnTierChanged`, `OnPowerBrownout`, `OnCoreDestroyed`. Visual mesh swaps/material instance separati dal dato. **Energia** inizialmente solo capacità di dispositivi, non terza valuta accumulata.

### 3.5 `SectorManager`

`FSectorDefinition` con `SectorID`, `Cost`, `MinWave`, `PrerequisiteIDs`, `UnlockObjectives`, `OpenedSpawnGroups`, `NewSocketIDs`, `LinkedDoors`, `ArtState`. `ServerRequestOpenSector()` verifica tutti i requisiti e transazione fondi; poi attiva geometria/porte, marker, nav links e solo alla prossima ondata set di spawn. Non trasformare la partita in un intero open world.

Per piccole mappe preferire level layout statico con cancelli e set di actors attivati. Data Layers/Level Instances possono essere introdotti se necessario *dopo* un test networking/streaming, secondo documentazione UE: https://dev.epicgames.com/documentation/unreal-engine/world-partition---data-layers-in-unreal-engine

### 3.6 `ClassAbility` / `Perks`

`UClassDefinition` Data Asset con HP, passive tags, active ability, cooldown, UI icon, VFX/SFX; ogni ability ha requisiti, consumo, replicazione e cancellation. Se HordeTemplate non usa GAS, una classe con `UActorComponent` + DataAssets è più piccola di migrare tutto a GAS. Se si sceglie Lyra, usare ability set/GAS nativo, non un secondo sistema parallelo.

### 3.7 Economy + Rewards

Transazioni server con `TxnId`, `PlayerId`, `Type`, `Delta`, `BalanceBefore/After`, `WaveId`, `ItemId`, `Timestamp`. Distinguere personali/team, separare grant e spend. Trasferimento opzionale crediti→fondi come transazione atomica. Evitare che kill XP venga assegnata due volte ai partecipanti del danno; assist credit calcolato con ring buffer per zombie oppure contributo per damage non duplicato.

### 3.8 Save/Session

Per MVP: checkpoint tra ondate solo **single-player** per opzioni/progressione, e per co-op evitare riconnessione tardiva finché non testata; nessun cloud o account. Salva schema versione, seed/runID, wave completata, classi, strutture/tier/socketID, HP core, aree aperte, risorse. In V1 co-op ripristino sessione host se robusto, altrimenti nessun mid-run save con comunicazione esplicita. Niente deserializzazione arbitraria da client.

## 4. IA e navigazione dinamica

Per il vertical slice usare NavMesh UE + AI Controller/Behavior Tree esistente. Target selection con service/evento, Attack telegraphed, stuck recovery. Barricate e porte devono poter influenzare costo/percorso solo se il navmode scelto lo consente. La documentazione UE offre `Static`, `Dynamic` e `Dynamic Modifiers Only`; la rigenerazione indiscriminata è costosa: https://dev.epicgames.com/documentation/unreal-engine/overview-of-how-to-modify-the-navigation-mesh-in-unreal-engine

**Strategia economica:** costruzione solo su socket già previsti nella mappa; corridoi di fuga e nav links disegnati a mano; `NavModifier` dove richiesto; due percorsi validi per ondata, un percorso minimo sempre raggiungibile. Un barricata sul percorso può essere bersaglio attaccabile, non un muro che spegne la nav. Alle torrette si assegnano i socket fuori dal navcorridor principale.

## 5. Performance budget iniziale da verificare

Target PC Windows non high-end: profilo qualità `Medium` su macchina reale da scegliere. **Obiettivo, non misura:** 60 fps 1080p con 2 player + 30–50 zombie attivi, 4 torri, Nucleo, VFX contenuti. Provare gradualmente 20/30/50/75 nemici. Il PC RTX 4090 serve a sviluppare, non a definire la macchina minima dei clienti.

Misure obbligatorie: game thread ms, render thread ms, GPU ms, AI/nav/ms, skeletal animation cost, RHI, draw calls, VFX cost, replicated bytes/s, RTT e packet loss. Profilare in *packaged Development build* più che PIE soltanto. Non usare Lumen/Nanite su ogni elemento senza budget; non renderizzare tutti gli zombie con tick/IK/morph completi lontani. Pooling per impatti/proiettili solo se profilo mostra il collo di bottiglia. Varietà da swap materiali/parti controllati e LOD.

## 6. Import e integrazione artistica

1. Asset acquisito con ricevuta; annotare URL, licenza, versione, file hash e formato.
2. Import in **progetto sandbox** della stessa UE, mai direttamente nel livello main.
3. Verificare scala (UE centimetri), pivot, collisioni, LOD, normals, dimensioni texture, retarget animazioni su UE5 Manny/Quinn o scheletro ufficiale usato dal template.
4. Fissare naming/canonical path e creare BP wrapper indipendente dal pack: una sostituzione grafica non deve richiedere di riscrivere AI o wave director.
5. Reimport, reference viewer, test cook/package e performance; solo allora passa da `Candidate` a `Approved`.

## 7. Struttura di progetto suggerita

```text
Source/<BaseTemplate>/                 # preserve vendored framework upstream if chosen
Source/ZDCore/                         # custom system components + interfaces
Content/ZD/Core/                      # game instance, primary configs
Content/ZD/Data/{Weapons,Enemies,Classes,Defense,Waves,Sectors}/
Content/ZD/Blueprints/{Core,AI,Defenses,Interactions}/
Content/ZD/Maps/{Blockout,VerticalSlice}/
Content/ZD/UI/
Content/ZD/Audio/
Content/ZD/VFX/
Content/ThirdParty/<PublisherPack>/   # immutable originals
Docs/{Design,LicenseReceipts,Tests,ADR}/
Tests/{Functional,Automation}/
```

Ogni pack va isolato nella propria cartella, niente editing distruttivo degli originali: creare material instance/child BP in `ZD/`.

## 8. Data schema minima (illustrativo)

```cpp
USTRUCT(BlueprintType)
struct FZDWaveDefinition {
    GENERATED_BODY()
    UPROPERTY(EditAnywhere) int32 WaveNumber = 1;
    UPROPERTY(EditAnywhere) int32 ThreatBudget = 10;
    UPROPERTY(EditAnywhere) int32 MaxAlive = 20;
    UPROPERTY(EditAnywhere) TArray<FZDEnemyWeightedEntry> EnemyWeights;
    UPROPERTY(EditAnywhere) TArray<FName> AllowedSpawnGroups;
    UPROPERTY(EditAnywhere) FName CompletionRewardId;
};
```

Non fare copy-paste di questo codice in produzione senza definire il tipo `FZDEnemyWeightedEntry`, i namespace/base del progetto e API reali dopo il G0. È **contratto di dati**, non classe compilabile.

## 9. Gate tecnici

- **G0 / base:** compile, launch, licenze, test 2p e foglio debito tecnico.
- **G1 / core:** 6 waves senza stuck, 3 armi, una torre, barricata, Nucleo, uno unlock, due player sincronizzati.
- **G2 / full loop:** tre classi, shop breve, ritorno lobby e restarts puliti, 10 waves, economie robuste.
- **G3 / quality:** lighting coerente, effetti/audio distinti, UI leggibile, 60 fps nel profilo prestabilito, nessuna regressione ad ogni integrazione asset.
- **G4 / release candidate:** packaged build, clean install, multiplayer con perdita pacchetti, changelog, diritti e save verificati.

## 10. Informazioni da non fingere di conoscere

- Non si conosce ancora il **contenuto esatto** e la provenienza di tutti i `.uasset` presenti in HordeTemplate.
- La licenza MIT del repository non prova da sola il diritto di redistribuire ogni immagine, suono o mesh di terzi incluso.
- La compatibilità con UE5.8 dichiarata dall'autore non prova compilazione nella nostra toolchain.
- Una demo di IA o turret pack **non** rappresenta una soluzione plug-and-play del nostro tower defense.
- Il target 60 fps e le stime di durata sono requisiti da provare, non risultati.

