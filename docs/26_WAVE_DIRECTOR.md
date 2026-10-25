# AI DIRECTOR V2 — ASSEDIO AUTONOMO + COMBATTIMENTO ESTERNO

**Un solo direttore server**, non i due spawn loops HordeTemplate simultanei. Divide minaccia in `SiegePressure` (nemici che puntano la base/torri) e `FieldPressure` (nemici fuori contro player). Nessuno dei due si sospende perché il player è lontano/dentro, purché sessione attiva e limiti performance. Non spawnare nemici nel locale upgrade.

## Modalità sullo stesso director

- `Waves` default: stadi finiti 1–10 con intervallo 15–30s, mai forcing return, player può fare upgrade in hub anche durante la wave. Avanzamento se `pendingSiege==0 && aliveSiege==0` (corpi morti esclusi). Field pressure gestita separatamente, non blocca un'ondata per zombie itinerante fuori.
- `Continuous`: queue continue che scala budget/cap a stadi ogni 2–4min (seed), con Nucleo e tower sempre attive. Nessun doppio spawn system o nuovo mondo. Milestone stage10 con Bruto; dopo stage10 cresce entro performance limits senza reset base. Modalità selezionata sul save/nuova partita, cambiare modalità a salvataggio avviato solo se definito supporto esplicito, non cambi improvvisi.
- `Checkpoint` su confine stage e dopo acquisti, con snapshot coerente: restart non duplica KillEvents o Rottami e non perde tier.

## Curva di pressione seed

Stage 1–3 Walker/Runner, stage 4–6 corazzato e primo Saboteur, stage7–9 pressioni multi-front, stage10 Bruto. Stage>10 più densità e unità speciali, non 12 nuove mesh.

| Stage | Siege budget seed | Field budget seed | Max siege alive seed | Event |
| ---: | ---: | ---: | ---: | --- |
| 1 | 8 | 8 | 8 | imparare uscita/base |
| 2 | 13 | 10 | 10 | compra torre rapida |
| 3 | 18 | 12 | 12 | base autonoma W3 con upgrade adeguato |
| 4 | 26 | 16 | 16 | corazzato |
| 5 | 34 | 20 | 20 | sabotatore torre |
| 6 | 45 | 24 | 23 | zona B |
| 7 | 57 | 30 | 26 | duo armored+runner |
| 8 | 71 | 35 | 29 | fronte multiplo |
| 9 | 86 | 40 | 32 | elite frequent |
| 10 | 105 + Bruto | 48 | 36 | milestone Bruto |

Questi numeri sono PRIMI SEED e non conteggi confermati; vanno bilanciati con rate effettivi delle torri, player melee, difficoltà in campo e perf. Campi `SiegeBudget, FieldBudget, WeightByEnemy, MaxAlive, SpawnGroups, Stage, Mode, CoreTier, PlayerCount`. I 10 seed devono essere *data driven*; zero moltiplicazione lineare cieca x4 coop.

## Counterplay fuori

Eliminare un `Richiamo` fuori può ridurre max 10% budget siege **di stage successivo** per un evento, mai far sparire un'orda già spawnata o disattivare indiscriminatamente le torri. Saboteur che muore prima di raggiungere una torre non disabilita dispositivo. Gli obiettivi hanno cooldown e reward bounded, no farm infinito.

## Difficoltà che supera una base

Nessun HP scripting contro la base quando torrette troppo forti; l'escalation è data da composizione/zombie veri (Runner elude turret rapida, armored resiste, Saboteur disabilita, Bruto resiste ma non è immune). Towers devono essere capaci di vincere da sole **se livello sufficiente**. Target test 120s W3 senza player presente, W7 con upgrade W3 soffre e con heavy/upgraded torna a reggere.

## QA
Simulare 1p e 4p con player in Zona B, hub, KO; torre AI server aggiorna comunque, CoreHP/destroy state sincronizzato; non disabilitare torre per server relevancy, no duplicate reward / despawn stuck. Continuous e Waves condividono damage, economy e persist. [43](43_AUTONOMOUS_BASE.md) e [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).
