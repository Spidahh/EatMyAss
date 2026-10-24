# Istruzioni per gli agenti di sviluppo — Zombie Defence

Prima di operare sul repository:

1. Leggi integralmente `README.md`, `docs/00_START_HERE.md`, `docs/01_GAME_DESIGN.md`, `docs/02_TECH_DESIGN.md`, `docs/05_ROADMAP.md`, `docs/06_TEST_MATRIX.md`, `docs/07_AI_DEV_CONTRACT.md` e `docs/08_DECISIONS_AND_RISKS.md`.
2. Rispetta quanto definito in `docs/07_AI_DEV_CONTRACT.md`; questo file ne è un indice operativo e **non** sostituisce quel contratto.
3. Il repo parte come **documentazione**. Non dare per presenti un `.uproject`, l'engine, gli asset o le classi del template. Verificali prima di nominarli/usarli.
4. Il prossimo lavoro è il gate **G0**: audit della base open source, licenze effettive di codice e contenuti, compilazione Unreal 5.8, test host+client e report GO/PATCH/NO-GO. Non creare meccaniche TD prima della decisione.
5. Non acquistare pacchetti, non trasferire risorse non licenziate e non sovrascrivere file esistenti senza necessità.
6. Per ogni modifica: task ID `ZD-xxx`, file toccati, test corrispondenti `T-xxx`, output osservabile, build o motivo `NOT RUN`, regressioni e rollback.
7. Il gioco resta FPS d'azione con zombie e difese; non introdurre idle, factory simulator, negozio gestionale o survival crafting senza approvazione esplicita.

**Stato attuale:** nessuna prova engine svolta. Tutte le disponibilità e compatibilità segnalate nei documenti sono da convalidare con il workflow descritto.
