# IA ZOMBIE V2 — ASSALTATORI DI BASE VS ESTERNI

## I cinque archetipi reali

1. **Walker (Nurse)**: unità base; cammina, attacca player esterno o barricata in assedio; animazioni idle/walk/alert/strike/hit/death.
2. **Runner**: veloce, aggira, pressa chi usa un fucile lento, può sfruttare percorsi verso perimetro; windup leggibile.
3. **Armored**: resistente alle armi automatiche leggere, vulnerabile alle heavy turret e mazza ben temporizzata, attacca portoni.
4. **Saboteur**: mira alle torrette e può spegnerle temporaneamente con attacco VISIBILE, player esterno può intercettarlo; effetto non è hack invisibile.
5. **Bruto/Boss**: milestone stage10, HP alti, telegraph, 2 attacchi fisici e armor weakpoint; **può morire anche per sola base sufficientemente potenziata**, nessuna immunità sceneggiata.

**Richiamo/Capobranco** è un *ruolo evento* riusando Walker/Runner con behavior, SFX e marker, non sesto 3D zombie. La rimozione fuori riduce un poco pressione futura, non azzera invasione. Zombie non possono apparire nell'interno upgrade. Si ripartisce budget between campo e perimetro nel solo director.

## State machine comune

`Spawn → SelectRole(Siege/Field) → AcquireTarget → Path → Telegraph → AttackWindow → Recovery → HitReact/StaggerCooldown → Dying → Cleanup`. AI server, perception, LoS, fair melee/ranged hit windows. Se l'avatar è entrato dentro base, un Field zombie non teletrasporta dietro l'hub; può ritarget su periferia oppure despaunare secondo director senza reward. Siege zombie sceglie gate/core/turret validi, non segue player all'infinito fuori mappa.

## Richieste di animazioni
Per ogni tipo: locomozione vera della sua velocità (runner non walk speed x3), attack telegraph/active/recovery con differenziazione tipo nemico, hit reactions e death, footstep/scream/blood, remote replication. Perfect parry contro normali: finestra e stumble con cooldown per evitare perma-stun. Heavy hit contro armored: clang/break per alcuni colpi misurati. Boss telegraph compatibile con melee-only Spezzatore.

## Danno dalla torretta

Correggere l'assunzione upstream su `DamageCauser` di tipo `ACharacter`: `KillAI` deve dipendere da Health<=0 e idempotenza, non dal fatto che ad uccidere sia player. Team reward diverso per tower kills ma zombie eliminato comunque. Zero phantom alive e zero doppio premio.

## QA
Due gruppi di zombie attivi contemporaneamente: player lontano fuori combatte i Field, base da sola abbatte Siege. AI/torri devono aggiornare anche quando nessun giocatore è vicino; ragdoll cleanup server. Con 20+ zombie misurare performance reale. Vedi [43](43_AUTONOMOUS_BASE.md).
