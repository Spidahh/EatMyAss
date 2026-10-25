# COMBATTIMENTO OUTSIDE — FPS, MELEE PROFONDO MA ACCESSIBILE, SPECIALIZZAZIONI

**L'obiettivo non è una classe con +15% danno spada, ma un sistema di combattimento che sia divertente da padroneggiare.** Le armi melee sono **primarie alla pari** con le armi da fuoco, non una spinta di emergenza su V.

## Arsenal design lock V1.0

| Codice | Arma | Distanza/uso | Ritmo | Combo/azione speciale | Asset |
| --- | --- | --- | --- | --- | --- |
| M_MACHETE | Machete | ravvicinata, singoli zombie | veloce | 3 colpi breve con angoli leggibili, terzo spinge un bersaglio | mesh/rig/anim realistici FREE da reperire e approvare |
| M_HAMMER | Mazza pesante / martello industriale | corto-medio, armored e frantumazione | lenta | attacco caricato che colpisce armatura, non stun permanente | FREE da approvare |
| M_POLE | Lancia corta / asta industriale | portata > machete, tiene distanze | media | affondo lineare, colpisce uno zombie in prima fila, fino a 2 solo su traiettoria valida | FREE da approvare |
| W_AR | Fucile d'assalto | media | ranged | ADS, reload, recoil, hit bone come già pianificato | Deadghost bundle come fonte prima |
| W_PISTOL | Pistola | secondaria a distanza | ranged | rapido cambio dall'arma melee | dal bundle se presente davvero |
| W_SMG | SMG | mobile | ranged | rate di fuoco | fonte FREE da approvare |
| W_SHOTGUN | Fucile a pompa | close range | ranged | può colpire più zombie se pellet server reali | fonte FREE da approvare |

**Asset non scaricati e animazioni melee non verificate.** Codex deve cercare gratuitamente pacchetti coerenti (Fab, Epic permitted sample, rig Blender/Control Rig), valutarli/approvarli e poi integrarne una arma alla volta, mai usare mesh di cubi o spada genericamente anime. Non comprare, non inventare file.

## Regole melee base, senza diventare soulslike

- **LMB** attacco rapido: machete combo max 3, mazza 2 swing, asta 2 thrust; ogni colpo ha windup/active/recovery associati a montages **veri** e hit detection server su traiettoria dal weapon bone, max uno hit per target per swing.
- **RMB** tiene parata: riduzione del danno **frontale** solo in arco di guardia, con costo su **stamina melee** minima e separata dalla sprint? Per evitare troppe barre: usare **unica Stamina** già usata per sprint (già nel template) con regen dopo 0,8s fuori guardia; niente mana.
- **Perfect parry**: finestra prime **0,20s** del blocco; se intercetta un colpo telegraphed, breve stagger sul singolo zombie normale, recovery ridotta e attiva **una risposta/counter** possibile con LMB entro 1s. Non parare 10 zombie allo stesso tempo, boss e corazzati possono sfondare guardia con attacchi segnalati.
- **LMB tenuto**: su mazza solo attacco caricato (soglia seed 0,5s), no stamina infinito; machete/asta rimangono rapidi. UI non richiede 10 nuove icone.
- **Colpo “a vuoto”**: completo recovery, stamina leggera per la mazza; il nemico se schiva premia precisione. Non spam invincibile e niente auto-aim che prende nemico alle spalle.
- **Colpo in armatura**: suono/clank + minor damage, indicazione weakpoint, la mazza può romperla dopo hits reali; niente stunlock ininterrotto.
- **Killing blow**: breve reazione fisica/blood/hit stop di pochi ms lato locale, niente camera freeze globale e niente finisher obbligatoria di 5 secondi.
- **Damage and hit priority**: arma trace/capsule sweep sul server, legata ai notifies, validazione line-of-sight/arco 70–120° (valori per arma), anti multi hit stesso target; FX client predetti solo cosmetic.
- **Co-op**: friendly-fire off default, attacchi melee non bloccano visivamente gli amici, target zombie non è continuamente staggered da un gruppo di 4 senza CD.

## Tre specializzazioni, scelte dentro la base

**Non è un RPG a dieci alberi**. Il player sceglie UNA specializzazione al terminale dentro la base. Tutti possono usare l'arsenale base, e tutti possono rianimare compagni. Ognuna ha una passiva e una sola abilità attiva Q. Nessuna skill ha un HUD gigantesco.

| Specializzazione | Passiva | Abilità Q | Scelta tattica | Cosa NON fa |
| --- | --- | --- | --- | --- |
| **Tiratore** | primi colpi ADS dopo cambio bersaglio hanno minore dispersione, non buff flat eterno | **Bersaglio Aperto**: segnala un punto debole di UN nemico in mira per 5s, il suo prossimo head/weakpoint hit subisce breve bonus e audio reale; cooldown seed 40s | precisione e gestione élite lontano | non controlla torrette da fuori, non distribuisce danni ad area |
| **Spezzatore** (melee) | parata perfetta riduce il costo della prossima risposta e apre spazio per il counter | **Rompiguardia**: prossima heavy melee contro bersaglio davanti rompe temporaneamente armor guard / stordisce breve **una** unità normale, reset se miss; cd seed 45s | gioca melee con tempismo, può equip modalità **Mischia pura** alla base (+counter tempo, +stamina guardia, gun slot disabilitati volontariamente) | non è invulnerabile, non fa spin attack infinito |
| **Tecnico** | upgrade base costano leggermente meno (seed 5%, niente creazione risorse) | **Disturbo mirato**: colpisce un elite fuori dalla base con short-range tool / arma pronta, ne blocca capacità di sabotaggio o richiamo per 5s, effetto visibile; cd seed 50s | difende la base indirettamente sul campo, senza spostarsi ogni secondo ai terminali | non è l'unica classe capace di migliorare difese, non crea torrette portatili |

**Mischia pura** è una *specializzazione selezionata volontariamente* dello Spezzatore, non una classe in più con nuovi rig. Si può togliere/cambiare dentro la base senza perdere arma posseduta; cambio bloccato durante cast e mentre si è Downed. I suoi bonus vanno tarati per permettere boss/Armored senza una pistola ma con vera skill. Se boss non è raggiungibile con melee, il game design/AI deve essere corretto.

## Meccaniche divertenti senza eccesso di costi

1. **Concatenamento**: dopo una parry perfetta, il counter dello Spezzatore può interrompere il windup di UNO zombie e aprire varco, non pulire un'intera wave.
2. **Taglio dei capibranco**: fuori dalla base ci sono nemici “Richiamo” (Walker/Runner con comportamento distinto, NON un sesto rig) che amplificano la pressione del fronte verso il Nucleo; ucciderli alleggerisce l'assedio per una finestra temporanea, senza interrompere completamente la wave. Possono essere fatti sia con mira da lontano sia con melee rischioso.
3. **Tensione di ritorno**: allarme base comunica che sta resistendo male, il player decide se continuare un contratto in zona esterna o tornare a potenziare. Il gioco non teletrasporta il player né lo obbliga ad assistere la torretta.
4. **Contratto élite**: un corazzato fuori base può essere affrontato in duello con heavy melee preciso per ricompensa più alta; evitare raccolte di crafting materiali post kill.

## Priorità produzione e art budget

Prima **Machete** finito con full anim 1p/3p, IK, colpi, block/parry, audio flesh, hit FX/death reaction su Nurse. Poi la mazza, poi l'asta nella roadmap dopo il core auto-defense. Per ogni arma melee: hold+equip+idle+walk/sprint, light combo steps, heavy se applicabile, block startup/hold/release, perfect parry/counter, hit impacts, miss, hit light/heavy, death/cancel, stamina/FX e remote replica; non chiamare “completo” con una sola animazione swing.

## Limiti severi

No dodge/roll system separato, no magico spell casting, no talent tree, no loot rare melee, no gore procedural expensive (fisica reazioni sì), no scontri PvP, no stamina+rage+mana. Personaggio action FPS capace di parare e colpire con feeling, senza diventare un Souls-like.
