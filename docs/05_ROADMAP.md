# Roadmap di produzione, dipendenze e backlog

**Vincoli di partenza:** sviluppo quasi gratuito, una persona + AI, PC Windows, Unreal 5.8, primo obiettivo una demo *giocabile* e visivamente credibile. Le durate seguenti sono stime illustrative in **giorni di lavoro effettivo**, non calendari garantiti: setup, conoscenza UE e bug possono moltiplicarle.

## Principi dell'ordine di lavoro

1. Ogni feature deve produrre una build apribile e una prova registrata.
2. Prova una sola variabile tecnica importante alla volta; no megamerge di pack/sistemi.
3. Prima *funziona*, poi *si sente bene*, poi *sembra bello*, poi *scala* — ma un lookdev one-room precoce impedisce scelte visive sbagliate.
4. Asset costoso/gratuito non risolve codice/animazioni da solo.
5. Una feature non entra nel prossimo sprint finché i test del gate precedente sono rossi.

## Sprint e criteri di uscita

| Gate | Attività, nell'ordine | Stima orientativa | Prove di accettazione |
| --- | --- | --- | --- |
| **G0** | audit HordeTemplate; clone isolato; engine/toolchain; due client; licenze; scelta baseline | 2–4 gg | build pulita, HUD/AI/shooting, rete 2 player, elenco diritti contenuti, ADR decisione |
| **G0b** | *solo se A bocciato*: spike Lyra e pianificazione di mapping | +3–6 gg | spara, spawn nemico, host-client, complessità quantificata |
| **P1** | blockout cortile, Nucleo HP, 2 ingressi, evento perdita/vittoria | 3–6 gg | zombie raggiungono nucleo o player, HP modifica game state, nessun stuck |
| **P2** | economy server; wave director 6 ondate; 3 archetipi nemici | 5–9 gg | 6 waves in successione, crediti no duplicate, 2p sync |
| **P3** | build socket, barricata, sentry, riparazione, targeting/LoS | 6–12 gg | placement valido/invalid, collisione, acquisti simultanei robusti |
| **P4** | upgrade armi, upgrade Nucleo, sblocco 1 settore | 6–10 gg | spesa effettiva, upgrade visibile/funzionale, nuova route nav senza stuck |
| **P5** | player class Assaltatore, UI overlay+shop ridotto, menu retry | 4–8 gg | ciclo completo 6 waves, azioni possibili con gamepad in futuro |
| **P6** | import 7 asset core, retarget, lookdev night, audio/FX gunplay, profilazione | 7–15 gg | 4 screenshot art gate, packaged build, no clippare armi/mani |
| **VS** | vertical slice beta + 3 playtest con 2 giocatori | 3–6 gg | niente crash, feedback di divertimento, primo performance report |
| **V1** | 10 waves, 3 classi, boss, nuove difese, 2 settori aggiuntivi | 20–45 gg | matrice completa `06_TEST_MATRIX.md` verde |
| **RC** | quality pass, QA networking, accessibility, legal/assets, package e store prep | 10–20 gg | clean machine launch, licenze complete, regression suite |

**Stima complessiva:** vertical slice circa **36–70 giornate effettive** dopo il setup (range ampio e non contrattuale); una V1 ulteriori 30–65 giornate. Può richiedere molto di più a un singolo dev se il template non compila o gli asset hanno incompatibilità. Evitare annunci/Steam fee finché la vertical slice non è bella e divertente.

## Product backlog prioritario

| ID | Storia / requisito | Dipendenza | Priorità | Definizione di completamento sintetica |
| --- | --- | --- | --- | --- |
| ZD-001 | scegliere la base con prova reale | nessuna | P0 | G0 PASS + decisione scritta |
| ZD-002 | ottenere la build package Windows | ZD-001 | P0 | avvio senza editor e log pulito |
| ZD-003 | 2 player in sessione con danni uguali | ZD-001 | P0 | kill e HP coerenti 10 minuti |
| ZD-010 | Nucleo danneggiabile e sconfitta | ZD-001 | P0 | fine partita su HP=0 una sola volta |
| ZD-011 | wave director data driven | ZD-010 | P0 | 6 waves determinabili da config |
| ZD-012 | 3 enemy archetypes e percorsi | ZD-011 | P0 | no stuck con 2 varchi |
| ZD-013 | arma/headshot/hit reaction adeguati | ZD-001 | P0 | prove audio/visive distinte |
| ZD-020 | team fund ledger + player credits | ZD-011 | P0 | impossibile saldo negativo/doppio spend |
| ZD-021 | socket costruzione + ghost preview | ZD-020 | P0 | green/red e rifiuto server corretto |
| ZD-022 | barricata/riparazione | ZD-021 | P0 | zombie danneggia e ricalcola route |
| ZD-023 | sentry autotarget/LoS/HP | ZD-021 | P0 | no sparo dietro muri, falloff e cooldown |
| ZD-030 | upgrade arma 2 tier | ZD-020 | P0 | cambia statistica e visual feedback |
| ZD-031 | upgrade base | ZD-020 | P0 | stato energia+HP+visual rep |
| ZD-032 | sector unlock area 1 | ZD-021, ZD-011 | P0 | varchi solo dopo apertura server |
| ZD-040 | classe Assaltatore | ZD-013 | P0 | skill e cooldown, UI e rete |
| ZD-041 | classe Ingegnere | ZD-023 | P1 | ripara + sinergia senza exploit |
| ZD-042 | classe Soccorritore | ZD-003 | P1 | revive/support test con 2p |
| ZD-050 | lookdev scena e vfx/sfx | ZD-012, ZD-013 | P0 | 4 screenshot e audio review |
| ZD-060 | boss e 10 wave curve | ZD-032, ZD-041 | P1 | boss battibile e non cheesable |
| ZD-070 | due zone aggiuntive | ZD-032 | P1 | apertura e nav runtime stabile |
| ZD-080 | save/reconnect (se necessario) | ZD-003, ZD-020 | P2 | test schema versioning + no duplicazioni |
| ZD-090 | endless / difficoltà aggiuntive | V1 QA | P3 | solo dopo retention playtest |

## Budget e decisioni di acquisto

**Scenario zero:** UE gratuito in fase di sviluppo + asset `Free` elencati + codice con licenza utilizzabile + host su PC del giocatore. Budget licenze asset iniziale 0 € **se** tutti passano. Escludere da 0€: costo corrente/hosting Internet, dati, commissioni di negozio, certificazioni, musica non CC0, costo dell'energia, eventuali licenze non-standard e tempo di lavoro.

**Purchasing gate:** pagare un singolo pack solo se prova: (a) estetica coerente, (b) almeno N giorni di lavoro risparmiati, (c) sistemi realmente pronti e documentati, (d) compatibilità UE, (e) licenza e refund. Nessun acquisto per il semplice fatto che contiene nel titolo Zombie/Tower Defense.

## Branch policy e integrazione AI

Non consentire all'agente di cambiare titolo, engine version o stile, di aggiungere pacchetti a caso, di cancellare pacchetti originali, né di marcare `DONE` per un sistema senza video/test/log. Un ticket per branch e build provata prima del merge. Ai primi bug di navigazione, riproduzione minima con due socket e un zombie, non riscrivere l'AI completa.

## Criteri Go/No-Go della vertical slice

**GO:** tre tester dicono che il tiro è gradevole; almeno due decisioni upgrade realmente contestate; difese utili ma non 'AFK'; nessun desync serio; qualità grafica coerente; performance misurata accettabile su profilo bersaglio.

**ITERATE:** gunplay piatto, torrette onnipotenti o inutili, troppo tempo nei menu, ondate repetititive. Correggere il *loop* prima di aggiungere classi/asset.

**STOP/PIVOT:** base open source non licenziabile o non compilabile senza interventi sproporzionati; co-op porta stack di bug non stimabili; la progettazione di mappa dinamica impedisce routing affidabile degli zombie.

