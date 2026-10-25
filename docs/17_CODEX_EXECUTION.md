# ORDINE DI ESECUZIONE PRONTO PER CODEX — START IMMEDIATO

## Il compito

Non proporre piani alternativi, non tornare alla fase di ricerca e non implementare torrette o classi. **Devi cominciare a realizzare il gioco Unreal nel repository**, a strati, senza feature fittizie. Il lavoro immediato è L0, poi L1, L2, L3, L4; prosegui nello stesso ordine dopo aver completato ciascuno, senza aprire tre sistemi contemporaneamente. I requisiti completi sono in docs/12, docs/13, docs/14, docs/15 e docs/16. AGENTS.md è vincolante.

### Sequenza esecutiva precisa

1. Leggi AGENTS.md e docs/12–17. Ispeziona repository e accessibilità Unreal, versione engine e strumenti.
2. Clona il **vero** https://github.com/DasBander/HordeTemplate in ambiente di lavoro autorizzato e fissa il commit utilizzato. Si usa il template come **base scelta**: non un test comparativo con Lyra. Mantieni attributions MIT e seleziona i file/asset che legalmente possono entrare nel repository pubblico. Assicurati che il progetto di gioco reale parta; se devi correggere build errors, fallo con modifiche tracciate.
3. **L1:** acquisisci Survival Character dalla scheda designata, integra il modello reale e il controllo movimento con camera FPS e rappresentazione corpo remoto, retarget vere animazioni, controller e footstep. Non avviare L2 se L1 non è chiuso.
4. **L2:** acquisisci FPS Weapon Bundle, scegli **un solo fucile d'assalto reale dal contenuto**, integra completo ADS/fire/reload/equip/sprint/dry fire e anima mani + arma, audio e VFX, recoil, muzzle/shell/hit; niente altri tipi di arma.
5. **L3:** acquisisci Zombie Nurse e anima/realizza tutti gli stati in docs/14, AI con movimento, telegraph, hit reaction, morte, audio e feedback. Correggi il collegamento damage/death per causer non Character.
6. **L4:** un piccolo isolato definitivo, uno zombie, un fucile, una sequenza FPS credibile e completa, HUD essenziale. Build/package Windows, registrazione gameplay reale e prova sincronizzazione client quando disponibile. Il resto della città resta in costruzione.
7. Solo quando L4 è COMPLETO secondo checklist puoi iniziare L5 (onde), poi Nucleo, torretta e upgrade **in strati ulteriori**, come da docs/12.

### Requisiti di ogni consegna

Il primo valore prodotto NON è “ho installato pack”, “personaggio cammina su un cubo” o “ho collegato un bottone Fire”: è un'esperienza breve che sembri un videogioco vero con **tutti** gli asset finali del primo scenario. Per ogni strato completato serve una breve evidenza osservabile e un risultato replicabile. Se un asset promesso non contiene la clip necessaria, **non lasciare un TODO nascosto**: completala con tool gratuiti oppure dichiara un blocco esplicito, senza fingere.

### Organizzazione tecnica

- Modifiche preferite nella cartella estensioni ZD del progetto; intervenire nel framework solo quando necessario e commentare la ragione.
- Mantieni i binari Fab/Epic in workspace PRIVATO, non pubblicare a GitHub gli asset sorgenti protetti. Nel repo pubblico salva il codice che hai diritto a condividere e il manifesto per ricostruire l'ambiente di sviluppo.
- Ogni task ha una sola finalità: L1 solo player, L2 solo weapon, L3 solo zombie, L4 solo primo isolato.
- Niente package acquistati, niente abbonamenti, niente sostituzioni generiche, niente refactor enormi, niente funzionalità che l'utente non ha richiesto.
- Se una risorsa Unreal richiede strumenti non presenti nel runtime di Codex, non dichiararla realizzata; prepara codice realmente applicabile e segnala **precisamente** quale tool manca. Il processo non deve mentire sui risultati.

### Messaggio finale Codex dopo ciascuno strato

**Strato:** L0/L1/L2/L3/L4  
**Stato:** DONE solo se tutto realizzato e verificato; altrimenti IN PROGRESS o BLOCKED  
**File esatti modificati / commit:** percorsi e hash reali  
**Asset realmente acquisiti e licenze:** elenco e percorso PRIVATO, niente copie sorgenti pubbliche  
**Animazioni:** richieste, effettivamente presenti, realizzate, mancanti  
**Gameplay:** cosa si vede e si sente veramente in game  
**Build e run:** versione UE, esito, log/errori  
**Visual proof:** video o screenshot soltanto se effettivamente prodotti  
**Rischi e bug residui:** tutti, senza nasconderli  
**Prossima operazione:** prima incompleta nello stesso strato oppure strato successivo se completato

### Criterio non negoziabile

Non scrivere mai “fatto tutto” quando hai solo cambiato sorgenti. Un video con il vero avatar, arma e zombie collegati e con le corrette animazioni conta più di mille righe di commenti. Nessun sistema di gioco appena inserito è definitivo finché non sono completi qualità visiva, suono, gameplay, UX e build.
