> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# Asset Bible + acquisizione e integrazione

## 1. Obiettivo visivo

**Art direction proposta:** industriale realistico con lieve stilizzazione funzionale; un complesso di fabbriche arrugginite di sera/notte, luci di emergenza ambrate, freddo blu nelle zone non alimentate, rosso per minaccia imminente, proiettori puntati sulle vie di accesso. Niente miscuglio casuale di lowpoly cartoon e fotorealismo; niente atmosfera tanto scura da nascondere i bersagli. Il giocatore deve leggere la silhouette zombie a 20–30 metri.

Color key: base freddo cemento/acciaio; luci arancioni per energia e costruzioni utilizzabili; segnali rossi per pericoli; verde/azzurro controllati per healing/alleati. Abiti civili usurati e corpi zombie coerenti con la fabbrica. Torretta sci-fi trovata su Fab: **da valutare con un look test prima di adottarla**, poiché può sembrare futuristica rispetto a armi moderne.

## 2. Libreria reale, non immaginata

Asset selezionati e verificati via pagine dei creatori il 24/10/2026. I singoli URL e requisiti sono in `03_ASSETS.csv`. **Non sono stati scaricati né aperti in Unreal**; descrizione, numero di oggetti e disponibilità indicati derivano dalle schede, non da ispezione locale.

### Set 0 — i primi 7 da acquisire per un test controllato

1. **HordeTemplate V2 Native** (repo pubblico, codice MIT): base di meccaniche, co-op e zombie. Prima va auditato ogni contenuto di terzi, e l'avvio in UE5.8 va dimostrato.
2. **Factory Environment Collection** (Fab, Free): officina/fabbrica industriale, sale, mezzi e oggetti. È un insieme artistico, non una mappa zombie bilanciata.
3. **FPS Weapon Bundle** (Fab, Free): 7 mesh armi riggate e 4 attachment, non un sistema di ricarica/tiro completo.
4. **Zombie Female: Nurse** (Fab, Free): zombie femminile, 3 animazioni, scheletro riferito a mannequin UE5; il publisher specifica che non ha AI.
5. **Zombie Animation Pack: Standard** (Fab, Free): 50 animazioni da retargetare, non modelli zombie.
6. **Survival Character** (Fab, Free): modello giocatore maschile con componenti modulari; controllare compatibilità skeleton e visibilità in prima persona.
7. **Sci fi turret** (Fab, Free): skeletal mesh/control rig per prototipo torrette; è **solo visuale**.

Due alternative zombie gratuite su Fab: `Male Zombie 1 - Animated` e `Zombie Number 8/10 - Animated` dell'autore Tony Flanagan. Da testare **prima** se l'aspetto combacia con Nurse; formato FBX/GLB, non presumere retarget seamless. Un'opzione a costo zero non passa il filtro artistico solo per essere gratis.

### Audio/UI/VFX verificati

- Tiny Bat `Free Game Sound Effects Starter Pack – 65` (Fab, Free) per un primo gruppo di zombie, ambience, UI, passi e alcuni altri effetti. SoundCue indicati nella pagina.
- Kenney `Interface Sounds`, `Impact Sounds`, `UI Pack`: licenza CC0 indicata sulle rispettive pagine. UI pack **placeholder**, non look finale.
- `Muzzle Flash (Niagara System)` free su Fab, o `Free Muzzle Flash Texture Pack` CC0 dichiarato. Validare intensità, smoke, performance e materiale su ogni arma.

### Esclusioni deliberate

- Fab `Post-Apocalyptic Scrapyard Pack`: listing gratuito trovato, ma il formato osservato è **UEFN**, con asset referenziati; non assumere funzionamento in un gioco Unreal PC distribuito.
- `Zombies Mini – Low Poly Animated Pack`: la scheda presenta acquisto/licenza selezionabile, quindi **non è nel budget zero**.
- Pack con titolo “Free Bonus”: il bonus può essere gratuito *solo dentro un pack a pagamento*; non è candidato free finché la pagina non mostra Free.
- Modelli Midjourney/AI generated o mesh da giochi commerciali reverse engineered: non includerli automaticamente, anche se li si trova in rete.

## 3. License gate obbligatorio

Per ogni asset scrivere un record `id, publisher, listing, acquired_date, license_name, license_document, pack_version, package_hash, source_formats, access_type, notes`. Fare screenshot della licenza **senza pubblicarlo** e archiviare testo/acquisto nell'area privata del progetto. Fab Standard License permette normalmente l'uso dentro il gioco e la modifica, ma non la rivendita della mesh isolata; i diritti variano per licenza, EULA/UE-only e Reference-Only. Fonte: https://www.fab.com/eula

Un repository MIT non garantisce che *tutti* i file binari inclusi siano degli stessi autori. Se non è possibile provare una licenza valida di un contenuto, **sostituire la risorsa** oppure sospendere quel pezzo. `license_status=unknown` impedisce la promozione a `Approved`.

Il lavoro dell'AI sul codice non autorizza la redistribuzione di mesh/audio terzi. Niente scraping che aggiri paywall, export UEFN verso giochi standalone in violazione delle licenze, asset 'rippati' da CoD o altri giochi.

## 4. Protocollo prove di integrazione per categoria

| Categoria | Prova tecnica | Prova artistica/gameplay | Esito richiesto |
| --- | --- | --- | --- |
| zombie mesh | skeleton, scale, root, LOD, anim retarget, collision, cook | riconoscibile in buio, attacco telegraphed, hit/death non rigido | closeup + 20 simultanei senza glitch |
| player | full-body 3p + viewmodel arms/weapon 1p, retarget, shadow | mani grip corrette su 3 armi, outfit coerente | sprint/ADS/reload senza clipping |
| armi | sockets, mesh rig, mag, muzzle, recoil pivot, material IDs | audio differenziato, mira leggibile, hand alignment | prova equip/fire/reload 100 volte |
| ambiente | collision simple, PBR map, LOD, lightmap/Nanite policy, occlusion | landmarks, visibility zombies, scale e route | 30/50 zombies e 2 players senza nav stall |
| turret | pivot yaw/pitch, range geometry, colliders, muzzle and LoS | statica/anim + hit feedback, riconoscimento tier | target prova + client replication |
| audio | sample rate, looping, concurrency, ducking e attenuazione | arma impatto distinto, zombie classificabili a orecchio | ascolto cieco comparativo |
| UI | safe zones, scaler, controller, font license | leggibile a 1080p, mai copre mira | usability con 2 giocatori |

**Rigging:** gli skeleton di UE4 mannequin, UE5 Manny e provider FBX/GLTF differiscono. Prima di affermare che qualcosa è compatibile, costruire IK Retargeter, retarget pose, mapping arti/root, animazioni idle/run/attack/die e osservare feet slide, penetration e hit align. Non mescolare modelli con scheletri diversi direttamente nello stesso AnimBP.

**Varianti con asset limitati:** 1 modello `Nurse` non deve produrre dieci cloni identici. Tinte/materiali, parti di costume, decals e accessori sono opzioni solo se licenza/mesh/skin consentono. Se modello non supporta modding, acquistare/rintracciare seconda mesh o dichiarare riduzione di scope.

## 5. Più bellezza con meno lavoro: ordine corretto

1. **Blockout prima di decorare:** linee di vista, 2 varchi, altezza coperture e socket. Testare spostamento player e AI con primitive.
2. **Lookdev one-room:** un angolo con Factory Pack, un zombie, arma, lampada, una sentry. Allineare materiali, exposure e postprocess senza sacrificare framerate. Confronto screenshot giorno/notte.
3. **Un asset per funzione:** soltanto dopo successful import portare varianti di zombie/armi.
4. **Audio prima della rifinitura grafica:** il colpo di arma nell'ambiente viene giudicato dal suono e dalle hit reactions, non solo dal modello.
5. **Profilare effetti:** fumo e blood decals non devono accumularsi indiscriminatamente nelle ondate.

## 6. Requisiti nominali di produzione

- Texture: scelta 2K default per molti props; 4K solo hero assets previa misura VRAM, non importare automaticamente a dimensione massima.
- Character LOD e anim update rate ottimizzati su distanza. Crowd sempre testato, mai assunto perché ha LOD.
- Mesh statica con collisione semplice o custom dove i proiettili devono interagire; no collision complessa su ogni detrito.
- Asset naming: `SM_`, `SK_`, `MI_`, `T_`, `ABP_`, `BP_`, `SFX_`, `NS_`; directory Terzi intatte e wrapper in `Content/ZD`.
- Documentare ogni modifica (material instance, scale conversion, retarget asset, blueprint wrapper).
- Non utilizzare asset a pagamento anche se gratuito per il proprietario dell'account di un altro collaboratore; ogni diritto di collaborazione/distribuzione da verificare.

## 7. Art gate: qualità coerente o rollback

Una scena con zombie, giocatore, arma e torretta deve superare un giudizio visivo con quattro screenshot: 1) closeup zombie, 2) combat 10m, 3) vista base, 4) notte 20m. Se il mix è disomogeneo, rimuovere la risorsa stonata; non coprire una differenza di qualità con color grading estremo.

## 8. Link primari

- Fab licensing: https://www.fab.com/eula
- Factory: https://www.fab.com/listings/2ee66462-8c2b-4303-892c-83f7fc0d9b3e
- FPS weapons: https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5
- Nurse zombie: https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc
- Zombie animations: https://www.fab.com/listings/82b55c77-c706-4634-839e-29ba827dac8d
- Survivor: https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e
- Turret: https://www.fab.com/listings/4abb6121-4d71-4b67-8e61-b83b7b3e2d10
- Kenney licensing: https://kenney.nl/support

