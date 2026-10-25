# UI / UX / INPUT / ACCESSIBILITÀ DEL GIOCO COMPLETO

## Filosofia

HUD discreto, adulto, leggibile in una città industriale con luci e zombie. Si mira e si combatte, i menu non devono diventare il gioco. Ogni elemento in UI mostra il dato autoritativo del server. Nessuna schermata inventa un bottone per feature non implementata. Ottimizzare per mouse+tastiera PC; controller gamepad è un requisito **eventuale post-v1** se i test/supporto lo consentono, non promettere 1.0 gratis.

## Frontend completo 1.0

`Main Menu`: Gioca Solo, Ospita Co-op, Entra (se trasporto disponibile), Opzioni, Crediti, Esci.  
`Lobby`: numero player 1–4, connessione/ready, classe con attiva/passiva e icona, equip iniziale disponibile, kick/leave host se framework lo supporta, start bloccato finché condizioni valide.  
`Loading`: progress no fake %, advice una riga, fallimento asset/version leggibile.  
`Pause`: resume (se solo e motore lo consente pause), settings, leave run con conferma e conseguenza per gli altri.  
`Results`: vittoria/sconfitta, dettagli progress reali, restart/new lobby.

## HUD in combattimento

- Crosshair/ADS/hitmarker (critical/headshot diverso), ammo mag/riserva, stance sprint/crouch icon, HP player e downed indicator.
- **Nucleo HP** sempre leggibile e tier/energia sintetici; wave `x/10`, alive enemies e remaining spawn, phase timer solo quando prep.
- Classe icon+cooldown progress, teammate HP/down state/distanza, minimappa di fronti opzionale; marker di pericolo ai cancelli e struttura sabotata.
- Crediti personali e team funds chiaramente distinti; non mostrare su tutti i client il credito privato degli altri salvo scoreboard aggregato.
- In interazione: [E] contesto, costo e trasformazione visuale; fuori range/non comprabile reason code (“Fondì insufficienti”, “piazzola occupata”, “solo fra ondate”, “serve Nucleo T2”). Non consumare input senza spiegazione.

## Interfacce d'acquisto

Un punto shop AR/PI/SG/SM: arma posseduta, miglioramento attuale, delta (es. Danno 26→29; stabilità...), prezzo, equip status. Acquisto con conferma breve e risposta autorevole. Su sockets mostra preview di range e arc sui muri reali, non pulsanti tutti uguali; upgrade torretta evidenzia cambio materiale/gun model e statistica. Sui cancelli area: costo, nuovo vantaggio e soprattutto **nuovo varco attivo dalla prossima wave**. In multiplayer mostra voto investimenti grandi.

## Input PC default (rimappabile)

| Input | Azione | Stanza blocco |
| --- | --- | --- |
| WASD | locomozione | Alive, no menu |
| mouse | look | Alive |
| LMB | fire | arma pronta |
| RMB | hold ADS | arma pronta, no sprint |
| R | reload | ammo reserve>0, no death |
| Shift | sprint | Alive, sprint consentito |
| Ctrl | crouch | Alive |
| Space | jump | Alive grounded |
| E | interagisci/repair/build/**Impulso Nucleo su pannello T2** | target valido; una volta per wave, non un tasto skill separato |
| Q | abilità classe | cooldown pronto |
| V | Spinta d'emergenza | Alive, cooldown 12s, bersaglio validato |
| Tasto centrale mouse | Marca bersaglio | target vivo in vista, cooldown 8s; una marcatura squadra |
| 1–2 / scroll | cambio arma | arma posseduta |
| Esc | pause/options/leave | sempre (non conferma pericolosa) |
| Tab | scoreboard/wave stats | in run |

EnhancedInput se integrabile con HordeTemplate reale, altrimenti non unire due binding per stessa azione. Salvare inversion Y/sens/FOV; riferimenti per mancini. Modalità 16:9/21:9, UI scale. Non disabilitare completamente il mouse look quando una UI overlay non modal è aperta.

## Audio/Video/Accessibility settings

Sens/ADS multiplier, FOV 80–110 (seed range), motion blur on/off, camera shake 0–100%, subtitles callouts con fonte, indicazioni direzionali audio/visuali, modifica colore hitmarker/contrast senza usare rosso come solo feedback, riduzione flash, interfaccia più grande, rebind tasti, scelta output display, quality low/medium/high, resolution scale, cap FPS, audio master/music/SFX/voice. Pausa single player solo con server local e stato coerente; in co-op pause è solo overlay e world continua.

**Nuovi indicatori 1.1:** due icone locali piccole Q e V; mark bersaglio sulla testa dello zombie e per la squadra solo 5s; stato “Impulso Core DISPONIBILE/USATO” **uno per tutto il team** accanto a Core HP, non una skill bar terza; settore preview `utilità + rischio nuovo varco + costo`; E durante W7 riattiva torre disabilitata. Non aggiungere meter o tasti ulteriori. Per regole: [40](40_SYNERGIES_SKILLS_AND_CITY.md).

## Onboarding non tutorial prolisso

Prima wave: freccia/marker Nucleo, indicatori zombie e arma; dopo wave1 highlight bancale upgrade vs difese; dopo wave3 unlock gate. Tutto contestuale e disattivabile, nessun menu di spiegazioni che blocca la sessione. Tre test condotti senza aiuti vocali dell'autore; deve capire movimento, obiettivo, acquisto, morte.

## Prove finali

1080p/1440p/ultrawide; scala 80/100/125; controller non richiesto; tutti i soldi/voti replicati; alto ping, loading failure, no host, downed, error. Nessuna label mancante, linguaggio coerente in italiano (testo in data localization ready), nessun text clipping, nessuna schermata placeholder finale.
