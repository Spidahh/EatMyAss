# ECONOMIA COMPLETA, COSTI, UPGRADE E PROGRESSIONE

## Intento

Il denaro è un **tradeoff di azione**: investire nel proprio fucile o fare contributi per aprire settore/costruire torre; difese e arma non sono indipendenti. Nessun inventario di materiali, raccolta giornaliera, cassa di negozio o risorse idle. Nessun acquisto con soldi veri. Tutto si azzera a fine run (tranne preferenze/statistiche).

## Le sole due valute

- **PC / Player Credits (personali):** guadagnati per danno utile, kill, assist e completamento wave. Spendibili in armi, loro upgrade, munizioni e consumabili minimi. Nessun bonifico da team funds a crediti personali.
- **TF / Team Funds (condivisi):** quota di completamento wave e possibili donazioni volontarie personali, acquistano difese/Nucleo/repair/settori. Squadra vede saldo, spesa e autore; importi in integer, mai floating. Gli zombie non lasciano valute raccolte in 3D come feature 1.0.

## Regole dell'assegnazione punti

- Una death produce evento server `EnemyKilled(EnemyId, KillTxnId, Participants)` **una volta**, non per ogni client; partecipante che ha inflitto almeno una soglia di danni negli ultimi X secondi riceve share contributo, killer bonus piccolo. Le torrette non attribuiscono kill a player ingiustamente; la ricompensa di una torretta è team e ridotta per evitare AFK.
- Crediti per kill: **Walker seed 25 PC**, Runner 30 PC, Armored 75 PC, Saboteur 50 PC, Boss 0 PC (termina run); assist share pool addizionale limitato. Questi seed vanno armonizzati con HP e ritmo, NON sono già bilanciati.
- Ricompensa automatica wave: team funds secondo `09_BALANCE_SEED.csv` (1=80, 2=95, 3=115, 4=135, 5=155, 6=180, 7=210, 8=240, 9=270; wave10 fine run); ciascun player vivo/ripristinabile riceve bonus personale wave seed 50/75/100... in DataAsset, non hardcoded.
- **Contributi donazione:** 1 PC = 1 TF come seed, irrevocabile, visibile nel log e con conferma. Limitare spam RPC e deduplicare TransactionId. Una classe Ingegnere non converte fondi gratis.

## Catalogo prezzi seed compatibile con precedente CSV

| Spesa | Valuta | Prezzo seed | Limitazioni |
| --- | --- | ---: | --- |
| Ammo refill | PC | 60 | max durante prep, singola arma |
| Pistola upgrade T1 | PC | 120 | arma posseduta |
| AR upgrade T1 | PC | 240 | arma posseduta |
| Shotgun upgrade T1 | PC | 280 | arma posseduta |
| SMG upgrade T1 | PC | 220 | dopo asset approvato |
| Barricata | TF | 100 | 1 per socket |
| Barricata riparazione | TF | fino 45 | scala con HP mancanti, mai oltre max |
| Sentry | TF | 220 | max 2 per settore, power disponibile |
| Sentry T1 | TF | 160 | tower completa prima di T2 |
| Slowfield | TF | 180 | slot dedicato |
| Core T1/T2/T3 | TF | 240/380/550 | prerequisito sequenziale |
| Officina S1 | TF | 260 | dopo wave 3, salvo permessi mappa |
| Deposito S2 | TF | 420 | dopo wave 6 |
| Tetto S3 | TF | 500 | dopo wave 8 |

**Incompatibilità da evitare:** sommare costi obbligatori che superano tutte le entrate TF senza alcuna donazione possibile in solo. Il sistema NON deve richiedere S1/S2/S3 per vincere; aprirli dà opportunità con rischi, non blocca una quest essenziale.

## Transazione unica server per ogni spesa

`RequestSpend(TxnId, ActorId, PurchaseId, TargetId)`:
1. Verifica sessione/wave phase, player, distanza/interazione, prerequisiti, rank, slot, cap e fondi.
2. Blocca saldo o riserva atomicamente, esegue spawn/applicazione upgrade senza side effects ripetuti.
3. Su successo registrare `LedgerEntry{txnId,before,delta,after,wave,time,item,origin}` e replicare.
4. Su fallimento restore e risposta di errore esplicita; ritrasmissioni con TxnId già completato restituiscono stesso risultato, non addebitano.
5. Se due player acquistano lo stesso socket, il primo atomicamente vince, il secondo ottiene occupied e zero spesa. Test con packet loss.
6. Le UI NON decrementano saldi autonomamente per finta; possono mostrare optimistic spinner, poi aggiornano valore autorevole.

## Bilanciamento senza improvvisazioni

Parametri chiave: PC/player/wave, TF/wave, cost upgrades, wave length, DPS arma, DPS sentry, repair efficiency, enemy HP, ammo used. Per ogni wave simulare 1p/2p/4p tre stili di spesa: **A** tutte armi, **B** torre/Nucleo, **C** mix. Se sempre vince una sola strategia, correggere distribuzione. Obiettivi: entro wave3 una scelta vera fra AR T1 e donate; entro wave5 acquisto difesa utile; wave7 pressione per riparare; prima di wave10 choice se salvare Nucleo o comprare upgrade.

## Upgrade visibili, dati e UX

Ogni upgrade prevede: descrizione, attuale→futuro, costo, effetti tangibili, mesh/material differenti o dettagli quando realizzabile, SFX unico, rilevanza reale. Niente finto tier in un menu che non cambia gameplay. Gli upgrade del player e delle difese sono **non rimborsabili** nella run 1.0. Acquisto ripetuto bloccato. Prezzi scalano per player count soltanto con tabella documentata e test, mai “* players” ovunque.

## Deliverable

`EconomyRules` data, ledger replicato, reward idempotenti, costo per device/tier/sector e 10 wave provate. Esportare in CSV transazioni replayable; ogni sessione multiplayer deve avere saldi uguali lato host/client.
