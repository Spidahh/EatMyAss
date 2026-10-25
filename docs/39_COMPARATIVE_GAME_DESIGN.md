> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# RICERCA COMPARATIVA — COME RENDERE ZOMBIE DEFENCE PIÙ DIVERTENTE SENZA COMPLICARLO

Data ricerca: **25 ottobre 2026**. Le fonti documentano i giochi citati; le meccaniche proposte per Zombie Defence sono **nostre**, non presenti in quei titoli né automaticamente legittimate dalla loro popolarità. Non riutilizzare asset/trademark/codice proprietario di giochi comparati.

## I tre riferimenti principali

| Gioco | Cosa funziona | Da importare nel nostro game design | Cosa NON importare |
| --- | --- | --- | --- |
| [Call of Duty: Black Ops 7 — Zombies](https://www.callofduty.com/blog/2025/09/call-of-duty-black-ops-7-zombies-deep-dive/) | armi FPS, loop zombie, upgrade, perk e field upgrades distinguibili | feedback arma, un'abilità Q per classe, feedback immediato su headshot, 10 onde progressive | 12+ perk, multipli ammo mods, loot random, tre valute, meta XP obbligatorio, asset/licenze CoD |
| [Sanctum 2](https://store.steampowered.com/app/210770/Sanctum_2/) | personaggio FPS spara accanto alle torri, core difeso, scelte di percorso, 4 classi | tradeoff arma/difese, fase pre-onda breve, gunplay vivo | maze-building libero che distrugge navigazione zombie in multiplayer |
| [Outpost: Infinity Siege](https://store.steampowered.com/app/1566690/Outpost) | base visualmente cresce, upgrade che hanno presenza fisica e potenza | Nucleo tier visibile, settori della città acquistati con nuovi vantaggi tattici | crafting/loot/farm RTS, 20 building types, outpost mobile e inventory laborioso |

## Due riferimenti moderni extra

- [SENTRY](https://sentrygame.com/): FPS action-defense con turret, trap e **environmental actions**, come porte antiesplosione e oggetti distruttibili. Trasferiamo il concetto di **ambiente come strumento di difesa**, ma in forma di un **solo impulso del Nucleo**, non un sistema fisico di porte che obbliga a riscrivere AI.
- [Orcs Must Die! Deathtrap](https://robotentertainment.com/news-archive/2024/8/15/orcs-must-die-deathtrap-our-new-loop-and-progression-systems): scelte tra ondate (Threads) e combinazioni eroe/trappola; ottima la sinergia attiva. Noi preferiamo **una scelta Tier3 della città** e classi con una skill ciascuna, senza 3 carte casuali dopo ogni round.

## Difetti e lezioni da evitare

- Feedback della community su *Deathtrap* segnala che un pool di carte troppo ampio può diluire le strategie desiderate, rendere i progressi troppo aleatori e non interessanti le ondate iniziali. Fonte: https://www.reddit.com/r/OrcsMustDie/comments/1ihgx3o/ ; https://www.reddit.com/r/OrcsMustDie/comments/1inc7fi/ . Sono opinioni dei giocatori, non prove sperimentali generali.
- Alcuni giocatori di *COD Zombies* moderni segnalano poca chiarezza nei molteplici livelli di perk/augment. Fonte: https://www.reddit.com/r/CODZombies/comments/1ubk2qj/newbie_in_bo7_zombies/ . **Un giocatore deve sapere cosa fa una skill senza leggere un wiki.**
- *Outpost* dimostra che FPS, TD e base building possono coesistere, ma introdurre crafting/campagna RTS sarebbe enorme per un developer singolo. Il nostro limitatore deliberato è **una mappa urbana, piazzole fisse, due valute, nessuna farming loop**.
- Più sistemi non significa più valore: una torretta che vince da sola toglie importanza all'FPS; un'abilità che fa tutto non dà decisioni significative. Ogni skill deve avere 1 effetto principale e un controgioco.

## Criteri di ammissione delle novità

**Accettiamo solo se tutte le risposte sono sì:**
1. Fa sparare, muovere o prendere una decisione tattica al player?
2. Può sfruttare server/network/AI/asset già previsti, invece di un nuovo framework?
3. Si capisce in meno di 3 secondi da HUD+VFX+suono?
4. Ha un costo chiaro (cooldown, 1/wave, tradeoff economico), non una nuova valuta?
5. Non rende inutili classe, torri, player o mappa?
6. Può essere completata con vere animazioni, suoni e FX nello strato di competenza?
7. Non aggiunge un nuovo menu, nuovo tasto oppure nuove richieste artistiche sproporzionate senza giustificazione?

## Decisione di design

**Non aggiungere altre classi, torri, armi o nemici alla 1.0** per queste idee. Diamo profondità ai pezzi già progettati con **quattro intrecci**:
1. Scontro FPS ↔ zombie: spinta di emergenza universale e danno leggibile.
2. Player ↔ torretta: ping prioritario a vista, rispettando sempre line of sight e range.
3. Classe ↔ struttura: Assault perfora, Engineer supporta dispositivo, Medic protegge compagni; una Q ciascuno.
4. Città ↔ assalto: settori migliorano un servizio di base ma aprono nuovi ingressi; il Nucleo dispone di una sola skill condivisa per ondata.

Specifica precisa, input, numeri-seed, asset e conflitti in [40](40_SYNERGIES_SKILLS_AND_CITY.md). Codex non è autorizzato a inventare nuove classi, valute o casualità.
