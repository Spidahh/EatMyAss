> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

> **AGGIORNAMENTO VINCOLANTE 25/10/2026:** questo file descrive solo l'inizio; il piano **integrale fino alla release 1.0** è in [18_MASTER_GAME_SPEC.md](18_MASTER_GAME_SPEC.md), [33_FULL_BACKLOG.csv](33_FULL_BACKLOG.csv) e [34_CODEX_MASTER_BRIEF.md](34_CODEX_MASTER_BRIEF.md). AGENTS.md governa tutte le fasi, non fermarti a L4.

# PIANO DI PRODUZIONE VINCOLANTE v0.2 — UN SISTEMA PERFETTO ALLA VOLTA

## 1. Cambio di metodo deciso il 25 ottobre 2026

Abbandoniamo le precedenti milestone intese come demo per vedere “se funziona”: **HordeTemplate è la base designata**, non un candidato da rimettere continuamente in discussione. Si parte a produrre dall'avatar e dalla prima arma; niente sviluppo in parallelo del TD. Gli asset devono essere reali e all'altezza della produzione. Non serve creare sistemi temporanei che il futuro team dimenticherà di rimpiazzare.

Qualità massima sostenibile a costo quasi zero: “perfetto” è un **criterio di uscita rigoroso** (funziona, si vede, suona, anima, si usa, si mantiene), non una garanzia magica o una scusa per non iniziare. La compilazione e i test del codice restano parte della realizzazione professionale, ma **non un progetto di prova separato**.

## 2. Decisioni bloccate

| Voce | Scelta |
| --- | --- |
| Engine | Unreal Engine 5.8, stesso pin del pacchetto sorgente |
| Framework | [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate), C++ / Blueprint solo per presentazione e data |
| Platform | Windows PC |
| Camera | FPS, con corpo completo coerente visibile agli altri; armi realmente impugnate |
| Player definitivo iniziale | [Survival Character — Arberry](https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e) |
| Arma definitiva iniziale | **Una** carabina/fucile d'assalto scelto realmente all'interno di [FPS Weapon Bundle — Deadghost Interactive](https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5) |
| Zombie definitivo iniziale | [Zombie Female: Nurse — RamsterZ](https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc) |
| Animazioni umane | locomozione da [Game Animation Sample Epic](https://dev.epicgames.com/documentation/unreal-engine/game-animation-sample-project-in-unreal-engine) se compatible con skeleton e retarget; azioni armi con set realmente presente o creato tramite strumenti gratuiti, niente loop fasulli |
| Animazioni zombie | Nurse include 3 clip; integra [Zombie Animation Pack: Standard — QuokkaVoid](https://www.fab.com/listings/82b55c77-c706-4634-839e-29ba827dac8d) per completare solo le azioni effettivamente disponibili; retarget, non supporre la copertura |
| Scenario iniziale | primo isolato urbano/industriale praticabile, resto della città in costruzione |
| Multiplayer | mantenere la struttura replicata del framework dal primo strato, controllo host-client dello strato finito |
| Budget | **0 € di nuovi acquisti** come target; nessun pagamento automatico |
| Stile | umano realistico adulto, urban decay/industriale, illuminazione leggibile, nessun mashup cartoon |

Le schede Fab oggi espongono Free per Player, Weapon Bundle, Nurse e pack animazioni; ciò non significa licenza acquisita sull'account e nemmeno asset scaricato. I record “Allows usage with AI: No” non autorizzano l'uso per raccolte dati generative. Prima di far manipolare asset a servizi esterni verificare le relative licenze.

## 3. Ordine immutabile degli strati

**L0 — Fondazione diretta nel progetto reale**  
Aprire HordeTemplate 5.8, creare la struttura modulare del nostro gioco e il branch di produzione. Preservare crediti/license. Non effettuare una serie di demo comparative o tre fork. Se compare un errore, correggerlo nel progetto reale; se non è possibile, registrare il blocco preciso. Uscita: progetto avviabile, repo source pulito, nessun nuovo gameplay.

**L1 — Player definitivo: modello + movimento + camera.**  
Importare Survival Character, skeletro/retarget con asset locali approvati, camera FPS con vista mani e full-body coerente, capsule/movement. Tutte le animazioni di movimento previste in docs/13 funzionanti, compreso blend e networking. Niente pistola provvisoria, niente torso/mannequin visibili. L1 **non è completo** senza animazione, camera, look e suoni dei passi.

**L2 — Un fucile definitivo con gunplay FPS completo.**  
Importare UNA vera arma del pack indicato, allineare mani/sockets, ADS, fuoco, ammo, ricarica, equip/unequip, camminare/sprintare con arma, recoil, visibilità in prima e terza persona, VFX muzzle/brass/impact, SFX distinti, UI munizioni e hit feedback. Collegare al sistema HordeTemplate, non sostituirlo con una nuova architettura ad hoc. **Non iniziare seconda arma** finché L2 non è verificato e convincente.

**L3 — UNA zombie definitiva e interazione di combattimento.**  
Importare Nurse, portare a termine ogni animation state realmente richiesto (docs/14), pathfinding, percezione, inseguimento, attacco con finestra corretta, danno, stagger, morte, ragdoll/death, suoni, sangue/impatti misurati, headshot, cleanup. Completo significa il giocatore spara, colpisce, zombie reagisce/attacca/muore con animazione credibile. **Non aggiungere altre varianti**.

**L4 — Un incontro completo e rifinito in città in costruzione.**  
1 spazio permanente piccolo, illuminazione coerente, coperture, collisioni, spawn/respawn controllati di 1 zombie alla volta, HUD essenziale, audio ambientale; esperienza fluida, concreta e presentabile, non menu demo o livello tutto cubi. Rieseguire L1/L2/L3 insieme, correzioni e build Windows. Questo è il **primo traguardo pubblico dell'esecuzione**, non la modalità Zombie Defence completa.

**L5 — Loop delle ondate e un piccolo gruppo di zombie.**  
Solo dopo L4 aggiungere gli stati di round definitivi, 2–3 zombie attivi in sequenza, uno schema di ondate con obiettivi e punti coerenti. Nessun secondo modello finché non necessario.

**L6 — Nucleo base e UNA barricata completa.**  
Difesa Nucleo, danni da zombie, riparazione, barricata finale con animazioni/UI/suoni, percorso zombie corretto. Una funzione chiusa prima di procedere.

**L7 — UNA torretta completa.**  
Sentry reale (mesh, rotazione, linea vista, munizioni/heat, effetti, prioritizzazione, danni attribuiti e sconfitta zombie anche senza killer di tipo Character), acquisto/riparazione con transazioni server, animazioni, UI e suoni. Non implementare molte torri assieme.

**L8 — Economia upgrade e progressione dentro run.**  
Arma, torre, Nucleo, fondi personali/squadra, costi configurabili, nessun doppio acquisto, feedback visuale. Prima rifinire un upgrade per ognuno, poi aggiungere tier.

**L9 — Espansione primo settore della città.**  
Porte, area urbana nuova, navigazione, nuovi spawn, rischio/ricompensa, nuove postazioni difesa. Città non più tutta in costruzione: estensione curata un settore per volta.

**L10 — Classi e abilità, una alla volta.**  
Assaltatore completo, poi Ingegnere, poi Soccorritore. Animazioni, audio, VFX, UI e multiplayer di ogni skill prima di aggiungerne un'altra.

**L11 — Contenuto aggiuntivo.**  
Nuove armi **una alla volta**, nemici speciali **uno alla volta**, nuove torrette e altre ondate; poi multiplayer 1–4 stabilizzato, opzioni, distribuzione, ottimizzazione.

Il contenuto dei vecchi file 01–11 resta valido come banca di idee e requisiti finali, **non** autorizza Codex a saltare l'ordine L0–L11.

## 4. Regola di avanzamento automatica

Per ogni strato: implementa completamente → anima → audio/VFX → collegamenti → HUD → correggi bug → package → prova funzionale e visiva → salva commit e breve report. Se manca una cosa non passare oltre: correggila **nello stesso strato**. Se una dipendenza/licenza è irrisolvibile senza soldi, scrivi BLOCKED e non inserire un sostituto di comodo. Se è risolvibile con tool gratuiti e modifica delle risorse consentita, esegui e documenta.

**Proibite le etichette “temporaneo”, “placeholder”, “bozza da rimpiazzare” sui file che entrano nel gioco prodotto.** Puoi lasciare incompleta la città perché è uno **strato futuro dichiarato**, non riempire il gameplay con false soluzioni.

## 5. Architettura: preparare per dopo senza implementare tutto subito

- Mantieni una sola origine degli stati gameplay sul server; dati progressivamente in DataAssets, mai costi e HP sparsi nei widget.
- Nome moduli di estensione prefisso ZD, separati dai sorgenti upstream; evitare duplicare armi, inventario e IA se già solidi.
- Prevedi gli eventi: OnWeaponHit, OnZombieDamaged, OnZombieKilled, OnWaveStateChanged, OnCoreDamaged, OnDefenseBuilt, OnSectorUnlocked. **Esporre interfacce solo quando lo strato pertinente le necessita**, non stub inutili.
- File di config reali in Source/ZD e Content/ZD; risorse terze conservate secondo le loro licenze in workspace PRIVATO, non nel pubblico.
- Dal primo evento lesivo separare DamageCauser, Instigator e Killer/RewardRecipient: è indispensabile per le torrette future.

## 6. Come capire quando un pezzo è davvero finito

La checklist va osservata con il gioco avviato. Compilazione, package, no missing assets, frame stabile per la scena iniziale, nessun bug evidente su camera/mani/hitbox, transizioni senza snap, audio non stock mal mixato, riproduzione completa del caso d'uso, sincronizzazione host/client e video dimostrativo. Chi lavora senza accesso all'editor **non** può auto-promuovere lo strato a Done, ma può consegnare codice e guida di verifica con stato parziale.

Le priorità artistiche e funzionali di L1–L4 sono dettagliate nei file 13, 14, 15, 16 e 17.
