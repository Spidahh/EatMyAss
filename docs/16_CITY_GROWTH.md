# CITTÀ IN COSTRUZIONE — MAPPA A STRATI, SENZA DISTRARRE DAL FPS

**Ordine:** la prima città NON è la prima milestone. Gameplay personaggio, arma e zombie devono essere chiusi prima di completare il mondo. Tuttavia L1–L4 richiedono una piccola area reale giocabile.

## Scena iniziale: isolato industriale urbano

Un solo piccolo spazio con: strada di accesso, magazzino/fabbrica esterna, angolo cieco dal quale arriva Nurse, un cancello chiuso per la crescita futura, una zona sicura di spawn. Luogo scelto per testare **nel gioco effettivo** corsa, salti, collisioni, ADS, colpi sulle superfici, audio di passi, avvistamento zombie e percezione. Geometrie modulari permanenti derivate dal pack Factory Environment Collection quando acquisito legalmente. Non riempire con scatole provvisorie, edifici di qualità incoerente o centinaia di props decorativi.

## Espansione cittadina futura per settore

| Strato | Settore | Nuova scelta di gameplay |
| --- | --- | --- |
| L4 | Isolato e cortile iniziali | player, rifle e Nurse giocano e si sentono bene |
| L6 | Punto del futuro Nucleo e primo varco | mostra come difendere qualcosa |
| L9-A | Officina/garage cittadino | potenziamenti e piazzole torretta |
| L9-B | Strada e deposito | secondo lato di attacco; nuove porte |
| L9-C | Tetti/passaggio sopraelevato | visuale diversa ma rischio aggiuntivo |

Ciascuna area viene completata con **navigazione, collisione, cover, materiali, illuminazione, audio, ingressi e connessioni** prima della successiva. Aprire settori non deve bloccare navmesh, generare nemici attraverso i muri o introdurre spawn in faccia al giocatore.

## Ambiente e rendering

- Leggibilità delle sagome degli zombie prevale su atmosfera buia; silhouette distinguibile in corsa.
- Stile industriale urbano realistico: cemento, metallo, insegne malmesse, detriti funzionali, insegne luce/energia.
- Interazione arma-materiali: concrete/metal/flesh con VFX/SFX specifici; capsule e mesh non devono impedirsi a vicenda il movimento.
- Ottimizzare progressivamente solo la zona completata: collisioni semplici, LOD, budget texture/luci, occlusion.
- Non chiamare “città finita” l'isolato iniziale. È un **settore definitivo dentro una città ancora in costruzione**, non un finto gioco completo.

## Regola

Mai costruire una mappa enorme per compensare meccaniche mediocri. Il mondo cresce solo dopo che i sistemi fondamentali sanno già stare in piedi.
