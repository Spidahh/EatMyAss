# ZOMBIE DEFENCE — GAME DESIGN UNICO: COME SI GIOCA, COSA CAMBIA, COSA PRODUCIAMO

**26 ottobre 2026 — CANDIDATO DI DESIGN, NON APPROVATO. Solo progettazione: NON TOCCARE CODICE.**  
**Questa è la proposta principale da discutere.** I documenti 49/50 sono allegati di idee tecniche/produzione, non possono cambiarne il gameplay senza feedback dell'utente. La fonte delle indicazioni confermate è [45](45_USER_DIRECTIVES.md), non la presente bozza.

## 0. VERITÀ DEL PROGETTO — quattro stati distinti

| Tipo | Contenuto |
| --- | --- |
| **RICHIESTO DALL'UTENTE** | Mappa come **COD Zombies**: gira, esplora, libera/apri nuove zone; la base è fisica e ci entri **solo per gli upgrade**; installi/potenzi difese che **sparano e reggono da sole** se adeguate; la minaccia cresce; armi da fuoco + melee vero, potenziale stile solo-melee; divertente, senza classi cliché; piano completo dal menu all'esito; niente codice in questa fase. |
| **PROPOSTA DI QUESTO GDD** | Una prima mappa interconnessa, round come ritmo iniziale da valutare, punti guadagnati combattendo e spesi per **porte / armi / base**, zone che rendono disponibili nuovi upgrade da acquistare **dentro** la base, tre comportamenti zombie e due famiglie di difesa per il primo contenuto rifinito, fine della run se la base cade o nessun giocatore sopravvive. |
| **VERIFICATO** | Esistono i documenti su GitHub e le direttive registrate. È possibile studiare la mappa e simulare scelte sulla carta. **Non** è verificato un livello Unreal, un sistema d'armi importato, un asset finale, un compilato Windows o il bilanciamento. |
| **APERTURE REALI** | Persistenza tra sessioni, round vs continuo, numero finale di armi/nemici/mappe, esatto sistema di sblocco, quantità e prezzi, co-op economy, morte/respawn e quale stile melee-only sono decisioni da valutare, **non già decise dall'utente**. |

### Promessa di gioco, senza aggettivi vuoti

**Sbloccare la città mi dà qualcosa da fare e percorsi da sfruttare; combattere mi dà risorse; potenziare la base le permette di sopravvivere senza di me; nuovi assalti mi costringono a cambiare come gioco.**

La differenza rispetto a COD Zombies **non** è "aggiungere torrette a una mappa". È questa: **quando ti allontani, accade un vero assedio alla tua base**, e le scelte fatte sui potenziamenti determinano quanto tempo hai per esplorare. Il giocatore può incontrare e uccidere **gli stessi zombie** che stavano marciando verso il rifugio: non una missione separata, non due giochi indipendenti.

### Tagli immediati

Nessun sistema di classi Tiratore/Tecnico/Spezzatore o "colpo preciso"; niente cento missioni a icone, survival fame/sete, crafting e miniere, fabbriche e timer, tre aree scollegate, spawn nella sala upgrade, raccolta di cinque valute, torrette che funzionano solo vicino al giocatore, auto-guadagno infinito mentre si resta fermi, progressione che richiede aspettare ore reali.

---

## 1. Menu → ingresso → primo obiettivo (senza fare finta che sia già implementato)

**Menu proposto, con solo funzioni realmente prodotte:** `Gioca` → `Solo` oppure `Ospita / Unisciti` se il multiplayer è pronto; `Opzioni`, `Esci`. `Continua` solo se la persistenza esiste davvero. Nessuna scelta obbligatoria della "classe" prima di entrare.

**Gioca** apre **la stessa mappa** che conterrà tutta la run; si vede una base industriale con una sala upgrade, una piazza davanti e due strade sbarrate. Un piccolo sistema di difesa iniziale già operativo all'esterno dimostra che la base **combatte da sola**. Il player ha una vera arma da fuoco iniziale e una melee utilizzabile; il primo zombie deve fare una morte credibile con reazione e suono, non scomparire al click.

**Il primo minuto** è: aprire il cancello, vedere un gruppo fuori, sparare/colpire, vedere che **qualche zombie diretto alla base viene invece eliminato dalla torre**. Nessun briefing parlato di 10 minuti. Al player rimangono due domande subito visibili: `Dove porta quella serranda?` e `Posso migliorare quella torre?`.

L'hub è **solo per upgrade**. Non è una safe house con 20 NPC, laboratori e quest. Puoi entrare quando vuoi; gli zombie all'esterno non si fermano per aspettare un menu.

---

## 2. UNA MAPPA VERA, COLLEGATA COME COD ZOMBIES

**Layout candidato unico, non una lista definitiva di zone.** Le lettere sono posti fisici nello stesso livello, `P` porte/ostacoli apribili progressivamente, `S` scorciatoia da aprire dal lato lontano.

```text
                           [F] TETTI / TIPO INDUSTRIALE
                             |                      |
                            [P]                    [S] (ritorno veloce)
                             |                      |
                   [D] DEPOSITO ----[P]---- [E] SOTTOPASSO
                      |                        |
                     [P]                      [P]
                      |                        |
                 [B] OFFICINE             [C] MERCATO
                        \                     /
                         [P]                [P]
                           \                /
                             [A] PIAZZA
                                  |
                                BASE
                         (INTERNO: UPGRADE)
```

**A Piazza**: uscita base, arene iniziali, puoi vedere entrambe le porte.  
**B Officine**: corsie con visuale lunga, utile per ranged; non un negozio da gestire.  
**C Mercato**: isole e corridoi stretti, utile per il melee e per girare attorno a un gruppo.  
**D Deposito**: svolta principale: esiste qui un dispositivo/armadio armamenti che **rende disponibile** nell'hub un miglioramento difensivo capace di affrontare la minaccia successiva. Lo *trovi* fuori, ma lo *acquisti e installi* dentro, coerentemente con la richiesta. Non serve raccogliere 10 materiali o fare un incarico.  
**E Sottopasso**: via alternativa, rischiosa ma rapida; collega i rami tramite D.  
**F Tetti**: arrivi in alto e sblocchi `S`, una via di ritorno breve verso la Piazza; cambia materialmente il tempo per intervenire alla base.

**La parte divertente non è il numero di stanze, ma questo:** puoi iniziare a sinistra o a destra, poi ricongiungere le due strade; gli zombie inseguono negli anelli di attraversamento; quando sai usare la scorciatoia puoi spingerti più lontano con un rischio ragionato. La prima apertura **non è uno spostamento di menu**, alza una serranda vera con collisioni/navigazione aggiornata. Ogni area deve cambiare una decisione, non solo le texture.

**Importante:** aprire un quartiere non deve attivare automaticamente un passaggio nascosto che manda zombie direttamente **dentro** la sala upgrade. La scelta di esplorare non può essere una trappola invisibile. Le traiettorie degli assedi sono visibili e si possono intercettare.

### Perché tornare a esplorare, dopo averla aperta tutta?

L'obiettivo non è visitare l'ultima stanza una volta. La mappa è **un circuito di combattimento**: all'inizio lo attraversi male, poi impari angoli/connessioni; i gruppi che avanzano richiedono percorsi differenti. Le aree contengono posizioni, accesso a tipi di arma e opportunità reali di intercettazione; non vengono riempite con fetch quest generiche.

---

## 3. LA REGOLA CHE TI FA PRENDERE DECISIONI — un'economia leggibile

**PROPOSTA, non approvazione**: un solo tipo di punti che si guadagnano **uccidendo zombie attivamente** e si spendono in tre cose reali:
1. **Aprire strade**: nuova area + possibile accesso a equip / scelte di difesa.
2. **Migliorare le proprie armi**: potenziamenti nel rifugio, effetti fisici osservabili in gioco.
3. **Migliorare la base**: la sentry regge più zombie, una difesa anti-corazza ferma un assalitore che prima la superava.

**Regola anti-AFK della proposta: zombie uccisi dalle torrette non generano punti spendibili**. Così una base più forte **regala tempo e libertà**, non un conto in banca infinito. Il giocatore lontano incontra altri zombie reali da combattere, con un budget distinto di obiettivi IA ma **senza duplicare zombie** per far quadrare l'assedio. Se preferisce rientrare e partecipare alla difesa, le sue kill personali valgono come quelle fuori.

**Prova economica numerica ILLUSTRATIVA, NON bilanciamento approvato:**
- zombie ucciso dal player: `10 punti`;
- zombie ucciso da torre: `0 punti` spendibili;
- prima serranda `100`, miglioramento torre `100`, miglioramento arma `100`;
- 15 uccisioni fatte da te = `150 punti`. Puoi scegliere **una** delle tre migliorie, non tutte e tre. Dopo, altri zombie danno ancora punti anche se la base ne elimina alcuni. Quando la base è abbastanza forte per un'ondata, questo non ti permette di comprare un upgrade senza giocare.

**Conseguenze verificabili, non teoria:** se compri la prima porta, sei esposto ma hai subito mappa nuova e nuove occasioni di uccisione; se scegli torre, ti permette di difendere senza dover rientrare sempre; se scegli arma, abbatti più rapidamente le orde e guadagni altre possibilità. Un giocatore inesperto non deve finire senza più punti, senza munizioni e senza zombie raggiungibili. Il melee resta utilizzabile anche quando l'arma ha il caricatore vuoto. Il valore preciso di punti/prezzi va calcolato *dopo* un test del time-to-kill reale.

**Co-op da valutare con un unico wallet di punti di squadra** (meno HUD, meno doppie valute): punti da kill e acquisti condivisi; le spese grosse della base richiedono una scelta leggibile del gruppo/host, senza voto per aprire ogni porta. Se i 4 giocatori guadagnano quattro volte più in fretta, il director bilancia minaccia e budget, **non** moltiplica di nascosto i prezzi nel mezzo della sessione.

---

## 4. PRIMI 25 MINUTI — cosa succede DAVVERO se premi "Gioca"

Tutti i tempi seguenti sono **obiettivi di prova**, non fatti né un cronometro rigido.

| Quando | Ciò che fai tu | Stato della mappa e della base | Perché non è ripetitivo |
| --- | --- | --- | --- |
| **0–3 min** | Esci, spari e passi alla melee su un nemico ravvicinato | Senty iniziale fa qualche kill al portone, tu affronti zombie fuori | Impari due modi di combattere, capisci che la torre è autonoma |
| **3–6 min** | Hai punti per scegliere una porta oppure una miglioria; apri Mercato **oppure** Officine | La serranda si apre realmente e si attraversa una nuova zona | Prima scelta di percorso, non livello lineare |
| **6–10 min** | Combatti nella nuova area e valuti se spingerti in avanti | La base continua ad assorbire attacchi anche senza di te | Fiducia nella torre, rischio esplorazione |
| **10–13 min** | Torni dentro, compri una miglioria fisica, riesci | Vedi la stessa torre che ora riesce a fermare gli stessi zombie di prima | Un cambiamento tangibile, non +stat in un menu |
| **13–19 min** | Apri il secondo percorso o avanzi verso il Deposito; raggiungi D/E da un lato | Ora intravedi un altro collegamento e una scelta difensiva diversa | Scoprire che il posto è collegato |
| **19–25 min** | Ricongiungi percorsi o apri S dai Tetti | Hai un anello di mappa e una via rapida verso la base | Il ritorno dalla lontananza diventa fattibile |

**Il giocatore non deve attendere l'onda per attraversare una porta**: la mappa è libera; tra le ondate (se quel ritmo viene scelto) è solo più tranquilla. Non avviare "missione conquista Mercato 1/3" con task tracking in un altro menù: si va, si apre, si attraversa.

### Dopo 25 minuti: serve ancora gameplay

Gli zombie non ricevono soltanto il doppio di HP. In questa **proposta tecnica** la minaccia cambia per categorie di comportamento, partendo da soli tre casi ben prodotti:
- **Camminatore**: numerosità e pressione lineare; la torre veloce può gestirlo.
- **Corridore**: può oltrepassare un angolo morto se hai investito tutto sul fronte principale.
- **Corazzato**: richiede un diverso comportamento di arma/difesa, o l'intervento del giocatore. Lo sblocco di D ti ha reso visibile una scelta di difesa più adatta.

Non sono tre classi del giocatore, né l'intero bestiario già approvato. **Ogni nemico deve avere rig, attacchi, hit reaction, audio, IA e counter reali**, altrimenti usare meno archetipi.

La ricompensa della base sviluppata è forte ma non eterna: quando affronti solo Camminatori ben coperti, **la base può vincere senza il player**. Con Corridori/Corazzati la stessa soluzione può fallire e devi scegliere un upgrade o partecipare direttamente, senza penalità scriptata. L'assedio deve avere **vere entità, targeting, collisioni, HP, danni e morti**.

---

## 5. RANGED E MELEE — nessuna classe finta

**L'utente NON ha approvato una classe Tiratore/Medic/Tecnico né “colpo preciso”. Non usarli.**

- **Ranged**: ADS, peso dell'arma, rinculo, reload, hit reaction e audio veri; spazi grandi favoriscono il tiro, strade strette lo rendono meno semplice.
- **Melee**: arma autonoma con portata/tempo d'attacco, animation hit windows, reazioni corporee e colpi che NON passano attraverso i muri. Non una spinta su `V`. In Mercato il giocatore può decidere di aprirsi un varco fra gli zombie o rischiare per risparmiare munizioni; in Officine può scegliere di ingaggiare a distanza.
- **Solo-melee opzionale**: non un nome di classe con +15% danno; se verrà adottato, servono mosse/sistemi che permettano di affrontare anche Corridori e Corazzati. Altrimenti è una promessa falsa.

**Una sola possibile meccanica aggiuntiva da valutare prima di farne dieci:** `INTERCETTA LA COLONNA`. Nelle strade della stessa mappa puoi vedere un gruppo che si dirige alla base, raggiungerlo tramite scorciatoia e ucciderlo/sviarlo. **Sono esattamente gli stessi zombie** e la torre li avrebbe combattuti se fossero arrivati al perimetro. Se il player li ferma, quella pressione è davvero sparita. Richiede soltanto IA con target/base e navigazione che erano già necessari; non una quest, non una ulti, non una classe. Se la map route non permette intercettazione chiara, non aggiungere un radar finto per nascondere il difetto: correggere la route.

**Fuori scope iniziale:** skill tree di 30 abilità, moltiplicatori di colpo preciso, gore procedural e 5 sistemi di dismemberment prima che il melee base funzioni, trappole automatiche in ogni stanza, fisica zombie costosa per centinaia di attori.

---

## 6. BASE: crescita reale, non fabbrica

**Ingresso fisico** dalla Piazza. Dentro: due punti candidati, `Equipaggiamento` e `Difese`; il numero dei terminali è solo proposta. Le torrette sono disposte in **slot predefiniti reali** sul perimetro (non free-form building): riduce il lavoro del singolo sviluppatore, aiuta pathfinding, permette art polish. Ogni upgrade deve cambiare asset/componente/anim o funzionamento visibile, e la IA continua durante l'acquisto.

### Una sequenza di crescita comprensibile

1. **Prima base**: un punto difensivo leggero controlla solo un tratto di fronte. Non è in grado di gestire ogni assedio, e in condizioni normali il giocatore deve combattere.
2. **Primo investimento**: ne aumenta la capacità operativa, e riesce a respingere da sola **lo stesso tipo di minaccia** che prima richiedeva aiuto.
3. **Nuovo tipo di zombie**: un corazzato sopravvive al danno leggero; non rende inutile tutto, ma crea un problema tattico.
4. **Scelta**: vai sul percorso D che rende acquistabile nell'hub un modulo anti-corazza, oppure **torni a intercettare personalmente** i corazzati per guadagnare tempo. Entrambe sono azioni di gioco.
5. **Base forte**: quando è adeguata alla minaccia corrente, il giocatore può esplorare anche a molta distanza. L'avversario non smette di crescere, ma non esiste una legge che faccia morire il Nucleo se il player rimane assente.

**Attenzione al problema della difficoltà**: non spawnare istantaneamente un assedio impossibile non appena esce il player; deve esserci un feedback anticipato, **motivo fisico del pericolo** e tempo per decidere. Rientrare serve a comprare upgrade, non a riparare ogni 30 secondi o premere `R` su torre passiva.

### AI e performance senza magie

- `ZombieActor` vero: destinazione giocatore o perimetro, colpi fisici e stato coerente.
- `SiegeDirector` usa budget per ondata e assegna obiettivi: quando un assediatore muore, sparisce dal conto, senza un'altra copia finta nel sistema base.
- `TurretActor` simulato dall'host: rileva, ruota, verifica range/line-of-sight, spara, applica danni reali. I client fuori campo possono saltare VFX/audio lontani **ma non i risultati di combat**.
- `Core` subisce danni per contatti reali/zombie non contenuti, **mai per countdown arbitrario**.
- Non promettere `100/200 zombie contemporanei` senza profiling: budget dipende da UE, animation LOD, NavMesh, replicated relevancy, GPU/CPU in una build reale.

---

## 7. ONDATE, CONTINUO, VITTORIA, SCONFITTA

**Ritmo consigliato per la primissima valutazione: ondate come COD Zombies**, per concedere finestre leggibili di scelta tra porta/arma/base. **Pressione continua resta un'alternativa richiesta dall'utente**, non una feature già approvata o esclusa. Entrambe, se scelte, devono usare **lo stesso sistema zombie** e non raddoppiare lo sviluppo.

**Il gioco deve avere un percorso completo:**
- si avvia da menu e carica la mappa;
- la mappa cresce durante la run;
- la base può reggere o perdere in base alle scelte;
- il giocatore può continuare finché la pressione lo sopraffà;
- risultati mostrano zone aperte, tempo, ondate (se presenti), armi usate, morte degli zombie causate realmente da player/tower, causa della sconfitta, scelta `Riprova` o `Menu`.

**Proposta minima di sconfitta:** Core distrutto oppure giocatore solo definitivamente KO; in co-op, tutti KO senza possibilità di revive. Non dichiararla definitiva: è una soluzione concreta che permette di descrivere l'intera esperienza senza fissare fin d'ora l'eventuale revival. **Un player KO non disattiva la difesa automatica** finché la sessione è in corso.

**Niente finale inventato a onda 10** e niente finta "estrazione" aggiunta perché serve una cutscene. Una run survival può essere un gioco completo se apertura mappa, assedi, progressione e rigiocabilità reggono. Un eventuale obiettivo finale specifico si sceglie dopo aver visto la qualità del survival loop.

**Persistenza fra sessioni:** l'utente non ha scelto run reset o base permanente. È possibile salvare e **riprendere la stessa run** senza concedere crescita infinita off-game, ma costo e coerenza del save si verificano tecnicamente; non annunciare progressione permanente già pronta.

---

## 8. LA PARTITA IN COOP (1–4 come obiettivo precedente, da verificare)

Non cambiare il gioco in una modalità diversa:
- entrate tutti nella **stessa mappa** e potete girare insieme o separarvi per esplorare/intercettare gruppi;
- una zona che viene sbloccata è aperta per tutti, una torre migliorata serve a tutti;
- una sola base con IA host-authoritative; se il player A è lontano e B in hub, **la torre non si spegne**;
- per evitare caos negli acquisti, un wallet condiviso è la proposta **più semplice**; in alternativa si separa parte del punteggio personale **solo se** un test dimostra che condividere rende l'esperienza ingiusta;
- scaling con più giocatori deve aumentare ciò che si combatte in modo leggibile, senza moltiplicare automaticamente HP di zombie/tower a ogni ingresso o usare "spawner magici" dietro il gruppo;
- KO/revive e disconnessione host devono essere gestiti con regole esplicite prima di poter parlare di co-op completato.

---

## 9. CONTROLLO DEL DIVERTIMENTO: FALLIMENTI CHE BLOCCANO NUOVE FEATURE

| Test pratico | Se fallisce, cosa si corregge, NON cosa si aggiunge |
| --- | --- |
| Prima porta attraversata in pochi minuti | Economia iniziale, percorso visivo o ritmo di spawn; **non** altra missione |
| Aprendo le prime due porte cambia la circolazione | Layout/grafo, scorciatoie e geometria; **non** altri zombie |
| Player può giocare melee senza sentirsi punito | Animazioni, portate/hit reactions e spazi di combattimento; **non** skill passive +50% |
| Base con upgrade corretto vince una vera ondata da sola | IA turret, range/LoS, targeting e danno; **non** autowin scriptato |
| Base senza upgrade corretto può perdere contro avversari nuovi | Tipi/composizioni/tattica minaccia; **non** HP base scalati artificialmente |
| Andare lontano dalla base offre un premio concreto | Connessioni, accesso a equip o scelta upgrade; **non** fetch quest |
| 20 minuti senza menu ripetitivo | Comprensione UI/pacing; **non** quattro stazioni extra |
| Restare AFK nella base non produce progresso | Punti solo per azioni giocatore, percorso per guadagnare fuori; **non** timer anti-AFK arbitrario |
| Perf. target e rete misurati su build reale | Pooling, anim LOD, rilevanza network, numero zombie attivi; **non** promesse di 200 zombie senza test |
| Un principiante può fare una cattiva spesa e recuperare | Prezzi, drop munizioni, melee sempre usabile, zombie raggiungibili; **non** moneta premium |

**Criterio editoriale:** tagliare la feature che richiede un altro sottosistema senza migliorare nessuno di questi test. Non gonfiare il progetto per sembrare originale. La meccanica caratterizzante è già difficile da fare bene: **esplorare una mappa COD-like mentre la base vive, combatte e può cambiare il risultato del match autonomamente**.

---

## 10. COSA SI COSTRUISCE, IN ORDINE, QUANDO IL COMMITTENTE AUTORIZZERÀ IL CODICE

**Adesso: DESIGN ONLY.** Non avviare Codex, non cambiare cpp/Blueprint/asset/build. Quando verrà autorizzata la produzione, lo scope tecnico resta uno per volta:

| Priorità | Incremento che deve essere COMPLETO, non placeholder finale | Dipendenze |
| --- | --- | --- |
| **P1** | Progetto Unreal/framework funzionante, licenze e modello del player reali | Accesso engine e asset reali verificati |
| **P2** | Player FPS: movimento, camera, anim 1p/3p, passi, collisione, danni | P1 |
| **P3** | Prima arma da fuoco completa: sparo, ricarica, recul, suoni/FX/impatti | P2 |
| **P4** | Primo zombie completo: IA, locomozione, attacco, hit/death, audio/VFX | P3 |
| **P5** | Primo melee completo su zombie vero, hitbox/reazioni e audio/anim | P4 |
| **P6** | Interno base e Piazza esterna reali, due strade visibili con porte | P5 |
| **P7** | Kill reward, primo gate apribile, zona B o C COMPLETA, UI spesa | P6 |
| **P8** | Zombie Siege attaccano veramente il perimetro/Core, prime ondate | P7 |
| **P9** | Prima sentry completamente autonoma, acquistabile e upgradabile, test da lontano | P8 |
| **P10** | Secondo ramo, collegamento D–E, ritorno F–A come primo circuito coerente | P9 |
| **P11** | Nuove minacce, difese e armi, con asset/anim/FX/AI reali e balancing | P10 |
| **P12** | Partita completa menu→esito e co-op 1–4 realmente verificato | P11 |
| **P13** | QA, prestazioni, suoni/anim/performance, Windows Shipping e licenze | P12 |

I blocchi non sono istruzioni per scrivere codice ora, né un backlog approvato. Dicono quale **risultato osservabile** dovrà sostituire il materiale provvisorio. L'ordine P7 → P8 → P9 impedisce il difetto precedente: non si può testare una torre autonoma senza **enemy Siege e un assedio reale**.

---

## 11. PERCHÉ NON È COD + TORRETTA INCOLLATA

I tre sistemi devono produrre **conseguenze incrociate concrete**:
1. **Sbloccare mappa** non è cosmetico: trovi percorsi di intercettazione, ritorni più brevi e accesso a scelte d'upgrade.
2. **Fare combat fuori** non è grind isolato: puoi uccidere gli assediatori **prima** che arrivino al perimetro. Le tue kill hanno effetti sulla base.
3. **Potenziare la base** non è idle game: ti libera tempo per spingerti nelle aree più lontane; la protezione raggiunta va ripensata contro tipi nuovi.
4. **Melee** non è un pulsante di emergenza: attraversa il layout delle aree strette con propri vantaggi/rischi, senza 12 classi RPG.

Questa interazione è il vero nucleo da valutare. Qualsiasi nome di classe, boss, moneta extra, missione, potere soprannaturale o altro elemento non necessario va **escluso dalla prima costruzione**.

### Ricerche di riferimento (NON copiare asset/testi/mappe proprietari)
- COD Zombies, fonte ufficiale: [Black Ops 6 Zombies gameplay overview](https://news.blizzard.com/en-us/article/24121368/black-ops-6-zombies-what-you-need-to-know) — le porte competono con equipaggiamento e upgrade per la stessa capacità di spesa, la mappa viene progressivamente esplorata, la circolazione conta.
- [Call of Duty guide Terminus](https://www.callofduty.com/guides/blackops6/zombies/call-of-duty-guides-black-ops-6-round-based-zombies-terminus) — round, sblocchi aree, scelte di armamenti mentre si apre la mappa.
- [The Riftbreaker, sito ufficiale](https://www.riftbreaker.com/) — esempio di esplorazione/combattimento che sostiene una base difensiva; **da NON copiare** la sua fabbrica/crafting/resource chain, qui deliberatamente assenti.

**FINE — DOCUMENTO DA VALUTARE. NON EQUIVALE A UNA BUILD GIOCABILE.**
