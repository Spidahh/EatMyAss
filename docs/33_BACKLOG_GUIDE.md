# BACKLOG DI PRODUZIONE V2 — 112 TASK SERIALI

**ANNULLA COMPLETAMENTE il vecchio backlog V1.1** che prevedeva città acquistabili, PC/TF e 3 skill vecchie. Questo elenco NON è solo per il prototipo: arriva all'intero gioco Windows Shipping con base autonoma e melee. I task sono in sequenza stretta, uno dipende dal precedente (`depends_on`). Tutti partono PLANNED perché nessun modulo Unreal è stato implementato da questa conversazione.

## Ordine degli strati

- **L0 — Framework HordeTemplate:** 3 task, specifiche [31_UNREAL_ARCHITECTURE.md](31_UNREAL_ARCHITECTURE.md).
- **L1 — Player Survivor completo:** 5 task, specifiche [13_PLAYER_WEAPON_ANIMATION.md](13_PLAYER_WEAPON_ANIMATION.md).
- **L2 — Primo ranged AR completo:** 7 task, specifiche [20_COMBAT_WEAPONS.md](20_COMBAT_WEAPONS.md).
- **L3 — Prima vera arma melee: machete:** 9 task, specifiche [42_MELEE_SKILLS_AND_SPECIALIZATIONS.md](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md).
- **L4 — Prima Nurse completa e integrazione melee:** 7 task, specifiche [21_ZOMBIES_AI.md](21_ZOMBIES_AI.md).
- **L5 — Hub base fisico + primo perimetro:** 7 task, specifiche [43_AUTONOMOUS_BASE.md](43_AUTONOMOUS_BASE.md).
- **L6 — Prima difesa autonoma completa:** 8 task, specifiche [43_AUTONOMOUS_BASE.md](43_AUTONOMOUS_BASE.md).
- **L7 — Rottami, core upgrade, first saving:** 8 task, specifiche [25_ECONOMY_BALANCE.md](25_ECONOMY_BALANCE.md).
- **L8 — Threat Director ondate/continuo:** 9 task, specifiche [26_WAVE_DIRECTOR.md](26_WAVE_DIRECTOR.md).
- **L9 — Altre armi melee complete:** 6 task, specifiche [42_MELEE_SKILLS_AND_SPECIALIZATIONS.md](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md).
- **L10 — Armi ranged rimanenti:** 7 task, specifiche [20_COMBAT_WEAPONS.md](20_COMBAT_WEAPONS.md).
- **L11 — Resto difese/zombie elite completi:** 12 task, specifiche [43_AUTONOMOUS_BASE.md](43_AUTONOMOUS_BASE.md).
- **L12 — Tre territori fuori ed eventi:** 7 task, specifiche [44_OUTSIDE_COMBAT_AND_PROGRESSION.md](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).
- **L13 — Specializzazioni/Co-op/Save:** 7 task, specifiche [42_MELEE_SKILLS_AND_SPECIALIZATIONS.md](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md).
- **RC — Finale, QA e release V2:** 10 task, specifiche [32_QA_RELEASE.md](32_QA_RELEASE.md).

## Regole per Codex

1. Leggere [AGENTS V2](../AGENTS.md), [41](41_CANONICAL_GAME_V2.md), [42](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43](43_AUTONOMOUS_BASE.md), [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md). Non usare requisiti V1.1.
2. Trovare **primo PLANNED**; eseguire solo quel task e completare modello reale, animazioni, SFX/VFX, UI, network, build e prove pertinenti **prima del successivo**.
3. Il numero di task non sostituisce il lavoro: per es. una torre autonoma “funzionante” richiede actual kills senza player nearby; uno script che toglie HP ai nemici offscreen NON è equivalente.
4. Se task manca di asset legale: BLOCKED, record GAP e source davvero gratuita da trovare/produrre con Blender in modo lecito. Non continuare cambiando gioco.
5. Task DONE solo con dati in `37_EXECUTION_STATUS.csv`, commit SHA, build/test logs e video/link pertinente. Aggiorna `33_FULL_BACKLOG.csv` stessa commit, non confondere documentazione completata con gameplay completato.
6. La matrice `38_RELEASE_CONTENT_MATRIX.csv` conta tutte le entità, anim/audio/VFX/collision/AI/replicazione; il release task finale non passa se una colonna manca.
7. V1 aveva 80 task. Ora questi sono **112 task tutti ridefiniti**; gli ID precedenti possono aver cambiato significato. Non usare checklist di vecchie issue come autorevoli: Git history è storico.

## Design lock

DENTRO HUB upgrade / FUORI FPS e melee / tower autonomous 24-7 **durante sessione** / NO offline / una moneta Rottami / 2 torrette + barricata + auto-pulse / 4 ranged+3 melee / 3 specializzazioni Tiratore/Spezzatore/Tecnico / 5 zombie / stage10 + continuation e modalità continua, salvar base host. Niente città economica.
