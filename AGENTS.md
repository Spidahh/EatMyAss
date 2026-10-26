# AGENTS — ZOMBIE DEFENCE: DIRETTIVE UTENTE PRIMA DI QUALSIASI PROPOSTA

**Aggiornamento: 26 ottobre 2026. Nessun codice o asset deve essere modificato nell'attuale fase di game design.** Questa istruzione vale per Codex e altri agenti: non confondere la scrittura di un piano con autorizzazione a implementarlo.

## 1 — Gerarchia obbligatoria

1. **[docs/45_USER_DIRECTIVES.md](docs/45_USER_DIRECTIVES.md)**: decisioni effettivamente espresse dall'utente, con riferimenti ai suoi messaggi.
2. **[docs/47_USER_QUOTE_LOG.md](docs/47_USER_QUOTE_LOG.md)**: formulazione originale delle correzioni, inclusa la richiesta NON TOCCARE CODICE.
3. **[docs/48_PLAYABLE_GAME_VISION_PROPOSAL.md](docs/48_PLAYABLE_GAME_VISION_PROPOSAL.md)**: partita raccontata dall'avvio all'esito. Solo proposta non approvata.
4. **[docs/49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md](docs/49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md)**: mappa e meccaniche che potrebbero renderla interessante. Solo proposta non approvata.
5. **[docs/50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md](docs/50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md)**: piano di tutto il prodotto e fasi di produzione. Solo proposta non approvata.
6. **[docs/51_CORRECTIONS_AUDIT_AND_APPROVAL_REGISTER.md](docs/51_CORRECTIONS_AUDIT_AND_APPROVAL_REGISTER.md)**: errori precedenti, stati d'approvazione e conflitti.
7. Documenti 00–44, backlog `33_FULL_BACKLOG.csv`, content matrix `38_RELEASE_CONTENT_MATRIX.csv` e vecchie issue: **materiale di studio storico/bozza, NON istruzioni autorizzate sui punti ancora non approvati**.

## 2 — Ciò che ha effettivamente chiesto

- **Mappa percorribile tipo COD ZOMBIES**: aree da **liberare/sbloccare**, porte, progressiva esplorazione, liberi di tornare indietro. NON tre zone fisse senza aperture.
- **Base fisica nella stessa mappa**: dentro si fanno UPGRADE e si esce per combattere. Le difese automatiche possono respingere gli assalti senza presenza del giocatore quando sono abbastanza potenziate.
- **Escalation**: nuove minacce rendono necessaria altra crescita della base.
- **FPS + melee vero** e interesse verso possibile specializzazione solo-melee, senza classi stereotipate.
- **Game design originale e non complicato**, dal menu a tutta la partita, non la solita lista di feature generiche.
- **Produzione a strati** con asset veri, tutte le animazioni/FX/SFX, un primo player/arma/zombie, nessun placeholder finalizzato.
- **L'utente decide**; idee dell'AI = `CANDIDATE-NOT-APPROVED` salvo dichiarazione esplicita. “Tiratore”, “Tecnico”, “colpo preciso” e precedenti buff generici sono NON APPROVATI.
- **NON TOCCARE CODICE**: l'utente ha dato questa disposizione esplicita. Nessuna modifica a C++, UE, script, Blueprint, assets, build e nessun tentativo di avviare Codex per programmare durante la fase di revisione del piano.

## 3 — Non partire dall'errato 112-task backlog

`docs/33_FULL_BACKLOG.csv` e `37_EXECUTION_STATUS.csv` riportano vecchi contenuti, classi, valute, numero di oggetti e una mappa incompatibile o non approvata. **Non eseguire quei task.** Non contrabbandare il CSV come “piano pronto”. Un possibile ordine COMPLETO di lavoro, dichiarato proposta e non mandato di implementazione, è nel [50](docs/50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md). Solo dopo il chiarimento delle scelte ancora aperte si potrà creare un backlog operativo di Codex coerente con la partita giocabile.

## 4 — Prova anti-errore per qualsiasi modifica futura

Annotare `UserDirectiveId / isUserApproved / PlayerMoment / RealVisual+Audio / Network+AI / Tests / AssetLicense / Blocker`. Se non c'è UserDirectiveId ma la feature richiede decisione di game design, registrarla come **proposta in attesa**, non svilupparla autonomamente. Se l'utente corregge, aggiornare [47](docs/47_USER_QUOTE_LOG.md) testo originale, [45](docs/45_USER_DIRECTIVES.md) sintesi, [51](docs/51_CORRECTIONS_AUDIT_AND_APPROVAL_REGISTER.md) storico e ogni documento colpito. Non “difendere” un'idea precedente del modello contro l'utente.

## 5 — Stato reale

La revisione ora riguarda **solo file di progetto Markdown e descrizioni delle issue**. Non esiste qui un gioco UE compilato o una build testata. I documenti 48–50 costituiscono **un piano proposto** da valutare, non il design approvato né il gioco realizzato.

## 6 — Controllo di realtà vincolante (UD-16, 26/10/2026)

L'utente ha chiesto: **«tieniti costante, reale, non fantasticare»**. Prima di ogni aggiunta, dire per iscritto se è: (a) fatto verificato in repo/build, (b) scelta espressa dall'utente, (c) proposta ipotetica non approvata, (d) blocco/asset non ottenuto. Non riempire vuoti con classe generica, meccanica cliché, numeri immaginati o “funzionerà” senza prove. Non trasformare lo storyboard in contenuto realmente implementato. Attenersi al **concept esistente** e alle limitazioni del progetto. Niente ulteriore proliferazione di documenti per simulare avanzamento e, finché UD-13 è attiva, **non modificare codice**. Priorità: individuare e risolvere contraddizioni di progetto concrete, non aggiungere feature per impressionare.

## 7 — Un solo design candidate, niente proliferazione (26/10/2026)

La proposta primaria aggiornata è [docs/48_PLAYABLE_GAME_VISION_PROPOSAL.md](docs/48_PLAYABLE_GAME_VISION_PROPOSAL.md). Contiene il ciclo completo menu→mappa COD Zombies con aree apribili→equip/melee→base auto-defense con zombie veri→nuova minaccia→sconfitta/replay, economia senza farming passivo e criteri testabili. **49 e 50 sono subordinati a 48 quando esprimono proposte divergenti**, non autorizzano skill o classi aggiuntive. Le direttive UTENTE di [45](docs/45_USER_DIRECTIVES.md) prevalgono su 48. **In questa fase nessun codice e nessun asset può essere modificato.**
