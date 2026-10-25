# MULTIPLAYER CO-OP 1–4, RETE, LOBBY, DISCONNESSIONI, SALVATAGGI

## Target verificabile della versione 1.0

PC Windows, **offline solo** e **listen-server co-op fino a 4** tramite LAN/soluzione amici ufficialmente supportata dall'integrazione del progetto dopo verifica. Non promettere online pubblico mondiale, matchmaking, server cloud, migrazione host, progressione account o anti-cheat professionale; niente abbonamenti. Il codice multiplayer esiste in HordeTemplate come classi e replica, ma non è stato ancora eseguito dal nostro progetto: implementare e rifinire quando lo strato corrente ha vera logica da sincronizzare.

## Autorità e ownership

| Dato | Server authoring | Replicare a | Regola |
| --- | --- | --- | --- |
| stato della run/tempo/ondata/vittoria | GameMode + director → GameState | tutti | client HUD read-only |
| zombie posizione/stato/HP/morte | Character + AIController server | client rilevanti | no client-determined kills |
| colpi player | server validate cadence/direction/ammo | owner + hit FX agli altri | client può predire solo elementi cosmetici |
| crediti personali | PlayerState server | owner, alcuni scoreboard | no client AddPoints arbitrario |
| fondi squadra | GameState server | tutti | ledger idempotente |
| strati difensivi/core/socket | server actors + manager | tutti rilevanti | no spawn torrette client |
| classe attiva/skill cooldown | PlayerState + ability component | owner/all necessari | no double cast |
| porte/settori aperti | SectorManager server | tutti | late join ricostruisce stato reale |

## Lobby e session flow

Host: New Game → solo / Host LAN co-op → lobby → 1–4 player joined → class/loadout choices ready → start. Join: select available host session supportata via OnlineSubsystemNull o soluzione prevista già dal framework → loading/version check → lobby. Una volta iniziata run **late join non supportato alla 1.0** (se desiderato più avanti sarà una feature distinta con sync snapshot completo), UI deve comunicarlo; niente player fantasma.

Slot team ≤4, reconnect durante run **non garantita**: se client disconnecta, server lo segna disconnected e rilascia lock di ready/vote, il personaggio può essere rimosso o diventare spectator secondo regola documentata; fondi team non vanno raddoppiati; non rimborsare crediti da player assente senza policy. **Host quit**: tutti ricevono schermata host-disconnected, sessione chiusa senza crash né corruzione; migrazione host esclusa 1.0. L'utente deve sapere che partita co-op è host-based.

## Sync qualità

- Camera/FPS owner fluida; remote vede weapon, muzzle, reload, sprint, down/revive, ability e zombie death con montages coerenti.
- Simula 80ms RTT e 2% packet loss durante build QA, attenzione doppio fuoco/acquisto/reward. Solo server può fare danno, ma local feedback deve sembrare immediato. Non fare multicast per ogni traccia audio globalmente.
- Server launch game con net role e inventory reale; no cast a Pawn/PlayerState senza null guard; cross-level travel e restart senza riferimenti zombie orfani.
- Pooled impact FX solo se non compromette visibilità del colpo, replication event budget misurato.

## Salvataggi persistenti 1.0

**Salvare soltanto:** video/audio/input/accessibilità, preferenze FOV/sens, preferenze classe/loadout (se ancora valido), local personal stats aggregate, opzione privacy/telemetry local. `SaveGame` versioned schema e fallback safe se versione cambia. **NON** salvare economy, wave, torri, HP Nucleo in corso per co-op 1.0: una run finisce e viene resettata. Da solo la sessione può ricominciare da wave1; menù deve comunicare regola prima di avvio. Salvataggio a checkpoint solo dopo V1 e dopo dimostrazione co-op serializer robusto.

## Sicurezza minima

Validate RPC per player ownership e rango; rate limiting request, bounds per costi/element IDs e amount; rejection con codice; TxnId dedupe; non accettare `Health=100000` da client; non dare fiducia a cooldown o collision client. Nessun dato personale in log/telemetria senza motivo. Nessun accesso amministrativo o command cheat esposto in Shipping.

## QA accettazione

2p e 4p, host e client casual, join lobby, class select, ready, start/return, almeno 10 ondate in 2p, single local offline, morte e revive, potenza Core, acquisto socket, aprire settore, riavvio nuova run. Tutti i client vedono identico saldo/server wave/core e nessuna duplicazione. Test host disconnect, packet loss, client crash, UI ricostruzione dopo travel, Windows packaged. Rapporto LAN vs internet REALMENTE verificato; se manca connectivity online non chiamarla multiplayer internet.
