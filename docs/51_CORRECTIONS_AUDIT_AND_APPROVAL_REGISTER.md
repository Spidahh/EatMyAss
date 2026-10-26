# AUDIT DEGLI ERRORI, CORREZIONI E STATO DELLE DECISIONI

**26/10/2026 • Solo documentazione: nessun codice Unreal toccato.** Questo registro serve a impedire che i documenti generati in precedenza prendano il posto delle richieste dell'utente.

## Gli errori già fatti e la soluzione verificabile

| Errore precedente | Perché ha rovinato il design | Correzione nei documenti 48–50 | Stato |
| --- | --- | --- | --- |
| “Città” come upgrade/base da esplorare nel gestionale | La mappa COD Zombies scompare | Base fisica interna **solo upgrade**; città esterna vera da esplorare, porte da aprire | PRINCIPIO CONFERMATO, schema di mappa PROPOSTA |
| «Tre zone esterne già aperte» | Non esiste scoperta di percorsi | Due rami iniziali, 2+ collegamenti e ritorno da scorciatoie, zone sbloccabili | PRINCIPIO CONFERMATO, layout PROPOSTO |
| Base come supporto non autonoma | Player deve presidiare/gestire sempre | Torretti fanno vera IA/danni/kill senza player nelle vicinanze | CONFERMATO |
| «Il player non serve perché la base uccide tutto» | Gameplay diventa idle | Attacchi evolvono; giocatore apre zone, affronta nemici, raccoglie upgrade attraverso combat | CONFERMATO crescita minaccia, dettagli PROPOSTI |
| Classi Tiratore/Spezzatore/Tecnico/Medic, “colpo preciso” | Cliché espressamente rifiutati | **RIMOSSE dalle meccaniche approvate**; idee fisiche e strumenti non-classe come proposte | RIFIUTATO CLASSI PRECEDENTI |
| Melee come spinta su un tasto | Non è uno stile di gioco | Arma vera con swing, hit, posizionamento e differenza concreta; possibile melee-only | CONFERMATO melee, mosse PROPOSTE |
| 2 valute PC/TF, poi Rottami imposta come moneta definitiva | Scelte arbitrarie | Trattare economia come **decisione da approvare**, proporre tradeoff apertura/equip/difesa | NON DECISO |
| 10 waves/boss/finale imposto | Decisione inventata | Non fissare fine, comparare sopravvivenza e obiettivo facoltativo; waves/continuous aperto | NON DECISO |
| Incarichi capibranco/cassa/elite imposti | Aggiungono missioni non chieste | Esposti soltanto come esempi opzionali, mai checklist approvata | NON DECISO |
| 112 task V2 trattati come piano approvato | Codex implementa cose non richieste | 112-task CSV marcato **LEGACY/DA RIVEDERE**, indirizzare al piano gameplay proposto e direttive UD | CORRETTO NELLA PRECEDENZA |
| Documenti/issue che si contraddicono | Codex prende istruzioni casuali | AGENTS + README + Issue #6 devono indirizzare 45–51 con priorità utente | DA ALLINEARE E VERIFICARE |
| “Completato” senza progetto Unreal | Promesse non supportate | Distinguere chiaramente **documentazione progettuale da implementazione/build** | CORRETTO |

## Documenti e precedenza

**Confermati dall'utente:** [45 Direttive](45_USER_DIRECTIVES.md), [47 Parole originali](47_USER_QUOTE_LOG.md).

**Nuove proposte integrate, NON approvate:** [48 Partita minuto per minuto](48_PLAYABLE_GAME_VISION_PROPOSAL.md), [49 Mappa/sistemi/idee](49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md), [50 Piano dal menu alla release](50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md).

**Legacy, non decidono il game design:** docs/00–44 dove incompatibili, `33_FULL_BACKLOG.csv` (vecchie decisioni di classe/armi/zone), `38_RELEASE_CONTENT_MATRIX.csv` (vecchie decisioni di asset). Non usare il numero righe dei vecchi CSV come misura di progresso.

## Regole di approvazione, senza giri di parole

- Se è una parola diretta dell'utente: `CONFIRMED-USER`.
- Se è una cosa suggerita dall'assistente: `CANDIDATE-NOT-APPROVED` finché non arriva feedback.
- Se l'utente la boccia: `REJECTED`, non riproporre come “nuova idea” in altri documenti.
- Se l'utente la corregge: mantenere storia e registrare `SUPERSEDED-BY UD-XX`.
- Un file chiamato `MASTER` o un issue assegnato a Codex non cambia lo stato d'approvazione.
- Non introdurre testo spacciato per citazione originale dell'utente, e non confondere una sintesi dell'assistente con decisione sua.

## Possono essere progettate e testate le seguenti cose senza inventare game design?

**Sì come produzione tecnica già richiesta:** framework/designato, un modello personaggio con animazioni definitive, una arma reale (sorgente confermata dopo acquisizione) e un zombie rigged completo con SFX/VFX/AI; mappa esplorabile con logica COD (solo nei dettagli approvati). **No come features definitive:** classi inventate, Rottami per forza, numero finale di unità, 10 onde, 3 zone fisse, skill “colpo preciso”, liste missioni esterne imposte.

## Verifica della vera qualità prima della programmazione

Un GDD è pronto per Codex solo quando la sequenza [48](48_PLAYABLE_GAME_VISION_PROPOSAL.md) contiene un inizio/mezzo/fine e tutti gli elementi che lo rendono divertente sono provabili, la topologia [49](49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md) è visualizzabile su carta, i conflitti approvazione sono risolti e [50](50_COMPLETE_DESIGN_AND_PRODUCTION_PLAN_PROPOSAL.md) è collegato a task non contraddittori. Se no, descrivere il documento come **bozza da valutare**, non `FINITO`.

## Non modificare codice per correggere un'idea

Questa revisione riguarda SOLO `.md` del progetto e descrizioni GitHub. Niente Unreal C++, Blueprint, assets, script, CSV di milestone o builder deve essere toccato per mettere ordine nel concept. Dovrà essere esplicitamente richiesto il lavoro sul codice.
