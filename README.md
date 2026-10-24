# Zombie Defence — Unreal Engine FPS + Tower Defense

Progetto in preproduzione per un gioco **FPS 3D di sopravvivenza a ondate zombie con difesa ed espansione della base**. Armi e potenziamenti, classi e abilità, barricate e torrette, un Nucleo da proteggere, zone da sbloccare. Il combattimento diretto rimane il fulcro: non è un gioco idle o un gestionale.

**Data dossier:** 24 ottobre 2026 · **Versione:** v0.1 · **Stato:** concept e progettazione completati; codice di gioco **non ancora implementato né testato** in questo repository.

## Da dove iniziare

1. **[Panoramica e prima decisione](docs/00_START_HERE.md)** — obiettivo, ordine di lavoro e scelta della base Unreal.
2. **[Game Design Document](docs/01_GAME_DESIGN.md)** — loop, classi, zombie, ondate, difese, risorse e mappa.
3. **[Technical Design](docs/02_TECH_DESIGN.md)** — architettura, dati, replication, IA, salvataggi e performance.
4. **[Catalogo asset verificati online](docs/03_ASSETS.csv)** — link dei pack reali, gratuità osservata e controlli necessari.
5. **[Roadmap e backlog](docs/05_ROADMAP.md)** — milestone, dipendenze e criteri per dichiarare un'attività conclusa.

## Tutta la documentazione

| File | Scopo |
| --- | --- |
| [00_START_HERE.md](docs/00_START_HERE.md) | Sintesi, scope e gate tecnico G0 |
| [01_GAME_DESIGN.md](docs/01_GAME_DESIGN.md) | Progetto completo delle meccaniche |
| [02_TECH_DESIGN.md](docs/02_TECH_DESIGN.md) | Componenti Unreal e interfacce fra sistemi |
| [03_ASSETS.csv](docs/03_ASSETS.csv) | Registro sorgenti, prezzi, licenze e test asset |
| [04_ASSET_PIPELINE.md](docs/04_ASSET_PIPELINE.md) | Direzione artistica, import e licenze |
| [05_ROADMAP.md](docs/05_ROADMAP.md) | Piano a sprint e backlog tracciabile |
| [06_TEST_MATRIX.md](docs/06_TEST_MATRIX.md) | Test riproducibili e prove di accettazione |
| [07_AI_DEV_CONTRACT.md](docs/07_AI_DEV_CONTRACT.md) | Regole operative per Codex/AI |
| [08_DECISIONS_AND_RISKS.md](docs/08_DECISIONS_AND_RISKS.md) | Decisioni, ipotesi e rischi |
| [09_BALANCE_SEED.csv](docs/09_BALANCE_SEED.csv) | Parametri iniziali delle 10 ondate, **non bilanciati** |
| [10_ECONOMY_SEED.csv](docs/10_ECONOMY_SEED.csv) | Costi iniziali di acquisti/upgrade, **non bilanciati** |

## Prima attività concreta: audit della base open source

La prima opzione da valutare è **[HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate)**. Il suo autore dichiara Unreal 5.8, co-op fino a 4 giocatori, ondate zombie, armi, inventario, IA e lobby; il repository ha una licenza MIT. **Non è una scelta definitiva:** prima di adottarlo bisogna compilare il progetto, eseguire sessioni host+client, verificare l'effettiva qualità di gioco e licenziare separatamente gli eventuali asset di terzi inclusi.

Se il gate G0 fallisce, la riserva è **[Lyra Starter Game](https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine)**. Il [template First Person Arena Shooter](https://dev.epicgames.com/documentation/unreal-engine/first-person-template-in-unreal-engine) è utile per un confronto sul gunplay, ma non va sommato indiscriminatamente agli altri progetti.

## Vertical slice da realizzare

Una mappa industriale, 6 ondate, 3 armi, 3 tipi di zombie, 1 Nucleo da difendere, 1 barricata, 1 torretta, 1 classe completa e 1 settore che si apre. Il primo test multigiocatore deve prevedere almeno due client sincronizzati. Poi si valuteranno le 10 ondate, 3 classi, boss e ulteriori sistemi.

## Struttura del repository

```text
/
├── README.md             # punto di ingresso
├── AGENTS.md             # istruzioni ai coding agent
├── .gitignore            # esclusioni Unreal future
└── docs/
    ├── 00_START_HERE.md
    ├── 01_GAME_DESIGN.md
    ├── 02_TECH_DESIGN.md
    ├── 03_ASSETS.csv
    ├── 04_ASSET_PIPELINE.md
    ├── 05_ROADMAP.md
    ├── 06_TEST_MATRIX.md
    ├── 07_AI_DEV_CONTRACT.md
    ├── 08_DECISIONS_AND_RISKS.md
    ├── 09_BALANCE_SEED.csv
    └── 10_ECONOMY_SEED.csv
```

Il futuro progetto Unreal andrà in root (o in una cartella dedicata scelta al gate G0), **non** si importa alla cieca prima di avere una baseline scelta. Per gli asset: il catalogo registra dei *candidati verificati sulle pagine dei produttori*, non dei pacchetti già acquisiti/validati nel motore.

## Vincoli

- Budget iniziale quasi nullo; evitare acquisti e servizi a consumo non autorizzati.
- Un solo framework gameplay principale, interfacce pulite e dati configurabili.
- Nessun asset senza provenienza e licenza documentate.
- Nessun ticket dichiarato `DONE` senza compilazione/test applicabili ed evidenza.
- No pay-to-win, niente sistema factory/idle che sostituisca lo sparatutto.

Le istruzioni operative dettagliate sono in [AGENTS.md](AGENTS.md). La scelta definitiva di stile, multiplayer al lancio e scope è registrata in [decisioni e rischi](docs/08_DECISIONS_AND_RISKS.md).
