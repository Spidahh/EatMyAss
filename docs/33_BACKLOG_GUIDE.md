# BACKLOG V2 CANONICO — 112 ATTIVITÀ

**Ordine definitivo corretto per le dipendenze reali:** L0 Framework → L1 Player → L2 AR → L3 **Nurse vera** → L4 **machete provato sulla Nurse** → L5 hub/perimetro → L6 **Rottami/Core/save** → L7 **director W1–3** → L8 **torretta autonoma con vera W3** → L9 ulteriori melee → L10 firearms → L11 altre torri/enemy/stadi4–10 → L12 zone fuori/eventi → L13 specializzazioni/co-op/save → RC.

Contiene **112 task** tutti PLANNED, ognuno dipende strettamente dalla riga precedente. Le liste vecchie V1.1 da 80 task sono superate, non riusare ID storici (rinumerati ora).

- L0: 3 task
- L1: 5 task
- L2: 7 task
- L3: 7 task
- L4: 9 task
- L5: 7 task
- L6: 8 task
- L7: 7 task
- L8: 8 task
- L9: 6 task
- L10: 7 task
- L11: 14 task
- L12: 7 task
- L13: 7 task
- RC: 10 task

**Codex:** leggi prima [AGENTS V2](../AGENTS.md), [41](41_CANONICAL_GAME_V2.md), [42](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43](43_AUTONOMOUS_BASE.md), [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md). Prendi la prima riga non DONE, non una quest qualsiasi. Ogni task completo include asset vero/licenza, animazioni, audio, FX, collision, AI/damage, UI, net e build reali pertinenti; dichiarare DONE solo con prove in `37_EXECUTION_STATUS.csv`. Se mancano Unreal/asset, IN_PROGRESS o BLOCKED, no placeholder. Non iniziare altra riga senza completare.

**Motivazioni ordine:** Nurse prima di melee, per non validare su fantocci. Wallet e director prima di tower, per testare autonomamente con stage3 e acquisti reali. Stadi4–10 si chiudono DOPO che le unità reali sono prodotte, mai con enemy placeholder. Il giocatore può usare gli upgrade solo entrando DENTRO la base anche se un'ondata è attiva; il mondo non si ferma per questo.
