# COMPITO COMPLETO A CODEX — ZOMBIE DEFENCE V2 (NON RECUPERARE LA V1.1)

**Missione:** sviluppa l'intero gioco in Unreal Engine 5.8 usando HordeTemplate V2 Native, rispettando [AGENTS](../AGENTS.md), [VISIONE V2](41_CANONICAL_GAME_V2.md), [MELEE/CLASSI](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [BASE AUTONOMA](43_AUTONOMOUS_BASE.md), [ESTERNO/PROGRESSIONE](44_OUTSIDE_COMBAT_AND_PROGRESSION.md), [BACKLOG V2](33_FULL_BACKLOG.csv) e [MATRICE ARTE](38_RELEASE_CONTENT_MATRIX.csv).

**NON FARE QUESTI ERRORI:**
- La città NON è la base. Dentro la base si fanno upgrade. Fuori si combatte; non spostare le torrette in negozi o strade da comprare.
- La base combatte automaticamente con AI server anche se il player è fuori, in hub, o morto temporaneamente. Non imporre presenza/mark/manual reload della torre.
- Il player ha armi **melee** principali con parry+counter, non soltanto shove con V. Lo Spezzatore può scegliere la modalità puro-melee.
- Una sola moneta Rottami, NON Player Credits + Team Funds, NO crafting.
- Non reset base dopo 10 wave, il mondo host ha stato persistente. No attacchi offline a game chiuso.
- Il player può rientrare per upgrade anche durante assalto. Non teletrasportare tra round e non fermare nemici per aprire upgrade UI.
- 3 territori fuori NON sono 3 quartieri base acquistabili. Nessuna passiva Officina/Deposito/Tetti della V1.1.
- Altri task/codici di V1.1 non hanno autorità sul nuovo design.

**Ordine:** leggere prima riga `PLANNED` in `33_FULL_BACKLOG.csv`, completare un pezzo con asset finali/anim/audio/VFX/network/QA, passare successivo solo con prova. Primo lavoro player Survival, AR, **Nurse completa**, quindi **primo machete completo provato sulla Nurse**, poi hub, Rottami/Core/save, director vero W1–3 e prima torretta autonoma su ondate reali. 4 ranged+3 melee, 5 zombie, due tower+barriera, 3 specializzazioni, 10+ stage con 2 ritmi, salvataggio host/co-op e final shipping. Non lanciare tre giochi alternativi.

**Legal/assets:** repository pubblico, raw binari Fab/Epic/terzi restano in privata workspace; se asset non Free/non acquisibile, record GAP e possibilità di modello proprio con Blender lecito, non far passare per free un listing Buy Now e non creare placeholder da dimenticare.

**Output per task:**
`TaskID | status DONE/IN_PROGRESS/BLOCKED | file esatti | commits | asset reali e license | animazioni reali | video gameplay | build log exit | auto-defense se pertinente | test multiplayer | save/resume | blocker | next task`.
Niente Done senza engine test reale; non ripianificare tutto e non chiedere ogni volta a utente cosa fare. Devi lavorare **fino alla release completa**, non fermarti alla prima scene di test.
