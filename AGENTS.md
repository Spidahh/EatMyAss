# CONTRATTO VINCOLANTE PER CODEX — ZOMBIE DEFENCE

**VERSIONE ATTIVA: 25/10/2026 — PRODUZIONE A STRATI.** Questo file prevale su qualsiasi vecchia istruzione in docs/00–11 in caso di conflitto. La progettazione precedente resta come materiale di riferimento per i sistemi futuri, non è un elenco di feature da costruire subito.

## OBIETTIVO IMMEDIATO, SENZA INTERPRETAZIONI

Costruisci su Unreal Engine 5.8 usando **HordeTemplate V2 Native** come framework di partenza (https://github.com/DasBander/HordeTemplate). Non aprire un'altra fase di comparazione fra template e non inventare un FPS da zero. La **prima consegna** è un unico ciclo di gameplay rifinito: un personaggio umano reale (Survival Character), **un fucile d'assalto completo** (FPS Weapon Bundle), **uno zombie Nurse completo**, nella prima piccola area della città in costruzione. FPS in prima persona con modello completo per la visuale degli altri giocatori.

Non costruire ancora torrette, economy, ondate multiple, classi, inventario ampio, dieci armi o una mappa grande.

## DOCUMENTI OBBLIGATORI, IN QUEST'ORDINE

1. docs/12_PRODUCTION_ORDER.md — decisioni bloccate e fasi.
2. docs/15_ASSET_LOCK.md — pack precisi, acquisizione, licenze, divieti.
3. docs/13_PLAYER_WEAPON_ANIMATION.md — personaggio, fucile, animazioni e feedback completi.
4. docs/14_ZOMBIE_COMPLETE.md — un nemico vero, AI, animazioni e impatti.
5. docs/16_CITY_GROWTH.md — città in costruzione ed espansione successiva.
6. docs/17_CODEX_EXECUTION.md — mandato immediato e reporting.
7. docs/01_GAME_DESIGN.md e docs/02_TECH_DESIGN.md solo per coerenza di sistemi futuri.

## REGOLE SENZA ECCEZIONI

- Un solo **strato alla volta**. Completa e rifinisci quello corrente prima del seguente. Implementazione, animazioni, audio, VFX, integrazione, packaging e correzioni del medesimo strato sono **un unico lavoro**, non una demo.
- **Vietati placeholder destinati a rimanere**: mannequin visibile, cubi come modelli di personaggi/armi/zombie, mesh stock casuali, suoni finti, animazioni inesistenti, asset di test nel contenuto finale. Se manca un asset approvato, acquisiscilo dal link indicato e integralo oppure dichiara chiaramente il blocco senza sostituirlo di nascosto.
- La città può restare **in costruzione**: crea una piccola zona permanente percorribile coerente con lo scenario urbano industriale. Non investire nel resto del mondo finché non è finito il combattimento.
- Non inventare path di asset, skeleton, nomi di Blueprint, nomi di file o contenuti di un pack. Ispeziona i file effettivi dopo averli acquisiti. Aggiorna l'inventario reale di ciò che hai usato.
- Non dichiarare “pronto”, “perfetto”, “finito” senza l'evidenza prevista. Il risultato deve funzionare in editor e in una build avviabile, con video del gameplay quando serve. Le prove sono QA **dello strato prodotto**, non spike/prototipi separati.
- **NON** usare il tag “NoAI” di Fab per raccolta dati destinata a generative AI; non caricare file protetti su servizi AI per addestramento o generazione. La scrittura del codice assistita da AI non autorizza l'uso dei contenuti come dataset.
- NON committare asset Fab, Epic o Marketplace su questo repository pubblico in forma sorgente se la licenza non consente tale redistribuzione. I file autorizzati stanno in un workspace di sviluppo privato; nel repo pubblico mettere istruzioni, sorgente redistribuibile e manifest riferimenti. Prima di pubblicare qualsiasi binario accertarne la licenza.
- Non comprare pack, non adottare abbonamenti, non sostituire asset con prodotti a pagamento. Se un pack non è disponibile: BLOCKED con URL, costo, ragione ed eventuale alternativa reale a costo zero, **senza saltare lo strato**.
- Non fare refactor generali al framework: cambi minimi e tracciabili. Non aggiungere Lyra, GAS o altro framework concorrente. Non passare a UE differente senza ragione tecnica verificata.
- Replicazione e sicurezza: riusa correttamente quanto HordeTemplate già implementa, ma il server decide colpi, HP, morti e munizioni. Mai fidarsi del client.
- Se l'engine manca dal tuo ambiente, puoi completare codice e documentazione realmente verificabili, ma **NON** chiamare completato uno strato. Registra con esattezza i comandi di build che non hai potuto eseguire.

## STATO CORRENTE

Repository di documentazione, senza .uproject di produzione. L'audit statico precedente esiste in docs/11_G0_HORDE_AUDIT.md. Ora è un **riferimento**, non una milestone che blocca l'inizio. Il primo task produttivo è specificato in docs/17_CODEX_EXECUTION.md e nella relativa GitHub Issue.

## DEFINIZIONE DI STRATO FINITO

Tutte le funzioni richieste dalla checklist dello strato sono implementate con asset approvati, transizioni corrette, audio e feedback reali; niente eccezioni note che impediscono una normale sessione; configurazioni non hardcoded inutilmente; performance e multiplayer pertinenti controllati; video o immagini del risultato; commit e changelog. Se una sola voce obbligatoria manca: stato IN PROGRESS o BLOCKED, mai DONE.

Il progetto **non è ancora un gioco funzionante**. Non confondere la completezza di questi documenti con il completamento del gioco.
