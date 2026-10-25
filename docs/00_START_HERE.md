> **AVVISO DI PRECEDENZA (25/10/2026):** per la produzione attuale leggere prima [AGENTS.md](../AGENTS.md), [12_PRODUCTION_ORDER.md](12_PRODUCTION_ORDER.md) e [17_CODEX_EXECUTION.md](17_CODEX_EXECUTION.md). Le fasi, le scelte di base tecnica e gli asset descritti qui sotto sono **materiale storico di progettazione** e non autorizzano Codex a iniziare più sistemi contemporaneamente. HordeTemplate è la baseline designata e la prima consegna è personaggio + un fucile + una zombie + primo isolato, completati in quell'ordine.

# ZOMBIE DEFENCE — Master dossier v0.1

**Data ricerca:** 24 ottobre 2026 · **Motore di riferimento:** Unreal Engine 5.8 · **Stato:** preproduzione; nessun gioco compilato, nessun asset scaricato, nessuna compatibilità certificata in runtime.

> Nome *Zombie Defence* provvisorio, non è una verifica di disponibilità del marchio.

## 1. Visione in 30 secondi

FPS 3D in prima persona, per PC, giocabile in solitaria e progettato per **co-op fino a quattro persone**. I giocatori difendono un avamposto industriale durante assalti zombie, uccidono personalmente i nemici e trasformano il campo di battaglia: armi da migliorare, tre classi con abilità, barricate, torrette, trappole, base centrale potenziabile e settori della mappa da conquistare. L'obiettivo non è un gestionale o un idle: **lo sparatutto resta il cuore del gioco**.

Tre promesse al giocatore:

1. **Shooting appagante:** colpi leggibili, headshot, hit reaction, feedback audio/visivo, armi diverse.
2. **Ogni spesa cambia il combattimento:** la stessa risorsa può rafforzare il giocatore, una torretta o la base; il trade-off è reale.
3. **Il territorio cambia:** si parte stretti, poi si aprono zone e linee difensive, aumentando sia le opportunità sia i punti deboli.

## 2. Decisione tecnica più importante

**Candidato A — primo da provare: [DasBander/HordeTemplate](https://github.com/DasBander/HordeTemplate).** Il README dichiara Unreal 5.8, C++ nativo, co-op 4 giocatori, lobby, shooting, zombie wave spawner, shop, inventario, AI e obiettivi. Il repository presenta una licenza MIT sul codice. È il candidato con la maggiore sovrapposizione funzionale al nostro progetto. **Non è ancora certificato da noi**: va compilato, esaminato e testato su due istanze, e vanno censiti i diritti dei contenuti grafici/audio. Nota: nel README il comando `git clone` punta a un repository con nome diverso dal repository pubblicato; seguire l'URL della pagina reale, non copiare alla cieca il comando riportato.

**Candidato B — [Lyra Starter Game](https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine):** base Epic modulare, armi, multiplayer, capacità GAS e UI, ma non nasce per ondate zombie e tower defence. Riserva qualora A fallisca la valutazione tecnica.

**Candidato C — [First Person / Arena Shooter](https://dev.epicgames.com/documentation/unreal-engine/first-person-template-in-unreal-engine):** base ufficiale veloce per provare il gunplay (armi, AI, HUD). Non va scambiata per un template co-op completo; utile per un prototipo separato, non da mescolare direttamente ad A o B.

**Regola:** una sola base di codice per la produzione. Non accorpare interi sistemi delle tre demo. Misurare prima di scegliere.

### Test decisivo di 2–4 giornate effettive, prima di qualsiasi feature

1. Clonare A in un progetto di prova *separato*. Aprire e compilare con versione UE 5.8 e toolchain documentata.
2. Avviare una mappa offline e una sessione host + client, uccidere zombie, comprare un'arma e verificare sincronizzazione HP, crediti, munizioni, ondate e morti.
3. Controllare log, asset mancanti, plugin richiesti, path hardcoded, qualità del movimento/shooting, codice realmente incluso e file di licenza dei **contenuti**.
4. Misurare 50 nemici attivi in scena di prova per 10 minuti con il PC bersaglio configurato; niente promessa di prestazione prima della misura.
5. Decisione registrata: **GO** (riusare l'ossatura); **PATCH** (debito tecnico limitato con stima); **NO-GO** (passare a Lyra senza trascinare dipendenze irrisolte).

## 3. Contenuto dell'archivio

| File | A cosa serve |
| --- | --- |
| `01_GAME_DESIGN.md` | GDD: loop, classi, zombie, torrette, base, economia, espansione, partita e bilanciamento |
| `02_TECH_DESIGN.md` | Struttura Unreal, componenti, contratti dati, IA, multiplayer, salvataggi, prestazioni, integrazioni |
| `03_ASSETS.csv` | Registro con **asset realmente individuati**, link originali, gratuità, formato, rischi e test richiesti |
| `04_ASSET_PIPELINE.md` | Art direction, qualità, import, retargeting, licenze, validazioni e fallback |
| `05_ROADMAP.md` | Passaggi, dipendenze, criteri di accettazione, backlog MVP/V1/post-lancio |
| `06_TEST_MATRIX.md` | Prove riproducibili di gameplay, rete, IA, exploit, contenuti, compatibilità e performance |
| `07_AI_DEV_CONTRACT.md` | Istruzioni operative per Codex/AI che implementa, con Definition of Done anti-invenzioni |
| `08_DECISIONS_AND_RISKS.md` | Decisioni assunte, ipotesi, elementi ancora aperti, rischi e misure preventive |
| `09_BALANCE_SEED.csv` | Parametri **esemplificativi da playtestare**, non presentati come già bilanciati |
| `10_ECONOMY_SEED.csv` | Costi fittizi da verificare in simulazione e playtest |

## 4. Scope economico e realistico

- Target iniziale: **0 € di acquisto di asset** se passano le prove. L'asset gratuito non significa automaticamente adatto né privo di vincoli.
- Unreal Engine per sviluppo giochi: piano royalty dopo la soglia pubblicata di 1 milione USD di ricavi lordi per prodotto; termini da ricontrollare prima della pubblicazione: https://www.unrealengine.com/license
- Niente server a pagamento nel prototipo: prima offline + LAN/listen-server. Online pubblico, relay, matchmaking, costi operativi e anti-cheat sono da valutare dopo una build di co-op stabile.
- Non pianificare oggi 100 zombie *networked* con mesh costose. Il tetto attivo verrà deciso misurando gameplay, CPU game thread, animazione, navigation e rete.
- Non considerare le 7 armi di un pack come 7 armi già *giocabili*: mesh, reload, ADS, recoil, audio, bilanciamento e animazioni sono lavori diversi.

## 5. Cosa realizziamo prima, davvero

**Vertical slice giocabile, una sola mappa:** fabbrica con ingresso e cortile; un nucleo difensivo, sei ondate e una mini-finale; giocatore con pistola/fucile/fucile a pompa (se il template supporta i tipi), zombie lento/rapido/corazzato, barricata, torretta e una sola classe completa. Un settore che si apre e un upgrade al nucleo. UI chiara e una sessione 2-player senza desync.

**V1 mirata:** dieci ondate, tre classi, 3-4 archetipi zombie + boss, 3 strutture + barricate, 3 settori collegati, upgrade per armi/base, economia con due valute semplici, co-op 1–4 verificata e menù/save appropriati.

Il vertical slice serve a dimostrare che la miscela *FPS + difesa* è divertente. Se non lo è, aggiungere sistemi non la risolve.

## 6. Fonti primarie da cui parte il dossier

- Unreal 5.8: https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available
- HordeTemplate: https://github.com/DasBander/HordeTemplate e licenza https://github.com/DasBander/HordeTemplate/blob/master/LICENSE.md
- Lyra e abilità: https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine e https://dev.epicgames.com/documentation/unreal-engine/abilities-in-lyra-in-unreal-engine
- Template FPS: https://dev.epicgames.com/documentation/unreal-engine/first-person-template-in-unreal-engine
- Replication: https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine
- Licenza Fab: https://www.fab.com/eula
- Licenza Unreal: https://www.unrealengine.com/license

## 7. Prossima azione immediata (non ancora eseguita)

1. Creare il repo Unreal dopo una decisione sulla base.
2. Mettere l'integrazione di tutti gli asset dietro il registro `03_ASSETS.csv`.
3. Compilare, eseguire la batteria di test al gate G0, produrre screenshot del gameplay e numeri, *poi* pianificare sprint di feature.

