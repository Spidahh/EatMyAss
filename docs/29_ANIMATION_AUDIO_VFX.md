# MATRICE GLOBALE ASSET / ANIMAZIONI / AUDIO / VFX — PER TUTTO IL GIOCO

**Scopo:** Codex non può più “dimenticare le animazioni” o considerare conclusa una meccanica quando funziona solo come calcolo numerico. Per ogni tipo è obbligatorio un `ContentCompletionRecord` con mesh e license, state anim, transizioni/IK, SFX, VFX, shader/material response, UI, collision, perf, network e video. Sorgenti ufficiali in [30](30_ASSET_PRODUCTION.md). Le voci sono requisiti, **non claim che i pack le includano**.

## A. Umano player — stato obbligatorio L1

- Mesh/clothing finali e viewmodel arms coerenti, corpo 3P shadow; nessun mannequin.
- Idle armato, walk 8 direzioni (blend di sorgenti genuine), run, sprint, start/stop, turn in place, crouch idle/walk, jump takeoff/air/land, aim pitch/yaw offsets, animazioni d'interazione, damage hit, death/downed/revive. Foot IK dove utile.
- Audio footsteps concrete/metal/gravel, cloth/gear, salto e atterraggio, hurt, low-HP feedback, death/revive.
- FX camera movement appropriati, damage directional hit UI, weapon stance.
- Networking all 3P; first-person owner non vede duplicato.

## B. Quattro armi — un record per ogni arma L2/L11

Ogni W_PI/W_AR/W_SG/W_SM: idle hold, hip fire, ADS enter/hold/exit, fire ADS, recoil/recovery, equip/unequip, tactical reload, empty reload (bolt/pump/slide corretto), sprint hold+exit, jump/land armed, dry fire, impact/interruption states; hands IK e mag/shell animati **in sync con reale arma**. Shot fire near/medium/far (attenuation), handling, trigger, eject shell, mag out/in, bullet/shot flesh, plate, metal, concrete, ambient tail. VFX muzzle flash, smoke, trace se applicabile, shell casing, muzzle lighting contenuto, impact puffs/decal, blood/headshot, ammo/hitmarker/crosshair UI. Remote replication del fire montage, no double sound.

## C. Zombie roster — un record per ciascun tipo L3/L11

| Enemy | Movement/detect | Attack | Reazione | Morte | Audio/VFX speciali |
| --- | --- | --- | --- | --- | --- |
| Walker | idle variant, shuffle, turn, detect | grab/swing telegraphed + recovery | light/heavy + head | hit collapse + ragdoll controllata | groan, foot drag, blood |
| Runner | idle jitter, sprint+turn+accelerate | leap/swing, miss recovery | stumble breve | crash fall veloce | scream detect, rapid steps |
| Armored | ponderous walk, turn, rage | overhead smash, recovery | armored bullet spark + exposed weakpoint | fall pesante | plate clank/break, low growl |
| Saboteur | stalk, target power, locomotion | disarm animation + melee | hit recoil | collapse e sparks residui | electric hiss, lock warning |
| Boss | intro + walk/charge, 2 stage, phase change | 2 attacchi distinti con anticipation/recovery | stagger limitato e weakpoint reveal | finisher death unico | telegraph siren/rumble distinto; no blinding VFX |

Per Nurse il pack scelto include solo Idle/Walk/Attack. Le clip non presenti vanno **prodotte o acquisite legittimamente** prima di chiamare la Nurse finita. Boss non è “Nurse scalata 5x”.

## D. Strutture e ambiente

| Oggetto | Animazione visiva | Soundscape | VFX/feedback | Stati HUD |
| --- | --- | --- | --- | --- |
| Nucleo | tier upgrade, damage stages, power active, collapse | hum loop, hit/critical alarm, powerout | lights/damage sparks/smoke per HP; no eccessi | HP/power/critical |
| Barricata | placement/repair, hit, splinter/metal bend, break | build, hammer/metal, zombie bash | debris bounded, damage material | HP/tier/cost |
| Sentry | placement raise, scan yaw/pitch, target acquire/fire/overheat, break | servo, lock cue, muzzle, out of ammo/power | muzzle/fire hit/smoke/damage | ammo/heat, power/target |
| Campo slow | spawn, pulse, expire, damage/destroy | low freq pulse, shutdown | area zone chiara, deform/electro mist controllati | radius/duration |
| Cancello settore | lock→power→opening, blocked/destroyed if design | mechanical latch, power, alarm | status light, open smoke minimal | cost/new varchi |
| Armeria/banco | UI open/close, highlight upgrade | click/upgrade confirmation | selected silhouette + actual weapon tier | prezzo/delta |

## E. Città

Ambience strada industriale, vento, neon, distant groans, sirene, pannelli elettrici; differenziare interno/officina da aperto/strade; 2–3 sound zones spazializzate reali, non musica continua su ogni wave. Adaptive tension layer al passaggio wave: niente audio che maschera corridori o boss. Materials concrete/steel/glass e decals coerenti.

## F. Requisiti comuni per tutti

- Original asset immutable/private, wrapper e instances, retarget source/version + mapping salvati nel manifest.
- Animation Sequence vera, clip/event name identificati; graph non può fare finta di mostrare un attack non animato.
- All actors combat: audio cues con attenuazione/concurrency/volume; niente multicast ridondante.
- Niagara/particles controllati: emitter spawn cap, durata FX e decal limitata; non saturare performance crowd.
- Real-time lighting/material blend, LOD, cloth, armature, FOV; niente asset 8K ovunque per sentirsi “belli”.
- Video/screenshot dell'intero ciclo; QA per 1p e 2p, 20 zombie dove applicabile. Missing any required row => strato IN PROGRESS.
