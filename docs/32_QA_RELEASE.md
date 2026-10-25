# QA DI TUTTO IL GIOCO + CRITERI DI RELEASE

## Perché la qualità è parte di ogni strato

Nessuno desidera infiniti prototipi: ogni strato comprende **implementazione + animazioni + suono + VFX + UI + bugfix + test di regressione + build** prima del prossimo. QA non è una milestone di studio disgiunta; è condizione di dichiarare finita la feature definitiva. “Perfetto” significa nessun requisito noto mancante secondo checklist e difetti bloccanti zero, non l'impossibile assenza assoluta di bug.

## Definition of Done universale

1. Codice eseguibile integrato nell'effettivo progetto UE, file/versione identificati.
2. Asset approvati e realmente acquisiti, rig/animation complete per quella feature; nessuna risorsa fittizia/temporanea esposta.
3. Anim blending, VFX/audio/hit feedback/UX, error handling e cleanup completati.
4. Stato server-client coerente dove la funzione è replicata; RPC validates e no saldo/danno duplicato.
5. Dati configurabili (non 10 costi hardcoded), import/manifests/licenze aggiornati.
6. Build Editor e packaged Windows quando engine disponibile, comando/log e versione concreta; nessuna affermazione “compila” da sola analisi statica.
7. Test della feature/edge cases superati con evidenze reali video/screenshot/log, FPS campione; regressione player+weapon+zombie fatta a ogni milestone.
8. README/AGENTS e issue con stato reale; commit dal quale si torna indietro. Se manca anche 1–7 ⇒ IN PROGRESS o BLOCKED.

## Matrice per sistema finale

| Gruppo | Accettazione minima |
| --- | --- |
| Player | idle/walk/run/sprint/crouch/jump/land/strafe 360, skin reale, view 1p/3p corretta, footstep, HP/down |
| 4 armi | equip/ADS/hip/fire/reload/dry/impact/bullet/audio VFX/distances, ammo authoritative, tiers e 2p |
| 5 nemici | AI all targets, attack windows, animations, hit/death ragdoll, no stuck, surface and category audio, 20+ |
| 10 wave | queue finite, zero kill duplicated, W10 boss, reward and prep, separate 1p/4p, opened sector interactions |
| Nucleo | HP/power/damage/recovery/tier1-3 UI audio, loss once |
| 3 difese | asset realistico, aim/nav/damage, build/update/repair/destroy, power, 2 clients concurrent purchase |
| 3 classi | passiva/attiva, cooldown, montage/FX, range reject, single/coop and revive |
| 4 settori | entry/exit, collisions/nav/spawns sockets, new attacks readable, lighting/audio and not blocked |
| Economia | PC/TF grant/spend/donate ledger no negative, vote, refunds and audit logs |
| UI/Options | menus, HUD, interact prompts, feedback, localization, scaling and remap, accessibility |
| Sessioni | solo, listen server 2p/4p, host loss handling, no cheat RPC, no desync, package shipping |
| Legal | provenance 100% included assets, Fab/Epic restrictions and 3rd party notices, no raw public redistribution |

## QA sinergie v1.1 (oltre alla matrice preesistente)

- V spinta entro 1,6m colpisce max un Walker/Runner valido, non spinge Boss/Armored, non duplica munizioni durante reload; 2 client vedono montage.
- Q Assault penetra meglio corazza solo per 6s, niente moltiplicazione permanente; Q Engineer repair max 15% e sentry cadence +15% max 4s senza stacking; Q Medic HP cap, downed bleed paused 4s, non auto-revive.
- MMB mark dura 5s, una per team, sentry solo se LoS/range; due richieste ping ravvicinate non fanno spam/stack.
- E al pannello Nucleo disponibile dal T2, una sola attivazione per wave per TUTTI i player, niente consumo senza target; slow ring 12m, Boss non bloccato, T3 Range *oppure* Repair.
- S1 ammo discount 15% PC, S2 barricade repair discount 15% TF, S3 warning special 6s, niente benefici quando settore chiuso; UI mostra rischio nuovo fronte.
- W7 tower blackout max 8s con warning, riattiva E 3s o Engineer Q, no softlock 1p senza sentry o engineer.
- Nessuna terza valuta, menu talenti, stack moltiplicativi slow o nuova metaprogressione introdotti per errore.

## Test di maggiore rischio / non saltare

- Spawn zombie non in zona chiusa; nessun zombie stuck con porta/barricata e un player su tetto.
- Una torre uccide zombie senza `ACharacter` killer: death e wave count corretti, team reward appropriato.
- Due giocatori comprano stesso socket contemporaneamente: un addebito, una torre.
- Boss può essere sconfitto dagli umani ma non dalle sole torri senza intervento.
- Downed/revive/die coincidono nei client; niente multi-revive reward.
- Wave state non dipende solo dal timer e non finisce con nemici vivi.
- Shot/reload/sprint ripetuti 100 volte, in 30–100ms ping, nessun ghost ammo.
- Opening sector non raddoppia wave budget; Nucleo S0 e UI restano validi.
- 1–4 player/4 class duplicates e solo: sempre una strategia possibile senza una classe obbligatoria.

## Performance: target, NON claim

Windows 1080p, qualità Medium, **60fps target** su GPU non top di gamma da scegliere; profilo test 20/30/50/75 zombie con diverse difese e 2/4 players. Registrare game thread, render thread, GPU ms, nav, anim/AI, network bytes/sec, VRAM, hitches e FPS 1% lows. Se non regge, correggere anim LOD, spawn cap e materiali nello stesso strato. Non abbassare qualità visiva a caso prima di misurare.

## Build/ship checklist

- Windows packaged Development almeno a ogni major strato e Shipping alla fine; install su PC pulito, avvio senza editor/plugin mancanti.
- Versioning, build number, changelog, controllo file size e path, screenshot reale, trailer solamente da gameplay reale, logo originale/non trademark conflict.
- Mouse/keyboard settings, accessibility, opzioni voce/audio, language UI IT, eventuale inglese con traduzione vera e testata.
- EULA/credits, privacy per eventuali telemetrie (default nessun raccolta esterna), rating/gore/compliance store da verificare **prima** di distribuzione.
- Co-op host/solo: schermate informative su LAN/internet, limiti server host, no promessa matchmaking inesistente.
- Crash handling/log locali, cleanup sessione, no save corrotti o leak di dati.
- Nessuna licenza Fab/Marketplace presunta dall'aver linkato una pagina; ricevute e diritti per tutti i binari nel package.
- Steam Direct o altri costi store NON si pagano durante sviluppo finché prodotto non è pronto; decisione commerciale separata.

## Report obbligatorio per ogni strato

`MilestoneID | stato | commit | asset approved + license | real animation clips | real SFX/VFX | real UE build + logs | video/screenshot gameplay | net tests | bugs residual | performance | next exact ticket`. Zero fake PASS. Nessuna data o durata garantita se non verificata.
