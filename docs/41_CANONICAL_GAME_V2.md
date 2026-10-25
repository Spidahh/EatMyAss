# ZOMBIE DEFENCE — CONCEPT CANONICO V2 (25/10/2026)

**FONTE PRINCIPALE.** Questo documento sostituisce **integralmente** l'idea precedente della “città da esplorare/acquistare” e del giocatore costretto a combattere accanto al Nucleo. Codex non deve recuperare i vecchi requisiti dai documenti storici. Il gioco non è stato ancora implementato: queste sono specifiche di prodotto.

## La fantasia centrale

**Costruisci una BASE che impara a sopravvivere senza di te, mentre tu combatti FUORI.** Dentro entri per effettuare upgrade, scegliere armi, specializzazioni e moduli di difesa. Fuori giochi in FPS action con armi da fuoco **e armi melee vere**, abbatti zombie e completi interventi brevi che finanziano la crescita. I nemici attaccano automaticamente la base anche se il giocatore è lontano, impegnato in un'altra battaglia o al suo interno. Le difese evolvono fino a respingere da sole gli assalti di livello attuale; nel tempo la minaccia sale e rende necessari nuovi investimenti e uscite in combattimento.

L'area urbana/industriale è **ESTERNO DI COMBATTIMENTO**, NON “la città-base” e NON un sistema di quartieri comprabili: officina, deposito e tetti come livelli di upgrade urbano **SONO CANCELLATI**. Al loro posto c'è UNA base centrale accessibile fisicamente, con sala upgrade e perimetro automatico. Il resto della mappa sono zone esterne da combattere, non da gestire.

## Esperienza in sei passaggi

1. Il player nasce **DENTRO** la base, passa alle postazioni `Armeria`, `Comando`, `Difese` e `Specializzazione` (poche postazioni semplici, non mini-game).
2. Esce da un cancello: parte il gameplay FPS/melee nel territorio attorno alla base. Nessun portale o cambio livello necessario nella prima mappa.
3. Uccide orde/elite e completa incarichi di combattimento **facoltativi** (3 categorie: eliminare un capobranco, distruggere un richiamo, riconquistare cassa rifornimenti dopo scontro). Ottiene **una sola risorsa: Rottami**, direttamente dalle uccisioni e dagli obiettivi, senza sacchetti da raccogliere a terra o ricette di crafting.
4. Intanto l'assalto dei nemici verso la base continua indipendentemente dalla posizione del player. Le torrette puntano, sparano, fanno danno e uccidono zombie autonomamente; le barriere assorbono colpi; le strutture possono essere sopraffatte o sabotati.
5. Il player può **rientrare quando vuole** attraverso i cancelli, anche durante un'ondata, aprire i terminali e comprare/assegnare upgrade usando Rottami. Dentro non si combatte, si gestisce la crescita con UI minimale; l'assedio all'esterno **NON si ferma**.
6. Quando la base è troppo forte per la minaccia presente, vince le ondate SENZA INTERVENTO. La minaccia cresce, introduce corazzati/sabotatori/elite e riduce progressivamente il margine. Il player deve guadagnare nuovi Rottami fuori e costruire meglio; può uscire a interrompere un gruppo nemico o rientrare a rinforzare la base.

## Obiettivo del gioco

Un ciclo di assedio **persistente** con progressione a stadi. Mappa base e difese restano salvate fra sessioni sul PC host. Prima tappa milestone **10 assalti** e uno speciale; dopo la tappa si può continuare la difesa con difficoltà crescente senza reset della base. Non inventare un secondo director: due ritmi configurabili sullo STESSO codice:
- **Ritmo a ondate (default):** assalti finiti con 15–30s fra uno e l'altro; si può comunque entrare nella base DURANTE l'ondata, non serve aspettarne la fine; player non teletrasportato.
- **Ritmo continuo (alternativa):** coda nemici continua e stadi di escalation temporizzati con avvisi; upgrade, ritorno alla base e autonomia funzionano identicamente; nessun “Game Over al timer” finché il Nucleo vive.

**Game Over solo se il Nucleo viene distrutto** (in co-op tutti i player KO non distruggono automaticamente la base). Il player sconfitto fuori rientra nella base dopo cooldown/spawn sicuro; la difesa continua. Niente invasione gameplay interna alla stanza upgrade nella 1.0. Non simularne la minaccia sullo sfondo offline: **quando nessuno gioca, il mondo non avanza e non consuma risorse**.

## Numeri chiusi per la prima release (scope)

- FPS Windows UE5.8, framework HordeTemplate come base designata, solo e co-op listen-server fino a 4 se verificato.
- **Player armato anche di melee**, parata, tempismo, reazioni d'impatto, combo breve e counter-play. Non è un FPS con solo una spinta V.
- **3 specializzazioni di combattimento** (non 3 personaggi obbligatori): `Tiratore` (fucili), `Spezzatore` (melee puro), `Tecnico` (supporto all'autodifesa). Tutti possono usare armi da fuoco e melee salvo scelta volontaria “Mischia pura” nello Spezzatore che concede bonus ma blocca le armi da fuoco finché equipaggiata. Nessun ruolo Medic obbligatorio, revive condiviso.
- 4 armi da fuoco massime: AR, pistola, SMG, shotgun; **3 armi melee** iniziali: machete, mazza pesante, lancia/arma lunga corta. Nessuna arma finta. Ogni weapon categoria deve avere rig, animazioni, hit/collision, suoni/FX e perk reali.
- **Base difesa automatica**: Nucleo/Comando, barricata-porta, torretta rapida anti-orda, torretta pesante anti-corazza e **1 potere automatico di emergenza** del Nucleo. No manual ping target obbligatorio, no microgestione nelle ondate, no energia da ricaricare a mano.
- **5 archetipi nemici**: camminatore, corridore, corazzato, sabotatore, bruto speciale (boss milestone). Fuori possono esistere capibranco/“richiami” come varianti/event actors, NON extra nemici 3D da produrre senza render. Ogni tipo ha animazioni/combat AI esatti.
- **Una base** e **3 zone esterne di combattimento** con diverse coperture/spawn/opportunità; no 3 settori di città da comprare né esplorazione open world.
- **Una risorsa Rottami**, usata per armi, upgrade personali e base. Nessun PC/TF separato, niente materiali di crafting; capacità elettrica del Nucleo è un limite alle torrette, NON valuta.
- **Una modalità assedio** con due ritmi, 10 stadi bilanciati + escalation facoltativa, un solo GameState, ai server spettano danni e upgrade.

## Progressione permanente senza MMO

- Base, torretti/slot e tier, armi/varianti sbloccate, denaro e stadio assalto si salvano fra sessioni **solo quando il gioco è offline/host termina su checkpoint valido**. Nessun timer offline o farming passivo a gioco chiuso.
- Per ridurre rischio di save corrotti e “devo per forza giocare altre due ore”, salvataggio dopo transazione/upgrade e a confine ondata; se l'host cade durante assalto riparte dall'ultimo checkpoint *all'inizio dello stadio* con economie idempotenti.
- In co-op **lo stato di base appartiene all'host**. Gli ospiti utilizzano equip e scelta ruolo nella sessione; niente inventare account globali o store.
- Progressione armi e classi è orizzontale e per-run/host-profile; niente skill tree infinito.

## Cosa rende questo gioco diverso

- La miglior ricompensa dei tuoi upgrade è **non dover presidiare la base**: puoi allontanarti per combattere, specializzarti e fare incarichi pericolosi mentre senti via radio “Perimetro stabile”.
- Un assalto supera le tue torrette? Il problema non si risolve con clic alla base in ogni secondo: hai scelto tecnologia sbagliata/upgrade insufficienti e devi crescere.
- Ogni giocatore è utile: il Tiratore elimina bersagli a distanza, lo Spezzatore domina il corpo a corpo, il Tecnico aggiorna le difese più efficientemente. Ma **non esiste composizione obbligatoria**.
- Difficoltà onesta: se la base ha potenza sufficiente, difende da sola, anche senza player; dopo alcuni stadi i nemici cambiano tattica/HP per superarla. Non rendere boss magicamente immune alle torri e non imporre un player vicino per farle sparare.
- Non c'è il ciclo “esco→raccolgo 40 legni→torno per craftare”: combatti→guadagni→decidi upgrade.

## Referenze verificate, NON modelli da clonare

- [The Riftbreaker](https://www.riftbreaker.com/): base e automatic defenses convivono con esplorazione e attacco, ma qui niente fabbriche/mine né vista isometrica.
- [7 Days to Die — Blood Moon](https://7daystodie.wiki.gg/wiki/Blood_Moon_Horde): minaccia crescente e ondate contro una base; niente mining, crafting o muri posizionati liberamente.
- [Killing Floor 2](https://killingfloor2.com/overview/weapons.html): melee con parry, armi reali e ruoli fisicamente distinguibili; non riprodurre equip/gore/brands protetti.

## Precedenza tassativa

Questo documento e i successivi 42–44 e AGENTS.md V2 prevalgono sui precedenti 00–40. I precedenti potranno essere consultati solo per *dettagli che non contraddicono* questa concezione. Il backlog CSV V2 è l'UNICO eseguibile per Codex. Non costruire la “città con bonus discount ammo” o il “Nucleo che rallenta solo su E” della V1.1; sono stati **ritirati**.
