# Zombie Defence — FPS zombie + Tower Defense (Unreal Engine 5.8)

**DOCUMENTAZIONE DI PRODUZIONE v1.1 · 25/10/2026**  
**Stato reale:** documenti, asset research e backlog completati; **nessun codice gameplay Unreal ancora integrato/compilato in questo repository**. Gli asset esterni vanno acquisiti legalmente sul workspace di sviluppo: non sono contenuti nell'archivio GitHub pubblico.

## Il gioco che stiamo costruendo

Un FPS d'azione cooperativo 1–4 per Windows. Si combattono ondate zombie con 4 armi potenziabili, 3 classi e abilità, mentre si protegge un Nucleo costruendo barricate, torrette e un dispositivo rallentante. La mappa è una città industriale con 3 settori acquistabili oltre al cortile iniziale. Economia personale + fondi difesa, upgrade a Nucleo/armi/difese, 10 ondate + boss, fine partita e replay. Asset credibili, animazioni e suoni completi, niente placeholder che rimangano.

**Base designata:** [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate) UE5.8. **Primo contenuto:** [Survival Character](https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e) + una vera arma del [FPS Weapon Bundle](https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5) + [Zombie Nurse](https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc). Poi ogni funzionalità di gioco completa, prima della successiva.

## Nuovo gameplay intrecciato (v1.1)

Aggiunte di design **senza nuove valute, classi o nemici**: V = spinta di emergenza, Q = una skill per classe, middle mouse = ping che indirizza priorità sentry, E al Nucleo = impulso di rallentamento una volta per ondata (dal Tier2), S1/S2/S3 = utilità della città con rischio di un nuovo fronte. I dettagli sono nella **[spec delle sinergie](docs/40_SYNERGIES_SKILLS_AND_CITY.md)**; la **[ricerca comparativa](docs/39_COMPARATIVE_GAME_DESIGN.md)** spiega cosa tenere/evitare da COD Zombies, Sanctum 2, Outpost, SENTRY e Orcs Must Die!.

## Apri qui il piano COMPLETO

| Punto | Documento | A cosa serve |
| --- | --- | --- |
| **0** | **[AGENTS.md](AGENTS.md)** | Regole obbligatorie per Codex/AI: valgono per l'intero gioco |
| **1** | **[Specifica madre 1.0](docs/18_MASTER_GAME_SPEC.md)** | Contenuto finale e scelte bloccate |
| **2** | **[Backlog integrale (80 attività)](docs/33_FULL_BACKLOG.csv)** | Tutto il lavoro in sequenza, task + dipendenze + Done |
| **3** | **[Guida backlog](docs/33_BACKLOG_GUIDE.md)** | Come non saltare strati e registrare le prove |
| **4** | **[Mandato esecutivo Codex](docs/34_CODEX_MASTER_BRIEF.md)** | Istruzioni da seguire senza reinterpretazioni |
| **5** | **[Matrice contenuto 1.0](docs/38_RELEASE_CONTENT_MATRIX.csv)** | Tutto ciò che deve essere realmente presente: anim, audio, VFX, UI, net |
| **6** | **[Status esecuzione](docs/37_EXECUTION_STATUS.csv)** | Stato reale e prova per ogni singolo task |
| **7** | **[Asset fonti e gaps](docs/30_ASSET_PRODUCTION.md)** | Pack concreti, licenze, componenti da trovare/produrre |
| **8** | **[Quality bar e release](docs/32_QA_RELEASE.md)** | Definizione di completo fino allo shipping |
| **9** | **[Skill integrate e città v1.1](docs/40_SYNERGIES_SKILLS_AND_CITY.md)** | Abilità giocatore, classi, Nucleo, quartieri e sinergie |
| **10** | **[Confronto titoli](docs/39_COMPARATIVE_GAME_DESIGN.md)** | Decisioni dopo ricerca giochi simili |

## Specifiche di tutti i sistemi

| Tema | Link |
| --- | --- |
| Sessioni, regole vittoria/sconfitta, down/revive | [19 — Partita](docs/19_SESSION_AND_RULES.md) |
| Shooting, 4 armi, migliorie, suoni/anim | [20 — Combat](docs/20_COMBAT_WEAPONS.md) |
| 5 zombie, AI, behavior, hit, boss | [21 — Zombie](docs/21_ZOMBIES_AI.md) |
| Nucleo, barricata, sentry, slowfield, energia | [22 — Difese](docs/22_DEFENSE_AND_BASE.md) |
| 3 classi, passive/attive, cooldown | [23 — Classi](docs/23_CLASSES_ABILITIES.md) |
| Cortile e tre settori città espandibili | [24 — Città](docs/24_CITY_AND_SECTORS.md) |
| Crediti, fondi, spese, ricompense e bilanciamento | [25 — Economia](docs/25_ECONOMY_BALANCE.md) |
| Curve delle dieci ondate, spawn, boss | [26 — Wave director](docs/26_WAVE_DIRECTOR.md) |
| Co-op 1–4, networking, lobby, salvataggi | [27 — Multiplayer](docs/27_MULTIPLAYER_SAVE.md) |
| HUD, input, UI, accessibilità | [28 — UI/UX](docs/28_UI_AND_INPUT.md) |
| Matrice di animazioni/audio/VFX per ogni oggetto | [29 — Media](docs/29_ANIMATION_AUDIO_VFX.md) |
| Classi Unreal, data assets, replication e codice | [31 — Tecnica](docs/31_UNREAL_ARCHITECTURE.md) |
| Store, licenze, costi, patches | [36 — Release](docs/36_RELEASE_AND_OPERATIONS.md) |
| Cosa non è verificabile senza file reali | [35 — Gap e decisioni](docs/35_DECISION_GAPS.md) |

## Sequenza di realizzazione SENZA sostituzioni fittizie

`L0 framework → L1 player completo → L2 AR completo → L3 Nurse completa → L4 prima zona città completa → L5 ondate → L6 Nucleo/barricata → L7 sentry/slow → L8 economia/upgrade → L9 città espansa → L10 classi → L11 armi/zombie/boss/resto 10 onde → RC UI/network/perf/legal/shipping`.

Ogni fase include le animazioni vere, audio, VFX, rete, collisioni, interfacce, bugfix e build dei propri contenuti. **Non iniziare la prossima fase finché la precedente non soddisfa tutti i requisiti.** L1–L4 NON sono tutto il gioco. I vecchi docs/00–17 restano archivi di progettazione e sono **subordinati** alle specifiche aggiornate.

## Github pubblico e asset

Fab Standard License normalmente permette asset incorporati nella build del gioco ma vieta redistribuirli come raw files standalone. Non caricare contenuti Fab/Epic non redistribuibili in forma sorgente nel GitHub pubblico. Usa il progetto privato locale ed esporta solo sorgenti/testi che abbiamo diritto a pubblicare; `.gitignore` esclude `Game/Content/` e `ExternalCache/`. Il link non equivale ad aver scaricato/importato.

## Quando entra Codex

**[Issue #6 — INTERO GIOCO](https://github.com/Spidahh/EatMyAss/issues/6)** è il mandato madre fino alla release 1.0; [Issue #5](https://github.com/Spidahh/EatMyAss/issues/5) traccia solo L0–L4. L'intero lavoro è nel backlog CSV. Leggere AGENTS.md e prendere solo prima riga non DONE. Helper PowerShell disponibile in [scripts/bootstrap_horde.ps1](scripts/bootstrap_horde.ps1); non è stato eseguito qui. Nessuna promessa fittizia di gioco già pronto.
