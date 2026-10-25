# DEFINITION OF DONE V2 — PROVE CHE IL GIOCO È QUELLO GIUSTO

**Non basta che compili** e non basta il piano: ogni task finisce solo con asset reale, anim 1p/3p, SFX/VFX, AI/network/save appropriati, build Editor e packaged, prova video/log.

## Test che impediscono di sbagliare concept

1. **Dentro = upgrade**: si entra realmente nel locale base, si usano Armeria/Comando/Difese/Specializzazioni, no nemici spawn nell'hub e nessuna fase di difesa imposta al player.
2. **Fuori = FPS + melee**: player esce fisicamente, spara AR e impugna machete vero, block/parry/counter, uccide Nurse. Movimento e impatto soddisfacenti (non un melee swing che attraversa mesh).
3. **AUTO-DEFENSE VERA**: player resta a più di due zone di distanza/KO/in hub per 120s, torre rapida abbatte in completa autonomia zombie siege W3 con upgrade congrui; rewards/tower shots/hit reaction reali registrati server, non script di HP.
4. **ESCALATION ONESTA**: se non aggiorni base da W3, a W7 corazzati/sabotatori possono superarla; con heavy turret e upgrade risulta nuovamente affidabile. Nessun “DPS cap scriptato”, torri non obbligate a perdere per design.
5. **TORNARE DURANTE WAVE**: il giocatore rientra e migliora torretta durante attacco e la vede migliorare fisicamente, senza arresto zombie e senza spesa doppia.
6. **PERSISTENZA**: salva base e wallet fra sessioni host; gioco chiuso non produce Rottami né consuma HP; restart da crash non duplica risorse.
7. **CONTINUO**: stesso director serve loop di spawn a pressione costante con escalation staged, senza interrompere AI base e senza plugin nuovo.
8. **CLASSI**: Tiratore, Spezzatore con opzione melee-only, Tecnico, ciascuno con 1 Q e passiva; classi non obbligatorie per sopravvivere W10.
9. **TERRITORI**: 3 zone fuori senza shop/bonus “settore città” o gestione NPC; incarichi combat brevi, Rottami direct gain.
10. **NETWORK**: un client fuori combat, uno dentro terminale, altri in zona diversa, torri server still firing; no ghost damage/saldo.

## Completezza tecnica per oggetto
Player real rig/skin+IK+animation+footstep; 4 firearm complete; 3 melee complete; 5 enemy anim/damage; barriere, rapida/heavy turrets e Core tiers; 4 terminali hub; 3 combat zones; wave/continuous and save; Rottami ledger; UI/options/audio; 1–4 listen host. Media matrix `38_RELEASE_CONTENT_MATRIX.csv` obbligatoria.

## Performance/legale
1080p medium 60fps come TARGET non validato su GPU non highend; server 20/40/60 zombies e 2 torrette mentre client lontano. Fab/Marketplace EULA e source redistribution controllate, no commercial raw assets in public GitHub. Shipping Windows avviabile senza UE editor e testata su PC pulito. Non dichiarare 1.0 done senza test 1p e 2p/4p effettivi e salvataggio solido.

## Report
`task_id | commit | asset source+license | anim clips reali | gameplay video | build log | autonomous defense test result if relevant | network state | save state | bugs | status`. Se manca prova pertinente, task `IN_PROGRESS` o `BLOCKED`, non DONE.
