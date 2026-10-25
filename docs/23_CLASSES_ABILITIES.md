# CLASSI, ABILITÀ, PASSIVE, EQUIP E REVIVE — COMPLETO

## Regole

3 classi 1.0, scelte in lobby prima dell'avvio (no cambio nel mezzo), possibili duplicati, tutte utilizzano le 4 armi: nessun class lock che costringe a giocare col loadout odiato. Ogni classe ha **una passiva + una attiva** nella 1.0, non 15 skill incompiute. Per la prima iterazione uno script `ClassDefinition` data-driven con `PassiveModifiers`, `AbilityId`, `Cooldown`, `Duration`, `AudioFx`, `VisualFx`, `AnimMontage`, `Icon`, `NetRules`. GAS solo se già davvero adottato dal framework; non inventare due ability systems.

## Ruoli e valori-seed (NON convalidati)

| Classe | Passiva | Attiva, input e risultato | CD seed | Compensazione |
| --- | --- | --- | ---: | --- |
| C_ASSAULT | -10% rinculo AR/SMG; più rapido switch | **Sfondamento**: per 6s -25% spread +15% perforazione contro corazzati, VFX attivo, audio inizio/fine | 45s | zero bonus riparazione |
| C_ENGINEER | riparazione +20% su strutture, stesso costo fondi | **Ripristino**: sceglie torre/barricata/Nucleo entro raggio, ripara massimo 15% HP o riattiva torre disabilitata; se target valido è sentry dà +15% cadenza per 4s senza stacking; niente exploit oltre max | 55s | meno utility in inseguimento |
| C_MEDIC | revive del compagno più rapido (-25%) | **Impulso medico**: cura entro raggio 8m fino a 25HP 1 volta e mette in pausa bleedout di alleati Downed per 4s (non li rianima subito), animation e telegraph riconoscibili, no heal sopra max | 50s | nessun boost armi/torri |

All'attivazione: client richiede, server valida Alive, cooldown, range, target, potenza/condizioni, esegue una sola volta e replica stato; UI indica durata e cooldown. Player Downed non può usare skill. Nessuna skill può stunnare tutta la horde o annullare tutte le mosse boss. Stessi parametri per 1/4 player con scaling non automatico, guardando efficacia.

## Sistemi condivisi non legati alla classe

Tutti possono riparare a prezzo standard, comprare strutture, rianimare compagno, usare tutte le armi e fare upgrade. L'ingegnere fa la stessa azione meglio, non l'unico che la possiede. Il medico riduce i tempi e cura gruppo, non è requisito. Assaltatore è superiore nel diretto gunplay ma non ha danno spropositato.

## Animazioni ed effetti per classe

- Assaltatore: gesture arma/sovraccarico coerente in 1p e 3p, suono attivazione/scadenza, HUD icon e carica, emissive sulla arma **senza coprire la mira**.
- Ingegnere: animazione di interazione/corto impulso verso torre; effetti di ripristino/power reconnect sui dispositivi, suoni circuiti/repair, indicator target selection; interrompibile secondo regole esplicite.
- Soccorritore: gesto dispenser/impulso, healing wave a distanza ridotta e SFX udibile agli alleati, notifica cura; un effetto visto anche in 3p.
- Ogni abilità: idle, activate, active, end, denied/out of range, unavailable/cooldown, interruption on down/death, multiplayer replication, no doppio FX.

**Regola universale condivisa:** oltre Q il player possiede V **Spinta d'emergenza** e middle click **Marcatore tattico**; non sono nuove abilità di classe, né sono legate a una progressione. Dettagli anim/anti-stunlock/targeting e input in [40](40_SYNERGIES_SKILLS_AND_CITY.md). Non aggiungere altre attive, ultimate o talent tree per 1.0.

## Interazione e controllo

Un tasto abilità (default Q, modificabile), hud icon con cooldown, area/target preview quando serve, conferma o rifiuto ragione. Non aprire menu equip durante il combattimento. L'Ingegnere se non ha target valido non consuma cooldown; il Soccorritore se tutti pieni mostra “nessuno da curare” e non spende uso; attivazioni ripetute durante ping elevato server idempotenti.

## Progressione classi

Nessuna progressione permanente 1.0. Upgrade class-specific fuori partita esclusi; niente XP grinding. Gli upgrade rilevanti durante run sono di armi/strutture/base, non 10 skill tree. Dopo 1.0 possibile aggiungere variante di attiva, ma non prima di stabilità e playtest.

## Bilanciamento/test

Sessioni solo per ognuna, 2p med+assault, 2p engineer+assault, 4p solo assault e 4p variato. Ogni squadra deve essere teoricamente in grado di vincere a Normale; misurare una differenza utile ma non enorme tra uso corretto di abilità e senza; test cooldown exploit, desync HP, cast interrotto, UI per compagni, revive/repair simultanei, networking. Definition of done una classe è **un playable avatar con attiva vera, animazione e VFX/SFX**, non una statistica cambiata dietro le quinte.
