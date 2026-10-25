# ARCHITETTURA UNREAL END-TO-END — CODICE, DATI, OWNERSHIP E INTEGRAZIONI

## Base reale vs nuove classi

**Upstream reale**: [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate), UE 5.8 dichiarato. Esistono nel repository sorgente `AHordeGameMode`, `AHordeGameState`, `AHordeBaseCharacter`, `ABaseFirearm`, `AZedPawn`, `AZedAIController`, `AZedSpawner`, `UInventoryComponent`, `AHordePlayerState`, `HordeTrader` e HUD classes. Il runtime del progetto non è ancora stato verificato. **Le classi ZD elencate di seguito NON esistono ancora e sono da implementare quando servono**. Non dichiararle esistenti in report o includerle in C++ senza creare i relativi files.

## Scelta di implementazione

Un unico framework di base. Creare namespace/prefisso `ZD` per estensioni; importare framework mantenendo notices MIT. Mettere dati in `PrimaryDataAsset` / `UDataTable` coerenti con moduli reali e config runtime in GameState. Blueprint = wiring, anim graph, UI, effect actors; C++ = invarianti, gameplay state, economia, validation/replication, AI interfaces, transaction ledger. Non creare due skill systems (GAS vs manual), due wave directors o tre inventory.

### Component map prevista (nomi CONCETTUALI)

| Sistema | Proprietario ed estensione prevista | Dati | Dipendenze |
| --- | --- | --- | --- |
| `ZDRunCoordinator` | estensione GameMode/GameState | RunRules, PhaseEnum | upstream multiplayer |
| `ZDCombatBridge` | integra `BaseFirearm` e `ZedPawn::TakeDamage` | WeaponDefs, DamageEvent | gunplay L2 |
| `ZDWaveDirector` | GameMode server, replicazione GameState | WaveDef, SpawnGroupRegistry | zombie L3 e sessione |
| `ZDEnemyDefinition` | data asset + child class existing zombie | HP, resists, AnimSet, AIProfile, Rewards | L3 e wave |
| `ZDBaseCore` | actor server replicated | HP, maxHP, power, Tier | wave |
| `ZDDefenseManager` | server manager con socket actors | DefenseDefs, tiers, sockets | Core e economy |
| `ZDEconomyLedger` | server authoritative per player/team | reward tables, costs, TransactionId | Wave/PlayerState |
| `ZDSectorManager` | server subystem o world actor | SectorDefinitions, nav, doors, spawns | map+economy |
| `ZDClassAbilityComponent` | attached player, server authoritative | ClassDefs, AbilityDefs, Cooldowns | L10 |
| `ZDProfileSave` | client settings SaveGame | config version+preferences | UI |
| `ZDPresentationRegistry` | soft refs sounds/FX/anims/material | asset manifest | every visible system |

**Non costruire la tabella intera al primo commit.** Ogni sistema nasce nel suo strato, ma aderisce ai contratti sopra per evitare riscrittura. Non introdurre complessi dependency injection/plugin non necessari.

## Ability e sinergia tra sistemi (v1.1)

**Aggiunte solo tramite componenti già necessari, non nuovo framework di abilità:**
- `PlayerAbilityComponent`: spinta V e Q classe condividono validazione server/cooldown, montage reali, determinazione del target e replicazione. Niente stamina separata.
- `GameState.TeamFocusTargetId` (nome concettuale) e `MarkedUntil`: input middle-click server trace e focus che il targeting Sentry legge se disponibile; non altera danni né LoS.
- `ZDBaseCore.ProtocolUsedWaveIndex` e `CoreProtocolChoice`: E sul pannello, server atomico, 1 uso per wave; usa il medesimo StatusSlow del campo rallentante con stacking max (non additive).
- `ZDSectorDefinition.SectorBenefit` in acquisti ammo/repair/UI; niente resource manager supplementare.
- `ZDWaveDefinition.OptionalEvent`: W7 referenzia il già esistente `Disabled` Sentry status, senza nuovo actor né aiuto obbligato dell'Ingegnere.
Dettagli completi [40](40_SYNERGIES_SKILLS_AND_CITY.md); questi nomi sono contratti architetturali, non classi upstream già esistenti.

## API/eventi condivisi

- `OnDamageResolved({VictimId,SourceType,CauserActor,InstigatorPlayerId,DamageType,BodyZone,Amount,ServerTime})` server only → cosmetics.
- `OnEnemyKilled({EnemyId,WaveId,KillEventId,RewardRecipient,DeathReason})` unica sorgente kill.
- `OnWaveStateChanged({RunId,Wave,Phase,RemainingAlive,RemainingToSpawn})` replicated.
- `RequestPurchase({TxnId,PlayerId,ItemOrUpgradeId,TargetActorId})` server only; `PurchaseResolved({TxnId,Success,Reason,NewBalance})`.
- `OnCoreStateChanged({HP,MaxHP,Power,Tier,EmergencyState})` replicated.
- `OnDefenseStateChanged({SocketId,DeviceId,Tier,HP,Power,TargetState})` replicated.
- `OnSectorUnlocked({SectorId,WaveIndex,NewSpawnGroups})` server event then replication.
- `OnAbilityActivated({PlayerId,AbilityId,CooldownEnd,Targets})` server event.
- `OnRunEnded({RunId,Victory,Reason,Results})` exactly once.

Sono **contratti di design**, non firme C++ compilabili, e `actor ID` nel gioco va collegato ad actor pointer replicato valido/NetGUID con cleanup.

## Schema dati e cartelle (target post bootstrapping)

```text
Game/
  HordeTemplateV2Native.uproject
  Source/HordeTemplateV2Native/           # upstream dove legalmente possibile
  Source/ZDGame/                          # gameplay esteso, da creare gradualmente
  Config/                                 # pin engine/input/network/maps
  Content/ZD/Data/{Run,Wave,Enemies,Weapons,Defense,Classes,Sectors}
  Content/ZD/Blueprints/{Player,Enemies,Defense,World,Items}
  Content/ZD/Animation/{Player,Weapons,Enemies,Abilities}
  Content/ZD/Audio/{Player,Weapons,Enemies,Defenses,World,UI}
  Content/ZD/VFX/{Weapons,Hit,Defenses,Abilities}
  Content/ZD/UI/{Menus,HUD,Widgets}
  Content/ZD/Maps/{DistrictZero}
  Content/ThirdParty/                    # raw assets solo nel workspace PRIVATO
docs/                                      # GDD e manifest/versione pubblici
scripts/                                   # import/bootstrap e controlli
```

In GitHub pubblico `Content/ThirdParty` NON viene pushato senza accordi specifici. Non committare accidentalmente gli .uasset di Fab tramite LFS: LFS non rende legittima la redistribuzione pubblica.

## State machine e life cycle del network

`GameMode` server: lobby/readiness, create RunId, spawn 1–4 pawn, wave state, NPC director, end game. `GameState`: phase/wave funds/core/sector to all. `PlayerState`: class, personal credits, perks cooldown, scoreboard. Player pawn/ability component: health/down state, weapon equip and server validated commands. Enemy: AI controller server, death and locomotion state replicated. Defense actors: server only targeting/damage, remote visuals played on event.

## Navigation e attenzione horde

Prebuilt paths/links e BuildSockets impediscono blocked routes. NavMesh data/doors validati prima di abilitare settore. Zombie crowd cap calcolato per profiler (game, render, GPU, Anim), non dichiarare 100 network zombies senza misurazione. Reuse combat damage pipeline per turrets e traps.

## Workflow integrativo per asset

Source raw in private folder → import into sandbox PROJECT di quella fase solo per preparazione → real ZD wrapper → asset name/version manifest → rig/retarget/LOD/audio → cooked build → screenshot QA. **Non restare nella sandbox e non creare un secondo gioco**: la preparazione si conclude con asset integrato nel progetto principale nello stesso task.

## Quality/performance/CI

Source compile UE5.8 pinned; Unreal Editor preview e build packaged Windows come requisito ogni volta che cambia gameplay reale; profiling su hardware target sotto RTX4090, bilancia in medium 1080p, 60fps come **obiettivo** non misurato. Stat unit/game/gpu/animation/navigation, network profiling 1–4, memory/VRAM. Pre-commit lint Markdown+CSV, source static checks, build test se self-hosted runner con UE realmente presente. Non creare GitHub Actions che dichiarano compilazione UE se il runner non ha Unreal/SDK o se licenze binarie mancano.

## Packaging/ownership

Public repo contiene solo materiale che possiamo distribuire. La release Windows include contenuti legalmente incorporati/cooked. Assets e licenze terze hanno un inventario privato e crediti necessari; nel binario la licenza Fab non permette ripubblicazione isolata raw assets. In caso di dubbio bloccare release, non mascherare riferimento raw.
