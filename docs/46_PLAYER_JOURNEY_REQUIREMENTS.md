# TRACCIA OBBLIGATORIA DI UNA PARTITA — COD ZOMBIES + BASE AUTODIFENSIVA

**NON È UN GDD CHIUSO.** È la verifica end-to-end che l'utente ha chiesto; si scrive da ciò che ha realmente indicato, separando i vuoti ancora da progettare e approvare. Codex NON deve inventare classi o tre zone predefinite per colmarli.

## La domanda che ogni proposta di game design deve saper risolvere

> «Se io avvio il gioco, cosa vedo nel menu, cosa clicco, dove appaio, perché vado a sinistra anziché a destra, quali percorsi posso aprire, cosa combatto, che cosa guadagno, quando rientro nella base, come reagisce da sola, come cambia il mio stile di combattimento, perché voglio fare un altro giro?»

Le risposte devono essere concrete e divertenti, non scatole “menu / gameloop / rewards” vuote.

## Percorso verificabile confermato dalle richieste

| Momento | Cosa è certo | Cosa NON è stato autorizzato a decidere autonomamente |
| --- | --- | --- |
| **01. Menu iniziale** | Il game design deve partire dal menu, con flusso completo e comprensibile prima del gameplay. | Nomi pulsanti definitivi, matchmaking, gestione salvataggi, numero modalità |
| **02. Si entra nella mappa** | Ambiente 3D di gioco percorribile **come COD Zombies**, non un piccolo cortile con tre zone decorative separate. | Luogo di spawn esatto, tema/scenario finale, durata run |
| **03. Si inizia a muoversi e combattere** | FPS e armi da fuoco; deve esistere melee autentico, non solo gesto accessorio. | Numero armi, tasti, stamina o parry preciso, valori statistici |
| **04. Si scopre la mappa** | **Sbloccare/liberare progressivamente zone**, continuare a esplorare, aprire percorsi, mantenere libera la circolazione. | Sistema di sblocco, valuta, prezzo, ordine, event gate, mappa delle porte |
| **05. Si usa la base** | Dentro la base si va **per gli upgrade** e si può tornare fuori; è una parte reale della partita. | Numero e tipologia terminali, vincoli temporal/esatti |
| **06. La base combatte senza player** | Difese automatiche si installano/upgradano; sufficientemente potenziata tiene testa all'ondata attuale autonomamente. | Modelli torri, numero, armi, costo e targeting avanzato |
| **07. Gli assalti crescono** | Zombie progressivamente più forti rendono necessarie altre migliorie alla base; possibile ritmo scandito o continuo. | Durata ondate, stage finale, boss, calendario assalti |
| **08. Scelte e abilità originali** | No solite classi; un'eventuale specializzazione melee-only è interessante ma non definita; skill sensate in un gioco zombie. | Classi specifiche, “colpo preciso”, skill generiche e nomi proposti dall'assistente |
| **09. Continuare o ricominciare** | Il game design deve descrivere tutta la partita e il suo esito/ritorno al menu in modo sensato. | Persistenza permanente, reset wave, game over esatto, modalità endless |

## Cose da non fare nello storyboard

- Non presentare Tiratore / Spezzatore / Tecnico, o altre classi RPG stereotipate, come approvate.
- Non mettere la base **fuori mappa**, in un gestionale o come intermezzo obbligatorio tra round.
- Non sostituire l'esplorazione progressiva **tipo COD Zombies** con “tre zone da fare una dopo l'altra”.
- Non rendere le torrette inutili senza giocatore nelle vicinanze.
- Non imporre finti upgrade (“10% precisione”) come contenuto zombie divertente.
- Non promuovere Rottami, 10 ondate, 3 territori, un boss, due modalità obbligatorie a decisioni dell'utente.
- Non costruire placeholder che poi diventano asset definitivi.

## Integrazione al backlog

La vecchia lista di 112 task è un **inventario provvisorio non validato dall'utente sul nuovo concept**. Prima di lavorare su mappe/skill/classes/economia, verificare i task contro UD-01…UD-12 e riscriverli. Non cancellare le parti tecniche buone: segnare `SUPERSEDED` le sole scelte sbagliate in una futura revisione tracciata. Non dire che è pronto il piano end-to-end finché non esiste una descrizione di partita approvata.

## Esempio di controllo di una proposta, NON decisione

Proposta: «In una mappa tipo COD Zombies un corridoio iniziale conduce a porte chiuse e a una base al centro; combattendo si aprono nuove strade, e ritornando nella base si potenziano torrette che continuano a difenderla mentre si esplora».

Questo esempio serve a verificare la **coerenza** fra requisiti già espressi, non approva né porte a punti né una mappa circolare né una base necessariamente centrale.
