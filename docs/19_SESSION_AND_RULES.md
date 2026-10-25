# PARTITA COMPLETA, OBIETTIVI, MORTE, FASI E REGOLE

## Modello della sessione

**Tipo:** una run chiusa 10 ondate con finale, 1–4 player e una mappa. Host autorevole, entrambe le valute reset tra partite. In lobby: selezione classe unica, nickname locale, impostazioni, eventuale presenza amici autorizzati dal trasporto reale. Classi duplicate consentite: il gioco non richiede per forza medico/ingegnere. Il loadout iniziale condiviso per equità è **pistola + arma base** da definire tra le quattro disponibili; fino alla realizzazione di tutto l'arsenale si usa esclusivamente il primo AR senza menu finto.

## Macchina a stati principale

`FrontEnd → Lobby → Loading → IntroPrep → WaveSpawning → WaveCombat → WaveCleanup → Reward → Intermission → NextWave/Finale → Victory/Defeat → Results → Lobby`.

- Ogni stato possiede owner **GameMode server**; GameState replica `RunId`, `WaveIndex`, `Phase`, `RemainingToSpawn`, `AliveEnemies`, `CoreHealth`, `IntermissionSecondsRemaining`, `TeamFunds`, `OpenedSectors`.
- Ogni transizione con reason code; `WaveWon` non viene generato due volte. UI legge GameState, non inventa timers locali che pretendono cambiare round.
- `WaveSpawning`: enqueue finito; `WaveCombat`: almeno uno zombie vivo o spawn in coda; `WaveCleanup`: nessuno in coda e zero zombie vivi e validi, ignorando corpi in ragdoll. Enemy despawn di recovery va contato **senza premio kill**, con log.
- Prep max 25s solo fra ondate; alla scadenza parte la prossima salvo attività bloccante reale e comunicata. Ready-skip avvia presto **solo se tutti i giocatori connessi e attivi pronti**. Un client disconnesso non tiene il voto in ostaggio.
- Le porte verso nuovi settori si acquistano in prep; i nuovi ingressi nemici entrano nella wave **successiva**, annunciati con audio/marker. Non compare mai uno spawn “di sorpresa” nella zona appena comprata.

## Stati player e down/revive

`Alive → Downed → Revived` oppure `DeadSpectating`. Un player a zero HP cade downed una volta con timer bleedout **seed 25s**, movimento e fuoco disabilitati, prompt revive con hold **seed 3s** (Soccorritore riduce). Invincibilità brevissima dopo revive, **seed 1s**, non accumulabile. Nessuno può rianimarsi all'infinito: un player solo ottiene **una self-revive per run senza costo**, opzionalmente consumabile, così il solo non è matematicamente inferiore; il cooldown del revive non genera immortalità. In co-op compagno vivo può rianimare; due che interagiscono non attivano due revive; il server sceglie una richiesta, annulla le altre. Se tutti Downed con nessuno in grado di rianimare, sconfitto. Le regole specifiche si bilanciano in playtest; i seed non sono verifiche.

## Vittoria/sconfitta

- `DefeatReason::CoreDestroyed` su core HP<=0; `DefeatReason::TeamWiped` quando nessuna possibilità valida di revive; `DefeatReason::HostQuit` quando la sessione non può più continuare.
- `Victory` dopo che tutti i nemici della ondata 10 inclusi Boss sono morti e CoreHP>0 e almeno un player attivo o rianimabile sopravvive. Un singolo evento conclusivo; i client vedono stessa schermata.
- Risultati: durata, ondate completate, zombie uccisi/assist, headshot, danno Nucleo evitato, riparazioni, spese di difesa, settore aperti, revives, damage dealt. Non usare metriche “MVP” che incentivino rubare kill e abbandonare Nucleo.

## Anti exploit/softlock di gioco

- Spawn esclusivamente punti autorizzati, validi e con route; se non c'è punto disponibile, tenere in coda e dare feedback di attesa breve; superata soglia di recovery scelta, loggare e sospendere onda senza inventare nemici alle spalle.
- Zombie imbottigliati: target switch o attacco barricata; la mappa deve mantenere almeno una soluzione d'attacco raggiungibile. Se player salta su luogo sicuro, l'IA deve poter scegliere core/strutture, non stare sotto di lui per sempre.
- Acquisti durante wave: **munizioni/riparazione emergenza** soltanto dove interagibile e se il design lo permette; costruzione strutture e apertura settori solo in prep per chiarezza.
- Se un client prova un acquisto durante transizione, il server assegna TxnId e conferma o rifiuta senza sottrarre fondi.

## Primo input verificabile di gameplay

Un tester che non conosce il progetto deve capire in 30s che deve **sparare agli zombie** e **salvare il Nucleo**; dopo la prima onda capire in 15s dove investire soldi e quali sono i varchi nuovi. Il gioco non deve chiedere dieci menu prima di iniziare.

## Parametri separati dal codice

`RunRules`: maxPlayers, firstWave, finalWave=10, prepSeconds=25, downedSeconds=25, reviveSeconds=3, soloSelfReviveUses=1, startCoreHP, maxSocketsByZone, modifiersByDifficulty. Ogni valore è un **seed di sviluppo** dove non si specifica diversamente; l'esito è definito ma i numeri non sono certificati.
