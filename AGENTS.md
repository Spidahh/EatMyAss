# AGENTS — PRIORITÀ ASSOLUTA ALLE DIRETTIVE DELL'UTENTE

**ATTENZIONE: DESIGN PRECEDENTE NON APPROVATO.** Alla data del 26 ottobre 2026 l'utente ha corretto di nuovo il gioco. Leggere **prima** [docs/45_USER_DIRECTIVES.md](docs/45_USER_DIRECTIVES.md) e [docs/47_USER_QUOTE_LOG.md](docs/47_USER_QUOTE_LOG.md). Le regole e i dettagli inventati dai precedenti assistenti non diventano decisioni soltanto perché si trovano in un file chiamato canonico o in issue #6.

## Fonte di verità nell'ordine

1. **Direttive esplicite dell'utente**: [45](docs/45_USER_DIRECTIVES.md); formulazioni originali [47](docs/47_USER_QUOTE_LOG.md).
2. **Percorso giocabile end-to-end da rispettare**: [46](docs/46_PLAYER_JOURNEY_REQUIREMENTS.md).
3. Documenti tecnici pregressi come **proposte**, inclusi docs/18–44 e vecchio backlog. Riutilizzare solo parti coerenti con i punti 1–2.
4. GitHub Issues e report di AI: non possono annullare una correzione dell'utente.

## Requisiti innegabili

- **COD ZOMBIES-STYLE MAP:** libera esplorazione, spostamento, aree da **sbloccare/liberare** durante la partita. NON ridurre tutto a “base più tre zone esterne fisse” e NON vietare a priori gli sblocchi.
- **BASE INTERNA PER UPGRADE** nella stessa esperienza, accesso/rientro reale. Difese e torrette **autonome** fino al punto che, se potenziate abbastanza, proteggono la base da sole mentre il giocatore è lontano.
- **ESCALATION**: quando i nemici diventano più forti, la base deve essere ripotenziata.
- **FPS + MELEE**, possibile specializzazione solo melee **non ancora definita**.
- **Niente solite classi o skill cliché**, in particolare NON imporre il “colpo preciso/bersaglio aperto” come abilità in un gioco zombie.
- **WAVE o CONTINUO** sono possibilità espresse dall'utente, non due modalità definitivamente richieste.
- **PROGETTO COMPLETO dal menu alla partita**; niente frammentazione in sistemi isolati senza vedere il gameplay.
- **UNA COSA FINITA PER VOLTA**, modelli reali, animazioni, suoni, FX, networking e QA, niente finti asset definitivi.
- **L'UTENTE DECIDE IL GAME DESIGN**. Le idee della AI restano proposte finché approvate.

## Stato del vecchio piano

Il backlog `docs/33_FULL_BACKLOG.csv` (112 righe) e la matrice `docs/38_RELEASE_CONTENT_MATRIX.csv` erano redatti prima dell'ultima correzione. **NON costituiscono autorizzazione a realizzare le classi Tiratore/Spezzatore/Tecnico, le skill di precisione, un'economia Rottami, una mappa limitata a tre territori o un numero arbitrario di armi/onde.** Sono **IN REVISIONE**. Prima di eseguire i task relativi a mappe, skill, classi, valute e loop, riallineare i file e mostrare le proposte come tali. Altri task tecnici già esplicitamente chiesti (framework HordeTemplate, player vero con arma, un primo zombie, animazioni) possono procedere senza inventare sistemi di gioco.

## Protocollo anti-smarrimento

Ogni correzione di gameplay ricevuta mentre lavoriamo su questo repository va **salvata via commit**:
- Frase dell'utente (con gli eventuali refusi) aggiunta a [47](docs/47_USER_QUOTE_LOG.md) con ID U progressivo.
- Traduzione operativa aggiunta a [45](docs/45_USER_DIRECTIVES.md) con ID UD, rilevando precedenze e precedenti elementi annullati.
- Correzione di AGENTS/master/issue/backlog o marcatura esplicita **NON ALLINEATO — NON ESEGUIRE** fino a revisione.
- Link/commit verificati, senza inventare salvataggi, approvazioni o build.
- Non promettere acquisizione automatica di futuri messaggi: aggiornare realmente durante le interazioni successive.

**Stato reale:** siamo alla progettazione. Non abbiamo compilato Unreal né realizzato un gameplay funzionante in questa conversazione; documentare come PLANNED tutto ciò che resta.
