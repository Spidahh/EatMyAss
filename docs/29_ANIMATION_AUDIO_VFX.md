# MATRICE ARTE/ANIM/AUDIO/VFX V2 — OGNI ELEMENTO FINITO NEL SUO STRATO

### Player Survival
Modello reale, FPS arms coerenti 3P remote; walk8, idle, sprint, strafe, crouch, jump/land, turn, reaction, Downed/respawn, porta ingresso base e terminal interaction. Foley passi metal/concrete/gravel, cloth, landing; HUD damage direction. Senza T-pose.

### Firearms: AR/Pistola/SMG/Shotgun
Ogni mesh rig deve essere reale, ads/hip/fire/recoil/reload empty/tactical/equip/sprint/aim offsets, owner + remote, muzzle/shell/smoke/impact flesh/armor/metal/concrete, near/far SFX e no doble sound in coop. Danno, ammo ed equip dal server.

### Melee: Machete/Mazza/Asta
Ogni arma: equip/unequip, idle/move, true 1p+3p light chain 2–3 step, windup/active/recovery, hit/miss, block start/hold/end, perfect parry/counter (arma-dependent), heavy charge quando previsto, impact/armor break flesh reactions, distinct real SFX whoosh/hit/clank, blood FX non esagerato, stamina e HUD feedback, remote montage and server trace. 1 weapon FINITO prima della seconda.

### Zombie: 5 archetipi
Ogni nemico con mesh e animation realmente acquisita/creata, locomotion della velocità, detect, Siege vs Field targeting, readable windup/attack/recovery, hit reactions ranged+melee, parry stumble with cooldown, ragdoll/death/cleanup, growl/footstep/swing/death SFX, VFX sangue/armatura. Walker Nurse ha solo 3 clip dichiarate nel pack: retarget/create per gli stati mancanti, non trattarli come già presenti. Saboteur attacco a torre con anim vera. Bruto attaccabile anche melee e torri.

### Base e torrette
**Interno**: porta, 4 terminali con animazioni reali di hardware UI, light ambience e menu SFX; niente dummy cubes. **Perimetro**: barriera deploy/hit/break/tier mesh e suoni, torre rapida con yaw/pitch/acquire/fire/reload/heat/destroy, heavy turret con movimentazione lenta e colpo pesante, Core tier0–3 luminosità/sparks/critical; **auto pulse** con VFX e sirena quando HP<35% seed e una volta/stage. Nessuna azione manuale obbligatoria per difesa.

### Territorio esterno
3 aree di combat: ambience specifico, cover e visibilità, terminal/supply event radio call, salvaging reward UI minimale, allarme base con audio spaziale coerente. Eventi solo combat senza NPC/dialoghi lunghi.

### Completeness gate
Per ciascun tipo: `Mesh + Skeleton/LOD + AnimationSet (real) + SFX + VFX + UI + AI/damage + Replication + Test video + License + Build`. Qualunque colonna mancante => IN PROGRESS/BLOCKED. Registrare status in `38_RELEASE_CONTENT_MATRIX.csv` e prove task. Non aggiungere effetto “provvisorio” mai sostituito. Video actual gameplay, mai concept art dichiarata gameplay.
