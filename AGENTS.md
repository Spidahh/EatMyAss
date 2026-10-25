# ZOMBIE DEFENCE — MANDATO VINCOLANTE A CODEX (V2)

**Aggiornamento 25 ottobre 2026.** Il committente ha corretto radicalmente il gioco: **BASE interna autonoma + combattimento FUORI dalla base**. La precedente concezione di città a settori acquistabili e difesa che richiede il giocatore vicino è **ANNULLATA**. Ignora i requisiti V1/V1.1 incompatibili anche se ancora citati nei commit storici o nel testo di una issue vecchia.

## Fonte di verità — leggere tutti nell'ordine

1. [41_CANONICAL_GAME_V2.md](docs/41_CANONICAL_GAME_V2.md) — descrive **cosa è veramente il gioco**.
2. [42_MELEE_SKILLS_AND_SPECIALIZATIONS.md](docs/42_MELEE_SKILLS_AND_SPECIALIZATIONS.md) — armi da fuoco, melee profondo, Tiratore/Spezzatore/Tecnico.
3. [43_AUTONOMOUS_BASE.md](docs/43_AUTONOMOUS_BASE.md) — hub interno upgrade e sistema di autodifesa reale, con torrette attive senza player.
4. [44_OUTSIDE_COMBAT_AND_PROGRESSION.md](docs/44_OUTSIDE_COMBAT_AND_PROGRESSION.md) — zone esterne, incarichi combat, Rottami, waves+continuo, save host.
5. [18_MASTER_GAME_SPEC.md](docs/18_MASTER_GAME_SPEC.md) — indice e confini di V2.
6. [33_FULL_BACKLOG.csv](docs/33_FULL_BACKLOG.csv) + [33_BACKLOG_GUIDE.md](docs/33_BACKLOG_GUIDE.md) — SOLO i task V2, un task alla volta, non dati di issue precedenti.
7. [38_RELEASE_CONTENT_MATRIX.csv](docs/38_RELEASE_CONTENT_MATRIX.csv) — ogni entità deve avere asset reale, animazioni, audio, VFX, AI, rete e prove.
8. [34_CODEX_MASTER_BRIEF.md](docs/34_CODEX_MASTER_BRIEF.md) — incarico pratico di sviluppo, non pianificazione.
9. [30_ASSET_PRODUCTION.md](docs/30_ASSET_PRODUCTION.md), [31_UNREAL_ARCHITECTURE.md](docs/31_UNREAL_ARCHITECTURE.md), [32_QA_RELEASE.md](docs/32_QA_RELEASE.md), [35_DECISION_GAPS.md](docs/35_DECISION_GAPS.md) — licenze, tecnica, uscita e incertezze reali.

**Precedenza:** AGENTS.md V2 + 41–44 + backlog V2 > eventuali altre note V2 > documenti legacy 00–17, 39–40 V1.1. Se incontri “difendere Nucleo stando fuori vicino alle torrette” o “città/officina/deposito/tetti acquistabili”, considera il requisito ANNULLATO. Le issue non possono sovrascrivere questo file.

## Missione completa V2 (NON solo primo personaggio)

Un Unreal Engine 5.8 FPS action Windows, partendo dal **codice reale HordeTemplate V2 Native**, con:
- **Dentro la BASE fisica**: cammini, cambi armi/classi, fai upgrade a Nucleo/barriere/torrette, spese in UNA moneta Rottami, salvi. Niente combattimento obbligato dentro.
- **Fuori dalla BASE**: FPS ranged + melee (3 armi melee e 4 ranged pianificate), combattimenti zombie e 3 tipi di incarichi opzionali, IA che reagisce a giocatore esterno.
- **Difesa davvero autonoma**: due tipi di torrette + barricata, tutte potenziabili; uccidono senza controllo del giocatore e senza presenza vicina. La base può resistere da sola agli assalti adeguati ai suoi livelli.
- **Assalti**: uno stesso director server per ondate (default) e flusso continuo, minaccia crescente, 10 livelli di escalation con Bruto milestone e possibile continuazione; CoreHP0 unico game over.
- **Tre specializzazioni**: Tiratore, Spezzatore con vera opzione melee-only, Tecnico; 1 attiva Q e 1 passiva ciascuno, revive comune, no healer obbligatorio.
- **Progressi salvati**: base persistente sul PC host tra sessioni, senza simulazione offline, no database o account.
- **Costo**: zero nuovi acquisti predefiniti; niente asset temporanei o illegali, niente city management/crafting/survival.

## Regole per ogni intervento

- Finisci UNO strato intero prima del successivo: codice, mesh reale, rig, animazioni di prima/terza persona, suoni, FX, UI, IA, multiplayer, build, QA visiva e nessuna regressione. **No placeholder finali**.
- Le vecchie skin Survival/AR Deadghost/Nurse restano prime sorgenti designate, ma gli **asset per armi melee e torre pesante sono GAP** da cercare realmente senza inventare licenza/mesh/animazioni.
- Non aggiungere Lyra, seconda weapon system, altre valute, 20 abilità, gestione fabbriche o torri che richiedono il player vicino per sparare.
- La base **continua ad attaccare** se il player è in Zona B, nell'hub o KO; il player può entrare anche sotto assedio, ma l'assedio continua. No autofarming offline.
- Scegliere prima un tipo tower e provarne AUTONOMIA COMPLETA; non attendere L11 per darla.
- Una sola `Rottami` e un solo ledger server; separare l'inventario moneta dall'energia-capacità torri. Upgrade solo nell'hub base fisico.
- Tutta la gameplay state è server-authoritative, incluse tower kills, melee parry/hits, danni, Rottami, salvataggi host, enemy spawns.
- Niente finta scena “città-base”; costruire un INTERNO vero e un ESTERNO con fronti di assedio e zone di combattimento.
- In presenza di mancanza reale asset/Unreal/permessi, documentare BLOCKED, soluzione a zero costo, e **non** proseguire fingendo Done. I codici pronti ma non compilati sono IN PROGRESS.
- GitHub è pubblico: non committare raw asset Fab/Marketplace/Epic non redistribuibili; usare workspace privato e documentare provenance.

## DoD e andamento

Il primo task non DONE del backlog è l'unico attivo. Lo stato DONE richiede video/screenshots reali, build/test pertinenti, attacco melee corretto se coinvolto, prova di base autonoma con player lontano per ogni upgrade difensivo, e risorse autorizzate. I task aggiornano [37_EXECUTION_STATUS.csv](docs/37_EXECUTION_STATUS.csv) con commit ed evidenze. **Nessuna build Unreal o asset importato è stato ancora eseguito da questa conversazione.** Il piano non è il gioco finito.
