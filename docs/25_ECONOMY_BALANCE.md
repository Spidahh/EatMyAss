# ECONOMIA V2 — ROTTAMI UNICA RISORSA, ZERO CRAFTING

**ANNULLATA la vecchia doppia valuta Player Credits + Team Funds.** Una sola risorsa `Rottami` guadagnata automaticamente dal combattimento e da incarichi OUTSIDE, spesa **solo alla base** per weapon, upgrade player, torri e Nucleo. No loot manuale corpi/oggetti sparsi, non 20 materiali, niente risorse che crescono da sole a gioco chiuso.

## Guadagni seed

`Kill` player fuori: Walker 5, Runner 7, Armored 20, Saboteur 16, Bruto 100; bonus stage completato 35→ crescente, eventi brevi completati 35–100. Tower kills concedono **parte ridotta** della ricompensa nello stesso fondo (seed 20%, max cap per stage) per sostenere l'idea che la base si autodifende senza creare AFK farming che consente crescita infinita; in tutta la partita il player guadagna molto di più combattendo fuori. Se player rientra dentro, tower kill continua ma contributi ridotti. Valori NON bilanciati.

## Spese seed

| Oggetto | Costo iniziale Rottami | Upgrade |
| --- | ---: | --- |
| Primo machete | gratuito iniziale o ottenibile via armeria | T1 70/T2 150/T3 300 |
| Primo AR | 90 | T1 100/T2 200/T3 350 |
| Torretta rapida | 180 | T1 130/T2 250/T3 400 |
| Torretta pesante | 300 | T1 220/T2 380/T3 550 |
| Barricata | 70 | T1 70/T2 130/T3 220 |
| Core | iniziale | T1 210/T2 430/T3 680 |
| Ammo refill | 25 | nessun crafting |
| Base repair | variabile HP | non overrepair |

Ci vuole sempre qualche guadagno possibile anche se la base non uccide nessuno, quindi primo gear+prima torretta va introdotta con progressione guidata e Rottami start scelti sulla base del primo assalto. Nessuna difficoltà insormontabile creata da costo iniziale sbagliato.

## Ledger e persistenza

Un solo `ZDWallet` host-authoritative condiviso per crescita base e gear nella V1 (un solo numero); `TxnId` di grant/spend, no saldo negativo/doppio premio, richiesta server validata con `InsideBase`, distanza terminale, tier, costi e prerequisiti. In co-op acquisti grandi richiedono consenso semplice dei partecipanti attivi o una politica host autorizzata, non si spende e basta con client fraudolento. Dopo la transazione la base salva il checkpoint e replica saldo. Gli eventi e zombie hanno `KillEventId`; server assegna reward una volta.

## Bilanciamento del loop

Dopo W3 la base opportunamente potenziata deve **autodifendersi** mentre il player guadagna fuori; a W7 con upgrade fermi a W3 deve incontrare difficoltà coerenti, non perdita HP arbitraria. Simulare investimenti tutti su fucili, tutti sulle torri e mix. Giocatore melee-only non deve guadagnare sistematicamente meno dei firearms se gioca bene. In modalità Continua premi per stage equivalenti alle ondate, non spawn farm infinito: quote/cap per unità di tempo.

## Salvataggi
Base, Rottami, armi sbloccate, torrette/tier, stage/difficoltà, specializzazione e opzioni host persistono, non simulare risorse offline. Uscita/crash durante assault usa ultimo checkpoint inizio stadio con journal atomico; ritorno alla base funziona mentre il mondo resta attivo. Dettaglio [44](44_OUTSIDE_COMBAT_AND_PROGRESSION.md).
