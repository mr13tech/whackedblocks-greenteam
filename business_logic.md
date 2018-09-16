Whacked Blocks: Wyrocznia <–> Rejestr zastawów 

------------------------------------------------------------------------------------------------------------------------------------- 

Legenda: 

Pdaw = pożyczkodawca 

Pbior = pożyczkobiorca 

RZ = rejestr zastawów 

SK = smart kontrakt (escrow) 

ZSO = platforma p2p; coś jak augur pod względem interfejsu, tj. ogłoszenia 

------------------------------------------------------------------------------------------------------------------------------------- 

Business logic krok po kroku 

Etap I – transfer Dai od Pdaw do Pbior; udzielenie pożyczki: 

1. Pdaw ma wolne środki finansowe, więc chce pożyczyć 100 Dai na 10% w skali 3 miesięcy; 

2. Pdaw tworzy i deploy’uje SK w ramach “zdecentralizowanego słupa ogłoszeniowego” (ZSO); 

3. Pdaw wykonuje transfer 100 Dai na SK (złożenie środków w depozycie) + 
Pdaw przekazuje do SK swoje dane konieczne dla realizacji transakcji (imię i nazwisko / nazwę spółki i adres zamieszkania / siedziby [credientials]); 

4. Pbior widzi ofertę pożyczki (SK) wystawionej przez Pdaw na ZSO i postanawia przyjąć ofertę; 

5. Pbior przekazuje do SK swoje dane konieczne dla realizacji transakcji (imię i nazwisko / nazwę spółki oraz adres zamieszkania / siedziby); 

6. Pbior składa wniosek o zarejestrowanie zastawu do sądu rejestrowego;

<<SK stanowi, że środki znajdujące się w depozycie zostaną przetransferowane na adres danego pożyczkobiorcy, gdy otrzyma informację od Wyroczni, że w RZ znajduje się zastaw ustanowiony na aktywach Pbior>> (np. tokenach udziałowych) wartych co najmniej 110 Dai, którego beneficjentem jest Pdaw; 

7. Oracle "nasłuchuje" bazy danych (np. KRS dla spółek, bazę PESEL dla osób fizycznych) i weryfikuje czy wpisane do SK dane (nazwa i adres) dla Pdaw i Pbior się zgadzają: 
W zależności od wyników powyższego checku: 

If true – SK tworzy umowę zastawu (RZ pledge = 1) składa wniosek do RZ (RZapplication=1); oba dokumenty zostają podpisane elektronicznie; 

If false – następuje rozwiązanie SK 

8. Oracle poke’uje RZ co 24h i sprawdza dwie rzeczy: (1) czy został zarejestrowany zastaw; (2) czy dane w RZ dla tego zastawu są prawidłowe i zgodne z wnioskiem; 

W zależności od wyników powyższego checku: 

If true – następuje wypłata 100 Dai od Pdaw do Pbior 

If false – pożyczka nie jest wypłacana i następuje rozwiązanie SK 

 

Etap II – kontrola spłaty i zwrot pożyczki: 

Wariant A - “wszystko zgodnie z planem” 

1. W ciągu 3 miesięcy Pbior przesłał 110 dai do SK; co 24 h leci ping do Oracla czy Pbior przesłał ten hajs; 

2. Oracle weryfikuje czy nastąpił trigger dla realizacji zastawu (co 24h i w ciągu 3 miesiącach czy Pbior dokonał transferu 110 dai na SK); 

3. Pbior przesłał 110 dai do SK, więc nie nastąpił trigger dla realizacji zastawu (jeżeli taki trigger jest, bo to jest dodatkowa opcja); 

4. SK przesyła 110 dai do Pdaw i jednocześnie generuje i składa elektroniczny wniosek o wykreślenie zastawu z RZ (podpisany elektronicznie przez Pdaw); 

5. SK ulega rozwiązaniu 

Wariant B - “Pbior spadł z rowerka”, czyli Pdaw zaspokaja się z zastawu 

1. W ciągu 3 miesięcy Pbior nie przesłał 110 dai do SK; 

2. Oracle weryfikuje czy nastąpił trigger dla realizacji zastawu (co 24h i w ciągu 3 miesiącach czy Pbior dokonał transferu 110 dai na SK); 

3. Pbior nie przesłał 110 dai do SK, więc nastąpil trigger dla realizacji zastawu (Pbior nie spłacił pożyczki w ciągu 3 miesięcy); 

4. SK przekazuje do Pdaw informację, że pożyczka nie została spłacona; 

5. Dodatkowo dla zastawu na aktywie cyfrowym (np. tokeny udziałowe): automatyczna egzekucja (przejęcie) przedmiotu zabezpieczenia, czyli tokenów, przez Pdaw 

 
