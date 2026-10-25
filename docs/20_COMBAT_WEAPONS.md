# COMBATTIMENTO FPS E ARSENALE 1.0 — QUATTRO ARMI, UN'IMPLEMENTAZIONE ALLA VOLTA

## Target del feeling

FPS moderno adulto, responsive, fuoco leggibile; headshots ad alto valore, impatto carne/armatura/superfici, audio forte ma non assordante, recoil gestibile, movimento e mira non intralciati da lunghe animazioni. **Una sola arma terminata interamente prima della prossima**. Non aggiungere meccaniche di COD coperte da risorse protette; il riferimento è soltanto al genere zombie wave shooter.

## Arsenale 1.0 e ruoli non sovrapposti

| ID | Archetipo | Gameplay | Limitazione intenzionale | Stato modello |
| --- | --- | --- | --- | --- |
| W_AR | Fucile d'assalto | versatile mid-range, gestisce corridori | spreca colpi se usato su massa senza controllo | **Deadghost FPS Weapon Bundle** scelto, modello effettivo ancora da censire dopo acquisizione |
| W_PI | Pistola | riserva, preciso, economico, danno utile headshot | rate/capacità inferiori | candidato dal bundle, **non confermato quale mesh** |
| W_SG | Shotgun | varchi, corazzati da vicino, effetto forte | caricatore piccolo, distanza corta | fonte gratuita finale **DA APPROVARE** |
| W_SM | SMG | muoversi, mirare rapido, pulizia piccoli nemici | meno affidabile sul corazzato lontano | fonte gratuita finale **DA APPROVARE** |

**Non dichiarare W_SG/W_SM con asset “finali” fino al manifesto ASSET-APPROVED.** Se nel bundle esistono modelli idonei, preferirli; se no GAP obbligatorio e sourcing mirato. Il gameplay non deve esporre un'arma non completata.

## Weapon data contract

`WeaponDefinition` proposta: `WeaponId`, `VisualAssetId`, `AnimSetId`, `SfxSetId`, `DamageBase`, `HeadMultiplier`, `ArmourPen`, `FireInterval`, `ProjectileType`, `SpreadHip`, `SpreadADS`, `SpreadMoving`, `RecoilCurve`, `ReloadTactical`, `ReloadEmpty`, `MagazineMax`, `ReserveMax`, `RangeMin/Max`, `AmmoEconomy`, `AllowedUpgrades`, `CrosshairStyle`. Non inventare classe C++ upstream: questa è una definizione da mappare su `BaseFirearm` e inventory reali.

## Parametri seed iniziali — non bilanciati

| Arma | Danno torso | Head x | Colpi/min | Magazine | Reload sec | Ruolo costo |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| AR | 26 | 1.75 | 600 | 30 | 2.3 | standard |
| Pistola | 35 | 2.0 | 300 | 12 | 1.8 | gratuito iniziale |
| Shotgun | 12×7 pellet | 1.3 | 75 | 6 | 3.8 totale | costoso close |
| SMG | 19 | 1.5 | 800 | 36 | 2.1 | medio |

Sono valori per rendere le differenze esplicite, NON misure validate. Danno distanza: AR/SMG diminuiscono gradualmente, shotgun spread e pellet validation server; non promettere pellet unico. Non “one shot headshot” indiscriminato: una Nurse L3 può morire per headshot iniziale, ma boss/corazzati devono avere resistenza parametrica. Tipi di munizioni semplici e coerenti; evitare ammo loot di crafting.

## Upgrade per arma

Tre tier `T0–T3` con **una scelta per tier** (mutualmente esclusiva se alternative offerte). Prevedere tre percorsi: **Forza** (+danno controllato), **Precisione** (-spread/-recoil), **Capacità** (+magazine e riserva / reload). L'upgrade deve modificare statistica + feedback visivo/sonoro + scheda UI, non un numero invisibile. Evitare cumulabilità infinita; niente tier oltre T3 alla 1.0. AR, Pistola, SG, SMG con valori per-tier in DataAsset. Acquisti personali al banco armamenti durante Prep. Interrompere reload? una volta partito, ammo trasferita solo a notify/momento coerente; cancellazione non duplica munizioni. Weapon swap con blend e lock sui frame appropriati.

## Camera, physics, feedback

Tutte le armi: viewmodel corretto in FPS, corpo 3P con montages per remote, IK hand grip, hips/ADS posizioni verificate, no clipping. Fire rate **server authoritative** e predizione visiva client con riconciliazione; recoil additive non manipola fisicamente punto impatto senza regola; hip-fire e ADS diversi; shell casing su socket (se arma ne prevede), muzzle flash, smoke, shot tail vicina/lontana, flesh/metal/concrete surface impacts, impact decal con limite e pulizia. Audio reload: magazine out/in, bolt quando necessario, dry-fire e equip, audio handling.

## Death e hit attribution

Colpi causati da `Weapon`, instigator `Controller/PlayerState`, DamageCauser `AActor`; kill/assist entity distinte. Zombie non può evitare `Die()` soltanto perché causer non è `ACharacter`. Testare danno da torre futura con lo stesso damage pipeline, **ma non implementare torre prima del suo strato**. Test idempotenza, fire cadence, packet loss, headshot bone mapping sul modello vero.

## Ordine DOD

W_AR completa prima di W_PI, poi W_SG, poi W_SM nel contenuto V1. Ogni arma comprende mesh/reload equip ADS hip movement, suoni completi, VFX, drop/score, 2-tier upgrade provabile e test 2 player. Una “mesh animata ma arma incompleta” blocca lo strato corrente.
