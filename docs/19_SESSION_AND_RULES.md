# REGOLE DELLA SESSIONE V2 — BASE PERSISTENTE, PLAYER LIBERO

La base non è la mappa dove devi sparare. Il player cammina nell'interno per upgrade, esce nell'esterno per FPS/melee, rientra **in qualunque momento** anche a nemici attivi. L'ondata attacca autonomamente il Nucleo/perimetro nel frattempo. **CoreHP0 è l'unico Game Over della difesa**; morte dei player causa respawn dentro base dopo 10s seed, non sconfitta istantanea. Gli upgrade non richiedono wave pause.

### Stati autorevoli

`BaseLoaded → Preparing → SiegeActive → SiegeResolved → NextStage`. In `Continuous` il director usa stessi stage come soglia di aumento difficoltà e non si ferma: `ContinuousStageActive → NextDifficultyTier`. Ogni player possiede separatamente `InsideBase / OutsideBase / Downed / Respawning`. Il cambiamento della posizione **NON** cambia esistenza/attivazione AI base. Nessun player entra nel terminale upgrade con zombie dentro la sala nella V1.

### Economia e sconfitta

Una sola moneta `Rottami`, conferita da combattimento outside e incarichi, custodita nella base (shared per host co-op). Gli upgrade sono acquistabili solo se `InsideBase` e server validate costo, tier, disponibilità socket. La run non resetta base alla decima onda; decima dà milestone, poi escalation. Salvataggio host ogni upgrade e confine stage, no progress offline. Defeat recuperabile ricaricando checkpoint pre-assalto con ledger coerente.

### Co-op

Listen-host 1–4, base e mondo sono dell'host. Player ospite può combattere fuori, rientrare dentro, avere classe diversa, comprare upgrade condivisi con consenso per spesa rilevante. Se un giocatore muore non spegne torre; anche con 4 Downed la base combatte. Ospiti mantengono equip nella sessione, host salva lo stato della base. Nessun database remoto.

### Regole di qualità

La base è davvero autonoma: log devono mostrare kill tower e riduzione wave senza player presenti, con player remoto ancora attivo. Spawn nemici di assedio solo fuori, mai nel terminale. Un interruttore menu non interrompe i raid. Niente ritorno forzato o teleport automatico tra ondate. Vedi [41](41_CANONICAL_GAME_V2.md), [43](43_AUTONOMOUS_BASE.md), [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).
