# DIRETTIVE ORIGINALI DELL'UTENTE — FONTE DI VERITÀ ASSOLUTA DEL PRODOTTO

**Stato: USER-CONFIRMED / 26 ottobre 2026.** Questo file prevale su ogni specifica di game design generata dall'assistente, inclusi AGENTS precedenti, docs/18–44, backlog, issue e numeri-seed. È il punto di partenza obbligatorio di ogni lavoro di Codex. [Trascrizioni originali U01–U08](47_USER_QUOTE_LOG.md).

**Principio di governo:** le scelte dell'utente sono decisioni; le idee proposte da ChatGPT/Codex sono solo **PROPOSTE NON APPROVATE** finché l'utente non le accetta esplicitamente. Non rinominare una proposta in “LOCK”, “canonico”, “definitivo”, “design decision”, o inserirla nei task come obbligatoria senza approvazione.

## A. Requisiti espliciti confermati

| ID | Decisione dell'utente | Provenienza |
| --- | --- | --- |
| UD-01 | Progettare **il gioco completo**, dal menu iniziale fino a tutta la partita e alla progressione, non una somma di sistemi o solo i primi minuti. Immaginare realmente cosa fa il giocatore, cosa vede e come funzionano le transizioni. | U02, U05 |
| UD-02 | **Mappe strutturate come Call of Duty Zombies**, da percorrere in libertà: camminare, combattere, scoprire, **liberare/sbloccare progressivamente zone** della stessa esperienza. Non tre aree esterne fisse senza progressione di apertura. | U05 |
| UD-03 | **Base fisica** che fa parte del gioco, nella quale il giocatore **entra per fare upgrade**. Può uscire e rientrare; le attività normali di combattimento sono fuori dalla base. Non una città che si esplora come menu/gestionale. | U04 |
| UD-04 | **Difesa automatica della base**: il giocatore installa e potenzia progressivamente torrette/altre difese, che arrivano a respingere autonomamente gli assalti del livello attuale. | U04 |
| UD-05 | **Minaccia crescente**: più avanti nemici più forti obbligano a migliorare le difese perché l'autoprotezione non resta eternamente sufficiente. | U04 |
| UD-06 | Possibilità di **ondate scandite** e anche di **ondata continua** come idea esplicitamente aperta. Non congelare una delle due come sola modalità approvata. | U04 |
| UD-07 | **Combattimento ranged e melee** sul territorio di gioco. Possibile specializzazione **solo melee**, ma NON è approvata una lista precisa di classi o skill. | U04 |
| UD-08 | Niente classi standard/ovvie o skill generiche prive di senso in un gioco zombie. **“Colpo preciso”** come abilità caratteristica è stato esplicitamente criticato e deve essere rimosso dalle meccaniche obbligatorie. | U04, U06 |
| UD-09 | Originalità e divertimento, con meccaniche e sinergie interessanti tra player, abilità, base e difese, **senza complicare troppo**. Proporre idee ma **mai approvarle al posto dell'utente**. | U03, U04, U06, U07 |
| UD-10 | **Produzione a strati**, uno completato bene prima del successivo; niente placeholder finali, asset casuali, falsi “finito”, animazioni/effetti dimenticati. Player con armi e **un solo zombie reale** come primo nucleo di sviluppo, senza disperdersi. | U01 |
| UD-11 | **Piano end-to-end** per tutti gli aspetti del gioco e istruzioni anti-improvvisazione per Codex. Pianificazione e specifiche non sono un gioco realizzato; validazioni durante la produzione, non una montagna di prototipi usa e getta. | U01, U02 |
| UD-12 | **Conservare tutte le correzioni**, mantenere tracciabilità e non fare proprie scelte arbitrariamente: in caso di contrasto la parola dell'utente prevale sulle proposte dell'assistente. | U07, U08 |

## B. Correzioni esplicite ai documenti già presenti

1. **ERRORE GRAVE: le mappe.** `docs/41` e `docs/44` erano stati scritti come “1 base + tre zone esterne non acquistabili”, negando la progressione alla COD Zombies. Questo non corrisponde alle ultime indicazioni. Corretto: **mappa percorribile ed espandibile tramite zone sbloccabili**. **Il metodo di sblocco** (punti, porte, interruttori, obiettivi, condizioni) non è ancora deciso dall'utente. Non sceglierlo per lui.
2. **ERRORE GRAVE: classi.** `Tiratore`, `Spezzatore`, `Tecnico`, vecchi `Assaltatore`, `Ingegnere`, `Soccorritore`, e abilità **Bersaglio Aperto/colpo preciso** sono proposte dell'assistente, **NON approvate e NON autorizzate per lo sviluppo**. L'utente vuole alternative originali e valide per un gioco zombie. Un ruolo solo-melee è POSSIBILE, non una classe già decisa.
3. **ERRORE: avventure/quest obbligatorie.** Le tre missioni capobranco, élite, recupero sono ipotesi dell'assistente, non istruzioni approvate. Non imporle al gioco.
4. **ERRORE: numeri fissati senza consenso.** Il numero definitivo di armi, nemici, torrette, zone, valuta “Rottami”, tier, checkpoint persistente, fase 10/boss, due modalità implementate, power-up del Core sono **scelte/proposte dell'assistente**. Non presentarle come confermate, salvo le esigenze generali dell'utente (armi, melee, zombie, torrette, minaccia crescente, possibilità di ondate/continuo).
5. **ERRORE: un hub isolato vs mappa COD Zombies.** La base è un luogo fisico per gli upgrade **integrato nell'esperienza giocabile**. Non trattarla come una schermata separata che invalida sblocchi di aree.
6. **ERRORE: interpretare “no prove” come “no QA”.** Niente demo/placeholder eterni; test e build sono parte del lavoro rifinito e servono a dimostrare che funziona.

## C. Stato di approvazione e lavoro Codex

**APPROVATO DALL'UTENTE come principi:** UD-01…UD-12.

**PRECEDENTI PROPOSTE NON APPROVATE:** docs/18–44, 112 righe di `33_FULL_BACKLOG.csv` e `38_RELEASE_CONTENT_MATRIX.csv` nei punti che assegnano dettagli inventati su classi, mappa, economy, modalità, numero di contenuti o obiettivi. Possono contenere pezzi tecnici riutilizzabili, ma **NON** scelte definitive di design.

**BLOCCO ALLE DECISIONI AUTONOME:** Codex non deve implementare classi/skill o la mappa delle tre zone secondo quei file. Può proseguire soltanto su foundation già esplicitamente commissionate (HordeTemplate di partenza, movimento con modello reale/arma e un modello zombie, con animazioni/effetti), e su soluzioni tecniche coerenti che non decidano elementi di design riservati all'utente.

**PROSSIMA ATTIVITÀ DI DESIGN:** scrivere/mostrare una **partita immaginata in dettaglio**, dal menu a map opening e upgrade base con zombi e sblocchi COD-style, etichettando ogni cosa che richiede decisione dell'utente. Ogni sistema aggiunto deve migliorare concretamente ciò che si fa giocando. [Traccia esperienza](46_PLAYER_JOURNEY_REQUIREMENTS.md).

## D. Protocollo per le prossime correzioni

1. Conservare la frase originale con identificativo `U09`, `U10`… nel registro 47 quando l'utente modifica o precisa la richiesta; evitare parafrasi che ne cambiano il significato.
2. Estrarre la nuova decisione `UD-13`, `UD-14`… e l'eventuale **revoca** di un'altra direttiva.
3. Aggiornare AGENTS, master design, backlog, issue, matrice e documenti interessati **nello stesso cambiamento**, oppure segnare chiaramente **NON ALLINEATO — NON ESEGUIRE**.
4. Non chiamare una decisione approvata quando è una proposta dell'assistente. Se un requisito è ambiguo, non completarlo inventando valori/funzionalità.
5. Ogni sessione di lavoro controlla questo registro **prima** di Codex o altri documenti. Il salvataggio concreto è il commit verificato su GitHub; non si può promettere sincronizzazione automatica di ogni futuro messaggio.

**Nota:** questo documento tutela le scelte dell'utente in un repository di progetto; non è un comando per ignorare vincoli legali, sicurezza o funzionamento tecnico.
