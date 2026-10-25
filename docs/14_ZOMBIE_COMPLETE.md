# L3 — SPECIFICA DI PRODUZIONE: LA PRIMA ZOMBIE DEVE ESSERE COMPLETA

## Un solo zombie, modello stabilito

**Zombie Female: Nurse** di RamsterZ, https://www.fab.com/listings/35246f73-70ca-41ac-816b-55ead87dbcbc . La pagina dichiara **solo tre animazioni**: Idle, Walk Forward, Attack Forward. NON include AI Blueprint. Scheletro basato su UE5 mannequin. Nessun sistema di combattimento pronto è incluso: l'AI verrà da HordeTemplate, rifinita in funzione del modello.

Per gli stati mancanti, prima fonte aggiuntiva il pack free **Zombie Animation Pack: Standard** (QuokkaVoid), https://www.fab.com/listings/82b55c77-c706-4634-839e-29ba827dac8d ; 50 clip dichiarati, non sappiamo se ognuno degli stati seguenti sia presente. Ispezionare e retargetare; eventuali clip specifiche non disponibili vanno prodotte come animazioni vere/derivate correttamente nel tool Unreal senza nuove spese, oppure BLOCKED. Non sostituire Nurse con mannequin senza avviso.

## Animation state machine definitiva del primo archetipo

| Stato | Comportamento | Qualità minima |
| --- | --- | --- |
| Idle | respiro, microvariazioni, ascolto | niente ciclo visibilmente a scatto |
| Detect/alert | percepisce giocatore, orienta corpo/testa, vocalizzazione | chiamata visiva/sonora leggibile |
| Walk chase | insegue e curva secondo NavMesh | piedi non slittano; blending turn |
| Accelerate / chase burst | breve accelerazione se archetipo lo richiede | niente teletrasporto velocità |
| Obstacle / door | se bloccata da porta/struttura, cerca route o attacca target autorizzato | mai ferma in parete 30s |
| Attack wind-up | prepara attacco chiaramente leggibile | durata configurabile e intervallo umano |
| Attack active | collisione hit solo durante notify finestra | un solo evento danno per swing e target |
| Recovery | termina animazione prima del prossimo attacco | no spam impossibile da evitare |
| Hit light | flinch upper body senza interrompere ogni volta | no permastun da AR |
| Hit heavy | breve stagger solo oltre soglia e cooldown | non annulla sistematicamente ogni attacco |
| Head hit | FX/hit marker su bone vero, moltiplicatore configurabile | no “headshot = sempre kill” su tutti futuri archetipi |
| Death | death montage reale → ragdoll controllato o posa persistente breve | no T pose, corpo non esplode in fisica |
| Despawn | dissolvenza/cleanup fuori vista quando opportuno | non sparisce in faccia al giocatore |

**I nomi sono stati di gioco da implementare, non un elenco garantito di clip presenti sul pack.** Retarget pose e match del root su rig Nurse controllati a vista e audio.

## AI e damage

Base da riusare: `AZedPawn` + `AZedAIController`, classi reali in HordeTemplate. Non implementare un secondo controller completo senza motivo. La prima Nurse deve:
- spawnare in un'area definita della città, camminare senza urtare le pareti, rilevare player solo con percezione e range coerenti;
- cambiare target, seguire le curve, rallentare presso il giocatore, raggiungere distanza di attacco effettiva;
- durante windup e active far partire e fermare la collisione via notifies/server; player può schivare allontanandosi o rompendo la linea di attacco;
- subire danni da arma con hitbox testa/torso/arti, HP veri, comunicazione impatti per remote player;
- morire una sola volta, cancellare gli attacchi, assegnare punti correttamente e rilasciare nav occupancy; nessun zombie a 0 HP che resta vivo;
- mantenere un contratto di danno neutro rispetto al killer, perché in futuro la uccideranno torrette, trappole e altre entità non Character.

**Bug specifico da prevenire già ora:** nella sorgente originale `ZedPawn::TakeDamage` richiama `KillAI` nel ramo letale solo se `DamageCauser` diventa `ACharacter`. Riscrivere **in modo circoscritto** l'attribuzione di death/credit nella prima integrazione, senza dare premi duplicati. Iniziare correttamente non significa costruire subito una torretta.

## Reazioni e sound design

- Diversificare idle groans, detection bark, breathing chase, shuffle footsteps, hit grunt leggero/pesante, swing whoosh, impact player, death vocalization, ragdoll body drop.
- Mix audio spazializzato; evitare clip in loop udibili a grande distanza o tripla riproduzione in co-op.
- Effetto sangue e microparticelle per tipo di superficie e forza, niente geyser per ogni proiettile; impatti faccia diversi dal torso quando mesh/effetti lo consentono.
- Hit reaction con fisicità del torso/testa e ragdoll controllata, ma non distruggere precisione delle hitbox.
- Stato hurt/death visibile sia al giocatore locale sia al client remoto.

## Scena dimostrabile prima di procedere

In un isolato urbano percorri, giri un angolo, senti lo zombie, lo avvisti, lo attiri, lo colpisci ripetutamente con l'AR, lo interrompi solo se colpo potente, lo lasci attaccare, subisci HP, poi headshot e morte pulita. Ripeti 10 volte con distanze e azioni diverse, con 2 client. Documenta clip effettive, retarget, origin di ogni audio, bug residui. **Non creare altri zombie** finché questa esperienza non è convincente e completa.

## Done

Tutti gli stati obbligatori coperti con vere animazioni/transizioni, audio e VFX; danni e attribuzioni corretti; niente corpse softlock, no AI stuck evidente, consistenza host/client, performance adeguata alla scena; screenshot/video e build Windows. Se non c'è death animation credibile o il modello non appare giusto, L3 rimane IN PROGRESS.
