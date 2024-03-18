# Uppgift 11 - Tests

# Syfte

I den här uppgiften testar vi att skriva tester på tre olika sätt, med de
inbyggda Doctest och Unittest samt med det populära externa biblioteket pytest.

# Inför uppgiften

Inför uppgiften, gör så här:

1. Lär dig om virtuella miljöer

   - Detta är viktigt för att hålla dina projekt och dess beroenden
     organiserade.

2. Utforska olika sätt att skapa tester
   - Python erbjuder flera inbyggda verktyg för att skapa tester. Se till att du
     förstår de tre huvudsakliga metoderna.
   - För `pytest`, som inte finns i Pythons standardbibliotek, använd Google för
     att hitta dess officiella webbplats och dokumentation.
3. Läs om Testdriven utveckling (TDD):
   - Besök [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
     av Martin Fowler för en grundlig genomgång av TDD-konceptet.

# Beskrivning

I denna uppgift ska du utforska och använda de inbyggda testmöjligheterna i
Python med unittest och doctest, samt det populära externa testbiblioteket
pytest. Ditt mål är att skapa tester för tre tidigare genomförda uppgifter.
Genom att tillämpa dessa olika testmetoder får du en bred förståelse för
Python-testning och hur du effektivt kan validera din kod.

# Testerna

Här är en tabell som inkluderar information om från vilken uppgift varje
testscenario kommer, samt de specifika filnamnen och testmetoderna som ska
användas för varje:

| Uppgiftsfil     | Från Uppgift | Testmetod | Testfil            | Antal Testfall |
| --------------- | ------------ | --------- | ------------------ | -------------- |
| palindromish.py | Uppgift 2    | Doctest   | -                  | Minst 3        |
| stringt.py      | Uppgift 3    | Unittest  | test_stringt.py    | Minst 3        |
| treecoords.py   | Uppgift 4    | Pytest    | test_treecoords.py | Minst 3        |

När du använder pytest för att skriva och köra tester, är det viktigt att
organisera ditt arbete på ett sätt som gör det enkelt för andra att replikera
din testmiljö. Detta gör du genom att skapa en virtuell miljö och en
`requirements.txt`-fil.

# Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. Använda Github Classroom och klona ditt uppgiftsrepository:

   - Om du läser det här i `README.md` har du redan börjat med uppgiften genom
     att klicka på en länk från din utbildare och klonat ditt
     uppgiftsrepository.

2. Lös uppgiften:

   - Din lösning ska skapas genom att ändra i de filer som nämns i
     uppgiftsbeskrivningen. Följ instruktionerna där för var du ska lägga in din
     kod.

3. Lämna in med Git:

   - När du är klar, använd `git add .`, `git commit` och sedan `git push` för
     att skicka in ditt arbete till GitHub.

4. Automatiska "smoke tests":

   - När du skickar in din kod körs "smoke tests" automatiskt. En grön bock
     betyder att de gick igenom, medan ett rött kryss betyder att något gick
     fel. Om du får ett rött kryss, kolla på GitHub varför testerna
     misslyckades.

5. Feedback och granskning från utbildaren:

   - När dina "smoke tests" får en grön bock väntar du på feedback från din
     utbildare. Utbildaren kan vilja att du ändrar något eller godkänna din
     uppgift direkt. Vänta med att slå ihop din kod ("Merge") tills uppgiften är
     godkänd.

   - Om utbildaren vill att du ändrar något, läs noggrant och gör de ändringar
     som behövs.

   - När uppgiften är godkänd och det inte finns mer att diskutera, kan du göra
     "Merge" med din "Feedback"-pull request. Men, vänta alltid tills du har
     fått ett godkännande.

6. Starta diskussioner i "Feedback"-pull requesten:

   - Utnyttja möjligheten att diskutera uppgiftens kod i din "Feedback"-pull
     request. Det är ett bra sätt att lära sig genom att ställa frågor, be om
     förklaringar eller diskutera lösningar och respons med din utbildare.

# Anteckningar

Inga.
