# ZOMBIE DEFENCE — GIOCHIAMOCI DAVVERO, DAL MENU ALL'ESITO

**Bozza giocabile di game design, 26 ottobre 2026. SOLO PROPOSTA: NON è un gioco realizzato e NON è una decisione dell'utente sui dettagli. NON TOCCARE CODICE.**  
**Vincoli espressamente richiesti:** mappe percorribili e sbloccabili **come COD Zombies**; base fisica nella mappa, visitata per upgrade; difese **automatiche**, sufficienti a respingere da sole la minaccia del loro livello; zombie progressivamente più forti; gunplay e **melee reale**, possibile scelta solo melee; idee originali ma poche, niente solite classi o "colpo preciso"; piano dall'avvio fino all'esito, produzione a strati definitivi. Fonte: [45 — direttive dell'utente](45_USER_DIRECTIVES.md).  
**Tutto ciò che segue con nome, numero, costo, tempo o evento specifico è una proposta concreta di test, non una feature approvata.** Non consegnare questo file a Codex come mandate d'implementazione finché non è stato valutato.

## 1. Qual è il gioco, in una frase?

**Esci dal tuo rifugio, apri una mappa zombie che diventa progressivamente più grande e interconnessa, combatti nel modo che preferisci e investi ciò che hai guadagnato per rendere la base abbastanza autonoma da permetterti di esplorare ancora più lontano.** Gli assalti non aspettano il giocatore e prima o poi nuove minacce mettono in difficoltà le difese che prima bastavano.

La progressione decisiva NON è "torre +10% danno": è **"prima non potevo allontanarmi; ora questa parte della città è raggiungibile perché la mia base regge da sola"**. Il momento COD Zombies è aprire una strada e scoprire che si ricollega a un luogo già attraversato. Il momento difesa è **vedere realmente la sentry uccidere zombie mentre si sta facendo altro**.

### Il test contro l'effetto "videogioco noioso"

Dopo 10 minuti il giocatore deve aver già:
- sparato **e** colpito uno zombie in melee (con impatti diversi);
- **aperto un accesso fisico** e attraversato uno spazio nuovo;
- visto una torre automatica realmente sparare su zombie che stavano attaccando la base;
- scelto almeno una volta se spendere per **nuova strada, equipaggiamento o difesa**;
- potuto tornare dalla zona sbloccata alla base senza caricamento né teletrasporto.

Se manca uno di questi eventi, il primo ciclo non mostra il gioco giusto. I minuti sono un **obiettivo di test**, non una promessa di pacing prima di avere il gioco in mano.

---

## 2. Da "avvia" a "sto giocando": le schermate vere

**MENU PRINCIPALE (esempio candidato):** `Gioca`, `Opzioni`, `Crediti`, `Esci`. `Continua` compare **solo se** è stata approvata e implementata una funzione di salvataggio tra partite. Dentro `Gioca`, solo `Solo` e `Ospita/Entra` **se** il multiplayer esiste davvero; non mostrare modalità fittizie.

**NUOVA PARTITA:** breve scheda di una mappa **solo quando ce n'è davvero una da scegliere**. Per la prima pubblicazione: una mappa rifinita è meglio di tre mappe vuote. Due righe di istruzioni, non dieci pannelli: `Apri la città. Migliora il rifugio. Resisti agli assalti.`

**CARICAMENTO:** carica una sola mappa continua; cancello, perimetro, base interna e aree bloccate appartengono allo stesso livello. Se si gioca online, lo stato di porte/base/zombie è autorevole dell'host e visibile a tutti.

**SPAWN:** dentro o appena all'uscita del rifugio; dopo pochi passi il giocatore vede già **la prima strada, due accessi ancora chiusi e uno zombie**, non un menu dove deve comprare qualcosa prima di poter giocare. Può attraversare la porta alle sue spalle per consultare gli upgrade. La prima minaccia arriva in modo leggibile, non uno spawn dietro la telecamera.

**PAUSA E USCITA:** `Riprendi`, `Opzioni`, `Esci` con conseguenze chiare. Un menu in coop non ferma tutte le AI sul server; in solo la pausa vera è una decisione tecnica/UI da verificare.

---

## 3. LA MAPPA — una mappa COD-Zombies-style, non tre arene

Schema di **UNA possibile prima mappa**, nomi provvisori. Le lettere sono aree, non livelli separati. Simboli: `--` strada già percorribile, `[P]` porta inizialmente chiusa, `[S]` scorciatoia da aprire dall'altro lato.

```text
              (G) TETTI / BELVEDERE
                  |          |
                [P]        [S]-------------+
                  |                        |
           (F) DEPOSITO / NODO             |
              /           \                |
            [P]          [P]               |
             /               \             |
     (D) PARCHEGGIO      (E) SOTTOPASSO    |
            |                 |            |
            [P]            [P]            |
            |                 |            |
     (B) VIA OFFICINE   (C) MERCATO        |
              \          /                 |
              [P]      [P]                 |
                  \    /                    |
             (A) PIAZZA ESTERNA ------------+
                   |
             BASE FORTIFICATA
           [INTERNO: SOLO UPGRADE]
```

**Come si usa, non solo come si disegna:**
- **A / Piazza:** spazio iniziale, due porte alternative; la base si vede, si sentono le torrette, ed è facile ritornare.
- **B / Officine:** lunga linea di vista per armi da fuoco, auto e cover, entrata al Parcheggio; non una "zona da acquistare" per sconto munizioni.
- **C / Mercato:** spazio stretto con isole attorno cui girare, ideale per rischiare melee, seconda entrata al Sottopasso.
- **D / Parcheggio:** rampe e un circuito ampio per gestire il gruppo, non un corridoio con spawn alle spalle.
- **E / Sottopasso:** zona più pericolosa, visuale corta, via alternativa.
- **F / Deposito:** i due rami si **ricongiungono**, puoi tornare a casa senza attraversare per forza le stesse stanze.
- **G / Tetti:** area visibile da lontano. Una scorciatoia aperta dal lato alto raggiunge la Piazza vicino alla base; il percorso di ritorno che prima richiedeva minuti diventa rapido.

**Regola di design testabile:** una zona aperta deve offrire **un motivo per entrare (mappa, equip o rischio), un ambiente di scontro differente, almeno una via logica verso altro luogo**. Non aprire un'area vuota solo per aggiungere superficie. Nella mappa completa, percorsi alternativi e collegamenti trasversali sono più importanti di un numero arbitrario di porte.

**"Liberare una zona" ha due significati da testare, NON ancora scelti dall'utente:** (a) spendere punti per un cancello/serranda, come classico COD Zombies; (b) respingere un gruppo localizzato e interagire con l'accesso. Preferire gesti brevissimi e chiari, niente missione di 15 minuti o fetch quest per ogni cancello. Una volta aperta nella sessione, la zona resta attraversabile. Nessuna porta si ricompra perché cambi ondata.

**VINCOLO fondamentale:** sbloccare una porta modifica *davvero* mesh, collisione, navmesh e percorso dei giocatori, non soltanto un marker. Gli zombie possono utilizzare i percorsi dove il level design lo permette, senza spawnare magicamente nella sala di upgrade.

---

## 4. PRIMI 12 MINUTI — seduto davanti al PC (pacing ILLUSTRATIVO)

| Quando circa | Cosa fai con le mani | Cosa succede davvero nel mondo | Che scelta stai facendo |
| --- | --- | --- | --- |
| 0:00–1:00 | Esci dalla base, guardi le due serrande, muovi/miri | Il primo gruppetto di zombie avanza; una torre d'inizio spara vicino al cancello ma **non basta a pulire tutto** | Resto vicino o affronto gli zombie fuori |
| 1:00–3:00 | Combatti con prima arma da fuoco, provi melee per un nemico vicino | Impatti/suoni distinguono pelle e metallo; i colpi non attraversano i modelli. Accumuli un valore da spendere | Combat e rischio valgono la pena |
| 3:00–5:00 | Ti avvicini a porta B o C e interagisci | La serranda sale realmente, suono e collisione cambiano, nuova strada comparsa | Aprire **Officine** per distanza o **Mercato** per gioco ravvicinato |
| 5:00–8:00 | Attraversi la prima zona, giri attorno a una formazione, usi cover o melee | L'ambiente cambia il modo di affrontare l'orda, non solo la texture dei muri | Spendere ancora per andare avanti o tornare |
| 8:00–10:00 | Torni per la via già aperta ed entri dentro la base | L'assedio **prosegue fuori**; senti i colpi. Vedi cosa la torre è in grado di fermare e cosa passa | Upgrade mio equip o vera difesa |
| 10:00–12:00 | Potenzi una sentry, esci e riprendi un altro percorso | Servo/audio/colpo e risultato cambiano; la stessa torre ora respinge da sola minacce normali per una finestra | Posso rischiare un tratto più lontano |

Queste non sono "scene da mostrare" o animazioni finte per il pitch: devono essere simulate con **zombie veri, danni veri, AI e sistemi reali** quando si passerà alla produzione. Prima rimangono un **test su carta**, non footage di gioco.

---

## 5. QUELLO CHE SUCCEDE MENTRE NON SEI ALLA BASE

**Schema concettuale di un singolo director (proposta implementativa):**
- alcuni zombie stanno attaccando un elemento **del perimetro** (cancello, barriera, torre, Nucleo) e percorrono vie reali;
- altri stanno cercando il player nella zona che sta esplorando;
- **non sono copie virtuali dello stesso zombie**: un zombie Siege ucciso nella mappa è davvero morto; se un zombie cambia obiettivo, cambia quell'actor, non si aggiunge uno spawn gratuito;
- il sistema tiene budget/cap di zombie reali per non raddoppiare la difficoltà quando ci sono più giocatori o nuove aree.

**Autodifesa vera:**
1. Sentry rileva, ruota e spara con una traiettoria valida, anche senza giocatori vicini.
2. Zombie riceve il danno del proiettile e reagisce. Se la salute arriva a zero muore, si pulisce e non è contato fra gli assediatori vivi.
3. La base può resistere completamente a un tipo di attacco con difese appropriate: questa è la ricompensa dell'upgrade.
4. Le minacce nuove introducono un **problema specifico** (es. corazza resiste al fuoco leggero, zombie rapido sfonda una via non coperta, sabotatore cerca una torre) e rendono insufficiente un vecchio assetto. Non scalare arbitrariamente HP del Nucleo verso il basso.
5. Se nessuno è lì a guardare, **il server deve continuare a simulare AI/HP/danni**; solo i suoni/FX lontani possono essere alleggeriti sui client. Nessuna scritta "base si difende" a sostituire il combattimento reale.

**La difficoltà giusta di tornare indietro**: un allarme deve permettere una scelta. Esempio di tuning da testare: dalla zona più lontana, una scorciatoia già liberata dà abbastanza tempo per tornare prima di un collasso probabile, **senza promettere salvezza**. Evitare una torre che cade in tre secondi quando il player è a due minuti di corsa: non crea tensione, crea ingiustizia.

---

## 6. IL SECONDO GIRO DELLA MAPPA — perché aprire un'altra porta

Immagina una partita in cui hai prima aperto C (Mercato). Durante un'ondata più difficile esci dalla base e passi per B (Officine), pagando un'altra apertura. Da lì guadagni D (Parcheggio), da cui vedi il Deposito F ancora sbarrato. Quando raggiungi F dal lato del Sottopasso, **il circuito si chiude**: puoi fare Mercato → Sottopasso → Deposito → Parcheggio → Officine → Piazza, oppure invertire il verso. Zombie che inseguono diventano un problema di **scelta del percorso**, non di corridoio unico.

Da G puoi aprire una scorciatoia [S] sul lato della base. Se suona l'allarme durante un combattimento lontano, **ora sai come tornare rapidamente**. È la forma migliore di upgrade della "città" che si possa fare senza fabbriche: cambi materialmente il percorso del giocatore.

**Non trasformarlo in open world senza direzione:** una mappa COD Zombies ha **rami leggibili, cancelli, circuiti**, punti di riferimento visibili, spawner sicuri e ritorni studiati. Non servono chilometri di quartiere vuoto.

---

## 7. GUNPLAY, MELEE E AZIONI ORIGINALI SENZA CLASSI INUTILI

### Gunplay
Deve restare FPS vero: arma riconoscibile, ADS/rinculo/reload, colpo leggibile, audio/FX, zombie reagisce all'impatto, bersaglio mancato = mancato. Una firearm completa per volta. **Nessuna skill “colpo preciso”**: la precisione appartiene al giocare con l'arma, non a una classe inventata.

### Melee
Non è il tasto V che spinge per un secondo. Il player **sceglie un'arma melee**, cambia stance, distanza utile e rischio. Tre famiglie **come esempio di varietà**, non come quantità già decisa:
- una lama veloce apre brevemente un varco contro un zombie normale;
- un colpo contundente più lento può sbilanciare un corazzato prima che attacchi;
- una lama/asta più lunga mantiene la distanza ma è meno comoda in un corridoio stretto.
Una parata o un contrattacco sono sensati solo con **hitbox, tempi, audio e reazioni** davvero precisi. Non copiare meccanicamente un soulslike pieno di barre. Una eventuale modalità **solo melee** deve essere percorribile contro **ogni minaccia essenziale**, altrimenti è una punizione mascherata.

### Idee non-classe candidate da testare (massimo 2 in prototipo)
**A. Rumore come scelta tattica.** Un colpo rumoroso può spostare un numero **limitato** di zombie dal percorso verso la base a quello verso di te, **se realmente nel raggio e capaci di percepirti**. Non è un pulsante magico "aggro entire wave". Vantaggio: allevi pressione dalla base; rischio: attiri un gruppo mentre sei solo nel Mercato. Se 100 zombie rendono AI audio costosa, scartare o semplificare: il design non obbliga a svilupparla.

**B. L'ambiente è una piccola arma.** Una serranda abbassabile o una leva in una zona offre 2–4 secondi di contenimento con anim/suono/collision reali; poi si riapre per cooldown o per riarmo. Non 30 trappole diverse e non un sistema crafting.

**C. Contrattacco fisico in melee.** Una parata ben temporizzata sbilancia un zombie contro quello subito dietro, creando tempo per passare. Limite chiaro: niente catena infinita di stuns e niente invulnerabilità.

**Solo A, B e C sono candidate**, NON tre abilità approvate né tre classi; se una non migliora il divertimento nei test viene tagliata. Non inventare skill a cooldown, ultimate, “buff critico” o nomi di classi finché non c'è un gioco base valido.

---

## 8. PUNTI E UPGRADE — la stessa scelta vista dal player

**Ipotesi preferibile da testare:** un solo tipo di punti ottenuti prevalentemente combattendo, spesi per **porte**, **armi/equip** e **torrette/strutture**. L'utente non ha ancora fissato valuta, cifre, wallet o progressione tra sessioni: non scriverle come definitive.

**Esempio numerico esclusivamente illustrativo di una prova di bilanciamento**: una porta iniziale può costare quanto un upgrade intermedio, cosicché dopo uno o due assalti il player debba scegliere. Non fissare qui prezzi: servono prove di quanti nemici un neofita uccide realmente per minuto e quanto la torre ne elimina senza giocatore.

**Tre domande per ogni acquisto**: cosa **cambia a vista**, cosa posso **fare che prima non potevo**, quale opportunità sto rimandando? Se l'upgrade non dà risposta, tagliarlo. **No due valute per obbligare il player a scegliere tra il divertimento e un gestionale.** Una base che uccide tutto senza giocare non deve generare più risorse della persona che esplora e combatte.

Nella base bastano, come **esempio candidato**, due postazioni chiare: `Armeria / melee` e `Perimetro / torrette`. Una UI in 2–3 passaggi, niente 4 laboratori obbligatori solo perché lo diceva un vecchio documento. Tutto dentro la base, mai portare il player in una schermata di gestionale esterna alla mappa.

---

## 9. ONDATE O PRESSIONE CONTINUA — due varianti della STESSA partita

L'utente ha proposto entrambe le possibilità, **non ha scelto un sistema definitivo**.

- **A ondate** (più vicino COD Zombies): assalto, respiro breve, prossimo assalto; puoi anche rientrare e comprare **durante** l'ondata. Adatta a imparare apertura della mappa e leggere le nuove minacce.
- **Continuo**: pressione che sale gradualmente mentre il player è sempre libero di attraversare la mappa/upgrade; nessuno stop artificiale tra round. Più rischiosa per il bilanciamento: evitare che il player non abbia mai tempo per aprire una porta.

**Proposta tecnica comune**: un solo director e stessi zombie/AI/danni/torri, differiscono soltanto gli intervalli di spawn. Non presentare “due modalità complete” finché non sono state progettate/approvate e poi verificate.

---

## 10. UN ESITO CHE NON SIA UNA PROMESSA INVENTATA

Non è ancora stato deciso dall'utente se Zombie Defence sia una **run che si azzera** come COD Zombies, una **base che persiste** fra sessioni, un gioco **endless** o una partita con una **uscita finale**. Non dichiarare "10 onde boss = vittoria" né "base permanente" come requisito confermato.

**Due versioni candidate, entrambe giocabili dal menu ai risultati:**
1. **Sopravvivenza a run**: zone e torri si aprono/potenziano nella partita, l'assalto si intensifica fino a distruggere base/KO; risultati mostrano zone, durata, zombie, armi e kill vere delle torrette. `Riprova` ricomincia la run. Può durare tanto quanto il giocatore resiste.
2. **Obiettivo oltre il sopravvivere**: aprendo la mappa si raggiunge una zona finale che consente di innescare un confronto conclusivo o scegliere `Continua a resistere`. NON aggiungere un boss o estrazione obbligatoria prima che l'utente scelga questa direzione.

**Quando il player muore** è altrettanto un elemento da decidere: revive in coop, respawn nella base, perdita di una vita, ecc. Per non far saltare il concept, **la base deve comunque continuare a sparare durante un eventuale stato Downed**, e il menu risultati deve dire perché è finita la partita. Non imporre un revive class o un medico.

---

## 11. UNA PARTITA PIÙ AVANTI — la tensione deve aumentare per motivi reali

All'inizio il player può restare vicino e la sentry leggera elimina pochi camminatori. Dopo un paio di upgrade quella sentry basta a tenere il cancello iniziale contro lo stesso tipo di nemico. Il player raggiunge Deposito, apre la scorciatoia, prova melee nel Mercato e torna quando riceve un allarme.

Più tardi un zombie con armatura può resistere alla sentry che prima bastava. **Non** diventa più forte all'insaputa del player perché una barra “difficoltà 8” rende tutti immortali. La stessa arma della torre continua ad avere gli stessi valori: è il nuovo tipo di attacco, una deviazione dal percorso, la saturazione del bersaglio o un sabotaggio visibile a cambiarne l'efficacia. Il giocatore può:
- prendere un percorso di ritorno breve e cambiare difesa;
- intercettare concretamente il gruppo fuori (gli stessi actor assediatori);
- rischiare ancora esplorazione, sapendo che la base potrebbe perdere.

Questo è **il conflitto divertente del gioco**. Non servono facoltà extrasensoriali e 12 classi, servono vie, armi, zombie e difese che seguono le medesime regole.

---

## 12. COSA VERIFICA CHE NON STIAMO FANTASTICANDO

Per ogni sistema della prima versione giocabile, test con risultati osservabili (non affermazioni generiche):

| Prova | Azione nel gioco | Risultato verificabile |
| --- | --- | --- |
| Orientamento | un tester apre il menu e avvia senza spiegazione orale | trova uscita, base e primo accesso in 30–60 secondi |
| Porta vera | spende i punti e apre Mercato | animazione/colonna fisica/collisione/IA aggiornata, il gruppo attraversa |
| Mappa COD-like | segue due rami e apre una scorciatoia | attraversa un circuito completo senza teletrasporto né dead end obbligato |
| Base autonoma | host o client attraversa mezza mappa e resta assente da base per un assalto intero | torre intercetta, spara e uccide con danni server veri, senza player vicino |
| Upgrade utile | potenzia torre in base e torna fuori | stesso tipo di zombie prima superava la difesa e ora può essere fermato, con effetti visibili |
| Escalation onesta | affronta tipo nemico più pericoloso con la vecchia torre | AI/armatura/numero/abilità rendono la torre insufficiente, non un danno scriptato al Nucleo |
| Melee vero | arma da mischia contro Nurse | la lama segue il montaggio e la hitbox, la Nurse reagisce; niente colpo attraverso muro o fantasma |
| Ritorno | allarme mentre player è lontano, scorciatoia già aperta | ritorno leggibile e utile; non game over arbitrario in un istante |
| Efficacia | un player usa solo armi e un altro prova melee nelle stesse condizioni | entrambi riescono a giocare, a costi e rischi diversi |
| Pacing | tester gioca senza ricevere spiegazioni per 20 minuti | riesce a capire quale strada può aprire e perché una torre o arma vale la spesa |

**Un test tecnico non dimostra automaticamente che il gioco sia divertente.** Registra anche: voglia di aprire altra zona, fastidio per manutenzione, qualità impatti, senso della crescita base, frequenza menu, mortalità ingiusta. Se la torre troppo forte porta AFK o la mappa è una sequenza di corridoi, correggere quelle fondamenta prima di produrre altre armi.

---

## 13. COSA È FATTO, COSA NO — SENZA FINTE COMPLETIONS

**CONFERMATO DALL'UTENTE:** COD Zombies come map design aperto a zone progressivamente sbloccate; base visitabile per upgrade con autodifesa automatica; minaccia crescente; armi da fuoco+melee; possibile solo-melee; originalità e vincolo di non complicare, niente classi cliché, tutto il piano dal menu alla partita, produzione a strati, NON toccare codice in questa fase.

**PROPOSTA DA VALUTARE (non approvata):** nomi/layout di questa mappa, costo porte con punti, due stazioni nella base, comportamento di IA sensibile ai rumori, trappole ambientali, parry, durata del giro iniziale, fine partita e sistemi di reward, modalità finale, numero nemici/torri/armi.

**FATTO VERIFICATO:** esistono repository GitHub, documenti di design e un framework esterno candidato; NON abbiamo verificato in questa interazione una build UE che realizzi questo gameplay, asset scaricati/riggati, test di rete, FPS, costi di produzione o fattibilità completa delle animazioni.

**NON FARE:** iniziare Codex o modificare codice su queste proposte, trattare il backlog legacy da 112 task come approvato, chiedere a un artist di produrre 8 ambienti prima che questo gameplay di partenza venga valutato.

**Esito del presente documento:** ora il gioco è **giocabile sulla carta**, in modo controllabile e criticabile; non è ancora un GDD approvato né una build.
