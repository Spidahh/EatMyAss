# MAPPA V2 — BASE UNICA + 3 ZONE ESTERNE DI COMBATTIMENTO

**ATTENZIONE: NESSUNA CITTÀ-BASE DA COMPRARE.** Il titolo di questo documento è mantenuto per compatibilità link, ma il contenuto dei vecchi S0 cortile/S1 Officina/S2 Deposito/S3 Tetti acquistabili è RITIRATO. La **base** è una sola struttura fortificata con hub upgrade interno. La “città” appare come territorio abbandonato dove si combatte fuori, non come quattro shop/discount passivi.

### Layout

```
            [ZONA B: Smistamento / capibranco]
                         |
[ZONA C: area infetta] -- [ZONA A: perimetro base esterno] ---- [accesso HUB interno]
                                       |
                               [SIEGE SPAWN ROUTES]
```

Il layout non è una mappa definitiva; va modellato con Factory Environment Collection e altre fonti FREE coerenti, creando un livello piccolo ma permanente. Linee vedute e corner per ranged/melee, accesso sempre chiaro alla base, porte fisiche che fanno transitare il player, collision/NavMesh corretti. Le Siege AI attaccano il **perimetro esterno** e non fanno path nello hub; Field AI affrontano player all'esterno. Non creare centinaia di metri di level vuoto.

### Zona A: perimetro
Quello che i player vedono entrando/uscendo: un cancello, 2/3 socket torre, Nucleo e barricate, zombie di assedio. Torri visibili sparano realmente ai nemici. All'inizio costruire qui il modulo completo personaggio+AR+machete+Nurse+prima torre. La base si espande **tramite nuovi socket e modelli sullo stesso edificio**, non compra aree città.

### Zona B: smistamento
Più spazi per il corpo a corpo, capobranco che aumenta pressione assedio, squadre piccole e 1 elite; incarichi combat ad alto valore e rischio. Non creare bottega NPC o raccolta materiali.

### Zona C: area infetta
Elite più duri/Bruto milestone, rischi e Rottami più elevati, recupero sotto attacco. Portata/ombra e ripari tali da permettere tutti gli stili.

### Apertura del territorio
Non serve comprare una zona come settore city. Sblocco progressivo in base al livello/minaccia raggiunto e se desiderato il cancello della Zona B/C si apre automaticamente una volta completato stage; il player decide quando recarsi, non paga un terreno. Nuovi spawner Field senza duplicare budget Siege; proteggere il frame rate anche con 4 player dislocati.

### Art/SFX/QA
Moduli industriali realistici e LOD, suoni differenti dentro/fuori, cammino e weapon impacts metal/concrete/flesh, luce leggibile, 1/3p, Zombie nav senza teleport. Hub pulito e funzionale, con quattro terminali. Una torretta deve operare da sola anche se nessuno vede la scena; test client remoto e line-of-sight. Dettaglio [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).
