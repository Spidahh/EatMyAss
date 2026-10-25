> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# Game Design Document — Zombie Defence v0.1

**Questo documento contiene una proposta completa, non una serie di requisiti già approvati.** I numeri sono seed di playtest. Non usare riferimenti specifici a contenuti, mappe, grafica o marchi Call of Duty nel prodotto: prendiamo solo il genere di esperienza come ispirazione.

## 1. Fantasy e posizionamento

Una squadra tiene in piedi un avamposto costruito su un complesso industriale durante l'epidemia. Il **Nucleo** alimenta luci, cancelli, torrette e comunicazioni. Ogni settore recuperato mette a disposizione opportunità preziose ma apre nuove linee di attacco. Il giocatore ha sempre un'arma in mano, può spostarsi liberamente in FPS, rianimare compagni, investire denaro in armi o difese.

Visuale first-person, locomozione modern FPS con sprint, mira, reload, scivolata **solo se il template offre già un buon feeling** (non requisito iniziale); nessun crafting di 50 materiali, nessuna raccolta survival, nessun negozio da gestire, nessun timer di attesa persistente.

**Unique hook:** *Ogni ampliamento della base è un rischio tattico.* Aprire un'officina dà nuovo spazio/upgrade e una linea di fuoco migliore, ma anche nuovi varchi. Bisogna decidere quando farlo e come difenderlo.

## 2. Loop a tre scale

**Secondo per secondo:** mirare → sparare → colpire/interrompere → muoversi e gestire munizioni → proteggere obiettivo/alleati → ricevere crediti e feedback immediato.

**Minuto per minuto:** leggere la direzione dell'assalto → riparare barricata o schierare torretta → usare abilità di classe → scegliere un punto critico → rischio in prima persona mentre difendi la base.

**Tra ondate (tempo breve, voto per anticipare):** comprare 1 upgrade arma o difesa, condividere piano, eventualmente sbloccare un settore e scegliere il prossimo investimento. Non costruire un sistema gestionale separato.

**Lungo periodo (fuori partita, post-V1):** cosmetici/riconoscimenti, eventualmente unlock orizzontali. Evitare una metaprogressione che renda banali le prime ondate o penalizzi i nuovi amici.

## 3. Struttura della partita

| Elemento | Vertical slice | V1 proposta |
| --- | --- | --- |
| Giocatori | 1 + sessione co-op 2 in test | 1–4, offline/LAN/listen server |
| Durata | 12–20 min stimati | 25–40 min stimati |
| Onde | 6 | 10 + variante endless in seguito |
| Base | un Nucleo, 2 ingressi | un Nucleo, 3 linee di difesa |
| Settori | cortile + 1 sblocco | cortile, officina, deposito, tetto (3 aree espandibili) |
| Classi | Assaltatore | Assaltatore, Ingegnere, Soccorritore |
| Nemici | 3 | 4 + evento/boss |
| Difese | barricata + sentry | barricata, sentry, rallentamento, mortaio solo dopo test |

**Flow della sessione:** scelta classe/equip iniziale → ondata attiva → pulizia residui e ricompense → scelta/riparazione potenziamento breve → prossima ondata → evento espansione → elite/boss → vittoria/risultati → ritorno lobby.

Sconfitta: HP Nucleo = 0 **oppure** tutti i giocatori incapacitati, nessuna rianimazione possibile. Vittoria: boss/ultima ondata superata con Nucleo vivo.

## 4. Combattimento e sensazione delle armi

Priorità di qualità: input responsive, rinculo leggibile, fire cadence corretta, reload sincronizzato con animazioni, headshot ben comunicato, impatti su carne/metallo diversi, danno in base a distanza, indicatore munizioni e hitmarker discreto. I nemici devono reagire ai colpi senza trasformare ogni proiettile in un lock/stun infinito. Reazione breve solo per soglia danno, headshot o colpo pesante; i nemici elite resistono al flinch ripetuto.

Archetipi armi iniziali:

- **Pistola:** affidabile economica, risparmio colpi in testa.
- **Fucile d'assalto:** medio raggio e flessibilità, miglioramenti di stabilità/ricarica.
- **Shotgun:** protezione di varchi ravvicinati, rischio avvicinarsi.
- **SMG / LMG:** aggiunte successive se tempo, animazioni e audio completi.

Upgrade arma `T0 → T1 → T2 → T3`: danno (+), controllo/rinculo, capacità o bonus contro un archetipo. Gli upgrade cambiano mesh/parti/materiale quando possibile. **Non** cambiare magicamente tutte le statistiche contemporaneamente. Accessori secondari solo se il gunplay base è solido.

## 5. Classi (non sono tre HP bar con colori diversi)

| Classe | Passiva proposta | Abilità attiva | Contropartita |
| --- | --- | --- | --- |
| **Assaltatore** | stabilità durante raffiche e swap più rapido | Sovraccarico: per breve tempo maggior controllo e penetrazione di bersagli leggeri | meno efficace nel ripristino difese |
| **Ingegnere** | riparazione strutture più efficiente; torretta vicina con migliore affidabilità | Ripristino d'emergenza su difesa/nucleo con cooldown | nessun grande bonus al danno diretto |
| **Soccorritore** | revive più rapido; kit ridotto per compagno | Impulso curativo breve nel raggio | meno vantaggio di danno e struttura |

Le classi **non** devono rendere impossibile vincere in solo: un giocatore può comunque riparare e curarsi; la classe rende quel compito più efficiente. Nessuna classe deve essere obbligatoria in squadra di quattro. Cooldown e durata da playtest, abilità associate a UI chiara. Per il vertical slice implementare una classe e il contratto tecnico delle altre.

## 6. Zombies e director

| Nemico | Comportamento | Minaccia specifica | Contromossa |
| --- | --- | --- | --- |
| Camminatore | prende la via breve, pochi HP | massa numerica | tiro preciso/torretta |
| Corridore | velocità e aggiramento, meno HP | costringe a muoversi | controllo varchi/reazione |
| Corazzato | lento, resistenza frontale | supera fuoco leggero | puntare punti deboli / fianchi |
| Sabotatore | prioritizza struttura attiva | spegne difesa strategica | intercettazione manuale |
| Boss (W10) | telegraph chiari, fasi, colpisce nucleo o spegne torri | rompe il piano statico | squadra coordinata, focus weakpoint |

Non promettere AI 'intelligente' senza comportamento provato. Il director controlla budget per ondata, composizione, varchi disponibili, intensità, massimo attivi; **non genera zombie dietro la visuale se sembra un trucco ingiusto**, non teletrasporta nemici davanti al giocatore. La salute scala poco, la pressione soprattutto per numero, velocità, pattern e compresenza di archetipi.

AI obiettivo: pesi dinamici `player`, `Nucleo`, `torretta`, `barricata` a seconda dell'archetipo. Evitare che tutti si accalchino sullo stesso punto. Se la torretta è distrutta, ripianificare; se un percorso è irraggiungibile, scegliere un ingresso lecito o attaccare un blocco, mai camminare contro un muro per 30 secondi.

**Fairness rules:** almeno un percorso verso obiettivo; marker ingresso/rumore di allerta; minimo intervallo leggibile tra colpi elite; cap di spawn; ingresso non attivo finché area non è stata aperta e protetta; no spam permanente di stun.

## 7. Base, costruzioni, torrette, trappole

**Scelta strutturale V1:** difese su **socket/piazzole predefinite**, non costruzione libera. È una decisione di costo e robustezza: impedisce exploit di chiusura sentieri, migliora il disegno degli assalti, semplifica navigazione, rete e telegraph. Un building mode libero è feature successiva condizionata dai test AI/navmesh.

| Struttura | Acquisto e funzione | Upgrade distinti | Vulnerabilità |
| --- | --- | --- | --- |
| Barricata | rallenta e assorbe colpi al varco | HP / rinforzo / piccole feritoie | può essere distrutta, non impermeabile |
| Torretta sentinella | ingaggia camminatori in cono, richiede LoS | gittata / cadenza / bersaglio prioritario | munizioni/raffreddamento; sabotatore |
| Campo rallentante | rallenta per breve tempo, non immobilizza | raggio / durata / recupero | cooldown, debole contro boss |
| Torretta pesante (post-V1) | anti-elite con fuoco lento | perforazione / splash controllato | costo molto alto, non anti-horde |

Ogni dispositivo ha `ownerTeam`, `HP`, `tier`, `socketID`, `cost`, `targetPolicy`, `cooldown/ammo`, `powerRequired`, `visualState`; client chiede azione, server verifica crediti/piazzola/stato fase e conferma. Compagni vedono preview o contestualmente una notifica; niente acquisto concorrente di due torri nello stesso socket.

**Punto chiave di design:** una torretta può tenere piccoli zombie, non sostituire il giocatore. Boss ed elite devono richiedere movimento, bersagli deboli, competenza FPS e interventi manuali. Limite torrette attive per zona e costi crescenti. Evitare automazione completa che trasformi il gioco in idle.

## 8. Nucleo / base principale

Il Nucleo ha barra HP, energia o capacità difensiva e livelli `T0–T3`.

- `T1 Fortificazione`: più HP e piccoli ripari visibili; non cambia la logica del gioco.
- `T2 Rete elettrica`: abilita una piazzola aggiuntiva/ricarica dispositivi in settore raggiunto.
- `T3 Comando`: sblocca una scelta finale tra riparazione d'emergenza o bonus difese, **non entrambi**.

Non integrare tre valute aggiuntive per queste strutture. Il costo deve competere con armi e torrette, ma senza punire chi salva la squadra. La base resta visivamente trasformata e il danno resta leggibile (luci, fumate, scintille, stati materiali).

## 9. Mappa espandibile (da level design, non da generazione casuale)

**Luogo principale proposto:** fabbrica/officina industriale abbandonata con cortile centrale, deposito e tetto. Il pack gratuito Factory Environment Collection offre una prima libreria tematica; la mappa definitiva si costruisce appositamente, non si consegna il demo level tale e quale.

```
Cortile/Nucleo ─ Officina (linea di fuoco ampia, nuove piazzole)
       │
    Deposito (materiali/upgrade, varco aggiuntivo)
       │
    Tetto (linee di mira, salita rischiosa)
```

L'immagine testuale è una **bozza concettuale** di adiacenza, non topografia verificata. Ogni settore ha `SectorID`, costo, porte/connessioni, set di spawn attivabili, socket torrette, ricompensa e nuovi rischi. Prima di aprire mostrare chiaramente che aumentano i varchi. Apertura server-autoritativa, aggiornamento navigazione e minimappa/HUD. Le zone devono rimanere leggibili con silhouette e luci diverse; nessun labirinto indifferenziato.

**Sequenza V1 indicativa:** prima ondate 1–2 nel cortile; dopo 3 possibilità di officina; dopo 6 deposito; tetto opzionale come rischio/ricompensa dopo 8. Non costringere tutti ad aprire immediatamente: il director legge lo stato della mappa e scala entrate solo dove la geometria è attiva.

## 10. Economia, spese e decisioni

Due sole risorse iniziali:

- **Crediti personali:** colpi/kill/contributo, bonus difesa del Nucleo; usati per armi, munizioni e upgrade personali. Evitare che chi 'ruba' l'ultimo colpo monopolizzi l'economia: quota per danno + quota per kill/team.
- **Fondi difesa condivisi:** derivano dagli esiti ondata/obiettivi, spesi in torrette, barricata, riparazione Nucleo e apertura settori. Il team decide insieme; niente possibilità per un troll di bruciare tutto: conferma/voto per investimenti sopra soglia, lock di acquisto server e log delle spese.

La scelta tra torretta e upgrade arma esiste indirettamente tramite contributo personale → team: il giocatore può donare crediti ai fondi difesa a rapporto fisso, ma non ritirare fondi pubblici per sé. Il rapporto si decide in test. In solo i costi devono adattarsi e le scelte devono rimanere vive.

**Invarianti:** saldo mai negativo; ogni azione un transaction ID e risposta univoca; refund se fallisce lo spawn; costo e ricompensa in Data Assets/Data Tables; UI mostra confronto attuale/prima e delta upgrade; niente drop a casualità estrema obbligatoria.

## 11. Difficoltà e ritmo

- Wave 1: imparare tiro e riparazione senza pressione elevata.
- W2–3: corridori e scelta fra upgrade arma/barricata.
- W4–6: sabotaggio strutture e primo ampliamento interessante.
- W7–9: due fronti, coordinamento, elite.
- W10: boss/fase combinata con difesa centrale.

Un esempio di budget di spawn è in `09_BALANCE_SEED.csv`. Serve a un playtest misurabile, **non** è un algoritmo bilanciato. Preferire 10 ondate curate e leggibili a endless monotono. Il post-wave propone 20–30 secondi **massimi** di pianificazione oppure avvio anticipato consensuale; il gioco non deve sembrare una schermata di attesa.

## 12. HUD e interfaccia

Sempre visibili in FPS: munizioni, vita, abilità+cooldown, Nucleo HP, numero/ondata, pressione da lato (indicatori sonori e minimappa opzionale), fondi difesa e crediti. Vicino a socket: interazione `[E] Costruisci` con preview blu/rossa, range, costo, tier, stato alimentazione e tempo di cooldown; *non* aprire un complesso menu di shop.

Tra ondate pannello a 3 schede massimo: **Armi / Difese / Settori**. Nel multigiocatore identificare sempre chi ha comprato cosa e separare saldo personale da fondi squadra.

## 13. Audio, accessibilità, feedback

- Testare un colpo di pistola, fucile e shotgun con tail, low end e colpo sulla carne; non usare lo stesso sample pitchato per ogni arma senza ascolto.
- Zombie leggibili per categoria anche dall'audio: passo trascinato, corsa, armatura, indicatore sabotaggio.
- Colorblind: il rosso non è unico stato; forme/testi e audio comunicano pericolo e build invalid.
- Motion: camera shake scalabile, FOV slider, sensibilità, invert Y, rimappatura tasti e sottotitoli per callout narrativi.
- Gore: V1 stilizzato/realistico contenuto, niente asset mutilazione obbligatori prima che animazioni/impatti funzionino.

## 14. Monetizzazione e contenuti esclusi

Obiettivo consigliato: demo gratuita o piccola versione premium completa, **niente P2W**, battle pass o server persistenti. Escludere dal vertical slice: open world, generazione procedurale della mappa, skill tree enorme, crafting/survival, 10 mappe, 30 armi, veicoli guidabili, live service, matchmaking globale.

## 15. Criterio di divertimento, non negoziabile

Un tester deve riuscire a descrivere almeno tre decisioni diverse prese nella stessa partita: `ho speso su arma`, `ho investito in difese`, `ho rischiato l'espansione`. Deve anche indicare un momento in cui la sua mira/movimento ha cambiato l'esito rispetto alle difese automatiche. Altrimenti il mix non funziona.

