# MANDATO COMPLETO A CODEX — REALIZZARE L'INTERO GIOCO SENZA INVENTARE NULLA

> QUESTO È IL TESTO PER L'AGENTE. Non è una richiesta di un altro documento di pianificazione: la pianificazione è già definita. Implementare i sistemi seguendo tutti i file obbligatori e il backlog CSV in ordine.

## Missione

Realizza **Zombie Defence 1.0** in Unreal Engine 5.8 con **HordeTemplate V2 Native** come codice di partenza. Gioco FPS action con zombie in 10 ondate, 4 armi rifinite, 5 archetipi zombie rifiniti e boss, Nucleo difendibile, 3 difese, 3 classi attive, 3 aree cittadine espandibili oltre S0, economia e upgrade, HUD/UX, solo e cooperativo host 1–4, build Windows. Tutti i sistemi **animati, sonorizzati, con FX, coerenza visiva e networking**. Non usare placeholder per fingere che un sistema sia finito. Budget nuovi acquisti 0 €. Non progettare un gioco diverso.

**Fonte di verità:** `AGENTS.md` → `docs/18_MASTER_GAME_SPEC.md` → **`docs/40_SYNERGIES_SKILLS_AND_CITY.md` (design lock v1.1)** → `docs/33_FULL_BACKLOG.csv` → docs/19–32 specifici. Il vecchio docs/12 descrive l'ordine delle fasi, già incorporato nel backlog. Se istruzione generica contrasta con regola dettagliata recente, applicare la recente e annotare il punto nel decision log. Non “reinterpretare” il concept.

## Esecuzione deterministica

1. Controlla workspace e individua primo ID backlog non DONE con dipendenze DONE. Prendi **quello solo**, lavora fino alla checklist completa. Non saltare perché asset/motion import è difficile.
2. L0: usa script `scripts/bootstrap_horde.ps1` se ambiente Windows adatto. Il framework è scelto. Non aprire un altro studio su Lyra o alternative salvo blocco tecnico insuperabile documentato. Mantieni copyright MIT; non caricare raw assets terzi nel repo pubblico.
3. L1-L4: Survivor reale, AR reale, Nurse reale, primo isolato reale; animazioni autentiche e SFX/VFX nello stesso lavoro. Non implementare core TD mentre l'AR non ha il reload corretto.
4. L5 e seguenti: Director unico, core, barricata, sentry, campo slow, due valute e tier, settori, classi, altre armi e nemici **uno per volta**, boss, QA/release.
5. Ogni nuovo tipo usa le definizioni dati ed eventi di docs/31, non una seconda state machine/weapon system. Non aggiungere asset di dubbia origine; ogni asset futuro è GAP finché approvato.
6. Scrivi il nome di **ogni file reale** creato o modificato, commit, esito build, screenshot/video; non inventare file di engine, asset UE, anim clip o tool disponibili.
7. Esegui test come condizione di **qualità di produzione**, non stage di demo. Se engine non è installato in quell'ambiente, puoi scrivere e verificare staticamente quel che puoi, ma stato IN PROGRESS/BLOCKED, non DONE.

## Proibizioni

- **Integra il design 1.1 senza nuovi sistemi inutili:** V spinta, Q classe, ping centrale su sentry, E Impulso Core 1/wave, una utilità per settore, crisi W7; tutto nel proprio strato e con asset/audio/anim/VFX veri. Non aggiungere altri tasti skill/valute.
- Nessun placeholder finale (mannequin stock, zombie generico, cubi, audio fake, texture stock fuori stile).
- Nessun sistema mezzo funzionante spacciato per completato. Se manca una animation/FX/suono, non passare al task successivo.
- Nessun acquisto, API pay-per-use, download pirata, reverse engineering asset commerciali illegali, pacchetto “gratuito” da pagina Buy now.
- Nessun porting a Unity/Godot, niente isometrico/RTS/idle, niente survival crafting, negozi, br, classi fantasy.
- Niente parallelizzare cinque lavori con dieci bug; niente ricostruire armi/inventory/AI da zero se riuso del template può raggiungere requisiti.
- Non inventare numeri definitivi: i parametri seed sono da usare come prima configurazione reale e tarare con gameplay, non certificarli senza prove.
- Non ritardare a priori tutti gli asset “belli” fino alla fine: ciascuno strato esce già completo con il suo art/audio.

## Se asset o licenza sono BLOCCANTI

Non usare un asset falso di comodo. Verifica esistenza di fonte free con licenza, adatta allo stile e rig. Se manca: aggiorna `docs/35_DECISION_GAPS.md` con costo 0 tentato, asset confrontati, motivo esclusione, impatto ed esigenza unica di intervento dell'utente (es. login Fab). Non inventare di avere fatto il download. Continui sullo stesso task finché è risolvibile senza violare il vincolo.

## Output obbligatorio in ogni turno/commit

```
TASK ZD-xxx | LAYER Lx | STATE DONE / IN PROGRESS / BLOCKED
Objective completed (observable): ...
Files changed (real): ...
Assets acquired/approved (and license, private location): ...
Animation/Audio/VFX required vs integrated: ...
Build command + exit status: ...
Tests actually run, logs and screenshot/video links: ...
Gameplay description from actual run (not assumption): ...
Remaining bugs/blocker and scope: ...
Next task ID (only if all dependencies DONE): ...
```

**Non descrivere il codice come un gioco completo se non esiste un video e una build reale dell'esperienza completa.** Le vecchie issue G0 chiuse non significano che la build sia stata fatta; indicano solo che i test devono essere interni agli strati produttivi.

## Full-game acceptance

Tutte le righe di `33_FULL_BACKLOG.csv` fino alla release 1.0 risultano DONE con file e prova, e tutti i sistemi nella matrice `32_QA_RELEASE.md` completi. Non modificare questa policy autonomamente per “finire più in fretta”. Per nuove richieste cambiare formalmente decision log e backlog senza distruggere progressi o sostituire di nascosto le scelte.
