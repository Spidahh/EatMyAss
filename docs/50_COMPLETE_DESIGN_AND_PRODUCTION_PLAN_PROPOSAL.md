# ZOMBIE DEFENCE — PIANO INTEGRALE DI PROGETTAZIONE E PRODUZIONE, DALLA PARTITA ALLA RELEASE

**26 ottobre 2026 · VERSIONE DA VALUTARE, NON APPROVATA DAL COMMITTENTE · SOLO DOCUMENTO, NESSUN CODICE.**

Non è una nuova lista arbitraria di classi, torri o numeri. È il piano **dell'esperienza complessiva** che mancava. Le decisioni certe del committente sono in [45](45_USER_DIRECTIVES.md); il percorso concreto minuto per minuto in [48](48_PLAYABLE_GAME_VISION_PROPOSAL.md); la mappa interconnessa e le azioni originali candidate in [49](49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md). Questo piano **sostituisce il vecchio backlog come proposta di direzione**, ma non cancella le analisi tecniche utili.

## 1. Premessa: cinque criteri inderogabili di divertimento

**A. Voglio aprire la mappa.** Entro nella mappa, intravedo zone non raggiungibili, compro/sblocco accessi, cerco scorciatoie, giro liberamente. Non è una successione di arene scollegate, né una base con soltanto tre aree sempre aperte.

**B. Voglio combattere, non tenere aperto un gestionale.** Armi da fuoco e melee con feeling distinti; scoperta e combattimento occupano la maggior parte del tempo. Entrare nella base serve a fare upgrade e scegliere: non a raccogliere minerali o curare ogni torre al secondo.

**C. Voglio vedere che la base serve.** Upgrade torretta = cambio fisico nel mondo = torre che ottiene kill vere mentre io non la guardo. Se ho fatto scelte sufficienti, una ondata può essere respinta totalmente senza il player. Il feedback non è un'informazione falsa in UI.

**D. Voglio una ragione per tornare a giocare dopo ogni sblocco.** Ogni area cambia circolazione, posizione/rischio del combattimento e cosa posso fare fuori. Ogni assalto costringe a rileggere una minaccia. Anche quando la base va bene, la mappa dà nuove opportunità e tensione.

**E. Voglio un gioco originale, non un catalogo di perk.** Se una skill equivale a “+10% precisione” non supera il filtro. Preferire azioni fisiche, zombies che reagiscono, mappe che cambiano percorso e difese che interagiscono con il mondo.

## 2. LOOP GLOBALE, non tre loop separati

```text
MENU / PARTITA
      ↓
MAPPA COD-ZOMBIES: SPAWN + PRIME PORTE CHIUSE
      ↓
FUORI: SPARI / MELEE / EVITI / GUADAGNI
      ├──→ SCOPRI + SBLOCCHI NUOVE ZONE → SPAZI / LOOP / SCORCIATOIE
      ├──→ FAI COMBAT PIÙ DIFFICILE → INVESTI NELL'EQUIP
      └──→ ENTRI NELLA BASE → POTENZI NUCLEO / TORRETTE
                                      ↓
                           AUTODIFESA REALE SENZA PLAYER
                                      ↓
                        PUOI ESPLORARE PIÙ LONTANO
                                      ↓
                           ORDE CHE CAMBIANO MINACCIA
                                      ↓
                       NUOVI PERCORSI / NUOVE DECISIONI
```

Il gioco deve continuare mentre il player entra in base; se in ondata continua, il loop è identico. I punti esatti di ricompensa, la forma della moneta e la persistenza oltre una partita sono ancora da decidere.

## 3. MENU E PRIMI 30 SECONDI — specifiche testabili

Menu chiaro, pochi bottoni veri (solo/host/join quando disponibili), opzioni/uscita. Avvio in una posizione da cui vedi contemporaneamente **uscita verso una mappa grande, primo cancello chiuso, segnale della base e uno zombie reale**. Niente cutscene lunga o 5 menu, niente selezione di 3 classi assurde prima di muovere il personaggio. Al primo ingresso la direzione è evidente. Il menu deve riprendere la fantasia “sopravvivere fuori, costruire la difesa” e il player la verifica in 30 secondi.

**DOD gameplay**: un nuovo tester senza istruzioni trova l'uscita, spara/colpisce, vede una porta acquistabile/apribile, capisce dov'è il rifugio.

## 4. MAPPA — criteri e consegne

**Una mappa sviluppata tutta e bene** prima di annunciare un numero di mappe non finanziato. La prima mappa CANDIDATA è un quartiere industriale abbandonato: garage-base, piazza, Mercato, Officine, parcheggio, sottopasso, centrale, tetti. Sono nomi/proposte artistiche e topologiche, non aree imposte dall'utente.

Ogni zona deve avere: ingresso in mondo reale, look memorabile, differenza di distanze/ripari, legame con almeno un'altra zona, vie zombie valide, elemento di interazione utile, collisioni/navigazione completa, suono proprio, illuminazione leggibile, nessun safe spot permanente. Una zona aperta non si richiude senza scelta comunicata. L'apertura aggiorna percorsi dei player/IA, suono della serranda e topologia. La zona lontana deve essere visibile presto come promessa di esplorazione.

**Grafo minimo di gioco proposto:** 2 scelte iniziali, rami che si ricongiungono, 2 scorciatoie verso area centrale/base, almeno 1 area sopraelevata con via di fuga reale. **Non sono “due zone e 3 shop”**: si percorre tutto, si gira e si torna indietro liberamente. Codex non costruisce muri temporanei per “indicare dove andranno le case”, completa geometria reale zona per zona.

## 5. SPAWN/ORDE — convivenza con la base

**Una sola minaccia/zombie system**, non due giochi. Una porzione dell'orda viene attirata/percorre route verso la base; altri zombie presidiano o inseguono il giocatore nel resto della mappa. Gli zombie **possono** cambiare bersaglio se un evento reale (rumore/linea di vista/colpo) lo giustifica, con limiti, senza moltiplicare count.

La base è un obiettivo attrattivo fisico: zombie arrivano da vie esterne, raggiungono cancelli/torrette, attaccano con animazioni vere. Turrets sparano autonomamente, incluse quando client/player sono lontani. Nuove zone aprono nuovi varchi di movimento **senza far comparire nemici dentro l'hub** o fargli attraversare muri.

**Due schemi da confrontare, non fissati:** rounds con finestra tra ondate (lettura facile/esplorazione COD) vs pressione continua (tensione elevata, meno pausa). Non creare due spawner indipendenti. Stage/pressione crescono col gioco; la variazione deve venire dalle caratteristiche delle unità e dalla tattica, NON solo da HP x10.

**DOD gameplay**: un assalto identico e con torri adeguate finisce anche senza player; un assalto più forte può superare quelle torri senza un danno scriptato; uno zombie ucciso dal player sulla route assedio non viene poi contato come vivo o respawnato “per fare difficoltà”.

## 6. BASE — come si entra e cosa si fa

Si entra fisicamente tramite un accesso con un interno vero. Dentro si interagisce con pochi punti ben organizzati (armi/melee, torrette/difese, stato base) e si vede il mondo esterno funzionare. **Solo upgrade**, non missioni e shopping NPC che sottraggono tempo.

Upgrade tower: presentare **effetto operativo nel mondo** (cambio rotazione, cadenza, specializzazione anti-corazza, resistenza/FX) e prezzo chiaro. Niente skill città inventate di propria iniziativa; la base migliora fisicamente. Upgrade personale: arma o melee e feedback visivo/sensazione, non precisione +2% come unica ricompensa. Le scelte co-op devono evitare che un singolo player svuoti la cassa condivisa senza consenso; metodo di finanziamento ancora da selezionare.

**DOD**: andare dalla zona più lontana al terminale con una scorciatoia sensata, upgrade durante siege, uscire e vedere tower comportarsi meglio, senza pause globale o nuovo livello caricato.

## 7. COMBATTIMENTO — la parte che deve reggere da sola

**Gunplay**: silhouette/weight dell'arma vera, mira e rinculo leggibili, esplosione/cadenza coerenti, reload specifico, reazione zombie con impatto distinguibile da colpo in oggetto, audio non stock per tutti. Gli zombi non possono attraversare i colpi né morire senza reazione.

**Melee**: arma impugnata con reach/collision coerente, attacco vero con anticipazione e recovery, parata/contrasto solo se funziona bene, diversa utilità per una lama veloce, un oggetto contundente e un'arma di portata (tipi CANDIDATI, non quantità approvata). Il gioco deve dare **vantaggi tattici reali** (interrompere, spostare, aprire il varco, colpire armatura con massa), non soltanto danno più grande. Lo stile solo-melee potrebbe emergere da un set di mosse/limitazioni scelto nella base, ma non deve diventare una classe cliché.

**DOD**: il player vuole scegliere il melee persino se ha munizioni; con la stessa Nurse, un'arma pesante e una lama fanno reagire in modo differente, in 1p/3p e in multiplayer.

## 8. ABILITÀ — filtro anti-cliché prima dei nomi

Nessuna lista definitiva di 3 classi. Prima progettare **azioni divertenti che hanno senso nel mondo** e poi, se utile, organizzarle come stili:
- Azione di **pressione sull'orda**: con rumore, percorso o coraggio il player devia parte dei nemici, correndo un vero rischio; si presta a ranged e melee.
- Azione di **contrasto fisico**: colpisci/parry con tempismo per sbilanciare 1 zombie, frenarne l'attacco e ritagliarti una fuga. Non è magia, non è +stat.
- Azione di **ambiente**: apri una serranda, fai cadere un ostacolo, attivi una trappola locale e gestisci la posizione. Pochi oggetti per mappa, non 15 gadget craftati.

**Tre idee da valutare, non tre classi da implementare**. Devono essere prodotte come vere animazioni/AI state/suoni/VFX se selezionate. Per ciascuna: quanto si usa? Perché qui e non un colpo di arma? Può sfruttarla il player quando la base si auto-difende? Una skill che non cambia il gameplay è scartata.

## 9. UPGRADE/ECONOMIA — scelte vere e niente softlock

Un'economia candidata **semplice** mette in competizione tre usi del valore guadagnato combattendo: aprire mappa, potenziare player, potenziare difese. Evitare 6 monete. Non fissare nomi, prezzi e due wallet senza decisione dell'utente. Evitare softlock: anche dopo una cattiva spesa deve esistere un percorso giocabile per riguadagnare risorse; se solo la torre uccide, il valore ottenuto dalla base non deve creare una strategia AFK più efficiente dell'esplorazione.

**DOD:** già alla seconda apertura il giocatore sente un'opportunità reale rinunciando temporaneamente a qualcosa. Le ricompense sono leggibili, non serve un foglio Excel per comprare una porta.

## 10. RISULTATI, RIPETIZIONE E PROGRESSIONE

Non imporre il numero 10 come finale, né boss unico, né salvataggi permanenti. La descrizione della partita completa deve gestire **un'esperienza con esito**, e almeno 2 opzioni candidate:
- `Survival run`: combatti fino alla sconfitta, risultati e restart; la base è potente **nella run**, e l'ordine delle porte cambia il tuo percorso.
- `Obiettivo/endgame`: raggiungi un'area difficile tramite apertura zone e sopravvivi ad una fase critica finale, con scelta di concludere o proseguire.

Se si desidera base persistente fra sessioni, è un'opzione da decidere esplicitamente con regole anticrafting/anti-snowball e checkpoint. Senza questa decisione non creare un sistema permanente o annullare i progressi. Descrivere sempre morte player, morte Nucleo, co-op host disconnect, continue/restart e risultati.

## 11. PRODUZIONE — un contenuto definitivo alla volta

| Fase | Contenuto che deve uscire realmente | Barriera obbligatoria prima di andare oltre |
| --- | --- | --- |
| **P0** | Valutare **partita concreta** del [48](48_PLAYABLE_GAME_VISION_PROPOSAL.md), grafo delle zone, scelte della base e risultati; tutte le correzioni dell'utente registrate | Nessuna classe, valuta, porta o modalità inventata viene spacciata per approvata |
| **P1** | UE5.8 + HordeTemplate acquisiti e ambiente reale | Engine compila e apre progetto vero, licenze per codice/asset controllate |
| **P2** | Personaggio definitivo e movimento FPS | Modello vero + mesh 1p/3p, anim, passi, danni e input funzionano |
| **P3** | Prima firearm definitiva | Mesh+anim corrette ADS/fire/reload, audio/FX/colpi server e video |
| **P4** | Prima Nurse/zombie definitiva | Vera IA Field, attack windup/hit reaction/death, anim, audio e network |
| **P5** | Prima melee definitiva contro Nurse | Hitbox reali, animazioni+impatti, parry/counter solo se scelti, no colpi fantasma |
| **P6** | Prima piazza esterna + interno base funzionanti | Giocatore entra/esce, dentro può solo fare upgrade, nessun mondo secondario |
| **P7** | Economia minima + prima porta reale + zona successiva completa | Kill reward reale, saldo/costo idempotente; porta animata/collisione/nav; apertura non finta |
| **P8** | AI Siege e direttore assalti iniziale, usando nemici già presenti | Zombie percorrono vere strade e attaccano fisicamente Core/perimetro; no trigger HP artificiale |
| **P9** | Prima torre autonoma realmente acquistabile e potenziabile | Player lontano, torre acquisisce e uccide **gli stessi zombie Siege**, no magia offscreen, test minaccia prima/dopo upgrade |
| **P10** | Secondo ramo e scorciatoia che chiudono il circuito della mappa | Due aperture alternative, vie che si ricongiungono, ritorno base reale, navmesh multiplayer |
| **P11** | Altre zone una per volta fino alla mappa completa | Ogni zona cambia combattimento o percorso, niente stanze vuote/asset finti |
| **P12** | Restanti armi, varianti zombie e difese **approvate** | Ogni nuovo oggetto completato con mesh/anim/audio/FX/AI/net prima del prossimo |
| **P13** | Meccaniche originali scelte dopo valutazione di [49](49_MAP_GAMEPLAY_AND_ORIGINALITY_PROPOSAL.md) | Solo quelle che funzionano nel gioco reale, niente classi cliché o perk generici |
| **P14** | Ritmo ondate/continuo ed esito della partita **secondo le decisioni approvate** | Menu → mappa → unlock → autonomia → escalation → fine/continuazione → retry o salvataggio se previsto |
| **P15** | QA solo/multiplayer verificato, bilanciamento, performance, licenze, Windows Shipping | Build eseguita realmente, prove filmate, niente falsi DONE e nessun codice scaricato senza permesso |

**Le fasi sono una sequenza di GAME DESIGN proposta, non ordini di scrivere codice.** Corrette dipendenze concrete: P7 punti/porta precedono gli acquisti; P8 porta la minaccia Siege vera; P9 può finalmente validare la sentry su zombie e ondate reali. Se per completare una fase manca un asset/audio/animazione, lo stato resta BLOCKED e non si aprono funzionalità di comodo che restano nel gioco. La scelta dell'utente prevale su ogni esempio.

## 12. Piano anti-errore per Codex

Codex deve poter rispondere prima di ogni task:
- Quale **decisione esplicita utente** sto eseguendo? (ID UD)
- Se manca, è proposta approvata o solo una mia invenzione? Se non approvata, STOP su quella feature.
- Quale momento concreto della partita migliora? Menu? Prima porta? Combattimento? Svolta mappa? Difesa?
- Quale asset definitivo, anim/audio/FX, IA e multiplayer devo vedere in editor per dire Done?
- Come dimostro il test **nella stessa mappa** (no demo separata che poi diventa il gioco)?
- Sto cambiando il gioco in una direzione già rifiutata? (classi banali, città fissa, torri passive, 3 zone indipendenti, colpo preciso)

Questa checklist deve essere l'entrata del piano, non l'ennesimo documento che Codex ignora.

## 13. Contratti di design aperti, non scuse per inventare

Queste decisioni richiedono ancora un giudizio **esplicito dell'utente**, non si colmano con una scusa:
`D-01` rilascio run vs persistent base; `D-02` wave o continuo o opzioni; `D-03` prezzo e meccanismo di apertura zone; `D-04` economia mono/doppia e condivisione; `D-05` equip iniziale e slot; `D-06` contenuti/esito della partita; `D-07` quali idee di abilità fisiche sono davvero divertenti; `D-08` quanti nemici/torri/mappe finali rientrano nel budget.

**Senza D-01–D-08 risolti non dichiarare “piano completamente approvato”.** È però possibile valutare il gameplay della mappa proposta **sulla carta** senza inventare scelte definitive. Il gioco non è implementato.
