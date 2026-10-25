> **ARCHIVIATO / NON ESEGUIRE — 25/10/2026 (V2):** questo file contiene decisioni storiche e può contraddire l'attuale Zombie Defence. **Vietato usarlo per definire loop, classi, torrette, city-map, soldi, skill o task.** Il committente ha richiesto **BASE INTERNA PER UPGRADE + BASE AUTODIFENSIVA + FPS/MELEE FUORI**, progressione persistente e Rottami moneta unica. Usare esclusivamente [AGENTS.md](../AGENTS.md), [41_CANONICAL_GAME_V2.md](41_CANONICAL_GAME_V2.md), [42 melee](42_MELEE_SKILLS_AND_SPECIALIZATIONS.md), [43 base](43_AUTONOMOUS_BASE.md), [44 esterno](44_OUTSIDE_COMBAT_AND_PROGRESSION.md) e il [backlog V2](33_FULL_BACKLOG.csv). Questo documento è conservato SOLO a fini storici/riuso di dettagli tecnici non incompatibili.

# ASSET LOCK — MATERIALI REALI DA USARE, NO SCELTE CASUALI

**Regola:** gli asset qui sono selezionati per la prima fase. Questo file prevale sul vecchio catalogo a 26 voci, che rimane una lista di risorse future. Codex non deve sostituirli senza aver accertato un impedimento reale e averlo documentato. **Tutti i prezzi sono “Free” visti sulla scheda web, non download già effettuati.**

| Ordine | Tipo | Asset selezionato / link | Fonte e condizioni dichiarate | Ruolo |
| --- | --- | --- | --- | --- |
| 1 | Base codice | [HordeTemplate V2 Native](https://github.com/DasBander/HordeTemplate) | GitHub, licenza MIT del repository, Engine 5.8 in .uproject | game framework reale, player controller, firing, inventory, zombie AI, game state |
| 2 | Personaggio | [Survival Character](https://www.fab.com/listings/11d20d01-b764-4936-8163-cb20d05c369e) (Arberry) | Fab Free, Epic Skeleton UE5.1, abiti modulari, 8K textures disponibili, flag NoAI | avatar umano finale |
| 3 | Locomozione | [Game Animation Sample](https://dev.epicgames.com/documentation/unreal-engine/game-animation-sample-project-in-unreal-engine) (Epic) | progetto Epic scaricabile tramite canali ufficiali; controllare licenza del contenuto | animazioni di movimento reali da migrare/retarget |
| 4 | Arma | [FPS Weapon Bundle](https://www.fab.com/listings/8aeb9c48-b404-4dcd-9e56-1d0ecedba7f5) (Deadghost Interactive) | Fab Free, 7 armi e 4 attachment, riggate; **non** promette animazioni complete | selezionare un singolo AR reale e sviluppare tutto il gunplay |
| 5 | Zombie | [Zombie Female: Nurse](https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc) (RamsterZ) | Fab Free, idle/walk/attack, UE5 skeleton, niente AI, flag NoAI | primo zombie finale |
| 6 | Animazioni zombie | [Zombie Animation Pack: Standard](https://www.fab.com/listings/82b55c77-c706-4634-839e-29ba827dac8d) (QuokkaVoid) | Fab Free, 50 clip dichiarate, compatibilità dichiarata UE4/UE5, flag NoAI | completare azioni effettivamente presenti nel pack |
| 7 | Ambientazione (più avanti) | [Factory Environment Collection](https://www.fab.com/listings/2ee66462-8c2b-4303-892c-83f7fc0d9b3e) (Denys Rutkovskyi) | Fab Free dichiarato | kit industriale per primo isolato cittadino |
| 8 | SFX UI (più avanti) | [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds) | CC0 dichiarata | UI quando esisterà il relativo gameplay |

### Anima prima, tecnica durante, finitura nello stesso strato

L'asset non è “usato” perché la sua pagina è linkata. Prima va acquisito sull'account autorizzato, messo in un progetto privato, importato, retargetato, collegato alle classi vere, visto in game con luci reali, ascoltato con audio appropriato. **Non preparare dieci pack in anticipo; importare solo ciò che lo strato L1/L2/L3 necessita.**

### Licenze e repository pubblico (non negoziabile)

- Fab Standard License permette normalmente usare/modificare/distribuire asset **incorporati** in un gioco; non consente la redistribuzione autonoma di mesh/animazioni/suoni. Questo repository GitHub è **pubblico**: non caricare qui gli asset Fab/Epic raw. Conservare link, manifest, note di import e script idempotenti nel repository; binari e ricevute in workspace PRIVATO con accesso autorizzato.
- Fab NoAI significa **non usare contenuti per raccolta dati destinata a IA generativa**; non usare gli asset come training dataset, non mandarli a servizi generativi per ricavarne asset nuovi. Consultare licenze specifiche prima di qualsiasi altra manipolazione.
- Un modello riggato non significa animazioni complete. Le 3 animazioni Nurse **non coprono** corsa/danno/morte; il weapon rig di Deadghost non garantisce reload hands. Questi sono compiti L2/L3, non sorprese finali.
- Per HordeTemplate, MIT è chiaramente indicata per il repository, ma vecchi contenuti Marketplace, suoni e mannequin richiedono attenzione alle relative licenze; evitare trasferire il pacchetto binario nel pubblico finché non si sa cosa è redistribuibile. Conservare LICENSE.md e avvisi copyright del codice usato.
- Non usare un asset UEFN Reference Only per un prodotto Unreal stand-alone senza diritto specifico.
- Quando un link richiede login/claim in Fab, il proprietario accede tramite Epic/Fab autorizzato. Codex non aggira login o paywall e non finge di aver acquisito l'asset.

### Formato manifest di acquisizione richiesto

Per ciascuno: nome reale + listing URL + publisher + data + licenza concreta + flag NoAI + versione UE dichiarata + file ricevuti + SHA/manifest + skeleton + AnimationSequences presenti + animation retarget mappings + percorso locale privato + test in-game + stati APPROVED/BLOCKED. Un nuovo asset non può essere sostituito silenziosamente a un altro.

### Se qualcosa manca

1. Leggi descrizione e contenuto scaricato: mancato download non equivale a bug di Unreal.
2. Se manca un'animazione, realizzala con Control Rig / Sequencer / keyframes e strumenti gratuiti nel rispetto della licenza oppure scegli fonte free **documentata prima dell'uso**; niente gesture inventate via rotazione casuale.
3. Se il pack non è scaricabile o non è utilizzabile legalmente, indica BLOCKED, il link, la ragione e una sola alternativa seria a zero euro; non introdurre modelli cartoon o mannequin spacciandoli per finali.

Riferimenti licenze: https://www.fab.com/eula e https://dev.epicgames.com/documentation/fab/licenses-and-pricing-in-fab .
