# GAP E DECISIONI APERTE — NON INVENTARE RISPOSTE

**Regola:** il piano è completo sul comportamento dei sistemi, ma alcuni materiali e dati non sono ancora disponibili. “Piano completo” NON equivale a fingere che ci siano già i file, i prezzi o le animazioni. Questi gap vengono risolti nello strato appropriato, e se non risolvibili senza soldi bloccano l'avanzamento. Tutto quanto segue non è autorizzazione a cambiare stile o scope.

| GAP | Decisione bloccata | Perché aperto | Azione obbligatoria |
| --- | --- | --- | --- |
| G-01 | AR finale dal bundle Deadghost | il contenuto reale va acquisito/importato | leggere mesh files e scegliere AR che supporta reload/muzzle/IK |
| G-02 | animazioni per tutte le azioni del Survivor | pack umano non garantisce ogni clip | import Game Animation Sample + retarget/autoring; completare missing |
| G-03 | Nurse full anim kit | la scheda include solo 3 clip | usare QuokkaVoid dove possibile o creare clip |
| G-04 | rig/visibilità della prima sentry | sci-fi turret non è coerente automaticamente | screenshot art pass o acquisire mesh industriale free |
| G-05 | barricata/slowfield visuals | no asset finale fissato | usare modular props industriali reali, animazioni/FX accurati |
| G-06 | rig di tre zombie speciali e boss | solo Walker Nurse source bloccata | trovare fonti gratuite reali, confrontarle con look e skeleton; non inventare mesh |
| G-07 | shotgun/SMG | il bundle dichiara 7 modelli ma inventory reale sconosciuto | censire e approvare o trovare due fonti free coerenti |
| G-08 | utility samples audio realistici | Kenney covers UI/impacts, non ogni gun/zombie | cercare foley free CC0/Fab con licenza e ascoltare |
| G-09 | performance target hardware minimo | il PC sviluppo non rappresenta client target | test hardware reale e scelta profilo, annotare FPS misurati |
| G-10 | co-op internet | solo LAN/host previsto; NAT/inviti dipendono implementazione | non promettere online pubblico; dichiarare trasporto realmente funzionante |
| G-11 | licenze raw assets | repo pubblico e Fab EULA | manifest e licenze; privata storage, package licito |
| G-12 | scelta camera spec a seconda del model | 1p arms e 3p body richiedono rig/IK | lock implementazione dopo import, senza cambiare look |
| G-13 | balance finale | tutti i numeri sono seed | simulate, test 1p/2p/4p e freeze params v1.0 |
| G-14 | nome commerciale/trademark | Zombie Defence è working title | naming check e logo solo prima release |
| G-15 | multiplayer steam integration | OnlineSubsystemSteam nel template non implica sessione ready | fallback LAN Null OSS e verifica concreta |

## Decisioni fissate e non rinegoziabili dall'agente

HordeTemplate UE5.8, FPS 1p con corpo 3p, Windows, zero acquisti nuovi, 10 onde + boss, 4 armi, 5 archetipi zombie, tre classi, tre difese, Nucleo, 3 settori oltre S0, 1–4 co-op via listen-server dove funzionante, niente P2W e niente crafting. Rimuovere una feature 1.0 richiede esplicita decisione del committente, non la comodità di un agente.

## Change-control

Ogni richiesta nuova ha `ID; problema giocatore; proposta; benefit; impatto su core loop; costi; asset; dipendenze; test; approvazione; version`. Lo scope 1.0 non cresce per iniziativa autonoma. Qualsiasi asset che non supera art gate è `REJECTED`, non “good enough”.

## Gap aggiunti dal design di sinergie 1.1

- **G-16 Spinta di emergenza V**: non esiste attestazione che Survivor o le animazioni già scelte comprendano push melee 1P/3P. Quando arriva L2/L3 produrre animazioni vere con rig autorizzati e relative zombie reactions; nessun montage finto.
- **G-17 FX core**: un anello di contenimento elettrico industriale con telegraph leggibile deve essere creato (Niagara+audio) quando arriva L8, senza usare nuovo pacchetto a pagamento. Lo status slowdown usa logica Slowfield già prevista, niente sistema duplicato.
- **G-18 Passivi S1/S2/S3**: non aggiungere nuove strutture costose; riusare banco, repair interaction e signal/light dei props esistenti. Mancanza di asset reale implica task settoriale non DONE.
- **G-19 Ping e onda W7**: nessun nuovo zombie o skill tree richiesti; sono riuso targeting/disable della sentry esistente. QA di LoS e 1p deve essere registrato.
