# TERRITORIO ESTERNO, EVENTI, ONDATE CONTINUE E SALVATAGGI

## Livello unico con hub centrale e 3 territori FUORI (non quartieri da comprare)

- **Zona A – Perimetro esterno**: piazzale industriale rovinato, linea di difesa della base visibile, coperture e zombie base. Nuovi player imparano rifle+machete e vedono una torretta che si difende da sola.
- **Zona B – Smistamento**: cortili/container/strade con più corridoi per melee, elite corazzati, Richiami. Un incarico è uccidere un capobranco/richiamo che aumenta l'intensità del fronte.
- **Zona C – Area infetta**: esterno di stabilimento/deposito lontano dalla base, zombie più forti e Bruto occasionale; premi Rottami migliori perché più pericoloso, non perché raccogli erbe/legni.
- Le zone sono **aree di gameplay già previste nella stessa mappa**, non beni immobili acquistati con Rottami. Si possono aprire per difficoltà/stadio minaccia/porte di world progression se necessario, NON come upgrade della città.

## Tre categorie di eventi giocabili

1. **Sopprimi il Richiamo**: un Walker/Runner elite incita gli assediatori (comportamento, voce/marker distinti senza un modello nuovo obbligatorio). L'evento indica un punto esterno; se lo uccidi, il prossimo budget assedio è **ridotto temporaneamente** di un quantitativo massimo limitato (seed 10%, un solo evento per stage, non stack). Altrimenti il mondo prosegue: la base deve poter combattere comunque.
2. **Elimina un Elite**: corazzato o variante potente con weakpoint chiaro; se vinci ricevi bonus Rottami e una **finestra di respiro** (riduzione lieve, non freeze di spawn). Machete e mazza devono essere validi ma con rischi diversi.
3. **Difendi un recupero**: raggiungi il relitto fuori, attiva E 2–3s, respingi piccoli gruppi per una durata breve e incassi Rottami. Nessuna costruzione automatica di cassa, niente inventario scavenging multi materiali.

Gli eventi sono facoltativi, max **uno attivo alla volta**, scegliibili via radio/hud; non diventano una lista MMO. Le ricompense di eliminazione ordinaria restano abbastanza per upgrade base lenti; fare missioni accelera, non è l'unico modo di progredire. Niente NPC/cittadini/traffic/trader simulation.

## Direttore unificato: automazione e minaccia vera

Il director server divide minacce totali in `SiegePressure` (attacco base) e `FieldPressure` (territorio attorno player), con cap per zona e budget totale. Se player lontano NON sospendere assalto e AI torrette; se player dentro NON poppare zombie in hub. In co-op 4 separati, le AI continuano su player outside e hub; non duplicare l'intera horde per ogni giocatore. Boss e invasori attaccano base se previsto dallo stage, ma possono anche combattere player all'esterno in modo raggiungibile.

**Ritmo assalto**: dieci stadi campagna da 2–4 minuti ciascuno (seed), mini pausa 15–30s **senza teletrasporto né freeze delle torrette**, poi ulteriori stadi infiniti oltre 10 a difficoltà progressiva limitata da cap hardware e fairness. Stadio 10 contiene Bruto speciale ed è un traguardo, non necessariamente reset/schermata fine. **Ritmo continuo**: stessi dieci livelli di difficoltà ma con spawn continuo e stage counter temporizzato, niente on/off delle torrette, nessun secondo sistema. Una sola `ZDThreatDirector` con `Mode=Waves|Continuous`.

### Auto-defense sempre in funzione

La differenza “base power ≥ siege pressure” deve esistere nel gioco. Scenario di QA: player parte da dentro, monta torrette, esce nella Zona B per almeno 2 minuti mentre il Core viene attaccato W3. Se le torrette sono adeguate la base resiste e uccide l'ondata **SENZA PLAYER**. Poi avanzando a W7 senza upgrade l'autodifesa peggiora, e con nuova heavy turret o tier torna competitiva. Non barare: questa traiettoria deve venire da caratteristiche nemico/tower e misure reali, non da uno script che toglie HP al Core “perché lo vuole la storia”.

## Complicazione dei nemici progressiva (senza 20 tipi)

W1–3 Walker/Runner → W4–6 Armored, primo sabotaggio → W7–9 elite e attacchi combinati, W10 Bruto speciale; oltre W10 gli archetipi crescono in numeri/varianti di comportamento, non si aggiungono nuove mesh senza approvazione. In ritmo continuo le stesse soglie avvengono a stage tempi equivalenti, con tetto FPS.

## Rottami, morte e loop persistente

- **Una sola valuta:** Rottami. Reward kill e obiettivi assegnati server direttamente al saldo della base/partita, senza dover lootare manualmente corpi o fare crafting di materiali.
- Comprare armi e difese **solo nella base**, costo chiaro e conferma, upgrade con differenza visiva.
- Se il player muore fuori: Downed breve, compagno può rianimare; in solo respawn automaticamente dopo 10s (seed) nel lato interno del cancello. Nessuna ricompensa per morte, objective reset se scade, giocatore non fa perdere automaticamente la partita.
- Se tutta la squadra è KO, la base continua automaticamente; dopo respawn si può tornare a combattere. Al CoreHP0 viene mostrata sconfitta ed è possibile ricaricare checkpoint stabile.
- Autosave: alla fine di ogni assalto/ogni upgrade base server, con journal transazioni. Uscita volontaria nel mezzo dell'assalto salva l'ultimo checkpoint sicuro e chiede conferma. Nessuna difesa “offline” quando il gioco è chiuso.
- Profilo base del **host** persiste fra sessioni; ospiti co-op non duplicano risorse/progressi propri quando cambiano host. Nessun account/database cloud.
- In solo partite con durata breve possibile interrompere e tornare, il senso della base non scompare dopo 10 onde; scelta Nuova Base reset volontario in menu con conferma.

## Evitare la perdita del feeling FPS

Mai trasformare gli eventi in “raccogli 5 pietre/legna”, attese NPC 30s, escort infinite, crafting recipe o inventario di risorse. Il gameplay fuori è combattimento diretto + skill. La soddisfazione di upgrade base arriva quando le torrette *davvero* abbattono un'orda mentre tu sei impegnato altrove. Nessun modulo finto invisibile nei menu.
