# ZOMBIE DEFENCE — REGOLE VINCOLANTI DI PRODUZIONE PER CODEX

**Versione attiva 1.1 — 25 ottobre 2026.** Questo file governa **l'intero gioco fino alla release 1.0**, non soltanto i primi quattro strati. Su punti incompatibili sostituisce i documenti storici 00–17.

## MISSIONE E FONTE DI VERITÀ

Devi costruire in Unreal Engine 5.8 un **FPS action zombie cooperativo 1–4 con ondate + tower defense + base upgradabile + città che si espande**, pronto Windows, riutilizzando [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate). Il prodotto completo (1.0) richiede **4 armi, 5 archetipi zombie incluso boss, 3 difese, 3 classi, Nucleo aggiornabile, 10 ondate, 4 settori di città, due valute, upgrade, multiplayer, UI/UX, audio, VFX, animazioni e packaging**. Niente gestionale negozio, idle, survival crafting, battle royale, asset di COD o P2W.

Leggi **in quest'ordine prima di ogni nuovo lavoro**:
1. **[Specifica madre](docs/18_MASTER_GAME_SPEC.md)** — il gioco completo, obiettivi e scope finale. Leggi anche **[40 — skill e sinergie città](docs/40_SYNERGIES_SKILLS_AND_CITY.md)**: decisioni V1.1 limitate e vincolanti.
2. **[Backlog sequenziale](docs/33_FULL_BACKLOG.csv)** e **[Guida](docs/33_BACKLOG_GUIDE.md)** — tutti gli **80 task** dal framework fino alla release, ogni task dipende dal precedente. Non saltare la prima riga non DONE.
3. **[Master brief Codex](docs/34_CODEX_MASTER_BRIEF.md)** — modalità operativa e divieti.
4. **[Matrice contenuti](docs/38_RELEASE_CONTENT_MATRIX.csv)** — completezza animazioni, mesh, suoni, VFX, AI e rete per ogni elemento.
5. **[Gap reali](docs/35_DECISION_GAPS.md)** e **[Asset](docs/30_ASSET_PRODUCTION.md)** — mancanze e fonti legali.
6. Documento specialistico del task: [partita](docs/19_SESSION_AND_RULES.md), [armi](docs/20_COMBAT_WEAPONS.md), [zombie](docs/21_ZOMBIES_AI.md), [difese/base](docs/22_DEFENSE_AND_BASE.md), [classi](docs/23_CLASSES_ABILITIES.md), [città](docs/24_CITY_AND_SECTORS.md), [economia](docs/25_ECONOMY_BALANCE.md), [onde](docs/26_WAVE_DIRECTOR.md), [rete](docs/27_MULTIPLAYER_SAVE.md), [UI](docs/28_UI_AND_INPUT.md), [audio/anim/VFX](docs/29_ANIMATION_AUDIO_VFX.md), [architettura](docs/31_UNREAL_ARCHITECTURE.md), [QA](docs/32_QA_RELEASE.md), [release](docs/36_RELEASE_AND_OPERATIONS.md).
7. Solo per i dettagli specifici della prima produzione: docs/12–17. I precedenti docs/00–11 sono storici e non creano nuovi task.

## REGOLE DI ESECUZIONE

- **UNO STRATO/UN TASK ALLA VOLTA.** Fai la prima riga non DONE, completa **anche** asset reali, animazioni, blend, SFX, VFX, UI, co-op, regole server e build quando pertinenti. Non sviluppare altre feature “per comodità”.
- **VIETATI I PLACEHOLDER FINALI.** No mannequin, cubi, zombie low-quality, eventi senza animation, test map spacciate per città, clip/effetti generici mai rifiniti. L1 player REAL Survival Character; L2 AR reale dal FPS Weapon Bundle; L3 Nurse reale, poi città. Gli altri asset si approvano quando arriva il loro task; non inventare il nome di mesh non scaricate.
- **Nessun numero/compatibilità inventato:** seed bilanciamento non sono valori certificati; non supporre 7 armi tutte buone né zombie con 15 animazioni. Repertorio in docs/30.
- **HordeTemplate fisso** come base. Non aprire nuovi comparativi con Lyra e non iniziare codice FPS da zero. Se la base presenta bug, patch circoscritte nel progetto. Non aggiungere nuovi framework duplicati.
- **Server autorevole:** ammo, danni, HP, morte, onde, Nucleo, acquisti, classi e settori. TxnId idempotenti; no reward doppia; death indipendente da `DamageCauser` player.
- **Asset licenze:** il GitHub è PUBBLICO. Nessun file raw Fab/Epic/Marketplace che non consente redistribuzione isolata. Scaricare solo tramite canali legali autorizzati, conservare asset in workspace PRIVATO, documentare manifest e utilizzare nella build cooked in conformità alla licenza; no acquisti o API a consumo non autorizzati.
- **NO loop di demo/bozze che restano.** I test sono parte del completamento delle feature reali, non un progetto parallelo. Se mancano strumenti engine, scrivi IN PROGRESS/BLOCKED con prova precisa di cosa manca, non DONE.
- **SKILL DI GIOCO V1.1:** solo V spinta, Q di classe, ping middle mouse, E impulso del Nucleo sul pannello (una volta/wave), 3 passivi settore. Vedi docs/40. Niente altri tasti skill, valute o carte casuali.
- **CONTINUA FINO ALLA 1.0:** arrivare a L4 non equivale a finire il gioco. Prosegui L5–RC in ordine col backlog, senza dimenticare difese, economy, 10 ondate, classi, boss, rete e pubblicazione.
- **CHANGE CONTROL:** nuove idee non incluse nelle spec si documentano in docs/35 e si chiedono solo se cambiano sostanzialmente scope; non aggiungere spontaneamente artiglieria, infinite mode, MMO, server persistenti.

## PROVE E CRITERI DONE

Compilazione e avvio REALI in Unreal, asset legalmente acquisiti, animazioni verificate, audio/VFX reali, gameplay video dove pertinente, sincronizzazione client/server e regressioni del task. Aggiorna il record specifico in `docs/33_FULL_BACKLOG.csv` da `PLANNED` a `DONE` **soltanto** quando tutte le acceptance sono osservabili. Aggiorna anche `docs/37_EXECUTION_STATUS.csv` con commit, build, prove e bug. Nessuna prova => IN PROGRESS/BLOCKED, non DONE. Leggi [QA release](docs/32_QA_RELEASE.md).

## PRIMA AZIONE QUANDO CODEX APRE IL REPO

Individua ZD-001 (L0) dal backlog, controlla Git status/engine, esegui con i file realmente disponibili, poi ZD-002 solo dopo DONE. Il bootstrap `scripts/bootstrap_horde.ps1` può aiutare in Windows **ma non è stato eseguito dall'autore del dossier**. Non chiedere un altro piano, **implementa**.

**Stato verificato del repository oggi:** contiene documentazione, backlog e helper, **non** il progetto Unreal compilato. Nessuno degli 80 task è stato marcato DONE.
