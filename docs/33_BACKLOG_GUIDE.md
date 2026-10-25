# BACKLOG TOTALE 1.0 — UNA SOLA FILA DI PRODUZIONE

Questo documento accompagna il [backlog machine-readable](33_FULL_BACKLOG.csv): **80 attività ordinate** e concatenate tramite `depends_on`. Per assicurare “prima finisce una cosa e poi comincia l'altra”, **ogni riga dipende da quella precedente**. Le righe sono pezzi concreti, non 13 milestone fittizie. Ogni completamento richiede l'accettazione della sua spec, build/test e prove visuali pertinenti; non segnare DONE dal solo codice.

## Carico di lavoro per strato

- **L0**: 3 attività — [spec](docs/31_UNREAL_ARCHITECTURE.md)
- **L1**: 6 attività — [spec](docs/13_PLAYER_WEAPON_ANIMATION.md)
- **L2**: 8 attività — [spec](docs/20_COMBAT_WEAPONS.md)
- **L3**: 7 attività — [spec](docs/14_ZOMBIE_COMPLETE.md)
- **L4**: 4 attività — [spec](docs/24_CITY_AND_SECTORS.md)
- **L5**: 5 attività — [spec](docs/26_WAVE_DIRECTOR.md)
- **L6**: 5 attività — [spec](docs/22_DEFENSE_AND_BASE.md)
- **L7**: 6 attività — [spec](docs/22_DEFENSE_AND_BASE.md)
- **L8**: 6 attività — [spec](docs/25_ECONOMY_BALANCE.md)
- **L9**: 5 attività — [spec](docs/24_CITY_AND_SECTORS.md)
- **L10**: 6 attività — [spec](docs/23_CLASSES_ABILITIES.md)
- **L11**: 9 attività — [spec](docs/18_MASTER_GAME_SPEC.md)
- **RC**: 10 attività — [spec](docs/32_QA_RELEASE.md)

## Regole di esecuzione

1. Cercare prima riga diversa da DONE in `33_FULL_BACKLOG.csv`; **solo quella** si lavora. Se blocked, non saltare a riga successiva.
2. Se task completato e verificato, aggiungere evidenza in `37_EXECUTION_STATUS.csv` con SHA, build, video/QA/link e flag DONE; aggiornare status nel backlog nello stesso commit.
3. Asset non disponibile? Aggiungere GAP in [35](35_DECISION_GAPS.md) e cercare fonte gratuita equivalente, mai placeholder. Senza risoluzione resta BLOCKED.
4. Tutti i documenti 19–32 sono specifiche di **tutto il prodotto** e contengono dettagli per le righe; nessun requisito deve essere perso solo perché non ha riga separata.
5. L1–L4 riguardano la prima esperienza FPS completa. L5–RC portano esattamente al gioco promesso. Non fermarsi alla prima esperienza né contrabbandarla come versione 1.0.
6. Test/bugfix inerenti al task fanno parte della sua riga. Le fasi RC sono test incrociati, shipping e performance su intero gioco, **non i soli controlli** previsti.
7. Seed balance numerici sono configurazioni di partenza, non dati definitivi. Vanno chiusi con misure prima di RC.
8. Aggiornare e riusare pacchetti terzi con licenza, non pubblicare file raw Fab/Epic in repo pubblico.

## Esempio di lettura

ZD-001 sceglie ed importa realmente HordeTemplate, ZD-002 ne sistema compatibilità, ZD-003 chiude ambiente reale; ZD-004 importa Survivor, ZD-005 camera e corpo, ... La dipendenza lineare impedisce di saltare fino alla sentry se prima lo zombie non è completo.

Non sostituire 80 task con riassunti vaghi. Questo backlog è un **contratto operativo di produzione**.
