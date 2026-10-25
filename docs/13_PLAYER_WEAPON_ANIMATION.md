> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

> **CONFINE TRA L1 E L2 (25/10/2026):** questo documento elenca animazioni di **due strati**. L1 termina con **personaggio reale senza arma**, tutte le locomozioni non armate (idle, 8 direzioni, crouch, sprint, jump/land, camera, footsteps, modello remoto) e gestione stati; **non richiede fucile, ADS né reload**. Tutte le varianti armate, aim offset con arma, grip, firing, equip e reload appartengono a **L2** e sono obbligatorie per dichiarare completato L2. Non inventare un fucile temporaneo per “chiudere L1”. L1 e L2 insieme devono coprire tutte le voci della matrice sottostante.

# L1 + L2 — SPECIFICA DI PRODUZIONE: PLAYER FPS E UN FUCILE COMPLETO

**Contratto:** [Piano](12_PRODUCTION_ORDER.md) e [asset bloccati](15_ASSET_LOCK.md). Non si consegnano un modello che cammina male o un fucile che spara senza le mani allineate. Il player **è** il primo prodotto reale.

## A. Personaggio definitivo L1

**Asset:** Survival Character (Arberry, Fab ID 11d20d01-b764-4936-8163-cb20d05c369e). Scheda: parti corpo e abbigliamento modulari, Epic Skeleton UE 5.1 e texture fino a 8K. Il pacchetto NON documenta un set completo di animazioni FPS: non assumere di trovarlo al download.

**Impostazione della visuale:** corpo full mesh per shadow e altri giocatori, camera prima persona posizionata correttamente rispetto a testa/spalle; rappresentazione braccia/arma coerente con Survival, senza differenza tra mani di colore/abbigliamento della FPS e corpo terza persona. Se la mesh full-body clip nella camera, usa una vista arms-only derivata lecitamente dallo stesso rig/modello, con animazioni sincronizzate e shadow body separata. No mannequin visibile, no mani sospese, no muzzle che attraversa pareti.

**Animazioni richieste, nessuna esclusa senza prova di impossibilità:**

| Gruppo | Stati/clip | Prova visiva obbligatoria |
| --- | --- | --- |
| Idle | armed idle, respirazione controllata, upper-body aim | 30 secondi senza foot sliding, muzzle stabile |
| Locomozione | walk avanti, indietro, strafe L/R, diagonali, start/stop, turn in place, jog | girare a 360° e cambiare direzione senza pop |
| Sprint | ingresso, loop, uscita, stanchezza eventuale se codice presente | passaggio da corsa a ADS senza snap |
| Jump | anticipazione se presente, takeoff, airborne loop, landing | piedi sul pavimento e camera non strappa |
| Crouch | ingresso, idle, move, uscita | collisione camera/capsule corretta |
| Aim | hip → ADS → hip, upper-body offset verticale/orizzontale | ottica/front sight centrata senza drift |
| Equip | arma alzata, lower, swap animation singola | arma non attraversa mani/camera |
| Hit | lieve recoil del corpo e hit feedback UI locale | controllo non perso ogni colpo |
| Death | collapse/knockdown + disarmo/spectator se sistema lo prevede | nessuna T-pose o ragdoll incontrollabile |
| Interaction | gestualità breve dove effettivamente visibile | camera + mano coerenti sul punto usato |

Fonte consigliata per locomozione: **Epic Game Animation Sample** con IK Retargeter sul rig reale di Survival. Epic documenta la possibilità di migrare le animazioni nel proprio progetto e l'uso di Motion Matching; adottare soltanto i clip necessari, non importare un secondo framework gameplay. Fonte: https://dev.epicgames.com/documentation/unreal-engine/game-animation-sample-project-in-unreal-engine .

**Animation Blueprint:** locomotion full-body con blend corretto su velocità/direzione/stance, aim offset/additive layer separato per upper body, montages per equip/reload/hit, anim notifies per footstep e stati. Se Motion Matching import costa eccessivamente, usare animazioni genuine con blendspaces ben configurati (no interpolazione da idle per simulare tutte le azioni). Confrontare in runtime retarget poses, scale pelvis, wrist rotations, locomotion root, feet planting, interaction IK.

**Audio del movimento:** superficie per footstep (concrete/metal/gravel), eventi solo ai notifies, intensità walk/run e distanza; cloth/gear leggero, suono atterraggio; niente ripetizione artificiale dello stesso sample a volume alto. Ottimizzare per una zona urbana industriale.

**Input e qualità:** movimento avanti/indietro/strafe, mouse look, sprint, crouch, jump, interazione, arma. Mappatura unica documentata; preferire Enhanced Input solo se il bridge con i vecchi binding viene completato senza doppie azioni. FOV/sensibilità regolabili; no zoom FOV che distorce mano/ottica.

**Network:** rotazione/locomozione visible remote, remote firing/crouch/equip senza differenze sostanziali, niente anim notifies che assegnano danno su client. Camera FPS locale distinta da rappresentazione remota.

## B. Primo fucile reale L2

**Asset:** FPS Weapon Bundle (Deadghost Interactive, Fab ID 8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5). Da selezionare **un solo fucile d'assalto riggato reale disponibile nei file**, registrando nome/mesh/sockets reali dopo import; il titolo della scheda garantisce 7 armi riggate, NON il set di animazioni richiesto. Collegare alle classi upstream vere `ABaseFirearm`, `AHordeBaseCharacter`, `InventoryComponent`; mantenere server fire cadence e munizioni.

**Ciclo funzionale completo:** equip → idle armato → walk/sprint → ADS fluido → singolo/automatico soltanto se la mesh e la logica consentono → colpo valido e impatto → reload parziale e reload da vuoto → swap/lower → zero ammo/dry trigger → morte/interruzione. Non introdurre tre armi mentre questa è incompleta.

**Animazioni weapon + arms (obbligatorie):**

| Azione | Requisito |
| --- | --- |
| Hold/idle | mano forte + support hand aderenti a grip/foregrip |
| Equip/unequip | movimento continuo e sincronizzato con visibilità e input |
| Fire hip/ADS | arma con rinculo e ritorno smorzato, upper body remoto sincronizzato |
| Reload tactical | mag fuori, mano sul mag, mag dentro, camera stabile, ammo assegnata al notify corretto |
| Reload empty | gestione camera/chamber/release differenziata se meccanismo lo richiede |
| Sprint enter/loop/exit | gun lowered appropriato, non spara se bloccato da regola |
| ADS transition/hold | sights centrati, posizionamento dipendente dall'arma |
| Land, jump armed | transizione compatibile con visuali FPS e terza persona |
| Dry fire | suono stato arma vuota + gesto minimo |
| Fire interruption | nessun teleport dell'arma, stati coerenti |

Se il pack non contiene clip di reload, gli step vanno **realizzati** con strumenti Unreal (Control Rig, montages, keyframes/Sequencer) e/o animazioni gratuite con diritti acquisiti e retarget compatibile. Non scrivere in report “reload pronta” solo perché il contatore aggiorna i proiettili.

**Gunplay fisico / numeri configurabili:** ADS target per offset/rotazione del fucile; fire interval, magazine, reserve, reload time definito per la singola arma; camera recoil con componente leggermente variabile, recovery progressiva, spread hip vs ADS, spread movement, crosshair feedback, zoom, hit bone/physical material. Salva parametri in data asset coerente con framework; valori finali tarati nell'uso reale. Non riprodurre gunplay 1:1 di contenuti protetti.

**VFX/SFX e impatto obbligatori:** muzzle flash ancorato al muzzle reale; sound gunshot con ambiente vicino/lontano; shell casing coerente con eject socket; smoke controllato; traccia proiettile discreta se giustificata; flash superficie flesh/metal/concrete; particelle, decal con durata limitata; flesh hit sound distinto dal rumore dell'arma; impatto e headshot leggibili; feedback audio/visivo per ammo empty e reload; camera shake ridotto e regolabile. Il proiettile NON deve risultare invisibile o colpire in un punto diverso dalla mira senza regole chiare. Se si riusano projectile/Hitscan upstream, mantenerne il modello coerente.

**Visibilità remota:** terza persona vede arma attaccata bene, muzzle flash, giusto montage, no duplicato mesh sopra al corpo; il client owner non vede il flash sparare due volte. Niente suoni multicast moltiplicati per listener.

## C. Definition of Done L1/L2

- Player reale Survival importato con licenza e texture scalate per budget, no mannequin nel contenuto visibile.
- Spostamento, direzioni, rotazione, sprint, crouch, salto, atterraggio; ogni ciclo possiede transizioni corrette e suoni adeguati.
- Fucile reale full rig + animazioni idonee per equip, shoot, reload, ADS, sprint, walk, empty mag e switch.
- A 60/120fps e latenza normale, niente doppio sparo, click fantasma, ammo negativa, clip grossolani, tremolio mani; FPS e rete in play reale.
- Una build Windows apribile e video **minimo**: camera 1p 60s, visuale 3p 30s, controllo 2-player con tiro/reload; tutti i passaggi vanno mostrati.
- Bug/blocchi nel report con file reali e prove. Se manca il fucile reale o la reload, **L2 NON È FINITO**.

**Ordine operativo:** prima L1 completo e rifinito, poi L2 completo e rifinito, poi L3. Non riordinare per convenienza.
