# 10 ONDATE FINITE — WAVE DIRECTOR, SPAWN, DENSITÀ, BOSS

## Una sola regia per le ondate

HordeTemplate presenta `HordeGameState::StartGameRound()` con generazione e fine-round per timer, `GameMode::InitiateZombieSpawning` e `AZedSpawner` con spawn continuo/wave/trigger. **Decisione:** un unico nuovo `ZDWaveDirector` AUTOREVOLE controlla la run e invoca ADATTATORI dei punti spawn validati, senza tenere due sistemi attivi in parallelo. Eseguire la migrazione nel solo strato L5 (non rifare l'intero template prima del suo bisogno).

## Data schema server

`WaveId`, `ThreatBudget`, `WeightsByEnemyId`, `MaxAliveByPlayers`, `SpawnIntervalRange`, `AllowedSpawnGroupsByOpenSector`, `EliteCap`, `BossId`, `PreAnnouncementId`, `VictoryConditions`, `TeamReward`, `PersonalReward`, `DelayStart`, `RecoveryTimeout`. Stage queue finita con generazione deterministica basata su seed run, ma **non** rigida se meno punti di spawn autorizzati. Budget spende costo threat per tipo: Walker=1, Runner=1, Saboteur=3, Armored=4, Boss separato. Non confondere `ThreatBudget` con count zombie. La composizione del CSV originale usa pesi, non count garantiti.

## Curva di progetto 1.0 (seed non misurato)

| Onda | Threat budget 1p | MaxAlive 1p | Composizione / evento | Ricompensa TF |
| ---: | ---: | ---: | --- | ---: |
| 1 | 12 | 12 | walker; insegnare shooter | 80 |
| 2 | 18 | 15 | walker + runner 10%, mostrare riparazione | 95 |
| 3 | 25 | 18 | runner 25%; offerta S1 dopo vittoria | 115 |
| 4 | 34 | 22 | armored introdotto 10% | 135 |
| 5 | 43 | 25 | sabotatore 5%, difese richiedono player | 155 |
| 6 | 55 | 28 | due fronti, apertura S2 disponibile | 180 |
| 7 | 69 | 32 | walker/runner + armor/sabotatore, **crisi breve sentry se esiste** | 210 |
| 8 | 84 | 36 | pressure, S3 disponibile | 240 |
| 9 | 100 | 40 | preparare fight finale, elite >20% | 270 |
| 10 | 120 | 44 | gruppo + boss univoco in scena sicura | nessuno; Victory |

I pesi effettivi delle tipologie sono in `09_BALANCE_SEED.csv`: solo seed. Dopo apertura S1/S2/S3 il Budget rimane governato dal director: **non duplicare nemici** per ogni settore nuovo. Gli ingressi acquistati redistribuiscono, non moltiplicano indiscriminatamente la difficoltà.

## Scala coop parametrica: non moltiplicazione cieca

ThreatBudget(n) = Budget1p × `PlayerFactor[n]` (seed: 1p1.0, 2p1.55, 3p1.95, 4p2.30); ActiveCap(n) = min(PerformanceCap, Cap1p + (n-1)×6) per test; enemy health normal x1 per ordinari (diventa lievemente più alto su elite/boss a più player solo dopo test). Boss HP factor seed 1p1, 2p1.5, 3p1.9, 4p2.3, non lineare 4x. Non usare 44 active zombies per 4p senza profilo reale; test progressivi stabiliscono PerformanceCap.

## Algoritmo rigoroso wave

1. Server seleziona wave data + settori aperti + n player alla partenza della wave (il player join/leave non cambia a metà la composizione già scelta).
2. Genera coda di `SpawnTicket(EnemyId, SpawnGroupId, SequenceId)` con somma threat budget <= max e pesi senza pack vuoti. Boss ticket separato alla 10.
3. Ciclo su server a intervalli: controlla active alive cap, gruppo con NavMesh, distanza/visibilità e area open, spawn actor reale con riferimento univoco.
4. Incrementa pending decrementa solo quando spawn riuscito; se no attende/ridistribuisce a gruppo valido, non perde il ticket senza log. Nessun nuovo zombie in settore closed.
5. EnemyDie risulta un solo messaggio death, decreasing alive; corpse cleanup indipendente.
6. Completion soltanto quando pending=0, alive=0, boss (se previsto) dead; reward Team/Personal eseguiti UNA volta per `WaveId`; prep timer avviato server.
7. Anti-stall: enemy stuck oltre finestra definita => cerca nuova route/bersaglio; se non risolvibile dopo retry limitati, despawn recovery senza reward, log e count; no wipe silenzioso davanti player.
8. Quando core è morto o team wiped => stop timer e spawner, niente wave rewards.

## Micro-evento tattico di W7 (non nuova modalità)

La settima onda, dopo preavviso 5s, può disabilitare **una sola sentry attiva per massimo 8s**. Si risolve tramite E interazione alla torre (3s) o Q ingegnere, non richiede quel ruolo per poter vincere. Con nessuna torre il micro-evento è solo una normale warning. Nessun aumento di zombie, valute, unità o sistema RNG: riusare stato `Disabled` del Sabotatore. Il Nucleo conserva un unico Impulso di Contenimento una volta/wave e la slow area non conta come enemy kill; le wave terminano sempre solo quando zero pending e zero alive. Specifica [40](40_SYNERGIES_SKILLS_AND_CITY.md).

## Adaptive director, solo dopo curva controllata

Il director può selezionare composizione **entro pesi fissati**, scegliere spawn group tra quelli aperti, modulare intervalli entro min/max. NON aumentare HP nascosti o spawn alle spalle perché il team spara troppo bene. Se performance degrada scende active cap e coda rimane valida, non salta wave.

## Boss

Alla 10 un ticket Boss, limite 1, non respawna se morte dichiarata. Se base distrutta e boss muore simultaneamente, definire precedenza `Defeat if CoreHP<=0`. Intro corta skippabile, fase1/2 via eventi affidabili, max add spawn controllato. Sentinelle possono ferire ma boss ha meccaniche che richiedono il player. Nessun boss preso da asset free senza manifest APPROVED.

## Test e accettazione

10 wave complete in 1p/2p/4p, due configurazioni settori aperti/chiusi, nessun softlock; reward una sola volta; esc supportato; FPS e banda misurati; nessun zombie illegale dietro visuale; boss e area compatibili; replay seed debug. All'uscita dello strato L5 deve essere completa una wave sequenziata, e a L11 tutte 10 curate.
