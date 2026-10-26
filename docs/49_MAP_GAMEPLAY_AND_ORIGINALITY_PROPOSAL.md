> **ATTENZIONE — 26/10/2026:** [48 — GAME DESIGN UNICO](48_PLAYABLE_GAME_VISION_PROPOSAL.md) è l'unica **proposta centrale corrente**. Questo file è materiale di approfondimento **NON APPROVATO** e potrebbe contenere idee in eccesso o precedenti alternative (trappole, abilità, numeri, mappe) **NON VINCOLANTI**. Se non compare in 48, non aggiungerlo al backlog; se contraddice 48, usare la versione 48. **Resta in vigore il divieto di toccare codice** dell'utente. La fonte realmente vincolante sono le [direttive utente 45](45_USER_DIRECTIVES.md).

# MAPPA, ECONOMIA, MELEE, DIFESA E ABILITÀ — PROPOSTA SISTEMICA

**26/10/2026 • SOLO GAME DESIGN • PROPOSTA NON APPROVATA.** Documento complementare all'esperienza [48](48_PLAYABLE_GAME_VISION_PROPOSAL.md). Il committente ha già confermato COD Zombies-style unlock, mappa percorribile, base interna upgrade, base auto-defense, zombie che crescono, melee, possibili specializzazioni solo melee e rifiuto classi banali. Tutti i numeri e nomi seguenti sono esempi di design.

## A — Mappa di esempio realmente collegata (non tre zone isolate)

```text
       [TETTI / BELVEDERE] ----- scorciatoia ----- [BASE + PIAZZA INIZIALE]
                 |                                      /        \
       [CENTRALE SMISTAMENTO]                   porta A          porta B
           /             \                       /                  \
    [PARCHEGGIO]       [SOTTOPASSO] ---- [MERCATO COPERTO]     [VICOLO OFFICINE]
           \                  |                 /                /
            +------ PASSERELLA/ANELLO ---------+----------------+
```

**SCHEMA CANDIDATO**, non level final autorizzato. Il contenuto indispensabile è la **struttura a grafo**: iniziale con almeno due aperture, rami con spazi tatticamente diversi, incroci che ricongiungono i rami, due o più shortcuts che tornano vicino alla base e una destinazione lontana chiaramente visibile prima di poterla raggiungere.

**Sezioni funzionanti:**
1. **Base/garage**: UPGRADES al suo interno, Nucleo e perimetro automatico all'esterno. Puoi tornare sempre. Non è un negozio/menu separato.
2. **Piazza iniziale**: due vie visibili, base visibile, arene per insegnare ranged e melee.
3. **Mercato coperto**: angoli stretti; melee, vie secondarie e possibilità di trappola ambientale, non gestione negozio.
4. **Vicolo officine**: linee di tiro più lunghe, vie rialzate e ingresso al parcheggio.
5. **Parcheggio multipiano**: verticalità e connessioni, giusto spazio per correre attorno a un gruppo; evita punti perma-safe.
6. **Sottopasso**: percorso rischioso ma scorciatoia utile, combat close; non un corridoio irreversibile.
7. **Centrale smistamento**: destinazione che si può intravedere molto presto, sblocca una nuova via tattica/elemento di mappa.
8. **Tetti/belvedere**: accesso alto, percorso rapido di ritorno se aperto, percezione del mondo interconnesso.

**Regola fondamentale**: un settore non è “una stanza vuota + 2 zombie”. Deve introdurre almeno uno tra: spazio diverso per combat, percorso alternativo, cambio di visibilità, scorciatoia, interazione ambientale. Una nuova porta NON deve aprire un spawn direttamente dentro base o raddoppiare i budget.

## B — Come si apre una zona

**Modello proposto, non approvato**: porte/serrande bloccate con prezzo di punti accumulati combattendo, analogamente al principio di COD Zombies; altre scorciatoie si attivano dall'altro lato o con una semplice azione dopo aver raggiunto l'area. Non imporre ricerca di chiavi e 5 generatori per ogni porta. Un solo gesto di acquisto/uso, chiaro costo/rischio.

Per ogni ingresso `GateDefinition`: `GateID`, aree che collega, direzione visuale, costo in unità **da decidere**, animation/open progress, collision/nav transition, connected spawn groups, audio cue, all clients replicated. Chi paga vede il gate aprirsi nel mondo, non semplicemente sparire.

La progressione è **nella mappa della stessa partita**; sbloccare una porta crea un nuovo percorso **per tutti** i giocatori della sessione. La base resta raggiungibile con un cammino non inutilmente lungo. Nel caso co-op, più player possono contribuire al costo oppure contribuire a un acquisto comune; NON è una valuta definitiva già approvata.

## C — Una regola fisica semplice per collegare spari e assedio

**PROPOSTA PRIORITARIA: gli zombie rispondono ai suoni.** Non inventare un RPG skill system per creare una sinergia: il mondo stesso lo fa.

- Sparare rumorosamente in una zona attira, entro un raggio misurato, un **numero limitato di zombie vicini**, non tutto il server. Puoi scegliere di attirare parte della pressione verso di te, ma ti esponi a un combattimento più difficile.
- Un'allarme ambientale attivabile in una zona potrebbe attirare un piccolo gruppo per una trappola (se implementato con FX/SFX corretti). Nessun dispositivo “magico”.
- Un zombie impegnato in assedio non diventa automaticamente preda di qualsiasi sparo lontanissimo: il director controlla l'aggressività e protegge la logica del Nucleo.
- Se attiri un assediatore, è lo **stesso actor** che cambia obiettivo e non un nemico duplicato; se muore, il suo vero assedio è alleggerito. La torretta continua a difendersi da quelli rimasti.

**Perché è interessante:** un melee specialist può farsi inseguire e tagliare una rotta, un ranged shooter apre un fronte rischioso, la base guadagna tempo attraverso scelta reale del giocatore. **Perché resta semplice:** un singolo sottosistema `HearStimulus/Retarget` sullo zombie che esiste già, senza skill trees o nuovi currency.

## D — Melee capace di farsi scegliere volontariamente

Il melee deve essere **un modo di giocare**, non un attacco di emergenza. Proposta di grammatica comune:
- Colpo rapido LMB con range/arco e timing per arma; colpo forte tenendo LMB solo sulle armi adatte.
- Parata RMB davanti a sé con finestra breve di controazione; senza invulnerabilità globale.
- **Corpi con reazioni vere**: spostamento/stagger breve quando colpiti, suono carne vs corazza, attacco zombie interrompibile soltanto prima della finestra di danno.
- **Effetti sulla minaccia**: un colpo alle gambe di uno zombie normale può farlo inciampare (non dismemberment obbligatorio), un attacco pesante su armored può scoprire un punto fragile invece di spammare danno invisibile.
- **Rischio in cambio di vantaggio**: un'uccisione melee in una situazione difficile può premiare leggermente di più nel sistema punti scelto, ma non creare una nuova valuta rage/stamina separata a priori.

**Possibile specializzazione solo-melee** = modifica concreta di movimenti/counter/colpi e miglior controllo del gruppo nel ravvicinato, **non una classe “guerriero” con +20% danno**. Non definire nomi, abilità o bonus specifici come approvati.

## E — Tre meccaniche davvero legate agli zombie (candidate, non classi)

1. **Devia-orda**: quando ti esponi e attiri il gruppo verso un percorso sicuro, puoi liberare fisicamente un accesso al perimetro per alcuni secondi. Nasce da rumorosità/linee di fuga, non da spell o skill Q. Limite: non funziona su ogni nemico, non cancella l'onda.
2. **Controcolpo fisico**: parare bene un colpo dà occasione di sbilanciare **un singolo zombie** contro quello dietro di lui, aprendo un varco. Richiede reazioni realistiche, non un AoE ultraterreno. Limite: un solo chain, niente perma-stun.
3. **Ambiente come arma**: un numero molto ristretto (uno o due per zona importante) di elementi già presenti — serranda, compressore, passaggio elettrico — che possono contenere o ferire zombie per pochi secondi. L'uso richiede posizione, attivazione e breve cooldown; non sostituisce armi e torrette, niente crafting.

**Queste non sono tre classi, non sono abilità finali e non devono essere inserite automaticamente nei task.** Sono azioni di gioco da provare mentalmente prima di decidere quale meriti sviluppo.

## F — La base automatica non deve distruggere il divertimento

Regola economica/di combattimento proposta: base con difese adeguate può vincere un'ondata **da sola**, con danni e kill REALI simulati server. Questo non significa che il player stia AFK a guadagnare risorse infinite. Il player **apre mappa, guadagna molto più efficacemente combattendo e può proteggere una linea** quando la nuova minaccia oltrepassa la tecnologia costruita.

- **3 scelte di spesa distinte** in una stessa risorsa proposta: comprare percorso nella mappa, migliorare proprio equip, potenziare base. Sono la vera economia del loop.
- **Tower kill award**: se si decide che le kill della base assegnano punti, dev'essere ridotto e/o limitato per ondata; se zero, la base non permette farming AFK ma devi capire come supportare il giocatore quando è in difficoltà. La regola va scelta dopo simulazione, non è stata approvata.
- **Minaccia cresca con tipi/tattiche, non solo HP**: resistenti, corridori, sabotatori visibili, cambi di priorità. Una torre adatta batte il suo nemico giusto; non esiste boss magicamente immune alla torre.
- **Previsione leggibile**: breve stato radio `Base sicura` / `Sotto pressione` / `Pericolo` sulla base di HP e capacità realmente misurati, non percentuali inventate.
- **NO doppio sistema di ondate**: una direzione d'assedio, con opzione ritmo continuo come possibilità progettuale, non obbligo già fissato.

**Test fondante:** mentre il giocatore è lontano dall'hub, i nemici Siege percorrono vere route, le torrette sparano davvero, i corpi reagiscono e muoiono, e la situazione cambia a seconda di tier e composizione. Nessuna eliminazione finta con «remove enemy after 30s».

## G — Ciclo decisionale senza menu infinito

```text
ARMA + MELEE (FUORI)
       |
       v
ZOMBIE / PERCORSI / PUNTI
       |
       +------> SBLOCCA PORTE → NUOVI SPAZI / SCORCIATOIE
       |
       +------> RINFORZA IL COMBATTIMENTO PERSONALE (dentro la base)
       |
       +------> RINFORZA LA BASE (dentro la base)
                         |
                         v
              AUTODIFESA MIGLIORE
                         |
                         v
             PIÙ LIBERTÀ DI ESPLORARE
                         |
                         v
                NEMICI PIÙ DIFFICILI
```

**Tutto si vede giocando**, non è un albero punti invisibile.

## H — Rischi e scelte ancora non approvate

1. **Durata run**: 20–40min, endless, progress host? Nessuna confermata. La mappa deve avere aperture utili nelle prime decine di minuti qualunque sia la durata definitiva.
2. **Moneta**: costo porte/upgrade con una sola risorsa è una proposta sensata, NON decisione già firmata dall'utente.
3. **Permanenza upgrade**: la base cresce durante la partita; salvataggio fra partite è un'altra decisione. Non usare la prima per imporre il secondo.
4. **Boss/quest/extraction**: non vincolati. Un finale va concepito ma può essere opzionale o sopravvivenza endless.
5. **Numero esatto di aree/torri/classi/melee**: le categorie servono a illustrare un sistema, non autorizzano un backlog fisso con 36 assets.
6. **AI audio / effetto colpi**: validare costo rispetto a 100 zombie, scartare se disturba server; il gioco deve rimanere fluido anche senza gimmick.
7. **No specializzazioni banali**: prima giudicare cosa si fa con mouse/tastiera in combattimento, poi eventualmente chiamarlo stile o classe, mai il contrario.

## I — Scenari di test su carta, prima di Codex

| Scenario | Giocatore | Base | Cosa vogliamo vedere |
| --- | --- | --- | --- |
| Apertura prima porta | compra il Mercato e corre nell'area | spara ai primi Siege | i nuovi percorsi sono giocabili, la base non smette di sparare |
| Giro lungo | passa dal Mercato a Parcheggio e torna dalla scorciatoia | difende automaticamente | non esiste un vicolo obbligatorio, il loop è memorabile |
| Melee contro gruppo | para uno swing e si apre un varco | nessuna dipendenza dal player | combat ravvicinato premia tempismo, non solo +stat |
| Minaccia speciale | affronta fuori un corazzato | torre leggera fatica | serve scegliere: intercettare, cambiare upgrade, rischiare |
| Fortezza potenziata | esplora la zona più lontana | vince Siege coerenti da sola | killer AI e proiettili reali, non “autowin” |
| Onestà difficoltà | resta con upgrade vecchi troppo a lungo | subisce danno per AI reale | non HP scriptato; chi torna in tempo può correggere |

La priorità di fattibilità è **una mappa ben connessa, una buona arma da fuoco, un buon melee, uno zombie realistico, un primo upgrade torre autonoma** prima di decine di boss e sistemi non decisi. QA e test fanno parte del lavoro finale di ogni strato.
