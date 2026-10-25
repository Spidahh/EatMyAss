> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# MODULO COMPLETO DI GAMEPLAY: SKILL PLAYER + CLASSI + CITTÀ + DIFESA (v1.1)

**DESIGN LOCK 25/10/2026:** queste sono le integrazioni deliberate e limitate per rendere la 1.0 più interessante. Non aumentano il numero di armi, torri, nemici, classi o valute del Master Spec. I numeri indicati sono **seed di bilanciamento**, verificabili solo giocando. Qualora un'integrazione renda impossibile chiudere uno strato con asset reali e tempo disponibile, registrare un blocker e valutare formalmente la riduzione; NON sostituirla con un'altra skill inventata.

## 0. Interfaccia del gioco: due abilità, non un MMORPG

Ogni player ha **1 abilità universale su V**, **1 abilità di classe su Q**, normale interazione con il mondo su E e **1 ping tattico su pulsante centrale del mouse**. L'azione speciale della città è attivata **fisicamente al pannello del Nucleo con E**, non occupa un nuovo tasto né usa mana, XP, energia spendibile o terza valuta.

| Sistema | Input | Limite fondamentale |
| --- | --- | --- |
| Spinta d'emergenza player | V | 12 secondi, una sola zombie normale colpita |
| Skill personale di classe | Q | una active / passive per classe; cooldown 45–55s |
| Marca bersaglio squadra | clic centrale | una marcatura globale attiva 5s, per-player cooldown 8s |
| Protocollo del Nucleo | E al pannello | **una attivazione totale per ondata, per squadra** |
| Passive di quartiere | nessuno | automatiche dopo sblocco, nessun nuovo comando |

**I tasti sono seed modificabili nelle opzioni.** Non aggiungere una seconda barra skill, equip di perk, token power o combo meter. Su gamepad futuro dovrà esistere un mapping contestuale, ma non duplicare oggi tutti i comandi.

## 1. Player: SPINTA D'EMERGENZA (universale, non abilità di classe)

**Perché:** quando uno zombie entra nella distanza minima, il giocatore deve salvarsi con una scelta e movimento, non essere stunlockato da 3 attacchi consecutivi. Tasto V = colpo con calcio dell'arma/spallata breve con **vera animazione FPS e 3P**; se armato, mano/arma non esce dai grip in modo assurdo.

- Range **1,6m**, cono **65°**, massimo **1 zombie normale** valido; cooldown **12s** (seed). Windup 0,18s, active 0,14s, recovery 0,35s. Weapon Fire lock durante azione; ammo e reload non duplicati.
- Walker: spinta indietro breve **0,6m** oppure stagger **0,5s**, mai entrambi cumulabili per exploit. Runner: interrompe lunge solo **se è ancora in windup**, non dopo hit già applicato. Armored: reagisce con suono metallico ma **non** subisce knockback; Saboteur: light flinch non infinito; Boss immune.
- Non è attacco farming: danno zero o minimo configurato **senza ricompensa kill**, non resetta automaticamente headshot. Il server decide bersaglio, stun window e cooldown; client mostra immediato preview cosmesi, niente client-only damage.
- FX/SFX: animazione shove vera, whoosh corto, carne/armatura differenziati, breath/grunt, crosshair cambia per cooldown. Non aggiungere 4 mosse melee, dodge/dash e skill tree alla 1.0.
- Implementazione: animazione + input L2 se fucile già introdotto, interaction su Nurse L3; COMPLETO solo quando entrambi hanno grip/hit/stagger e rete coerenti, QA L3. Non dichiarare L2 incompleto se l'impatto zombie non esiste ancora: chiudere anim/invocation L2, effect on zombie L3.

## 2. CLASSE Q: UN'ATTIVA E UNA PASSIVA, SINERGIA VISIBILE

Mantenere personaggi e classi del doc 23: non cambiare i tre nomi né i cooldown senza prova.

| Classe | Q attiva definita | Passiva | Coinvolgimento tattico |
| --- | --- | --- | --- |
| **Assaltatore** | **Sfondamento**: per 6s proiettili colpiscono meglio l'armatura (+15% perforazione, -25% spread seed), animazione arma/FX sottile; CD 45s | -10% rinculo AR/SMG | il player abbatte corazzato/saboteur marcato e libera il campo della sentry |
| **Ingegnere** | **Ripristino**: ripara fino 15% HP di UNA struttura (core/sentry/barricata) entro 8m; **solo se target sentry valido** aggiunge +15% cadenza per 4s, senza creare energia o colpi gratis; CD 55s | +20% riparazione standard (stesso costo) | riattiva temporaneamente la sentry nel fronte in crisi, mentre gli altri sparano |
| **Soccorritore** | **Impulso medico**: entro 8m cura 25HP per player Alive, e mette **in pausa bleedout per 4s** a Downed (NON revive istantaneo); CD 50s | -25% durata revive manuale | protegge la squadra che raggiunge Nucleo sotto assalto, senza eliminare rischio |

**Sovrapposizione:** l'Impulso del Nucleo NON cura player, la skill Ingegnere NON rinnova l'uso del Protocollo; l'Assaltatore non potenzia direttamente DPS tower; il Soccorritore non può salvare un Nucleo morto. Il target del Q Ingegnere va scelto con crosshair, non un menu. Se nessun target valido/nessuno ferito, no cooldown consumato e UI “bersaglio non valido”.

## 3. PLAYER ↔ SENTRY: MARCATURA TATTICA

**Input:** middle-click su zombie visibile, entro range visivo ragionevole; mostra icona sopra il target e ping ai compagni. Una sola marcatura attiva per squadra, **durata 5s**. Ogni player ha cooldown locale server-authoritative di **8s**; nuova marcatura valida sovrascrive l'ultima (niente stacking).

**Effetto:** sentry che già vede quel nemico con LoS e range regolari **lo mette in cima alla lista priorità**, non riceve danni extra, headshot “automatici” o mira attraverso muri. Se il target è immune/irraggiungibile, morto o dietro muro, ripristina normale AI di targeting. Il ping resta utile senza sentry (info compagni).

**Valore:** si può puntare il Saboteur prima che disabiliti una torre, oppure coordinare focus fuoco Runner. Non concede a un player un potere di comando totalizzante: no RTS selection, no ping wheel a 8 opzioni, no tower control direzionale manuale.

**Tecnica:** `TeamFocusTargetId` in GameState, `MarkedUntilServerTime`; replica piccola, target valido e server trace/range. No ping spam: rate limit e cooldown. All'uscita/distruzione tower o zombie, cleanup. La sentry rimane conforme al docs/22; upgrade targeting e comando condividono solo policy, non danni.

## 4. CITY ABILITY: UN PROTOCOLLO DEL NUCLEO UNA VOLTA PER ONDATA

**Nome:** **IMPULSO DI CONTENIMENTO**. Disponibile acquistando il Nucleo T2; attivazione al pannello accanto al Nucleo con E (interazione contestuale), consumo **1 uso per wave condiviso in 1–4 giocatori**, ricarica **solo all'inizio della wave successiva** (non a tempo, non con crediti). Serve come pulsante di emergenza difensivo, NON torretta gratuita.

- Dopo conferma server, il Nucleo emette un **cerchio elettrico di 12m** (seed) intorno al Core. Normali Walker/Runner/Saboteur nell'area **rallentano del 40% per 5s** (seed); Armored rallentati max 15%, Boss max 10%, nessuno stoppato a zero. Non infligge danno, non interrompe boss, non apre/chiude porte e non modifica NavMesh.
- Il player deve raggiungere il pannello; in co-op ogni player Alive può attivarlo, il primo acquista lo stato `used` server. UI visibile a tutti “Protocollo disponibile/usato”. Per evitare grief non si perde un uso se non ci sono bersagli nel raggio (mostrare unavailable); in 1p nessuna votazione. In coop un'azione rapida è più sensata di un voto durante combattimento.
- Visual: sirena rossa breve, ring luminoso sulla strada, lampade Nucleo pulsanti, suono elettrico spazializzato; zombie con VFX shock leggero, anim walk speed coerente e niente micro-teleport. Tutto visibile a host/client e mai doppio FX.
- **T3** sceglie **UNA sola modifica definitiva per la run** durante la Prep, non due poteri simultanei: (A) **Portata** = raggio 16m invece di 12; oppure (B) **Ripristino** = dopo il pulse, Nucleo recupera **fino al 10% MaxHP**, senza full heal né ripristino dopo sconfitta. Le due opzioni sono esclusive: collegare alla vecchia scelta “difesa vs riparazione” già nel doc 22, non aggiungere nuova UI di talenti.
- Il danno/tier HP normale del Core rimane indipendente: T1 corazza, T2 rete e impulso, T3 scelta Portata/Ripristino. Zero nuove valute e cooldown bar complicate.

**Contromosse e anti-sfruttamento:** non influenza zombie fuori 12m, nessun bonus torre DPS, solo 1/wave e nessuna ripetizione per join/leave/reset. Se premuto esattamente durante phase transition, il server assegna l'uso alla wave effettiva una sola volta. Il Boss mantiene la sfida; server-authoritative area query bounded. Il raggio non cresce con player count.

## 5. CITY PASSIVES: APRI ZONE PER VANTAGGI + NUOVI RISCHI

Ogni settore ha **UNA utilità permanente della città nella run**, passiva o contestuale a servizi già esistenti, **non una quarta skill Q**. Il costo è già TF per apertura, non una nuova valuta. Il vantaggio deve essere disponibile in solo e in coop e deve compensare l'aumento di fronti.

| Settore aperto | Utilità della città | Valore seed | Rischio e fairness |
| --- | --- | --- | --- |
| S0 Cortile (inizio) | riparazione Core e banco arma normali; protocollo del Nucleo dal T2 | una attiva/wave | 2 direzioni attive |
| S1 Officina (offerta dopo W3) | **Banco di manutenzione**: munizioni acquistate da quel banco costano **15% meno PC** | -15% solo per refill, rounding integer | apre 1 nuovo varco est dalla wave successiva; sblocco non obbligatorio |
| S2 Deposito (offerta dopo W6) | **Scorte rinforzo**: riparazioni barricate costano **15% meno TF** (non core/sentry) | -15% rounded integer | apre un secondo nuovo fronte e più socket |
| S3 Tetti (offerta dopo W8) | **Faro tattico**: durante i primi 6s di ogni ondata, evidenzia **direzione** del primo nemico speciale in S3, non lo vede attraverso interi edifici | warning informativo, no damage | accesso alto/route Runner e varco successivo |

Non vendere l'espansione come “+10% più FPS” invisibile. Mostrare prima di comprare: `VANTAGGIO / NUOVO INGRESSO / COSTO` con colori + icone e direzioni sulla mappa. Chi non apre S1 non perde l'abilità Q o l'unica via per vincere. Il numero di zombie complessivo **NON** cresce solo perché hai aperto una zona: il director ridistribuisce il budget tra ingressi attivi.

## 6. WAVE TWIST: UNA CRISI LEGGERA, NON UN SISTEMA ROGUELIKE NUOVO

Solo dopo che 10 ondate base funzionano. A **wave 7** introdurre UNA “crisi di rete” preannunciata 5 secondi prima: una torretta attiva viene **disalimentata per max 8s**; il team può riattivarla anticipatamente con il Q dell'Ingegnere **oppure** con 3s di interazione E al pannello della torre (quindi solo/assaltatore/medico possono affrontarla). Saboteur può già disabilitare torri: riusare precisamente gli stessi stati/network/VFX di disabilitazione. Sulla W7 NIENTE più zombie extra, niente perdita valuta, niente improvvise nuove rig. Se non esiste alcuna sentry, il twist è sostituito da un normale preavviso di fronti (nessuna torre fake da disabilitare).

**No deck random** e nessuna modificazione segreta permanente. La crisi si può evitare/risolvere dal player, non dal menu. Testare che W7 non sia impossibile per 1p o troppo facile per 4p.

## 7. SYNERGY MAP — COME LE SKILL SI INCROCANO

| Momento | Giocatore | Città/Difesa | Risultato desiderato |
| --- | --- | --- | --- |
| Runner ti raggiunge durante reload | V spinta 1 nemico | barricata prende pressione in varco | hai 1 secondo per muoverti, non invisibilità |
| Saboteur corre verso torretta | ping middle mouse sul target | sentry lo priorizza se vede target | tiro e torre cooperano, no tower wallhack |
| Molti Walker spingono sulla sentry | Ingegnere Q ripara/sovralimenta | sentry recupera e guadagna tempo | il player deve rimanere vicino esponendosi |
| Armored arriva a metà ondata | Assault Q armor pen | slowfield rallenta corridoio | il player decide di colpire weakpoint |
| Due compagni downed vicino core | Medic Q rallenta bleedout e cura vivi | Nucleo pulse rallenta il gruppo zombie | si tenta il revive senza full heal automatico |
| Core sotto 30% HP in W10 | player torna al pannello e usa E una volta | Tier3 Ripristino oppure Portata, non entrambi | momento drammatico scelto, non win button |
| Apri Officina W3 | rifornimenti PC meno cari | nuovo fronte W4, una piazzola nuova | scelta rischio-beneficio reale |
| Apri Deposito W6 | repair barricade più economico | nuova route attack | investire città non è solo decorazione |
| Apri Tetti W8 | warning speciale più precoce | esponi route alta | information vs geography risk |

**La sensazione ideale:** stiamo sparando perché solo le armi dei giocatori risolvono gli elite; le difese tengono linee, il Nucleo compra tempo una volta per wave, i settori migliorano la base mentre aggiungono rischio.

## 8. CONTRACT TECNICO PER CODEX — niente sistemi paralleli

- `PlayerAbilityDefinition`: per V universal, Q class selected; state/cooldown replicated; animation montage + owner/local feedback, server hit/cast validate, no parallel second ability system.
- `TeamMarkTarget`: rep state in GameState, set owner validated line of sight, expiry, focus policy in EXISTING sentry target selector, never direct extra damage.
- `CoreProtocolDefinition`: enum None/Containment, tier unlock, usedWaveIndex, base radius and slow spec; one server-wide activation; change T3 enum RANGE/REPAIR; reuse `ZDBaseCore` and existing slow status from Slowfield (do not code two debuff engines).
- `SectorBenefitId` attached to existing `SectorDefinition`; lookup at purchase/refill or barricade repair, and callout on WaveState change. No new inventory/power currency.
- `SpecialWaveEvent` at W7 implemented as Data-driven event referencing Sentry `Disabled` state, with no additional actor, repair via existing E interaction.
- Use source-owned DataAssets and GUID/TxnId, anti double reward. Mark, pulse, class abilities, zone passive **must show state** in UI and remote client; no fake icons.
- No script/class signatures assumed to exist: these are *behavioral contracts* and must map to real code when each milestone is reached.

## 9. Scope / time budgeting

The above modifies **existing tasks**: ZD-011/014/017 (player+weapon shove anim), ZD-019/021/022/024 (zombie response), ZD-040/044 (mark + sentry), ZD-048/050 (Core protocol Tier2/3), ZD-051–055 (city benefits), ZD-057–059/061 (class skills), ZD-069 (W7 wave event), ZD-071/072 (HUD/input). Do not create another massive system or extend 80 task queue without formal approval. All new abilities must satisfy [29](29_ANIMATION_AUDIO_VFX.md) media requirements.

## 10. Anti complexity — RIFIUTATO PER V1

- No stamina+mana+powerup meter combo; only existing PC/TF economy.
- No perk trees, rune sockets, random cards every round, loot rarity drops.
- No dodge/dash/parkour independent system, wallrunning, hookshot, grappling gun.
- No 4 active skills per hero or explosive ultimates covering entire map.
- No city simulation with citizens/workers/traffic, no generator-factory, no long menus.
- No freeform building walls and path manipulation: only authored pads.
- No screen full of skill icons: ammo+HP+one Q+one V+one team Core-ready indicator.
- No huge boss roster or 20 tower types, one full game first.

## 11. Quality gate per mechanic

A mechanic is DONE when animation+audio+VFX+UI+damage/cooldown/network+edge cases+packaged build are observed; each must have **one gameplay clip** of use, one invalid-action rejection, 2 player synchronization where applicable; boss/armored immune cases checked. The design lock does NOT claim the code or assets exist already.
