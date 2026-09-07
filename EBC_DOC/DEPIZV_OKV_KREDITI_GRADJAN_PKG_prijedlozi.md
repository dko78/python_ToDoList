# DEPIZV_OKV_KREDITI_GRADJAN_PKG - prijedlozi optimizacije i mjerenja

## Kontekst
Zadnja mjesečna obrada trajala je osjetno duže od uobičajenog trajanja.
Analiza ukazuje da je glavno usko grlo per-row poziv logike za dohvat stanja konta, uz ponavljane upite nad istim kombinacijama podataka.

## Prijedlozi optimizacije
1. Izbaciti per-row pattern za `P_STANJE_KONTA_DAN_DNEVNA` i prebaciti na bulk/set-based dohvat stanja za cijeli `l_data` chunk.
2. U pomoćnoj logici minimizirati ponavljane upite nad `STANJA_PARTIJA`/`SUME_PROMETA` po istoj partiji/kontu/valuti.
3. Uvesti cache u PL/SQL kolekciji po ključu `(par_id, kto_id, val_id, datum_obrade)` kako bi se izbjegli repetitivni dohvat-i unutar iste obrade.

## Prijedlozi mjerenja (instrumentacija)
1. Dodati mikro-metrike u petlju: mjeriti vrijeme prije/poslije poziva `P_STANJE_KONTA_DAN_DNEVNA`.
2. Agregirati metrike svakih `n` partija (npr. 100/500) i upisivati u log tablicu.
3. Bilježiti minimalno:
   - broj obrađenih partija
   - broj cache hit/miss
   - ukupno vrijeme u `P_STANJE_KONTA_DAN_DNEVNA`
   - prosjek i max vrijeme po partiji
4. Budući da `OBRADE_STAVKE` nije popunjen za ovaj paket, metrike voditi u zasebnoj tablici ili kroz postojeći standardizirani logging mehanizam.

## Operativna preporuka
Ako je cilj brza validacija već na idućoj mjesečnoj obradi, napraviti minimalno invazivan instrumentation patch:
- bez promjene poslovne logike
- samo mjerenje i logiranje trajanja po segmentima
- mogućnost uključivanja/isključivanja preko parametra.

## Sljedeći korak
Mogu odmah pripremiti konkretan patch za paket s:
- helper procedurama za mjerenje
- batch agregacijom metrika
- kontrolnim parametrom za uključivanje instrumentacije.
