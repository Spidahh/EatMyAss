# G0 — Audit statico HordeTemplate (25 ottobre 2026)

**Stato: PARTIAL / STATIC SOURCE INSPECTION ONLY.** Non è stato eseguito Unreal Engine né compilata una build, quindi **G0 NON SUPERATO**. Fonte upstream: [DasBander/HordeTemplate](https://github.com/DasBander/HordeTemplate), branch `master`, repository aggiornato a settembre 2026 al momento del controllo. Questa è una verifica del codice remoto, non un test runtime. L'adozione e la redistribuzione dei contenuti sono sospese.

## Evidenze reali esaminate

- Repository upstream: [albero sorgente](https://github.com/DasBander/HordeTemplate/tree/master/Source/HordeTemplateV2Native), file `HordeTemplateV2Native.uproject` con `EngineAssociation: "5.8"`. Dichiarazione autore, **non build confermata**.
- Inventario remoto: **127 file .cpp/.h**, **374 .uasset**, circa **520 file** totali rilevati nell'albero; nessun archivio di contenuti trasferito nel nostro repository.
- `Source/HordeTemplateV2Native/HordeTemplateV2Native.Build.cs` dichiara AI, NavigationSystem, OnlineSubsystem, UMG, EngineCameras e moduli Steam/Null. `.uproject` abilita `OnlineSubsystemSteam` **e** `OnlineSubsystemNull`: testare sessione LAN senza Steam e configurazione effettivamente selezionata prima di adottare rete.
- `Private/Gameplay/HordeGameState.cpp`: `StartGameRound()` invoca `InitiateZombieSpawning(GameRound * ZedMultiplier)`; `ProcessRoundTime()` conclude per timer. **L'attuale fine-round non coincide necessariamente col requisito “elimina l'intera ondata”**.
- `Private/Gameplay/HordeGameMode.cpp`: `InitiateZombieSpawning` usa `AAISpawnPoint`; un secondo percorso di generazione è presente in `Private/AI/ZedSpawner.cpp` (`AZedSpawner` con mode Continuous/Wave/Triggered e attivazione prossimità). **Rischio due sistemi paralleli non coordinati**. Non usarli entrambi in produzione senza director unico.
- `Private/AI/ZedPawn.cpp`: `TakeDamage()` gestisce point/radial; `KillAI(ACharacter* Killer,...)` assegna punti al player via `GivePlayerPoints`. Per i danni letali da arma automatica/torretta l'attribuzione e la morte vanno analizzate e disaccoppiate dall'obbligo del player come causer. In particolare, in `TakeDamage()`, dopo `Health<=0`, `KillAI` è chiamata solo se `DamageCauser` può essere convertito a `ACharacter`: **potenziale zombie a 0 HP non morto con torretta**, da riprodurre prima di patch.
- `Private/AI/ZedPawn.cpp`: headshot `BoneName == "head"` uccide istantaneamente. Incompatibile come default con boss/corazzati e sistemi HP diversi; servono danni per archetipi e weakpoints configurabili.
- `Private/Gameplay/HordePlayerState.cpp`: `AddPoints` aumenta `Points` replicati; non equivale automaticamente al nostro ledger atomico di crediti personali + fondi difesa. RPC autorizzazione di spesa da implementare e testare.
- File `LICENSE.md` upstream contiene testo MIT con copyright Marc Fraedrich. **Separare diritti sul codice da provenienza dei 374 .uasset**: la presenza di un file MIT non prova da sola licenze/ownership delle singole risorse create da terzi.
- `Content/HordeTemplateBP/Assets/Mannequin/` e `Content/HordeTemplateBP/Assets/Sounds/` contengono risorse usate con path hardcoded in codice; la sostituzione artistica richiederà wrapper/soft refs e una validazione del cook.

## Matrice del riuso e compatibilità con il nostro GDD

| Sistema upstream | Prova da codice | Scelta progettuale | Priorità |
| --- | --- | --- | --- |
| Co-op, lobby, game/player state | classi C++ reali e moduli rete | **Candidato riuso**, T-003/T-501 mancanti | P0 |
| Armi, inventory | `BaseFirearm`, `InventoryComponent`, `Weapon_HM5` | **Candidato riuso**, test reload/mira/authority | P0 |
| Zombie AI | `ZedPawn`, `ZedAIController`, BT tasks | **Adattamento richiesto** per target strutture e danni torrette | P0 |
| OnDate, due spawner | `HordeGameState`, `HordeGameMode`, `ZedSpawner` | **Da riconciliare**, director unico basato su budget | P0 |
| Crediti | `HordePlayerState::AddPoints` | **Da estendere** con transazioni atomiche e fondi team | P0 |
| Difese torretta/barricata | nessun modulo dedicato nel tree Source | **Nuovo codice ZD** | P0 |
| Nucleo e sconfitta | nessuna classe `BaseCore` nel tree Source | **Nuovo actor ZD** | P0 |
| Settori acquistabili | `Door` e `SafeZoneDoor` esistono | **Riusare porte se sicure**, aggiungere `SectorManager` | P1 |
| Abilità delle classi | classi personaggio esistenti | **Contratto custom**, no promessa GAS upstream | P1 |

## Rischi e ticket mirati

1. **ZD-G0-01 BUILD:** procurare Unreal 5.8 + Windows SDK + Visual Studio C++ compatibili; clone in sandbox con commit hash fissato; compilare `Development Editor Win64` e package Windows. Registrare log e exit code. NON eseguito.
2. **ZD-G0-02 MULTIPLAYER:** due processi host/client, LAN con Null OSS, poi Steam solo se necessario; verificare HP, ammo, kill, round, trade/points. NON eseguito.
3. **ZD-G0-03 LICENSE:** inventario asset 374 .uasset per categorie e provenienza, verificare licenza degli asset e delle dipendenze Epic/Marketplace. Senza approvazione, NO-GO per trasferimento contenuti. NON eseguito.
4. **ZD-G0-04 ZOMBIE KILL:** riprodurre danno letale da `AActor` non `ACharacter`; dimostrare una morte sola e award solo per eventi idonei. Codice suggerisce criticità, **non ancora provata in editor**.
5. **ZD-G0-05 WAVE:** dimostrare modalità round corrente con numero zombie residui, timeout e doppio spawner; specificare come sostituire `RoundTime` con evento wave completion senza regressioni.
6. **ZD-G0-06 GUNPLAY:** testare ADS, reload, recoil, animazioni e audio con temp asset, confronto al GDD. NON eseguito.
7. **ZD-G0-07 MAP/AI:** in scena minima 20 zombie contro punto struttura con barriera; test nav e target se scegliamo riuso. NON eseguito.

## Criterio di decisione

- **GO:** G0-01/02/03/04/05 superati e difetti riparabili in tempi stimati; usare framework come baseline.
- **PATCH:** engine avviabile/licenze pulite ma bug confinati; fare spike sul danno delle torrette e onde prima dell'import grafico.
- **NO-GO:** diritti asset non dimostrabili oppure compile/networking non sostenibili; preservare audit e valutare Lyra senza copiare assets.

**Decisione odierna: HOLD / PROCEED WITH ISOLATED TEST.** Non incorporare ora HordeTemplate nel repository pubblico e non marcarlo compatibile con il gioco. Il primo ticket pratico è ZD-G0-01, in parallelo con verifica diritti G0-03.

## Comandi guida per ambiente Windows (da adattare ai percorsi reali)

```powershell
git clone https://github.com/DasBander/HordeTemplate.git HordeTemplate-Audit
cd HordeTemplate-Audit
git rev-parse HEAD
# Aprire HordeTemplateV2Native.uproject con Unreal 5.8 e generare i file VS.
# Compilare Development Editor Win64 dal toolchain Visual Studio installato.
# Salvare log reali e versione esatta del motore in docs/evidence/G0/.
```

**Riferimenti al codice:** [GameState](https://github.com/DasBander/HordeTemplate/blob/master/Source/HordeTemplateV2Native/Private/Gameplay/HordeGameState.cpp), [GameMode](https://github.com/DasBander/HordeTemplate/blob/master/Source/HordeTemplateV2Native/Private/Gameplay/HordeGameMode.cpp), [ZedPawn](https://github.com/DasBander/HordeTemplate/blob/master/Source/HordeTemplateV2Native/Private/AI/ZedPawn.cpp), [ZedSpawner](https://github.com/DasBander/HordeTemplate/blob/master/Source/HordeTemplateV2Native/Private/AI/ZedSpawner.cpp), [PlayerState](https://github.com/DasBander/HordeTemplate/blob/master/Source/HordeTemplateV2Native/Private/Gameplay/HordePlayerState.cpp), [Project](https://github.com/DasBander/HordeTemplate/blob/master/HordeTemplateV2Native.uproject), [License](https://github.com/DasBander/HordeTemplate/blob/master/LICENSE.md).
