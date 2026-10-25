> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# Test Matrix — certificazione funzionale prima dei merge

Ogni test ha ID, riproduzione, risultato atteso, evidenza. **PASS solo con build realmente eseguita**; al momento tutti sono `NOT RUN`. Per ciascuno registrare Commit/Engine version, map, player count, hardware, screenshot/video, log, FPS e fail reason.

## G0 — audit e baseline

| ID | Procedura | Esito atteso |
| --- | --- | --- |
| T-001 | compilare repository selezionato su Windows con UE 5.8.x | 0 errori, version pin e dipendenze documentate |
| T-002 | test packaged development (senza editor) | menu → gioco → uscita senza crash |
| T-003 | host+client due processi; sparare a 20 zombie | salute nemici, uccisioni, scorte munizioni identiche nei due punti di vista |
| T-004 | 2 giocatori nello stesso punto comprano l'ultimo oggetto/shop slot | esattamente un acquisto, no saldo negativo |
| T-005 | ispezione tutti `Content/` e plugin di terzi | elenco asset/licenze/receipts o blocco evidenziato |
| T-006 | test 10 minuti con 50 zombie attivi | niente crash, log navigation e performance catturati (non pretende 60fps priori) |

## FPS gunplay e danno

| ID | Input/Setup | Esito atteso |
| --- | --- | --- |
| T-101 | 100 click in semi-auto con variazione input | 1 shot max per fire interval, munizioni mai negative |
| T-102 | automatica, sprint, ADS e reload alternati | non spara durante action proibite; state machine coerente |
| T-103 | shoot durante reload/cambio arma | anim interruption valida o azione rifiutata; no dupe mag |
| T-104 | due clienti shoot stesso zombie 1 HP | una morte e una sola wave kill reward |
| T-105 | head, torso, distance test | danni da DataAssets, hitmarker coerente col risultato server |
| T-106 | colpo light su zombie normale/elite | flinch secondo soglia, no stun-lock infinito |
| T-107 | mira con 3 mesh armi e 2 skin classi | mani, sight, muzzle, anim e reload non clip |
| T-108 | spari su flesh / metal / barricate | audio e VFX differenziati, no spam simultaneo |

## Onde, IA e direzione di attacco

| ID | Input/Setup | Esito atteso |
| --- | --- | --- |
| T-201 | sei ondate consecutive senza morire | fasi e reward una volta sola, contatore uccisioni realistico |
| T-202 | enemy cap 20 e budget 50 | sempre alive ≤ cap; coda si svuota correttamente |
| T-203 | tutte le route con barricate vive/distrutte | zombie trovano percorso o attaccano barriera con telegraph |
| T-204 | player salta su supporto alto | non blocca permanentemente wave; nemici cambiano obiettivo |
| T-205 | zombie senza nav dopo cambio porta | recovery, log e nessun softlock |
| T-206 | due settori chiusi poi apertura | niente spawn in zone chiuse, set corretti alla prossima wave |
| T-207 | idle / chase / attack / stagger sotto alta densità | anim no glitch, no pile-up senza limiti |
| T-208 | boss su unica torre attiva | boss non si lascia uccidere passivamente senza intervento player |

## Difese e base

| ID | Input/Setup | Esito atteso |
| --- | --- | --- |
| T-301 | build in socket valido | costo addebitato 1 volta, device network visibile, ghost green |
| T-302 | build da client su socket non valido/occupato | rifiuto senza spesa, ghost red e messaggio chiaro |
| T-303 | spam 30 RPC build simultanei da due client | una sola struttura nel socket, registro transazioni corretto |
| T-304 | torre con zombie dietro parete | no shooting attraverso ostacolo, se ne cerca un altro |
| T-305 | disable power al nucleo | torre cambia stato senza teleport e replica a tutti |
| T-306 | torre distrutta mentre target muore | nessun accesso nullo/crash, AI reset pulito |
| T-307 | modifica Tier1→2 torre mentre spara | range/cadenza e visual cambiano, no duplicato actor |
| T-308 | distruzione Nucleo durante wave | una sola defeat e stop a reward successiva |
| T-309 | riparazioni concorrenti senza fondi | nessun saldo negativo, UI aggiornata a tutti |

## Economia, abilità e interfacce

| ID | Input/Setup | Esito atteso |
| --- | --- | --- |
| T-401 | donate → team fund, acquisto build | non crea o perde crediti, ledger consistente |
| T-402 | assist damage su zombie ucciso da torre | ricompense senza double-award e senza kill steal abusivo |
| T-403 | Ingegnere abilità sulla base con HP pieno | costo/cooldown regolato da dati, niente heal sopra max |
| T-404 | due revive co-op in perdita pacchetti | un solo revive, HP corretti e nessun duplicato actor |
| T-405 | cambio classi in lobby o reconnect autorizzato | attributi vecchi rimossi, skill corrette, niente stacking |
| T-406 | wave prep: menu armi/torre/settore, pad e mouse | < 3 passaggi per acquisto frequente; UI no overlap |
| T-407 | 1080p e 1440p, scala UI 80/100/125% | tutti importi, icone e cooldown leggibili |

## Rete, crash, performance e shipping

| ID | Input/Setup | Esito atteso |
| --- | --- | --- |
| T-501 | listen-server + client 80ms latency simulata | richieste riflesse senza economia divergente |
| T-502 | packet loss 2/5% simulato | nessun duplicate purchase o wave reward |
| T-503 | host esce in onda | terminazione chiara o recovery documentato, no save corrotto |
| T-504 | client cade/rejoin dove supportato | stato ripristinato oppure messaggio esplicito non supportato |
| T-505 | wave 1,5,10 con 20/30/50/75 zombie | CSV grafici ms CPU/GPU, rete e memory; identificato max verificato |
| T-506 | build Shipping su installazione pulita | package avviabile senza editor, nessun file mancante |
| T-507 | import asset new e restart editor | nessuna reference persa o redirector non risolto |
| T-508 | content/license audit finale | ogni asset approvato ha receipt/licenza, no Reference-only abusato |
| T-509 | opzioni camera shake off; disabilità colore | azioni chiave restano comprensibili senza codifica colore unica |

## Playtesting qualitativo obbligatorio

Fare tre sessioni registrate: solo nuovo utente, 2-player casual e 2-player esperti FPS. Non spiegare gli acquisti in voce al test. Dopo la partita chiedere:

1. `Quale scelta di upgrade hai fatto e perché?` (deve ricordare almeno 2 alternative rilevanti)
2. `Le torrette hanno aiutato oppure fatto il lavoro al posto tuo?` (evitare entrambi gli estremi)
3. `In quale momento hai percepito un impatto forte dell'arma?` (hit reaction e audio)
4. `Ti è stato chiaro il costo di aprire un nuovo settore?` (rischio leggibile)
5. `Dove e perché ti sei annoiato?` (ripetizione/attesa/tempo fra ondate)

Annotare con timestamp 3 problemi maggiori per test e risolverne almeno 2 prima del successivo giro. Un video bello non sostituisce questa prova.

