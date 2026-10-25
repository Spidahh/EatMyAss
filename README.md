# Zombie Defence — Unreal Engine FPS + Tower Defense

**Stato:** inizio produzione a strati (documenti pronti, **gioco Unreal non ancora creato in questo repository**). Ultimo aggiornamento: 25 ottobre 2026. Repository pubblico: non caricare mesh/audio/animazioni Fab o Epic in sorgente senza esplicito diritto di redistribuzione.

## Il lavoro concreto adesso

**Una base definita:** [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate) su Unreal Engine 5.8. **Un solo personaggio:** [Survival Character](https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e). **Un solo fucile d'assalto:** selezionato dai modelli veri di [FPS Weapon Bundle](https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5). **Una sola zombie:** [Zombie Female: Nurse](https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc). Piccolo settore di città urbana industriale, il resto in costruzione.

Prima completare **player reale e tutte le animazioni di movimento**; poi il **fucile vero** con mani, mira, sparo, ricarica, effetti e audio; poi la **zombie vera** con IA, locomozione, attacchi, hit reaction e morte; infine una prima scena cittadina rifinita. Solo **dopo** si realizzano ondate, torrette, upgrade, classi e ampliamento base, uno per volta.

Niente mannequin o cubi spacciati per modelli finali, niente placeholder che rimangono, niente codice inventato, niente sistemi iniziati e abbandonati. Il file AGENTS.md è la regola primaria per Codex.

### Istruzioni vincolanti (LEGGERE IN QUEST'ORDINE)

| Documento | Contenuto |
| --- | --- |
| **[AGENTS.md](AGENTS.md)** | **Contratto di lavoro principale per Codex; ha precedenza sugli altri** |
| **[12_PRODUCTION_ORDER.md](docs/12_PRODUCTION_ORDER.md)** | Scelte definitive e fasi L0–L11 |
| **[15_ASSET_LOCK.md](docs/15_ASSET_LOCK.md)** | Pacchetti reali obbligatori, licenze, divieti |
| **[13_PLAYER_WEAPON_ANIMATION.md](docs/13_PLAYER_WEAPON_ANIMATION.md)** | Animazioni, sistema FPS, un'arma completa |
| **[14_ZOMBIE_COMPLETE.md](docs/14_ZOMBIE_COMPLETE.md)** | Zombie completo, comportamento, animazioni, audio/VFX |
| **[16_CITY_GROWTH.md](docs/16_CITY_GROWTH.md)** | Prima strada cittadina e crescita per settori |
| **[17_CODEX_EXECUTION.md](docs/17_CODEX_EXECUTION.md)** | Mandato operativo esatto per avviare lo sviluppo |

### Altri documenti: riferimento NON prioritario

| Documento | Scopo |
| --- | --- |
| [00_START_HERE.md](docs/00_START_HERE.md) | Dossier iniziale, da interpretare secondo il nuovo ordine |
| [01_GAME_DESIGN.md](docs/01_GAME_DESIGN.md) | Progetto complessivo del gioco dopo la prima scena |
| [02_TECH_DESIGN.md](docs/02_TECH_DESIGN.md) | Architettura futuri sistemi |
| [03_ASSETS.csv](docs/03_ASSETS.csv) | Catalogo di candidate risorse per fasi future |
| [04_ASSET_PIPELINE.md](docs/04_ASSET_PIPELINE.md) | Convenzioni di grafica, import, diritti |
| [05_ROADMAP.md](docs/05_ROADMAP.md) | Roadmap precedente, superata dove contrasta con L0–L11 |
| [06_TEST_MATRIX.md](docs/06_TEST_MATRIX.md) | Suite QA future, non sprint autonomi |
| [07_AI_DEV_CONTRACT.md](docs/07_AI_DEV_CONTRACT.md) | Precedente contratto, sostituito da AGENTS.md |
| [08_DECISIONS_AND_RISKS.md](docs/08_DECISIONS_AND_RISKS.md) | Storico decisioni e rischi |
| [09_BALANCE_SEED.csv](docs/09_BALANCE_SEED.csv) | Numeri non bilanciati per fasi avanzate |
| [10_ECONOMY_SEED.csv](docs/10_ECONOMY_SEED.csv) | Seed costi per fasi avanzate |
| [11_G0_HORDE_AUDIT.md](docs/11_G0_HORDE_AUDIT.md) | Audit statico esistente, **non** gate preproduzione autonomo |

## Prima issue produttiva

[Elenco Issues](https://github.com/Spidahh/EatMyAss/issues) — usare **L0→L4** come unico incarico, e non aprire quattro task separati di indagine mentre player e primo nemico restano non prodotti.

## Note tecniche e legali

HordeTemplate è scelto come framework iniziale, **ma nessuna sua build è stata eseguita qui**. Gli asset esterni scelti sono indicati come gratuiti sulle pagine Fab, ma non sono stati scaricati nell'account dell'utente. Non attribuire un numero di clip a un pack senza ispezionarlo. La compilazione/QA e l'eventuale verifica diritti diventano **attività interne allo strato che utilizza il materiale**, non una serie di progetti separati. I sorgenti MIT possono essere riusati rispettando i notices; i raw binari Fab/Epic non vanno pubblicati indiscriminatamente.

Questo repository contiene la documentazione e potrà contenere il codice con diritto di redistribuzione e i manifest. Il contenuto binario protetto va gestito in workspace privato fino a eventuale scelta di rendere il repo privato.
