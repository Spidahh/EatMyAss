> **NON APPROVATO / IN REVISIONE (26/10/2026):** le precedenti classi, abilità (“colpo preciso”), numero di zone esterne, economia, ondate e altre scelte specifiche in questo documento sono PROPOSTE DELL'ASSISTENTE, non decisioni dell'utente. **Nuova direttiva: mappa come COD Zombies con esplorazione e ZONE SBLOCCABILI, base da cui entrare/uscire solo per upgrade e che si autodifende, melee e idee originali.** Per la fonte autorevole leggere [45_USER_DIRECTIVES.md](45_USER_DIRECTIVES.md) e [46_PLAYER_JOURNEY_REQUIREMENTS.md](46_PLAYER_JOURNEY_REQUIREMENTS.md). Codex non deve implementare quanto contraddice queste direttive.

# MASTER SCOPE — ZOMBIE DEFENCE V2

**SOSTITUISCE INTEGRALMENTE LA PRECEDENTE MASTER SPEC 1.0.** Definizione dettagliata, autorevole: [41 — V2](41_CANONICAL_GAME_V2.md), [42 — combattimento/melee/classi](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 — base autonoma](43_AUTONOMOUS_BASE.md), [44 — esterno/progressione](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).

## Prodotto bloccato

Un gioco **FPS + melee action**, dentro una base-upgrade attraversabile e fuori in territori di combattimento. La base si autodifende per mezzo di torrette *server-autonome* anche senza player in range. La progressione non resetta dopo ogni match. Onestà del design: il livello della base determina quali assalti riesce a respingere senza intervento; col tempo l'ondata cresce. Rottami è l'unica moneta, le armi sono sette categorie (4 ranged, 3 melee), 3 specializzazioni (Tiratore/Spezzatore/Tecnico), due torrette automatiche + barriera, 5 zombie archetipi, 10 stadi + continuation, 1 hub + 3 zone esterne di battaglia, PC host 1–4 co-op.

**NESSUNA “città come base” e NESSUN “player sempre sul muro a sparare”.** La mappa esterna può ricordare un distretto urbano abbandonato ma serve al combattimento; non ci sono aree S1–S3 da comprare.

## Condizioni di sconfitta e persistenza

GameOver su Nucleo distrutto, non se tutti i giocatori vengono abbattuti temporaneamente. Respawn player dentro base, difese continuano. Assalti 10+ crescente, modalità ondate o continua sullo stesso director; base/upgrade persistono su checkpoint locale host fra sessioni, nessun avanzamento di tempo offline. Solo 1 valuta Rottami accreditata da kill/eventi di combattimento. Upgrade solo dentro base, anche durante gli assalti.

## Interpretazione dei documenti

I documenti 19–32 sono riletti in versione V2 e contengono requisiti specialistici. Il vecchio dossier 00–17 e 39–40 è storico/ritirato nei punti incompatibili; 41–44 governano. Codex DEVE usare soltanto `33_FULL_BACKLOG.csv` V2 aggiornato e la matricola `38_RELEASE_CONTENT_MATRIX.csv`.

## Fuori scope

No farming minerale/crafting, nessuna produzione passiva a game chiuso, no city builder, no base con lavoratori e fabbriche, niente PvP, MMO o battle royale, niente perk deck infinito, nessun framework concorrente a HordeTemplate, nessun servizio a pagamento senza consenso. Non chiamare Done un modulo incompleto di animazioni e audio.
