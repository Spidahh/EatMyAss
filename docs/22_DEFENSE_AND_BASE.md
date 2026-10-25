# SISTEMA DIFENSIVO, NUCLEO, TORRETTE E COSTRUZIONE

## Contratto giocabile

Il **Nucleo** è la condizione di sopravvivenza e il fulcro visuale. Il giocatore in FPS può comprare strutture su **piazzole determinate dal level design** (non piazzamento libero), orientare dove permesso, ripararle, potenziarle e proteggerle. Gli zombie possono attaccare le difese, aggirarle o sabotarle. Le sentry aiutano su un fronte ma NON giocano al posto del player. Il sistema arriva solo dopo fucile+zombie perfetti, ma deve essere costruito interamente, una difesa per volta.

## Nucleo (L6) — completo

`ZDBaseCore` proposta: `CoreId`, `HP/MaxHP`, `Tier 0–3`, `PowerCapacity`, `PowerUsed`, `State Normal/Damaged/Critical/Destroyed`, `CoreRepairPolicy`, `LinkedSectors`; server authority e replicazione. Seed HP max base 3000 per 1 player, scala via difficoltà co-op controllata (non moltiplicare x4 automaticamente). Segnali: tre stati mesh/materiale, luce/sirena, HUD vita, colpo metallo/power damage. HP0 ⇒ fine partita UNA volta.

**Upgrade Nucleo:**
- T1 Fortificazione: +25% MaxHP e componenti di riparo visibili, aggiorna HP secondo regola esplicita (mantenere percentuale attuale, non full heal gratuito).
- T2 Rete: +2 PowerCapacity seed, attiva una piazzola extra preesistente; feedback elettrico e linea di potenza leggibile.
- T3 Comando: migliora velocità riparazione base **oppure** riserva di emergenza; una scelta singola durante la run (non entrambe).
Riparare HP usando fondi team, con cap, costo per punto riparato e preview; mai oltre MaxHP. Power è capacità, **non terza valuta**.

## Piazzola di costruzione

`SocketId` unico in mappa/settore; `AllowedDefenseTags`, `SectorRequired`, `Powered`, `OccupiedActorId`, `BuildTransform`, `FacingArc`, `PreviewBounds`. Predisposizione per 2 torrette per settore, una barricata per varco, slowfield su socket apposito; non consentire chiusura della NavMesh. Client preview verde/rosso e costo prima di conferma. RPC `ServerRequestBuild(SocketId, DefenseId, TxnId)` verifica socket disponibile/settore aperto/Prep/fondi/cap/energia, riserva e crea actor, registra transazione idempotente e replica. Se spawn fallisce rollback totale. Richiesta simultanea => una sola struttura.

## Catalogo delle difese 1.0

| ID | Acquisto, funzione | Upgrade T1 / T2 | Debolezza/controgioco | Asset |
| --- | --- | --- | --- | --- |
| D_BARRICADE | rallenta zombie al varco e prende danno | +HP / rinforzo contro breaker | Runner la aggira se c'è percorso, Armored la distrugge | modello barricata metal/wood coerente **DA APPROVARE**, non box |
| D_SENTRY | target walker/runner entro arco, fuoco con LoS | +range / policy anti-runner | overheats, power limit, sabotatore e boss | [Sci-fi turret](https://www.fab.com/listings/4abb6121-4d71-4b67-8e61-b83b7b3e2d10) come **candidato artistico non approvato**; serve look industriale |
| D_SLOW | area rallentamento con intervalli | +radius / +uptime limit | armatura/boss parzialmente resistenti | mesh/FX coerenti **DA PRODURRE/APPROVARE**, non dischetto invisibile |

**Scelte fissate:** nessuna torretta missilistica, no mortaio, niente mine antiuomo random, no costruzione libera, niente produzione passiva di risorse o crafting. Sentry ha stato `Idle/Acquire/Track/Fire/Cooldown/OutOfPower/Damaged/Destroyed`, yaw/pitch limiti reali, muzzle flash/scia e suono, rifrazione antenna/servomotore, hit surfaces, projectile policy unica (preferire codice weapon condiviso). Line of sight ogni fire confirmation. Target policy prioritize Runner/Saboteur configurabile. Nessun shot attraversa muro.

## Interazione e manutenzione

Player in area e guarda socket → `[E] Build/Repair/Upgrade`, UI con prezzo e delta reali, spenti se insufficient funds. In wave si può riparare in modalità emergenza a costo aumentato e con animazione che espone a rischio, ma build e tier upgrades solo in prep; parametro configurabile unico. Demolire? **Escluso 1.0** per impedire refund exploit; struttura distrutta libera socket, sostituire alla prep successiva. Nessuna riallocazione punti a piacere.

## Energia, torrette e collaborazione

La potenza è una capacità globale di base; più torri accese consumano slot power, T2 lo espande. All'assenza energia si spegne solo dispositivo più nuovo secondo ordine stabile, la UI avvisa prima dell'acquisto che non può alimentarlo. Gli upgrade non devono invalidare una difesa già comprata senza spiegazione; perciò controllare power budget prima di confermare. In co-op i fondi sono condivisi, **acquisti costosi sopra soglia** richiedono voto/squad approval semplice nella Prep, con timeout chiaro; host non riceve poteri economici speciali. In solo nessun voto.

## Balance seed

Barricata 100 fondi, riparazione fino al massimo 45, sentry 220, sentry T1 160, slowfield 180, core T1 240, T2 380, T3 550. Sono gli stessi seed di `10_ECONOMY_SEED.csv`. Ogni ricompensa e costo deve essere simulato con la distribuzione wave 1–10 prima di congelare bilanciamento; non usare prezzi già validati nella UI.

## Test di accettazione

Core si danneggia e muore una volta, no overrepair; AI attacca barricata senza softlock; sentry colpisce solo visibile nel cono e dà reward corretto, non può uccidere boss AFK; build parallel da 2 client costa 1 volta; annullamento/no fondi no spawn no addebito; materiali/upgrade/animazioni/audio/effetti mutano visibilmente; settore chiuso nessun socket build; no potenza no acquisto bug; player può vincere senza tower abuse. Se un pezzo visual/audio manca, lo strato non è completo.
