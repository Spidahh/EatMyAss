# ZOMBIE DEFENCE — UNA PARTITA VERA, DALL'AVVIO ALLA FINE
**VERSIONE CANDIDATA PER VALUTAZIONE, 26/10/2026. NON È APPROVAZIONE DEL COMMITTENTE.**

## 0 — Cosa ha chiesto il committente, senza interpretazioni

Mappa percorribile e progressivamente liberabile **come COD Zombies**. Base dentro la stessa mappa, in cui si entra per fare gli upgrade. La base ha difese automatiche e, quando è sufficientemente sviluppata, resiste all'assalto anche da sola; l'aumento della forza degli zombie richiede aggiornamenti successivi. Fuori si combatte con armi da fuoco e **melee vero**, forse esiste una specializzazione solo melee. Le skill devono essere originali e sensate in un gioco zombie, non le solite classi. Il ritmo a ondate o continuo è ancora aperto. Una produzione completa e ordinata, senza placeholder definitivi. Le decisioni originali sono registrate in [45](45_USER_DIRECTIVES.md); tutto il resto in questo documento è **una proposta testabile**, non una decisione dell'utente.

## 1 — Immaginiamo di avviare il gioco

**Schermata iniziale**: un angolo di città industriale di notte. Dalla strada si vedono zombie, serrande, strade sullo sfondo e la luce di una base barricata. Un piccolo gruppo di torrette sul tetto del rifugio apre il fuoco: la base è già parte del mondo, non un'altra modalità.

Proposta menu breve:
- `Gioca`: Solo, Ospita amici, Entra (soltanto se multiplayer effettivamente disponibile).
- `Opzioni`: grafica, input, audio, accessibilità.
- `Crediti`, `Esci`.
- `Continua` solo **se** il design approva salvataggi persistenti e c'è una sessione compatibile da caricare. Non mostrare pulsanti finti.

**Primo click di Gioca**: selezione mappa e difficoltà solo se esistono realmente più mappe. Per la prima 1.0 candidata una mappa **completa e rigiocabile** vale più di tre mezze mappe. Una schermata semplice spiega: «Esplora, apri nuove zone, potenzia la tua base. Le torrette continueranno a sparare mentre sei lontano».

**Caricamento**: 3D reale, nessuna falsa barra. Spawn iniziale **all'ingresso/garage della base**, non in un menu gestionale. Puoi vedere la città oltre il cancello e senti i primi zombie. Il percorso per uscire è evidente. L'interno contiene poche postazioni upgrade, non cittadini, fabbriche o raccolte di materiali.

## 2 — Minuti 0:00–3:00: il primo motivo per giocare

Il giocatore è in prima persona, ha un'arma da fuoco iniziale e può vedere un'arma da mischia impugnabile; nell'area esterna antistante la base ci sono due direzioni evidenti: **Strada delle Officine** (spazio largo, più visuali, zombie veloci) e **Vicolo del Mercato** (stretto, coperture, combattimento ravvicinato). Entrambe conducono a zone che non si vedono ancora interamente.

Esce dal garage e il gioco comincia. Quattro-cinque zombie della prima minaccia (conteggio SOLO esempio di pacing) avanzano dal lato strada. La prima torretta esistente è debole: abbatte un nemico vicino al portone e si vede **il proiettile che colpisce, la reazione e la morte reale**, anche se il giocatore non guarda. Gli altri zombie sono suoi: li schiva, spara, colpisce di melee.

Un semplice avviso diegetico dalla radio: «Perimetro attivo». Basta. Non compare un tutorial di dieci pannelli. Col primo gruppo eliminato, i punti/crediti d'esempio si aggiornano e il giocatore vede davanti a sé una porta bloccata, mentre una seconda via è più economica. La domanda reale è già: «Apro prima il Mercato? Aspetto un'arma? Torno a rinforzare la torre?»

**Vincolo progettuale**: il potenziamento della base è già possibile, ma non deve fermare il mondo o richiedere al player di fare manutenzione continua per due minuti.

## 3 — Minuti 3:00–7:00: APRIRE la prima zona

Il giocatore sceglie la **serranda del Mercato**. Interagisce, spende una cifra di prova (non approvata) e la serranda sale realmente con animazione, audio metallico e collisione aggiornata. Scopre un corridoio coperto, bancarelle rovesciate, una scala per un balcone e un accesso ancora chiuso verso il Deposito ferroviario.

Dentro il Mercato non c'è «un altro negozio» da gestire: ci sono zombie, spazi in cui può correre in cerchio, un punto di rifornimento e un interruttore di **trappola ambientale** esistente (esempio: serranda industriale che abbatte/ritarda alcuni zombie, con cooldown e segnali chiari). Non è un'abilità generica in HUD e non è una torre da costruire; sfrutta l'ambiente.

Nel frattempo, si sente una raffica provenire dalla base. Una piccola notifica «Perimetro sotto pressione» permette di tornare alla via iniziale. Il giocatore decide se proseguire verso un'altra apertura o rientrare.

**La sensazione desiderata**: hai aperto un pezzo permanente della mappa per quella partita. Non hai soltanto comprato «un nuovo riquadro sul menu». La nuova zona deve dare almeno una via, uno spazio da combattere e qualcosa di concreto da scoprire.

## 4 — Minuti 7:00–11:00: rientrare NON significa smettere di giocare

La mappa è continua. Dal Mercato il giocatore torna al piazzale (oppure usa una scorciatoia se già aperta) e **attraversa fisicamente** il cancello della base. Dentro può scegliere poche migliorie: arma/melee, difese, protezione del Nucleo. I menu compaiono solo in base e terminano appena si esce. Niente mappa gestionale RTS.

**Esperienza visiva**: scegli «torretta rapida migliorata» e sul tetto esterno compare un componente fisico, una diversa raffica/servomotore, un suono identificabile; non solo «+10% DPS» in una riga di testo. La difesa continua a sparare automaticamente durante la scelta; se l'assalto è forte, la base può soffrire comunque. L'interno deve rimanere leggibile e non far sparire la minaccia in una schermata di inventario.

Il giocatore esce. Ora vede che la torre abbatte da sola i camminatori al cancello. È una ricompensa immediata e concreta: «Ho costruito qualcosa che FUNZIONA». Può allontanarsi senza presidiare il Nucleo.

## 5 — Minuti 11:00–17:00: la mappa comincia a chiudere i circuiti

Il giocatore apre una seconda via dalla **Strada delle Officine**, salendo verso un **Parcheggio multipiano**. Nel livello c'è un attraversamento che si vede dal Mercato ma è chiuso dall'altro lato: il giocatore lo apre e crea il primo **circuito completo**. Ora può correre attraverso Mercato → parcheggio → strada iniziale senza fare una marcia indietro obbligata.

Un varco laterale è pericoloso: più accessibile al giocatore, crea anche una rotta di transito per alcuni zombie (preannunciata), con una scelta di percorso più rischiosa. **Nessun nemico appare improvvisamente dentro la base perché hai comprato una porta**, e non raddoppia il numero di zombie solo perché la mappa è più grande. I nuovi ingressi sono diversi instradamenti dei budget e delle linee di vista.

L'elemento *COD Zombies* da rispettare è la libertà di movimento, il poter «trainare» orde e sfruttare loop/percorsi; non tre corridoi separati con un'icona di missione ciascuno.

## 6 — Minuti 17:00–24:00: la vera decisione tra esplorazione e autodifesa

La base, potenziata per gli zombie normali, gestisce da sola un'intera porzione di assalto. Tu ti spingi fino alla **Centrale di Smistamento**. Lì compare per la prima volta un nemico con proprietà davvero diverse: ad esempio uno che colpisce lentamente ma sfonda le difese oppure uno che tenta di sabotare una sentry. Non deve per forza essere una nuova specie/modello: deve avere comportamento, animazione e controgioco reali.

La radio avverte: «Il lato nord non regge». **Questo non è un game over scriptato**. È il risultato misurabile di un corazzato che prende poco danno dalla torre leggera. Puoi:
- Continuare ad esplorare e rischiare HP del Nucleo.
- Rientrare tramite la scorciatoia e potenziare le difese.
- **Intercettare realmente** lungo la via uno degli assediatori per guadagnare tempo; se lo uccidi sparisce dal conto assedio (non viene duplicato da uno spawn “di scena”).

La terza opzione è fondamentale: i sistemi di FPS e base defense si parlano **nel gameplay reale**, non soltanto in due menu.

## 7 — Minuti 24:00–35:00: combattere nel modo che vuoi

Il giocatore che preferisce armi automatiche affronta il fronte da un percorso lungo con buona visibilità. Chi vuole **melee** può usare Mercato e sottopassi come spazi di ingaggio: coperture, angoli, imbottigliamenti e armi con vere reazioni di colpo. Un'eventuale **specializzazione solo-melee** deve cambiare il modo di affrontare l'orda — ad esempio controllo ravvicinato attraverso posizione/tempi di attacco — e non essere semplicemente «+12% danni di spada».

**Nessuna classe approvata**: non introdurre Tiratore, Tecnico, Soccorritore, Berserker o «colpo preciso». Le tecniche candidate sono nel file 49 e vanno giudicate come idee a parte, non feature obbligatorie.

Aprendo la terza grande porzione della città, si raggiunge un tratto sopraelevato: da lì si scorge sia un lato nuovo della mappa sia la base in lontananza. Una scala/ascensore permette un ritorno più veloce, se sbloccato. Ciò che prima sembrava una strada lunga diventa una rete percorribile.

## 8 — Minuti 35+: non solo “zombie con più HP”

La pressione cambia perché arrivano tipi che **mettono in discussione scelte difensive precise**. I camminatori sono gestiti dalle torri leggere; l'unità corazzata chiede una torre diversa o l'intervento del giocatore; una minaccia di sabotaggio crea una finestra di vulnerabilità reale; un gruppo rapido approfitta di un settore con molte curve. Il progresso delle difese non è inutile, ma non risolve ogni minaccia per sempre.

Un evento conclusivo possibile (NON APPROVATO) è «viene sbloccata una via di fuga / una centrale da riattivare; puoi tentare di concludere la partita oppure continuare a resistere». Questo offre **un esito scelto dal giocatore**, invece di assegnare una vittoria automatica a un numero arbitrario di ondate. Alternativa altrettanto ammissibile: partita sopravvivenza con record e game over, senza evacuazione. La scelta finale è del committente.

## 9 — Se sei sconfitto, cosa succede?

La base ha HP/condizione difensiva visibili e la partita deve comunicare il rischio senza interrompere l'azione. **Proposta di sconfitta**: la distruzione del Nucleo termina la sessione con risultati (zone aperte, tempo, assalti resistiti, migliori azioni melee e ranged, torri che hanno davvero ucciso). La morte del giocatore fuori può usare un sistema Downed/Revive oppure respawn limitato: non approvato; evita di inventare un sistema automatico che distrugge il divertimento.

La schermata risultati permette di vedere dove hai investito e come hai perso: difesa troppo debole contro corazzati? Mappa rimasta chiusa? Progressione difficile per scelte sbagliate? Poi `Riprova`, `Menu`. Persistenza tra partite NON è stata decisa: distinguere progressione **dentro la run**, certa come desiderio di crescita, da potenziamenti permanenti attraverso più run, che richiedono scelta.

## 10 — Cosa vale la pena rigiocare

- **Biforcazione iniziale** delle porte e ordine diverso di apertura, non un tracciato fisso.
- **Strutture difensive** che funzionano in modo visibile e reale: una build forte non è automaticamente la migliore per la minaccia seguente.
- **Stili combattimento**, compreso melee, capaci di sfruttare realmente mappe e parti del corpo degli zombie.
- **Scorciatoie** che ripensano la mappa e cambiano il tempo per tornare in base.
- **Variazione controllata** di origini e combinazioni zombie, mai spawn inventati dietro il giocatore o aumento nascosto di HP.
- **Scoperta leggera**: un paio di elementi opzionali ambientali, non dieci Easter Egg obbligatori o un crafting game.

## 11 — Cosa DEVE rispondere un playtest

Dopo i primi tre minuti il giocatore capisce l'obiettivo senza un tutorial di dodici pagine? Aprire una porta sembra cambiare davvero la mappa? Dopo dieci minuti il giocatore vuole esplorare o sente di dover tornare a riparare ogni due secondi? La torretta può **uccidere REALMENTE** quando il giocatore è lontano? Il melee è soddisfacente con hit reactions e decisioni di rischio? Riusciresti a giocare mezz'ora senza aprire un menu ripetitivo? Se la risposta è no, correggere quel sistema prima di aggiungere altre feature.

**Questo documento è un'esperienza candidata per verificare la direzione. Non esprime approvazione dell'utente sui dettagli proposti.**
