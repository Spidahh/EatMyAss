# DISTRIBUZIONE, COSTI, MANUTENZIONE E STRATEGIA DELLA VERSIONE 1.0

## Perimetro di pubblicazione

**Proposta prodotto:** Windows PC, demo giocabile offline+host e successiva piccola release premium o demo gratuita; nessun negozio di microtransazioni, pay-to-win, battle pass, account service, daily login, battle royale, endless grind. Tutte le feature della 1.0 sono nel Master Spec, no quest sistemi extra. Monetizzazione definitiva e prezzo retail non scelti perché dipendono dalla qualità della build; **l'agente non imposta prezzi né apre store autonomamente**.

## Costo di sviluppo

- Asset pack prima selezionati puntano a zero costi di licenza nel momento in cui sono Free e ottenuti ufficialmente; non assumere che licenze future rimangano free o che la qualità sia sufficiente.
- Unreal Engine royalty/soglie e termini correnti devono essere verificati con EULA Epic **al momento dell'uscita**; nessuna royalty durante il piano o previsione di guadagno fittizia.
- Hosting: listen server sul PC host per ridurre costi; traffico/rete, cloud relay, matchmaking e server dedicato non inclusi.
- Publishing: store onboarding, Steam Direct fee per prodotto, immagini trailer, rating, tasse, licenze sound/music sono costi eventuali e **non approvati**.
- Github pubblico: solo codice e documentazione che possono essere diffusi; asset license-encumbered in privata location e pacchetti cooked distribuiti secondo EULA.

## Quality bar prima di store

1. Tutto il loop completo da avvio a risultati funziona con Windows packaged Shipping su installazione pulita.
2. Ambientazione, gameplay e unità reali, audio e VFX distinti, UI e controlli coerenti, 10 ondate e boss, classi, upgrade e mappa espandibile.
3. Test single e co-op 1–4, host quit graceful, performance misurata e regressione senza crash/softlock evidenti.
4. Originalità: branding, UI, icone e ambientazione non replicano asset protetti CoD; attribuzioni terze legali.
5. Licenze, privacy, gore/content rating e compatibilità Windows sistemate.
6. Video gameplay catturato realmente dal gioco: no trailer inventato/immagini che promettono contenuti assenti.

## Distribuzione/patch

Ogni build ha semantic version + commit SHA e note regressioni. Versionate save settings e compatibilità lobby; su rete mismatched version si rifiuta sessione anziché crash. Crash reports solo locali/no raccolta identificativa senza consenso; monitor problemi supporto via issue. Prima patch priorità crash/softlock/cheat RPC prima di nuovi oggetti.

## Oltre la 1.0

Solo **dopo** feedback e budget reali: endless mode, nuove mappe, altri zombie/armi/torrette, cosmetici, controller, matchmaking, mid-run saves, host migration, achievement. Nessun sistema P2W. Non iniziare post-launch feature per saltare un blocco nel loop base.

## GO / NO GO

GO solo con tutte le condizioni docs/32 e dipendenze backlog chiuse. Se la base open source o un asset non è legalmente utilizzabile, progetto/feature resta BLOCKED e viene proposta soluzione economica valida; non nascondere la mancanza.
