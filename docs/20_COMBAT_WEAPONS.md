# COMBAT V2 — 4 ARMI RANGED + 3 ARMI MELEE

**La melee NON è più una spinta accessoria.** Gameplay completo in prima persona, con animazioni visibili per 2p e IA che reagisce ai veri impatti, parry e colpi caricati; restano il gunplay e gli headshot. Spec melee definitiva [42](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md).

### Ranged

- **AR** medio raggio, da bundle reale [Deadghost](https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5).
- **Pistola** secondaria economica e switch rapido.
- **SMG** mobilità/crowd da vicino, piccolo danno per colpo.
- **Shotgun** vicino, pellet per target/arco reali, scambio arma strategico.

Ciascuna arma: mesh, grip/IK, equip, hip, ADS, fire, reload partial/empty, sprint, recoil, ammo server, muzzle+eject, shell, sparks/flesh+concrete impacts, sound distance, hitmarker, tier in armeria e rete. Tutti gli asset devono essere reali e licenziati; no file inventati. Danno, spread, magazine e prezzi sono `DataAssets` seed fino a misure.

### Melee

- **Machete** per primo, tagli rapidi + mini combo max3.
- **Mazza pesante** per secondo, colpo lento/caricato anti-armor.
- **Asta industriale/lancia corta** per terzo, maggiore portata e affondo controllato.

Ogni arma melee include 1p/3p montages attacco e parata, perfect parry limitato, hit sweep su blade head dal server, 1 hit/target/swing, corpo zombie che reagisce, metal/flesh/whoosh suoni, camera feedback, miss/recovery, upgrade in base. Guard stamina condivisa con sprint (unica risorsa stamina). Non rendere il boss irraggiungibile in melee.

### Input
WASD/mouse, LMB fire/swing, RMB ADS/block, Shift sprint, Ctrl crouch, R reload, Space jump, 1/2/3 equip (numero slot da schema finale), Q attiva specializzazione. Parry = primi 0,20s del block, counter LMB per risposta; tutto mappabile. Niente V shove obbligatorio: V1.1 ritirata. Scelte/upgrade SOLO in Armeria interna.

### Ownership/QA
Server decide danno e death dei zombie indipendentemente da player o torretta, tasti validati, remote animation, NO animazione finta. Prove: melee contro Nurse, later armored e Bruto, due client, ragdoll e decal; arma/firearm no double shot, no ghost reload. Il fucile non monopolizza il combattimento.
