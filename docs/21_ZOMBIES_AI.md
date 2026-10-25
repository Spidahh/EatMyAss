# ROSTER ZOMBIE, ARCHETIPI, AI, ANIMAZIONI, BOSS

## Un archetipo alla volta, senza cloni dichiarati contenuto finale

| ID | Nemico | Attributo di minaccia | Target preferito | Contromossa | Asset grafico |
| --- | --- | --- | --- | --- | --- |
| Z_WALKER | Camminatore | massa, lento, HP bassi | player vicino → Nucleo | headshot/AR, sentry | **Zombie Female Nurse** (RamsterZ) approvata come scelta di produzione, da acquisire |
| Z_RUNNER | Corridore | rapido, HP ridotti, aggira | player isolato → Nucleo | SMG, reazione e skill | nuova mesh gratuita **DA APPROVARE**, non recolor Nurse spacciato per modello nuovo |
| Z_ARMORED | Corazzato | piastra frontale, lento, alto HP | Nucleo/barricata | shotgun da fianco, weakpoint | mesh/armatura vera **DA APPROVARE** |
| Z_SABOTEUR | Sabotatore | attacca/spegne dispositivi | sentry alimentate → Nucleo | intercettazione, priorità bersaglio | mesh/anim rigged **DA APPROVARE** |
| Z_BOSS | Boss finale | fase multiple e telegraph, alto HP | Nucleo/giocatori/torrette | team movement + weakpoint | **asset boss dedicato DA APPROVARE**, NO nurse ingrandita |

Ogni archetipo nasce completo: modello, LOD, materiali, rig, locomotion, attacchi, hit reaction, death, audio riconoscibile, AI state, VFX, multiplayer, QA. Roster non completato se mancano fonti gratuite idonee; niente finti nemici definitivi.

## State machine AI comune

`Dormant/Spawn → Alert → AcquireTarget → Approach → Repath/Obstacle → Windup → ActiveAttackWindow → Recovery → Pursue/Retarget → Stagger (cooldown) → Dying → Corpse → Cleanup`. Solo server decide target e damage; anim state dei client segue eventi replicati. Target memory breve, no wallhack attraverso intero livello; usare AiPerception attuale se affidabile, niente seconda AI autonoma senza review. Riprogettare mapping dei Blackboard reali di HordeTemplate, non presumere nodi inesistenti.

## Matrice di animazioni per ogni classe

- Walker: idle variation, detect, walk start/loop/stop, turn, 1-2 attack windup/recover, hit light/heavy, head hit, death, get unstuck.
- Runner: idle alert, sprint start/loop/stop, turning alle strette, lunge windup/active/recovery, collision miss, stagger, death; nessun run con walk speed moltiplicata e footslide.
- Armored: locomotion pesante, armoured stagger piccolo, weakpoint hit, power windup e slam, recovery lunga, plate break visual/audio, death.
- Saboteur: locomotion, rilevamento torre, interazione e disabilitazione con VFX/gesture, combat se intercettato, hit, death.
- Boss: intro leggibile, locomotion, almeno 2 attacchi diversi con telegraph, stato vulnerabile, transizione fase, stun con limite e death finale spettacolare ma senza problemi di replication.

Zombie Nurse elenca solo 3 animazioni nella scheda (idle/walk/attack): altre vengono dal pack zombie approvato o ricreate concretamente con rig retarget/Control Rig, non inventate al report. Vedere [14](14_ZOMBIE_COMPLETE.md).

## Numeri proposti per prototipo di bilanciamento 1.0 (NON VALIDATI)

Walker HP100, move 180 cm/s, attack 15 ogni 1.5s; Runner HP65, 380 cm/s, 9 ogni 1.1s; Armored HP450, 125 cm/s, 30 ogni 2.3s (armatura frontale riduce danni ordinari); Saboteur HP120, 250 cm/s, attacco dispositivo e player basso; Boss HP4500 per 1p, fino a scaling **non lineare** per 4p, non affrontabile con sola sentry. I numeri sono seed, non capacità confermate dal codice.

## Target selection e fairness

Priority score = reachability + role modifier + threat + distanza (pesi per archetipo). Non esiste un “enemy che ti corre dietro per sempre se sali su un container”: after timeout passa alla base oppure a una struttura raggiungibile. Lo zombie non può passare attraverso porte chiuse o coperture; se barricata attaccabile blocca route, bersaglia barricata, altrimenti navmesh calcola percorso alternativo. I nemici marcati “barricade breaker” hanno animazione di attacco alla struttura, non attacco player copiato con zero differenze. Target invalid/dead → pulire blackboard, restart scoring.

### Regole anti-frustrazione

- Spawn gruppi leggibili con preavviso 1–2s (seed), mai dentro metri immediati alla schiena se player guarda in quella direzione; sottostanti NavMesh.
- Damage window legata al montage o curva server, **un hit per attack target**; colpo evitabile con movimento/prontezza.
- Reazione leggera ogni tanto, cooldown stagger; AR non può tenere 1 zombie perma-stun con autofire. Weakpoint armor fa feedback riconoscibile.
- Niente teletrasporto di recovery visibile ai giocatori; softlock rilevato server, priorità al re-path o corretto cleanup senza reward.
- Zombie morti rimossi dal conteggio dei vivi **prima** di ragdoll/decay. Nessun dup reward death/despawn.

## Boss e battaglia finale

Alla wave 10: spawner dedicato, breve preavviso, appare boss con 2 fasi basate su HP; fase 1 pressione su team, fase 2 tenta colpire Nucleo e temporaneamente disabilitare una sentry, sempre con preavvisi; 2 attacchi diversi e weakpoint esposto per breve periodo. Combat non risolvibile restando dietro a una torretta invulnerabile. Non creare cutscene lunga di introspezione: intro 3–6s seed, skippabile co-op. Ricompensa finale non spendibile perché run finita.

## Contratto evento per le difese

Ogni zombie è Damageable anche se `DamageCauser` è torreta/barriera/trappola; `SourceType` enum con `PlayerWeapon`, `Defense`, `Hazard`; `RewardRecipient` può essere player/team/nullo. Killed una sola volta, corpse una volta, wave counter una volta.

## Done di una nuova unità

Archetipo completo se AI affronta player e strutture secondo ruolo, tutte le animazioni specifiche senza T-pose, hit/death audio/VFX distinti, nave senza impigliarsi in tutte le aree aperte, coop 1 e 4, performance con 20 attivi misurata e licenza app provata. Zero ambient placeholders.
