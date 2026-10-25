# SPECIFICA MADRE — ZOMBIE DEFENCE (PRODUZIONE COMPLETA v1.0)

**Data 25 ottobre 2026 · update design 1.1.** Questo è il **contratto di contenuto dell'intero gioco**, non un piano per il solo inizio. In caso di divergenza con i documenti 00–17, prevalgono AGENTS.md e questo documento. Si esegue **uno strato completo alla volta**, ma si progettano fin dall'inizio le integrazioni di TUTTI gli strati. Nessuna riga di questo documento dimostra che il gioco esista già.

## Prodotto preciso

Gioco PC Windows **FPS action 3D** zombie + difesa base: movimento/mira/colpi come attività primaria; zombie in ondate; Nucleo da proteggere; 3 classi e abilità; armi/upgrade personali; torrette, barricate e trappole/upgrade della difesa; piccola città industriale che si espande **per settori preprogettati**; solo o cooperativa fino a 4 giocatori. Durata target partita 25–40 minuti (**non verificata**). Esperienza replayable con 10 ondate e boss finale. Il giocatore deve scegliere dove investire: forza personale, potere difensivo, apertura del territorio. Non è un survival crafting, un gestionale, un tower defense top-down, una modalità idle o un clone che contiene asset protetti di Call of Duty.

**Taglia della versione 1.0 (deliverable):**
- **Una sola mappa completa**: quartiere industriale urbano con Nucleo, cortile centrale, officina, deposito, zona sopraelevata; 3 settori acquistabili dopo la zona iniziale.
- **Dieci ondate, con finale** e una scelta di difficoltà normale/veterano fatta mediante parametri server, non secondo level design distinto; endless solo dopo 1.0 se desiderato.
- **Tre classi:** Assaltatore, Ingegnere, Soccorritore. Scelte in lobby prima della partita, una attiva per giocatore.
- **Cinque archetipi nemici:** Camminatore, Corridore, Corazzato, Sabotatore, Boss. Non dichiarare “cinque modelli” fino a quando tutte le mesh approvate saranno nel manifest.
- **Quattro archetipi armi:** pistola, fucile d'assalto, shotgun, SMG. Un modello finito per archetipo; LMG e altre armi in backlog non 1.0. Il pack Deadghost è fonte designata per il primo AR; NON presumere che contenga proprio tutti e quattro i modelli finali senza apertura del pack.
- **Tre difese principali:** barricata, sentry automatica, campo rallentante; **Nucleo** con 3 upgrade. La sentry non può vincere da sola. Non aggiungere mortaio, generatori separati o artiglieria prima della 1.0.
- **Due valute nella run:** crediti personali (armi e munizioni) e fondi squadra (difese, riparazioni, settori). Nessuna terza valuta di crafting.
- **Co-op 1–4 players** con listen-server/host; nessun account, database remoto, servizio in abbonamento o server dedicato al lancio. Matchmaking pubblico, migrazione host e cross-play **non promessi**. Invito/amici dipende da integrazione effettivamente verificata.
- **Almeno sei pacchetti completi di animazioni e feedback**: player, 4 categorie armi, 5 nemici, 3 strutture, Nucleo, UI; ogni entità è completa prima della successiva.
- **Salvataggi:** preferenze persistenti e statistiche locali; progressione e acquisti della singola run si resettano dopo il risultato. Nessun salvataggio mid-wave in co-op 1.0: scelta deterministica per ridurre bug, chiaramente comunicata.

## Gameplay distintivo V1.1: pochi poteri condivisi

L'identità finale mette insieme l'azione FPS, le difese e una città giocabile come strumento tattico, NON come gestionale. [Specifiche complete](40_SYNERGIES_SKILLS_AND_CITY.md), senza ulteriori valute o tasti:
- **V universale = Spinta d'emergenza** corta, 1 zombie normale, cooldown 12s seed; animazione vera + hit reaction + network.
- **Q = una abilità di classe**: Sfondamento Assaltatore, Ripristino/boost mirato Ingegnere, Impulso medico/pausa bleedout Soccorritore; una passiva ciascuno.
- **Middle click = marcatura squadra** di un zombie 5s, priorità sentry soltanto se LoS/range; non aumento DPS e non wallhack.
- **E al pannello Nucleo, dal T2 = Impulso di contenimento**: slow ad area, **una volta per wave** per tutto il team, non una nuova risorsa; T3 sceglie portata oppure ripristino HP Core (non due abilità).
- **La città concede una passiva per area acquistata**: S1 sconto refill ammo, S2 sconto repair barricata, S3 radar warning speciale. Ogni settore introduce rischio di un fronte aggiuntivo senza moltiplicare budget totale wave.
- **Wave7, se esiste sentry**, micro-crisi di blackout preannunciata e risolvibile con Q Ingegnere o E manuale: nessun nemico/valuta extra.

Le capacità aggiunte sono incluse nei task esistenti e hanno animation/audio/VFX/server-QA propri. Nessun deck random perk o slot magici.

## Principi non negoziabili

1. **Codice riutilizzato prima di nuovo codice**, quando passa compilazione e integrazione: HordeTemplate V2 Native su UE 5.8. Non aggiungere Lyra o un secondo sistema di weapon/inventory/AI. Lo stato originale upstream è in docs/11.
2. **Un solo proprietario di stato**, il server: zombie e danni, direzione ondate, vita del Nucleo, crediti, acquisti, difese, settori, vittoria.
3. **Mai un'entità finta finale**. Asset reale approvato dal manifest, animazioni specifiche, VFX, SFX, UI, collisione, replication e qualità di gameplay completi.
4. **Un nuovo tipo alla volta**, ma senza rifare architettura. Un weapon config comune, uno zombie data type, una defense definition, una class ability interface, una mappa dei settori data driven.
5. **Non spostare le scelte nei TODO**. Ogni mancanza diventa un record di GAP, con soluzione concreta e dipendenza bloccante; mai etichettare DONE in assenza di contenuto.
6. **L'ordine di costruzione** è l'ordine L0–L11 di docs/12, esteso dai dettagli 19–33. Nessuna fase iniziata prima dell'accettazione della precedente.
7. **Test e misure sono parte della finitura**, mai «prima facciamo una demo brutta, poi la rifacciamo». Va preservato il senso della richiesta: finire davvero ciò che si inizia.
8. **Zero acquisti nuovi per default**, gratuito non equivale a diritto di redistribuire asset sorgente sul GitHub pubblico.

## Contratto del core loop

Lobby → scelta classe → scelta equip iniziale → caricamento unica mappa → 5s preparazione iniziale → ondata → combat+difese attive → tutti gli zombie del budget effettivo eliminati → ricompense una sola volta → fase preparazione breve max 25s (skip se tutti pronti) → spesa/repair/apertura area → ondata successiva → dopo la decima ondata e boss ucciso vittoria → risultati → lobby. Sconfitta se Nucleo 0HP **o** squadra eliminata definitivamente. Non fare countdown di wave che salta automaticamente nemici ancora vivi, né spawn infiniti senza obiettivo.

## Fonti autorevoli per sottosistemi

| Documento | Responsabilità; leggere prima di implementare lo strato |
| --- | --- |
| [19](19_SESSION_AND_RULES.md) | cicli, game states, classi di obiettivi, punteggio, vittoria |
| [20](20_COMBAT_WEAPONS.md) | 4 armi, gunplay, munizioni, upgrade |
| [21](21_ZOMBIES_AI.md) | roster nemici, animazioni, targeting, combat |
| [22](22_DEFENSE_AND_BASE.md) | Nucleo, barricate, torrette, campo lento, transazioni |
| [23](23_CLASSES_ABILITIES.md) | classi, cooldown, revive e regole |
| [24](24_CITY_AND_SECTORS.md) | mappa, piazzole, spawn, espansioni |
| [25](25_ECONOMY_BALANCE.md) | entrambe valute, premi, prezzi e bilanciamento |
| [26](26_WAVE_DIRECTOR.md) | composizione 10 ondate, scalabilità 1–4, boss |
| [27](27_MULTIPLAYER_SAVE.md) | sessioni, rete, stato, salvataggi, host |
| [28](28_UI_AND_INPUT.md) | interfacce, UX, impostazioni e accessibilità |
| [29](29_ANIMATION_AUDIO_VFX.md) | matrice di completezza per OGNI entità |
| [30](30_ASSET_PRODUCTION.md) | sourcing/risorse mancanti/licenze/art-direction |
| [31](31_UNREAL_ARCHITECTURE.md) | moduli, dati, integrazione, replicazione, dipendenze |
| [32](32_QA_RELEASE.md) | definizione di finito, QA, release e packaging |
| [33](33_FULL_BACKLOG.csv) | tabella di lavorazione completa e sequenziata |
| [34](34_CODEX_MASTER_BRIEF.md) | singolo incarico esecutivo senza libertà creative |
| [35](35_DECISION_GAPS.md) | cose non deducibili/non confermate che vietano improvvisazioni |
| [39](39_COMPARATIVE_GAME_DESIGN.md) | ricerca su 5 riferimenti e criteri di selezione |
| [40](40_SYNERGIES_SKILLS_AND_CITY.md) | scelte gameplay v1.1 e integrazioni player ↔ difese ↔ città |

## Condizione di completezza dell'intero prodotto

Non chiamare il gioco “terminato” se manca anche una delle categorie del contratto 1.0, se una singola clip necessaria è simulata male, se uno zombie resta stuck, se il player può comprare una torre in due client contemporaneamente senza autorità, se il boss è ucciso da difese AFK, se una mappa è solo graybox, se le licenze contenuti non sono state validate o se manca la build Windows Shipping testata su macchina pulita.

In caso di vincolo reale di costo/licenza, **non falsificare** la conclusione; compilare GAP, proporre risorsa davvero gratuita e legalmente utilizzabile o chiedere una sola scelta di scope. Il numero di contenuti previsti non è una promessa che tutti gli asset esistano già.
