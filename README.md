> **DIRETTIVE UTENTE AGGIORNATE 26/10/2026:** questo README e la V2 sotto contengono ancora **ipotesi dell'assistente non approvate**, soprattutto classi/abilità Tiratore–Spezzatore–Tecnico, “colpo preciso” e mappa di sole 3 zone. **NON usarle per sviluppare.** La regola ora è: mappa **stile Call of Duty Zombies** con esplorazione libera e **zone sbloccabili**, base fisica per upgrade che **si autodifende**, combattimento FPS+melee e scelte originali approvate dall'utente. Leggere [AGENTS.md](AGENTS.md), [45 Direttive](docs/45_USER_DIRECTIVES.md) e [46 Percorso di gioco](docs/46_PLAYER_JOURNEY_REQUIREMENTS.md) **prima di tutto**. Il piano 112 task è **IN REVISIONE**, non approvato nelle decisioni di gameplay.

# Zombie Defence — FPS + Melee + Base Autonoma (V2)

**CONCEPT CANONICO CORRETTO · 25 ottobre 2026**  
**Stato reale:** specifiche, task e piano pubblicati; non esiste ancora una build Unreal del gioco in questo repo. HordeTemplate è la baseline scelta; asset Fab/Epic non sono già scaricati e non possono essere pushati raw sul GitHub pubblico.

## Cos'è il gioco (leggere prima di qualsiasi Codex)

La **BASE è un hub fortificato accessibile fisicamente**. Dentro si fanno upgrade di armi, specializzazioni, Nucleo, torrette e barriere. Fuori si combatte **in prima persona con armi da fuoco e melee reali**, si eliminano zombie/elite e si completano brevi eventi per guadagnare **Rottami**.

**La base si autodifende**: le torrette mirano, sparano e uccidono anche se il giocatore è lontano, dentro la base o KO. Una base ben potenziata riesce a resistere da sola agli attacchi del livello attuale; col passare degli assalti arrivano nemici più forti e serve potenziare ancora. Si può rientrare **quando si vuole**, anche durante un'ondata. La base persiste fra sessioni host; quando il gioco è chiuso non avviene simulazione offline.

Non ci sono “settori cittadino da comprare”, non serve difendere il Nucleo sparando sempre da vicino, non esiste idle farming, niente raccolta di 50 materiali o negozio gestionale.

## DOCUMENTI AUTOREVOLI V2

| Ordine | Documento | A cosa serve |
| --- | --- | --- |
| 0 | **[AGENTS.md](AGENTS.md)** | Contratto di Codex e precedenza V2 |
| 1 | **[41 — Game vision V2](docs/41_CANONICAL_GAME_V2.md)** | Definizione esatta del gioco dentro/fuori base |
| 2 | **[42 — Melee e specializzazioni](docs/42_MELEE_SKILLS_AND_SPECIALIZATIONS.md)** | Pistole/fucili/machete/mazza/asta, parry, counter, 3 specializzazioni |
| 3 | **[43 — Base automatica](docs/43_AUTONOMOUS_BASE.md)** | Hub, torre rapida/pesante, portoni, autocombat, upgrade |
| 4 | **[44 — Esterno e progressione](docs/44_OUTSIDE_COMBAT_AND_PROGRESSION.md)** | Tre zone esterne, incarichi e Rottami, ondate/continuo, salvataggi |
| 5 | **[18 — Master spec V2](docs/18_MASTER_GAME_SPEC.md)** | Registro del perimetro del prodotto |
| 6 | **[33 — Backlog V2](docs/33_FULL_BACKLOG.csv)** | Lavori concreti in ordine lineare e criteri di completamento |
| 7 | **[38 — Matrix completa](docs/38_RELEASE_CONTENT_MATRIX.csv)** | Modelli, animazioni, audio, effetti, AI, rete per ogni oggetto |
| 8 | **[34 — Mandato di Codex](docs/34_CODEX_MASTER_BRIEF.md)** | Come eseguire, non reinterpretare |
| 9 | **[30 — Asset sourcing](docs/30_ASSET_PRODUCTION.md)** | Asset selezionati, gap reali, diritto d'uso |
| 10 | **[32 — QA e release](docs/32_QA_RELEASE.md)** | Build, autonomie, melee e multiplayer |
| 11 | **[35 — Decisioni e GAP](docs/35_DECISION_GAPS.md)** | Quello che manca veramente |

Le precedenti idee della città S1/S2/S3 acquistabile, del vecchio protocollo attivato manualmente e delle classi Assaltatore/Ingegnere/Soccorritore sono **ritirate**. I documenti 00–17 e 39–40 v1.1 non prevalgono mai sul V2; eventuali note legacy sono conservate solo per storico.

## Sviluppo in strati definitivi

HordeTemplate base → Player Survival completo → primo AR completo → **Nurse vera** → **machete completo contro Nurse** → HUB base reale → Rottami+Core/save → direttore assalti W1–3 → **prima torretta automatica completa** → assalti persistenti → altri territori, torri, armi, zombie, classi, modalità continua → co-op e build finale. Ogni passaggio include animazioni, effetti audio/video, gameplay e test reali. Niente asset provvisori spacciati per definitivi.

## Ricerca e vincoli

Riferimenti: [The Riftbreaker](https://www.riftbreaker.com/) per l'autodifesa + combattimento fuori, [7 Days to Die](https://7daystodie.wiki.gg/wiki/Blood_Moon_Horde) per escalation assalto, [Killing Floor 2](https://killingfloor2.com/overview/weapons.html) per melee gunplay. Non si importano sistemi di mining/crafting, né codice/mesh di titoli commerciali.

**GitHub pubblico:** file Fab e Marketplace non ridistribuibili raw rimangono in workspace privato. Script bootstrap esistente in [scripts/bootstrap_horde.ps1](scripts/bootstrap_horde.ps1); non compilato né eseguito in Unreal qui.

## Incarico di sviluppo

[Issue #6 — gioco V2 completo](https://github.com/Spidahh/EatMyAss/issues/6). Il backlog è la singola fonte per l'ordine di lavoro. Si comincia dal primo task PLANNED: non si saltano strati e non si inventano asset.
