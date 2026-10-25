> **AVVISO DI PRECEDENZA (25/10/2026):** per la produzione attuale leggere prima [AGENTS.md](../AGENTS.md), [12_PRODUCTION_ORDER.md](12_PRODUCTION_ORDER.md) e [17_CODEX_EXECUTION.md](17_CODEX_EXECUTION.md). Le fasi, le scelte di base tecnica e gli asset descritti qui sotto sono **materiale storico di progettazione** e non autorizzano Codex a iniziare più sistemi contemporaneamente. HordeTemplate è la baseline designata e la prima consegna è personaggio + un fucile + una zombie + primo isolato, completati in quell'ordine.

# Decision register / Risk register

Stato: `PROPOSED` fino al primo feedback e ai gate tecnici. Le scelte già esplicite dell'utente prevalgono sempre su queste assunzioni. Aggiornare con data, autore, motivazione ed eventuale rollback; non cambiare design per impulso durante un ticket di bugfix.

## ADR — proposte da confermare con prototipo

| ID | Decisione proposta | Perché | Stato / rollback |
| --- | --- | --- | --- |
| ADR-001 | FPS moderno in prima persona, PC Windows | core shooting stile wave zombie richiesto | PROPOSED; 3P non prioritaria |
| ADR-002 | Solo dal day 1, co-op 1–4 come target; server authority | evitano rifacimenti tardivi | PROPOSED; G0 ne decide il costo |
| ADR-003 | A: HordeTemplate; B: Lyra; C: First Person shooter per spike | alto riuso verso zero budget | PROPOSED; G0 GO/PATCH/NO-GO |
| ADR-004 | Factory industriale realistica ma leggibile | disponibilità free di pacchetto coerente | PROPOSED; art gate one-room |
| ADR-005 | Difese su socket fissi in V1 | navmesh/rete/AI controllabili | PROPOSED; libero solo post-V1 |
| ADR-006 | 2 valute: personale + fondi difesa condivisi | tradeoff senza gameplay gestionale | PROPOSED; playtest 3 sessioni |
| ADR-007 | Una base Nucleo e 3 zone espandibili, mappa non procedurale | scope finibile con una persona | PROPOSED; plot test nav |
| ADR-008 | Assaltatore, Ingegnere, Soccorritore | differenze tattiche leggibili | PROPOSED; 1 classe VS |
| ADR-009 | 10 waves finite + boss; no endless iniziale | esperienza curata prima di volume | PROPOSED; valutare dopo VS |
| ADR-010 | Zero store/microtransazioni e nessun sistema online persistente in VS | focus costi quasi zero | PROPOSED; rivalutare se pubblico online |
| ADR-011 | Niente gore costoso nel prototipo; hit feedback priorità | qualità prima di quantità | PROPOSED; rating + art gate |

## 2. Rischi che fanno fallire i giochi piccoli

| Gravità | Rischio | Segnale anticipato | Contromisura e stop condition |
| --- | --- | --- | --- |
| **CRITICA** | HordeTemplate non compila, non replica o dipende da asset ambigui | crash, plugin mancanti, asset/no license | G0 isolato; non investire asset/feature prima di GO; passa a Lyra |
| **CRITICA** | mix di pack esteticamente incoerente | zombie lowpoly vs armi realistiche | art bible e scena closeup; sostituire singola risorsa |
| **CRITICA** | build e AI/path sono exploitabili | route bloccate o zombie stuck | socket prefissati, varchi obbligati, nav tests per ogni settore |
| **CRITICA** | authority client, money/kill duplicati | request spam e due player in conflitto | transaction ID, server checks e test perdita pacchetti |
| ALTA | guns asset mesh ma senza anim/suoni corretti | reload/ADS clip e colpi flosci | gunplay gate precoce, una weapon perfetta prima di 10 |
| ALTA | scalabilità orde non regge | game thread e skeletal mesh saturi | limite attivi misurato, LOD/UpdateRate, spawn budgeting |
| ALTA | tetris di plugin complica upgrade | version incompatibili e classi duplicate | version pin, un framework, wrapper intorno ai pack |
| ALTA | torrette rendono gioco AFK | il giocatore non deve sparare | boss weakpoints, budget/heat/ammo, teste non copribili |
| ALTA | le difese diventano inutili | giocatori spendono sempre sulle armi | wave attaccano Nucleo, overload su più ingressi |
| ALTA | espansioni aumentano troppi zombie/porte | difficoltà salta ad ogni unlock | telegraph nuovo rischio, budget director e gradualità |
| MEDIA | shop fra onde rompe il ritmo | tester attende troppo | shop 3 tab, 20–30s max o skip consensuale |
| MEDIA | classi obbligatorie e solo impossibile | ingegnere sempre indispensabile | ripara/curarsi disponibile universalmente |
| MEDIA | asset free “UEFN only” | import non supportato | escluso dal registro production |
| MEDIA | costi nascosti di distribuzione | hosting/login/store music | demo locale first, spese separate e note prima release |
| MEDIA | progetto AI cresce senza prove | descrizioni “completato” senza build | AI contract DoD, test ID e regressioni |

## 3. Dipendenze decisionali

`Base scelta` abilita `Inventory + Gunplay + Coop + Zombie AI`; da lì partono in parallelo *solo a livello di pianificazione* `WaveDirector` e `Art scene`. `Economy` dipende da wave e player state. `DefenseManager` dipende da economy + mappa + replication. `SectorManager` dipende da nav + defenses + waves. `V1 classes` dipende dal combat bridge; il multiplayer deve precedere i sistemi complessi, non essere aggiunto a fine sviluppo.

## 4. Domande da fare al committente, ma non bloccano il dossier

1. **Co-op vera al lancio oppure dopo demo single-player?** Presumo co-op 1–4 nel piano. Se la risposta è 'solo single' i tempi scendono; se è 'online immediato', cresce il rischio.
2. **Tono visivo:** horror realistico industriale (scelto per ora) oppure stilizzato adulto/arcade? Cambia quali asset approvare.
3. **Struttura delle partite:** 10 ondate con finale oppure endless? Scelto finale e endless più tardi.
4. **Stile di movimento:** FPS tattico più lento o arcade agile? Scelgo intermedio moderno, da misurare con gunplay test.
5. **Danno/gore:** moderato o esplicito? Impatta rating, performance, asset e animazioni.
6. **Stile upgrade:** upgrade durante run con reset tra partite (scelto) o progressione permanente? Scelta attuale evita grind e P2W.

## 5. Policy di change control

Nuova idea → scrivere problema del giocatore → alternative → impatto su core loop → dipendenze → test → costo stimato → scelta. Se il beneficio non è provabile nel prossimo playtest e la feature pesa più di 2 sprint, parcheggiarla in Post-V1. Bug e nuove feature sono ticket separati; il progetto non deve rimbalzare di architettura tra messaggi di AI.

## 6. Cosa è **fatto oggi** e cosa **non è fatto**

Fatto: ricerca documentale con fonti primarie e link, architettura proposta, lista asset con categoria/prezzo di pagina, GDD, scope, rischi, test, prompt e cost seeds.

Non fatto: scaricare e acquistare asset, licenze associate ad account, verificare file locali, compilare UE, creare progetto, testare 2-player, provare la grafica/gunplay su GPU, misurare performance, validare livello/bilanciamento, pubblicare su store. Non chiamare mai 'completo' il gioco o il suo MVP fino ai gate.

