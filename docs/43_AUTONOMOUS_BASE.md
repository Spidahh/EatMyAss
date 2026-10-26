> **NON APPROVATO / IN REVISIONE (26/10/2026):** le precedenti classi, abilità (“colpo preciso”), numero di zone esterne, economia, ondate e altre scelte specifiche in questo documento sono PROPOSTE DELL'ASSISTENTE, non decisioni dell'utente. **Nuova direttiva: mappa come COD Zombies con esplorazione e ZONE SBLOCCABILI, base da cui entrare/uscire solo per upgrade e che si autodifende, melee e idee originali.** Per la fonte autorevole leggere [45_USER_DIRECTIVES.md](45_USER_DIRECTIVES.md) e [46_PLAYER_JOURNEY_REQUIREMENTS.md](46_PLAYER_JOURNEY_REQUIREMENTS.md). Codex non deve implementare quanto contraddice queste direttive.

# BASE AUTOMATICA E HUB INTERNO — SPECIFICA SISTEMI E BALANCE

## DUE ZONE FUNZIONALI NELLO STESSO LIVELLO

**Interno protetto**: player cammina e usa 4 postazioni interattive, senza combattimento, torrette costruite solo tramite terminale/overview upgrade. Luogo fisico reale con porte, animazione ingresso/uscita, UI della base, suoni della centrale. Non si costringono i player ad aspettare fine wave, rientro consentito anche sotto assedio. Qualsiasi nemico raggiunge soltanto il **perimetro esterno** e colpisce fortificazioni/Nucleo con target/hit reali; non spawnare zombie nell'hub upgrade (fallimento di base avviene quando Nucleo 0HP). Dentro non diventa un gioco gestionale, i terminali hanno massimo 2-4 scelte chiare.

**Esterno**: player è attivo con armi da fuoco e melee, AI zombie, incarichi rapidi, percorso di ritorno. Se player è lontano o spento dal combattimento per morte temporanea, le torri continuano automaticamente a difendersi. **Non** disattivarle per assenza del proprietario o distanza di replica: l'autorità server e AI update restano attivi.

## Fisica dell'autodifesa

Ogni torre possiede target selection autonomo: zombie con una route alla base, priorità su distanza pericolosa, ruolo nemico (armored vs runner) e target availability; verifica range+LoS effettivi; spara secondo cadence, recoil/FX, ammo policy e cooldown senza comando player. Non usa ping MMB per poter essere utile. La base non è una fiction di scoreboard: tower-kills e HP zombie sono calcolati server con l'identico sistema di danno che usa player. Corpo zombie death/counters gestiti in modo idempotente.

**Autonomia misurabile:** a parità di assalto Wn, base con upgrade adeguati DEVE poter respingere tutti i nemici senza l'intervento diretto del player. La difficoltà si alza su Wn+2... e introduce corazzati, sabotatori e nuovi spawn, così la stessa configurazione gradualmente perde margine. **Non** aumentare HP alle spalle del giocatore perché le torri hanno troppo DPS. Mostrare in HUD/terminale la stima **Copertura Attuale vs Minaccia Assalto Prossimo** derivata dai valori veri della simulazione, come indicatore indicativo non percentuale inventata. La previsione può essere sbagliata per comportamento AI, ma deve essere calcolata, non dichiarare 100% sicurezza.

## Costruzioni (solo da dentro la base)

Tre tipi in 1.0, piazzole fisse su pareti/tetti/perimetro, nessun freeform base builder:
- **Barricata portone:** HP/armatura, intercetta bersaglio che cerca il varco; upgrade T1/2/3 aumenta tenuta e restituisce poco danno da urto (T3, seed), animazioni/material per tier.
- **Torretta rapida:** automatic, contro Walker/Runner, T0 fuoco continuo con heat controllato, T1 raffreddamento, T2 doppia priorità minacce in fascia, T3 migliore armor pen moderata; non deve battere heavy sul corazzato.
- **Torretta pesante:** colpi lenti e potenti anti-Armored/Bruto, T0 cap minimo di angolo, T1 rotazione migliore, T2 penetrante, T3 minor windup/raffreddamento; una vera mesh rig realistica e suoni diversi dalla sentry rapida.
- **Protocollo Nucleo** (NON quarta torre da piazzare): al T2 sblocca un'**onda d'urto automatica d'emergenza**, trigger **quando CoreHP scende sotto soglia seed 35%**, un massimo di una volta per ondata/stadio, spinge/rallenta i nemici vicini per tempo limitato, non danneggia o uccide boss gratis. T3 miglioramento di raggio O supporto riparazione automatica, **una scelta**.
Niente campo rallentante da piazzare come terza torre, niente sirena azionata manualmente via E per salvare una wave: il Nucleo è *automatico* e prende una decisione dalla sua HP. Niente cura automatica ogni 2sec illimitata.

### IA attacca la BASE, non il player a prescindere

Due gruppi di enemy aggro: **Assedio** punta perimetro/torrette/core; **Esterni** punta player nel territorio, può invadere area assedio solo tramite event. Il director controlla pressione totale per evitare che uccidere zombie al campo faccia raddoppiare l'orda alla base. Walker attacca gate se route bloccata, Runner cerca varchi scoperti, Armored sfonda barriera, Saboteur disabilita torri per una finestra che un player può prevenire uccidendolo fuori dalla base, Bruto richiede alta capacità difensiva oppure supporto umano per essere superato. **Nessun enemy immunità totale alle torrette**: se la base è davvero sufficientemente potenziata, può vincere anche contro Bruto.

### Parametri di base (solo SEED)

| Parametro | Iniziale | Nota |
| --- | ---: | --- |
| CoreHP | 3000 | scaling e tiers data |
| Damage rate turret light | 8 colpi/s | da tarare su AI e calibro, NON promise |
| Damage rate heavy | 1 colpo/s | alto danno per colpo/penetration |
| Max torrette iniziali | 2 | base capacity unlock fino a max 6 |
| Power capacity iniziale | 2 | slot limit, non nuova risorsa |
| Emergency pulse soglia | 35% | 1 per onda, trigger server idempotente |
| Target autonomia | 120s W3 con base adeguatamente aggiornata e player lontano | QA target, non benchmark certificato |

## Terminali upgrade interni, zero menù RTS

- **Armeria**: equip/rifornimenti/upgrade pistole, AR, SMG, shotgun, machete/mazza/asta; 1 lista corta/2 viste.
- **Difese**: layout schematico semplice del perimetro, socket con tipo torre e T0-T3, costo Rottami, auto upgrade con clic; mesh/animazione fisica fuori visibile subito.
- **Comando**: Core HP/power/tiers, stadio attuale, allarmi, prossimo assalto, indicator Copertura vs Minaccia, riparazione, eventuale scelta T3.
- **Specializzazioni**: Tiratore/Spezzatore/Tecnico, una passiva/attiva, equip “Mischia pura” per Spezzatore. Nessuna seconda valuta o skill tree.

I terminali sono nello stesso interno fisico, raggiungibili camminando pochi secondi, con scorciatoia menu di scelta **solo mentre sei effettivamente dentro** per evitare tempi morti, non teletrasporto costante.

## Progressione tramite Rottami

Ogni acquisto fa transazione unica server: `SpendTxnId`, saldo, target socket/core/weapon, costo configurabile, validazione sessione e player dentro base, rollbacks, fanout UI. Acquisti possibili **anche durante assalti**, con animazione upgrade; se torre è distrutta, ricostruire dopo scelta. In co-op nessun host può spendere i Rottami di un altro player per upgrade weapon: unica risorsa di gioco ma conto `wallet personale` per equip e `deposito base` come saldo comune? **Non creare due valute**: entrambi sono saldo di Rottami, trasferibili liberamente mediante terminale, con consentimento dei proprietari. Per semplicità V1: Rottami raccolti dai combatant entrano **automaticamente nella cassa della base comune**, acquisti weapon/class sono a carico comune con log/confirmation in co-op; acquisti grandi richiedono doppia conferma di player attivi per evitare grief. Solo stessa moneta e conto unico. Se questo blocca gameplay 1p, introdurre policy di permessi host senza secondo currency.

## Failure e responsabilità

Nucleo 0HP termina la sessione assedio con schermata Failure. Persistenza: base salvataggio checkpoint **prima del nuovo assalto**; su perdita non cancellare progressi conquistati, ma ritorno all'ultimo checkpoint (nessuna progressione gratis e senza exploit). Se player muore fuori, rientra dentro dopo respawn, l'orda continua; se team intero è downed, non forza Game Over, base può resistere e i respawn riprendono. Alla completa distruzione il player può ricostruire dal checkpoint salvato, non reset al livello 1.
