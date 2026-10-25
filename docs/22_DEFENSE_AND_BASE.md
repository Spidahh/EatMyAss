# HUB + BASE AUTODIFENSIVA V2

**Regola primaria:** le torrette non sono “supporto al player che presidia il Nucleo”. Sono **difesa principale autonoma**: possono respingere da sole un intero assalto adeguato al loro tier mentre il player combatte altrove. Questa versione annulla il vecchio potere E manuale e il campo slow da piazzare della V1.1.

**Interno**: Armeria (armi, equip e upgrade), Difese (socket/perimetro/turret tier), Comando (Core HP/tier/energia-capacità/minaccia), Specializzazione (Tiratore/Spezzatore/Tecnico). Entrata/uscita fisica, upgrade durante l'ondata ma nessun nemico e nessun combattimento nell'interno. **Esterno perimetro**: Nucleo e fortificazioni visibili e danneggiabili, user può osservare la propria torre sparare.

**Tre difese**: barricata/portone con HP e repair; torretta rapida anti-Walker/Runner con heat/range; torretta pesante anti-Armored/Bruto con slow heavy rounds. Le torri cercano automaticamente bersagli Siege secondo posizione/LoS/threat score, sparano anche con player a chilometri e colpiscono con la stessa damage API di armi. I socket sono prefab selezionabili soltanto dal terminale, no freeform nav blocking. Max tower budget power dal Core, non consuma una valuta secondaria o ammo manuale.

**Core T0–3**: T1 +fortificazione HP; T2 potenza e auto shockwave a HP<35% una volta/stadio; T3 scegliere più portata o breve automatic repair quando trigger (non entrambe). Non occorre il player per attivare l'emergenza. Non diventa invulnerabile. CoreHP 0 = sconfitta con checkpoint. Costi tutti in Rottami.

**Upgrade visibili**: ogni torre ha mesh e materiali/turret barrels/anim states, FX e SFX di tier. DPS e capacità misurate contro le composizioni. Mostrare grafico sintetico Copertura vs Minaccia nel Comando, senza promessa di sicurezza matematica. Una base sufficientemente aggiornata vince W3 auto; lasciata al tier W3 fino a W7 subisce pressione da armatura/sabotatori. Non usare il player presente come moltiplicatore invisibile.

**Coop/cheat**: spesa ledger idempotente, host stato, server validation; due player non costruiscono due torri sulla stessa piazzola, player fuori non apre terminale shop, power cap e tiers validi. Vedi [43](43_AUTONOMOUS_BASE.md) per logica dettagliata, policy damage e save.
