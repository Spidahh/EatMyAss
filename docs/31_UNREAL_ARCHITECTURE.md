# ARCHITETTURA UNREAL V2 — HUB/BASE/EVENTI/MELEE, UN SOLO FRAMEWORK

**Baseline:** HordeTemplate V2 Native UE5.8 designato. Esistono upstream `HordeBaseCharacter`, `BaseFirearm`, `ZedPawn`, `ZedAIController`, `HordeGameMode`, `HordeGameState`, `ZedSpawner` e inventory; estendere con prefisso ZD, non introdurre Lyra o un secondo inventario/AI. I seguenti nomi ZD sono **CONTRATTI**, non classi già presenti o codice compilato.

| Sistema | Owner server | Funzione |
| --- | --- | --- |
| `ZDWorldBaseState` | GameState o Actor replicated host | livelli turret, socket, HP Core, PowerCapacity, Rottami, profile id |
| `ZDBaseInteriorVolume` | collision authority server | traccia InsideBase, upgrade consentiti solo nei 4 terminali |
| `ZDDefenseManager` | server AI subsystem | automatic target acquire/range/LoS, firing, damage, heat, repair/power, no player relevancy |
| `ZDCore` | actor replicated | HP0 fail, autorepair tier e auto emergency pulse threshold once/stage |
| `ZDThreatDirector` | GameMode/server | 2 stream FieldPressure/SiegePressure, Waves/Continuous stesso codice, cap, checkpoint |
| `ZDWeaponAdapter` | integrazione BaseFirearm | ranged fire/damage/ammo/impacts server, saved upgrades |
| `ZDMeleeComponent` | player server component | swing montages/notify windows, collision swept trace, block/parry/stamina, counter, net |
| `ZDEnemyBehavior` | ZedPawn/ZedAIController data | role Siege/Field, target core/towers vs player, hit reactions and death |
| `ZDSpecializationComponent` | player state/pawn | Tiratore/Spezzatore/Tecnico passiva, Q, mode solo melee |
| `ZDOutsideEventManager` | server | one short mission active, objective reward bounded, siege budget modifiers |
| `ZDWalletLedger` | server | one Rottami resource, grant/spend TxnId idempotence, shared/host permissions |
| `ZDBaseSave` | host SaveGame | saved base/world between sessions, versioning/checkpoint/journal |
| `ZDUI/HUD` | client presentation | Hub terminals, outside shooting, auto-defense warnings, no fake stats |

## Un solo stato di danno

DamageEvent con `SourceActor` `Instigator` (può essere nullo per torretta) `TargetActor` `HitZone` `Amount` `EventId`; morte una sola volta a HP<=0 da player arma, melee o turret. Award Rottami diverse quote in funzione fonte e evento unico. No aspettativa `DamageCauser is ACharacter`.

## Timer/AI tick/relevancy

Zombie Siege/server e torre AI sempre attivi nella simulazione durante una sessione, anche se nessun player nella distanza del perimetro: il server può ottimizzare tick con dati temporali ma **non può spegnere il sistema**. FPS/HUD e audio FX possono essere replicati/cullati per client distanti, mantenendo risultato fisico; usare AI spawning/cap reali e NavMesh. No fake damage al Core per “simulare” wave lontana.

## Runtime flusso

`HostStart/LoadBase → InsideHub`; un player che cammina tramite cancello viene identificato Inside/Outside; `Outside` cambia solo UI/opzioni disponibili per player, non wave state; quando player torna può spendere durante Siege senza interrompere timer. `ThreatDirector` può generare spawn Field e Siege contemporaneamente senza doppio conteggio; a stage10 boss, base salva milestone. Difficoltà migliora nemici veri via defs, non fake timer HP.

## Persistence

Data versioned `BaseSaveId` sul PC host, SaveGame snapshot a stage boundary e ad acquisto, backup atomico. Mid-assault crash reload checkpoint pre-stage; se wallet ha grant dopo checkpoint, non riapplicare journal senza matching stage/event ID. A offline non run tick/spawn. Co-op guest no persisting duplicate.

## Architettura asset

Workspace PRIVATO con raw Unreal assets da Fab/Epic; repo pubblico contiene codice lecito, documenti, manifests, script, config e `Content/ZD` SOLO assets propri/autorizzati alla redistribuzione. Quattro terminali reali hub, player rig real, turret meshes e zombie real, no placeholder. Blueprint solo presentation/Animation BP/Niagara/wiring, C++ per invariant/damage/saving/AI. Video in editor e package provano completezza.

## Test obbligatori

Host avatar in Zona C e tutti i client fuori, server torri difendono W3 120s. Entrare upgrade durante wave e tornare fuori, nessun stop spawn; ctrl save/restart host co-op corretta, tentativi doppio acquisto. Melee parry network same time and damage. Mode Waves/Continuous share asset/state. No build claims without engine.
