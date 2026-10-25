# ASSET STRATEGY DI TUTTO IL GIOCO — REALI, GRATUITI, MAI INVENTATI

## Regola madre

Gli asset di seguito sono separati in 3 livelli:
- **LOCKED SOURCE:** è stata scelta una fonte nominativa e reale, ma NON implica pack già scaricato/importato/licenza attribuita all'account.
- **CANDIDATE / ART CHECK:** esiste una pagina concreta con disponibilità osservata; prima del lock confrontare look e rig nell'engine.
- **GAP BLOCKING:** nessuna risorsa finale gratuita è stata individuata/approvata e non si può completare il tipo finché non viene acquisita/creata legalmente.

La “completa disponibilità di asset” **non si deduce dai titoli dei pacchetti**. Ogni pack deve essere importato in workspace privato e verificato. Catalogo storico dettagliato: [03_ASSETS.csv](03_ASSETS.csv). Per un repository pubblico GitHub vietata la pubblicazione dei file sorgente Fab/Epic senza autorizzazione a redistribuirli come asset isolati; standard Fab normalmente autorizza uso incorporato in prodotto e collaborazione privata, non free redistribution standalone: https://www.fab.com/eula .

## Tabella di sorgenti effettive

| Sistema | Source | Costo visto | Status di produzione | Caveat |
| --- | --- | --- | --- | --- |
| Framework e C++ | https://github.com/DasBander/HordeTemplate | gratis MIT repository | LOCKED SOURCE | UE 5.8 dichiarato; build non eseguita; provenance .uasset da verificare |
| Umano Survival | https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e | Free | LOCKED SOURCE | NoAI; non confondere rig con set di animazioni FPS |
| Locomozione umano | https://dev.epicgames.com/documentation/unreal-engine/game-animation-sample-project-in-unreal-engine | Epic sample | LOCKED SOURCE | migrare anim genuine/retarget compatibile, NO importare intero sistema secondo framework |
| 7 mesh armi incl. primo AR | https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5 | Free (storico catalogo) | LOCKED SOURCE per AR | identificare le 7 armi reali dall'archivio, non dichiarare shotgun se manca |
| Prima zombie Nurse | https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc | Free verificato 25/10 | LOCKED SOURCE | 3 animazioni soltanto, niente AI |
| Animazioni zombie | https://www.fab.com/listings/82b55c77-c706-4634-839e-29ba827dac8d | Free su scheda storica | LOCKED SOURCE | 50 clip dichiarati, copertura reale da censire, NoAI |
| Città industriale | https://www.fab.com/listings/2ee66462-8c2b-4303-892c-83f7fc0d9b3e | Free catalogo precedente | LOCKED SOURCE | adatto fabbrica, da integrare in layout urbano |
| Alternative modello zombie | https://www.fab.com/listings/986b1ef0-f319-40cd-9020-2936fa6e3ab6 | Free su catalogo precedente | CANDIDATE | look/rig/LOD da valutare; non dire Runner |
| Modello zombie var 8 | https://www.fab.com/listings/79584058-ab08-45d4-a7be-68a65256aa99 | Free su catalogo precedente | CANDIDATE | non è garantito possa fare armored/saboteur |
| Modello zombie var 10 | https://www.fab.com/listings/a9d3d190-893e-4e08-a17d-e7a656eb02c5 | Free su catalogo precedente | CANDIDATE | no boss finché non approvato |
| Sentry rig | https://www.fab.com/listings/4abb6121-4d71-4b67-8e61-b83b7b3e2d10 | Free verificato 25/10 | CANDIDATE / ART CHECK | estetica sci-fi potrebbe non funzionare; è mesh rigged, non AI tower |
| FX muzzle | https://www.fab.com/listings/435b3bcb-d7f5-467d-99aa-2edc97a6c5fd | Free in catalogo precedente | CANDIDATE | verificare VFX e compatibilità |
| Suoni starter | https://www.fab.com/listings/c00b1073-0f0b-42be-a049-fc4c22d0243f | Free in catalogo precedente | CANDIDATE | 65 effetti, non copertura totale SFX |
| Audio interfaccia | https://kenney.nl/assets/interface-sounds | Free CC0 confermato | LOCKED SOURCE | UI/feedback soltanto |
| Audio impatti | https://kenney.nl/assets/impact-sounds | Free CC0 confermato | CANDIDATE | alcuni suonano sintetici; non usarli per flesh se inadatti |
| UI art base | https://kenney.nl/assets/ui-pack | Free CC0 confermato | CANDIDATE EDIT/ART | solo elementi componibili, NON UI finale stock |
| Props urbani postapocalypse | https://www.fab.com/listings/e7fb410a-a652-424d-b91d-4abd5511b033 | Free verificato 25/10 | CANDIDATE | 6 props; alcuni generati con AI, verificare standard artistico |

**NON GRATUITI:** Post-Apocalyptic Urban City (Akairo) e Modular Post-apocalyptic City (ScaleStudio3D) mostrano “Buy now”; non includere in piano zero euro solo perché parlano di un “free pack” esterno. Non utilizzare asset UEFN-only come giochi stand-alone senza diritto di export.

## Gap reali che Codex deve risolvere, non nascondere

| GAP | Elemento mancante | Soluzione a costo 0 da perseguire | Quando blocca DONE |
| --- | --- | --- | --- |
| AS-01 | animazione reload/equip/ADS esatta per AR Deadghost | produrre rig hands/weapon in Unreal Control Rig+Sequencer; usare motion retarget lecito dove compatibile | L2 |
| AS-02 | animazioni zombie run/stagger/death sul modello Nurse | retarget dal pack zombie/creare clip proprie corrette | L3 |
| AS-03 | city street props completi oltre fabbrica | modular design da environment selezionato + props free legalmente acquisiti | L4 |
| AS-04 | tre modelli zombie finali Runner/Armored/Saboteur | ispezionare free zombie var 1/8/10, creare differenze morfologiche/armatura quando legalmente possibile, approvare screenshot art gate | L11 |
| AS-05 | mesh boss distinta rigged | ricerca mirata pacchetto free adatto; possibile propria variante **nuova** modellata/riggata se qualità alta, non Nurse scaled up | L11 |
| AS-06 | shotgun e SMG finali se non compresi bundle | catalogo Fab free specifico, 2 genuine 3D mesh rigged + hands/anim finale | L11 |
| AS-07 | barricata e slowfield finali | assemblare mesh modulari veri + Control Rig/static animated states + Niagara custom, materiali coerenti | L6/L7 |
| AS-08 | sentry industriale coerente | art check del rig NavXGen; se stona, altra mesh free reale o modifica lecita con Blender, non cartone placeholder | L7 |
| AS-09 | suono AR vero, reload cloth e zombie categories | audioteca free licenziata e foley proprio; lasciare audio breve incompleto significa fase incompleta | L2/L3/L11 |
| AS-10 | classe ability montage/VFX/voce | realizzare gesture, niagara, SFX coerenti con ogni ability | L10 |
| AS-11 | boss animation telegraph/death | asset rig + animation authoring dedicato, non standard attack scaling | L11 |

## Protocollo acquisizione

1. Richiedi il pack ufficiale, leggi EULA e flag NoAI; registrare `AssetId,ListingURL,Publisher,Version,License,NoAI,AcquireDate,Files,Checksum,ApprovedForPublicRepo,PrivatePath,UseCase,AnimClips,QAResult`.
2. Non scaricare automaticamente su account senza accesso/autorizzazione. Nel repo pubblico tenere manifest testuale e scripts; raw Fab/Epic solo privata.
3. Import in Unreal con Scala/Skeleton/Material/Pivot/Collision/LOD/Retarget; registrare mesh names reali **dopo** apertura, non inventarli dal titolo.
4. Lookdev in scena già prevista nello strato, in FPS e remote 3P, non color swatch astratti.
5. Integralo come asset definitivo del nuovo sistema, verifica FPS/performance, audio, copyright; solo allora `APPROVED`. Se una risorsa gratuita non raggiunge estetica coerente, scartarla e trovare altra fonte a costo 0.

## Art direction e budget

Urban industrial realistico adulto, notte leggibile, nessun mismatch cartoon/realistic, texture 2K default salvo hero, LOD per crowds, lights funzionali per distinguere zombies. In futuro ogni nuova risorsa deve confrontarsi con quattro screenshot art gate della scena iniziale, non cambiare stile a ogni pack. **Una città bella può nascere con pochi asset buoni combinati bene, non con 200 pacchetti incoerenti.**
