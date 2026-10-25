# CITTA INDUSTRIALE ESPANDIBILE — LEVEL DESIGN E SPECIFICA DEL MONDO

## Una mappa preprogettata, costruita in ordine

**Nome provvisorio:** Distretto Zero. Moderno quartiere industriale urbano semi-abbandonato (strade, officina, magazzino, tetti/cavalcavia). Mappa NON procedurale, NON open world, NON survival. Quattro aree leggibili, tre comprabili, tutte persistono nello stesso livello nella run. Il “resto città in costruzione” significa che la sua modellazione arriva dopo player/weapon/zombie; l'area già finita non viene buttata.

### Schema di connessione e rischio

```
     Spawn nord esterni
           |
  [OFFICINA / S1] ----- [TETTI / S3]
        |                    |
 [CORTILE / NUCLEO / S0] -- [DEPOSITO / S2]
        |
    Spawn sud esterni
```

Disegno concettuale, NON coordinate/prefab fabbricati. Il primo isolato S0 è definitivo L4: spawn player, area di avvistamento Nurse dietro angolo, un muro concreto e uno metallico per impatti, margine di sicurezza, strade/ingressi. Il Nucleo viene introdotto nel punto riservato L6, ma non sostituito a valle da altra geometria.

| Area | Stato all'avvio | Vantaggio acquisito | Nuovo rischio | Socket previsti | Debito artistico |
| --- | --- | --- | --- | --- | --- |
| S0 Cortile/Nucleo | aperta | copertura centrale, banco arma, due ingressi | due direzioni già attive | 1 sentry + 2 barricate | completare per L4/L6 |
| S1 Officina | dopo wave 3, compra | miglior angolo di fuoco, 1 piazzola, spazio di manovra | varco laterale est | 1 sentry, 1 slowfield | ambiente Fab industriale |
| S2 Deposito | dopo wave 6 | corto accesso fondi/munizioni, bretella difensiva | varco a sud-est | 1 sentry, 1 barricata | props warehouse coerenti |
| S3 Tetti | dopo wave 8, opzionale | linea di tiro elevata, choke point | accesso verticale da Runner | 1 barricata, 1 slowfield | scala/rampe e nav links sicuri |

**Apertura:** richiesta durante prep, prerequisito wave + settore collegato aperto se richiesto, spesa fondi team e conferma; porte/volumi/markers/navigazione si aprono con stato server replicato. Spawn dei nuovi varchi **solo dalla wave successiva**, preannunciati in UI. La chiusura della mappa non nasconde spawn attivi invisibili.

## Funzioni della città — una utilità per settore (design lock 1.1)

I settori non devono essere soltanto nuove geometrie o piazzole; ogni unlock aggiunge **una** capacità direttamente utile alla difesa già funzionante, senza nuovo tasto/valuta:
- **S0**: Core T2 sblocca Impulso di Contenimento, E al pannello, una volta per wave.
- **S1 Officina**: un banco munizioni già previsto offre refill a -15% PC (seed), solo lì; la wave successiva usa un nuovo varco.
- **S2 Deposito**: riduce del 15% TF (seed) il costo **solo** di riparazione barricata, non Nucleo o torre; nuovo fronte successivo.
- **S3 Tetti**: faro tattico comunica per i primi 6s della wave la **direzione** di arrivo dei nemici speciali nel settore, non wallhack globale; nuovo percorso d'assalto.

Mostrare VANTAGGIO/COSTO/NUOVO VARCO nella preview prima di ogni compra. I nuovi fronti redistribuiscono lo stesso threat budget; nessun nuovo spawn nascosto. Specifiche [40](40_SYNERGIES_SKILLS_AND_CITY.md).

## Regole di level design prima dei dettagli

- Progetta prime 2 route zombie verso Nucleo e 2 percorsi di fuga giocatore in S0. Ogni settore aggiuntivo apre un vantaggio tattico e almeno un rischio, ma non deve diventare 4 spawn incrociati inevitabili.
- Nessun vicolo o tetto raggiungibile dal giocatore che immobilizzi per sempre AI. Se c'è sniper spot, Runner può raggiungere oppure l'AI ripiega su Nucleo.
- Piazzole difensive NON sul centro del cammino NavMesh; barricata al varco bersagliabile; sentry con fire arc leggibile e ostacoli che blocchino davvero i colpi.
- Ogni area include collisioni ragionevoli, scale, LOD/texture budgeting, navigazione, lights, occlusion, ambient SFX, indicatori direzione degli assalti, spari su concrete/metal, linee vista 5m/15m/30m.
- Materiali e look uniformi con Factory Environment Collection approvato; non fare collage casuale di downtown foto-realistic + sci-fi anime.
- La notte non può impedire di riconoscere Runner e Saboteur; backlight e outline di servizio soltanto quando funzionalmente utile.

## Specifiche di `SectorDefinition`

`SectorId`, `DisplayName`, `Prerequisites`, `EarliestWave`, `TeamFundCost`, `DoorActors`, `NavLinks`, `SpawnGroupIds`, `BuildSocketIds`, `MusicZone`, `POIs`, `RadarBounds`, `Warnings`. Runtime `Closed/Pending/Open`. Apertura idempotente, non si paga due volte, non si chiude a partita in corso, replicazione e joiner vedono porte coerenti.

## Prezzi seed (non bilanciati)

S1 260, S2 420, S3 500 fondi squadra. S2/S3 prerequisiti scelti in level config, con controllo di accessibilità: non richiedere S1 implicitamente se il percorso vi è già collegato. L'opening deve competere con torretta/core upgrades; in 1p non rendere economicamente obbligatorio aprire per sopravvivere. Livelli di spawn non attivi vengono ignorati dal WaveDirector.

## Esito richiesto a ogni settore

Il giocatore può entrare e uscire, la mappa non ha geometrie finte, torri/porta/IA/missione/marker/ambience funzionano, zombie non nascono a vista, niente arresti navigazione, light/grafica coerenti, boss gestibile nella mappa intera e in configurazione S0–S1 se le altre zone non sono comprate. Screenshot topdown dal livello + FPS su ciascun ingresso e percorrenza registrata. La mappa “grande” non è una feature da usare prima di finirne una piccola parte.
