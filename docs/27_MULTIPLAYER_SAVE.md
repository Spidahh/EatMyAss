# MULTIPLAYER E SAVE V2 — BASE CHE CONTINUA, HOST PERSISTENTE

**Windows 1p offline e co-op listen-host fino a 4 quando realmente verificato** su HordeTemplate; niente server cloud o account esterni promessi. Il mondo/BASE appartiene a host. Tutti i player possono essere FUORI in combattimento o DENTRO in upgrade; questo non spegne le torri. Con client lontani dall'AI base, AI/damage/spawn rimangono autorevoli server, il sistema di relevancy replica i cambi di stato ai client senza disattivarli.

## Dati server e compatibilità
`BaseSaveId, Stage, Mode(Waves|Continuous), CoreHP, TowerSockets, TowerTiers, WallHP, PowerCap, RottamiWallet, ClassChoices, WeaponUnlocks, WavePressureState` gestiti da server/host, inviati ai client. Player input requests equip, shoot, parry, abilities, upgrade con validazioni; no client HP/kill/tower authority. Spawn identity e kill event IDs unici, nessun doppio award o bilancio negativo.

## Save persistente
Host solo/coop salva checkpoint quando compra upgrade, termina stadio, esce volontariamente in prep; schema versionato e checksum atomico (scrivere temp, flush, rename, backup) e journal `TxnId`. Se host interrompe durante wave, riprende da ultimo checkpoint stabile **inizio stadio** con tower/risorse coerenti; non recuperare da client un saldo non registrato. Non salviamo nemici in posizione esatta durante fighting. A programma CHIUSO non continua assedio né auto mining.

## Co-op e player death
Ospite rientra in base dopo morte/10s seed, server rimane attivo; gli altri combattono e torri operano. Downed temporaneo e revive manuale universale, non Medic class. A host quit interrompere simulazione e tornare menu, non continuare timer client. Reconnect mid siege non promesso se il framework non lo supporta; informare in UI. Base/risorse sono host world, ospiti non ottengono copie permanenti del mondo.

## Purchases
Solo terminali **DENTRO** base attivano server spend; in coop acquisti grandi richiedono confirmation vote o host policy esplicita, non carta bianca ai client. Il wallet è uno solo Rottami, non PC/TF. Le torrette respingono zombie anche con host avatar KO; solo host server devono continuare thread AI.

## QA
1p entra/ esce/ combatte/ compra in wave, 2p uno fuori e uno dentro, 4p tutti fuori → base difende per 2 minuti, 4p tutti dentro → core subisce/torri sparano, host crash checkpoint rollback, due upgrade simultanei, perdita internet, no doppie transazioni. Misurare CPU/network quando torrette combattendo nessun client guardando.
