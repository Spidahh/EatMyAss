# Zombie Defence — progetto di Game Design (26/10/2026)

**Stato: PROPOSTA DI GAME DESIGN DA VALUTARE. NESSUN CODICE MODIFICATO NELLA REVISIONE ATTUALE.** La base del motore indicata nelle ricerche precedenti è HordeTemplate su UE5.8, ma l'implementazione non è stata verificata qui.

## Il gioco richiesto

FPS zombie con mappe **come COD Zombies**: puoi esplorare liberamente, **aprire/liberare progressivamente nuove aree**, scoprire scorciatoie e ricollegare percorsi. Nella stessa mappa hai una **base**: dentro fai soltanto upgrade, fuori combatti con armi da fuoco e melee. Torrette e fortificazioni **difendono automaticamente** la base, anche mentre sei lontano; col crescere della minaccia vanno potenziate. Gameplay divertente/originale e contenuti sviluppati a strati senza placeholder permanenti.

**Questa definizione viene dalle correzioni dell'utente.** Il tipo di abilità, le classi, i numeri di armi/torri/onde e la struttura della progressione permanente **non sono approvati**: niente "Tiratore/Tecnico", niente "colpo preciso" o vecchie classi banali.

## Leggi il vero piano di gioco — non le vecchie liste

| Priorità | Documento | Contenuto/stato |
| --- | --- | --- |
| **1** | **[Direttive esplicite del committente](docs/45_USER_DIRECTIVES.md)** | Requisiti confermati, prevalgono su tutto |
| **2** | **[Trascrizioni originali](docs/47_USER_QUOTE_LOG.md)** | Ogni correzione finora registrata nel dossier |
| **3** | **[Partita concretamente simulata sulla carta](docs/48_PLAYABLE_GAME_VISION_PROPOSAL.md)** | **PROPOSTA PRINCIPALE AGGIORNATA**: menu, intera mappa a circuiti, primi 12 min, ritorno base, melee, pericoli, bilanciamento, esito e test osservabili |
| **4** | **[Mappa vera e sistemi che interagiscono](docs/49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md)** | **PROPOSTA**: grafo di zone, map opening, melee, IA, torretti |
| **5** | **[Piano dall'inizio alla release](docs/50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md)** | **PROPOSTA RIORGANIZZATA**: economia e porta prima della torre, IA Siege prima del test di autodifesa, asset finali per ogni fase |
| **6** | **[Registro errori corretti](docs/51_CORRECTIONS_AUDIT_AND_APPROVAL_REGISTER.md)** | Controprova dei conflitti e delle idee respinte |
| **7** | **[AGENTS.md](AGENTS.md)** | Blocco del vecchio backlog e del codice durante la fase di design |

## Una partita — principio fondamentale

Inizi dentro/vicino alla base e vedi la città bloccata oltre un primo accesso. Esci, combatti, raccogli i risultati del combattimento, scegli quale porta/settore aprire, scopri aree fisicamente percorribili e colleghi i rami con scorciatoie; puoi tornare fisicamente alla base per migliorare le torrette. La base combatte gli zombie **in autonomia**, mentre il player continua a esplorare e a decidere come affrontare gruppi e nemici più difficili. Nessun nuovo scenario “negozio gestionale”; il ritorno alla base fa parte della stessa partita.

Questa scena è una **proposta illustrativa** coerente con le direttive, non una lista chiusa di feature già approvate.

## Rischi: non avviare il vecchio piano

I file storici `docs/00–44`, il vecchio `docs/33_FULL_BACKLOG.csv` (112 task) e la `docs/38_RELEASE_CONTENT_MATRIX.csv` (36 voci) conservano scelte dell'assistente respinte o non approvate (3 territori sempre aperti, classi standard, "colpo preciso", valuta, num. armi e boss). **NON sono un incarico valido per Codex.** La loro sostituzione con task reali avverrà soltanto dopo che il game design avrà superato una revisione coerente. Per ora leggere la [proposta completa](docs/50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md) e il [registro](docs/51_CORRECTIONS_AUDIT_AND_APPROVAL_REGISTER.md).

**Non è stato scritto, compilato o eseguito gameplay Unreal.** Questo repository contiene design e strumenti preparatori; asset commerciali/Fab non sono stati automaticamente acquisiti. Non caricare binari Fab raw su GitHub pubblico senza i necessari diritti.

## Issue principali

[Issue #6 — revisione game design del progetto](https://github.com/Spidahh/EatMyAss/issues/6). Fino a decisioni approvate e specifiche compatibili, niente codice e niente dichiarazioni di gioco completo.
