PROMPT_V1 = """
Przypisz kategorię i priorytet do tego zgłoszenia:

Od wczoraj nie moge sie polaczyc z VPN z domu, wyskakuje blad 809. Potrzebuje dostepu do serwera z danymi do jutra rana, bo oddaje projekt.
"""

PROMPT_V2 = """
# ROLA
Jesteś operatorem pierwszej linii wsparcia IT. Klasyfikujesz zgłoszenia
szybko i spójnie.

# ZADANIE
Przypisz zgłoszenie z sekcji DANE do jednej kategorii i jednego priorytetu.

# KATEGORIE (użyj dokładnie tych etykiet)
- SPRZET: awarie komputerów, drukarek, projektorów, peryferiów
- OPROGRAMOWANIE: instalacja, błędy i licencje programów
- KONTO: hasła, blokady kont, uprawnienia, logowanie
- SIEC: Wi-Fi, VPN, brak internetu, dostęp do serwerów
- INNE: wszystko, co nie pasuje

# PRIORYTETY
- WYSOKI: blokuje pracę wielu osób lub zagraża danym/egzaminowi
- SREDNI: blokuje pracę jednej osoby, jest obejście
- NISKI: pytanie, prośba, drobna niedogodność

# FORMAT
Zwróć wyłącznie obiekt JSON:
{
  "kategoria": "SPRZET | OPROGRAMOWANIE | KONTO | SIEC | INNE",
  "priorytet": "WYSOKI | SREDNI | NISKI",
  "uzasadnienie": "jedno zdanie"
}

# DANE
<zgloszenie>
Od wczoraj nie moge sie polaczyc z VPN z domu, wyskakuje blad 809. Potrzebuje dostepu do serwera z danymi do jutra rana, bo oddaje projekt.
</zgloszenie>
"""

PROMPT_V3 = """
# ROLA
Jesteś doświadczonym operatorem pierwszej linii wsparcia IT. Klasyfikujesz
zgłoszenia szybko, spójnie i bez zgadywania.

# KONTEKST
Zgłoszenia pochodzą od studentów i pracowników uczelni. Są pisane
nieformalnie, bywają niepełne. Twoja klasyfikacja trafia do systemu
ticketowego i decyduje, który zespół zajmie się sprawą.

# ZADANIE
Przypisz zgłoszenie z sekcji DANE do dokładnie jednej kategorii i jednego
priorytetu.

# KATEGORIE (użyj dokładnie tych etykiet)
- SPRZET: awarie komputerów, drukarek, projektorów, peryferiów
- OPROGRAMOWANIE: instalacja, błędy i licencje programów
- KONTO: hasła, blokady kont, uprawnienia, logowanie
- SIEC: Wi-Fi, VPN, brak internetu, dostęp do serwerów
- INNE: wszystko, co nie pasuje, lub zgłoszenie zbyt niejasne

# PRIORYTETY
- WYSOKI: blokuje pracę wielu osób lub zagraża danym/egzaminowi
- SREDNI: blokuje pracę jednej osoby, jest obejście
- NISKI: pytanie, prośba, drobna niedogodność

# ZASADY
1. Wybierz tylko jedną kategorię z listy. Nie twórz nowych.
2. Jeśli zgłoszenie jest niejasne lub pasuje do kilku kategorii, wybierz
   INNE i ustaw "wymaga_czlowieka": true.
3. Priorytet oceniaj wyłącznie na podstawie treści zgłoszenia, nie tonu
   (wielkie litery i wykrzykniki nie podnoszą priorytetu).
4. "uzasadnienie" to jedno zdanie, max 20 słów.
5. Zwróć wyłącznie obiekt JSON, bez komentarza i bez markdown.

# FORMAT
{
  "kategoria": "SPRZET | OPROGRAMOWANIE | KONTO | SIEC | INNE",
  "priorytet": "WYSOKI | SREDNI | NISKI",
  "uzasadnienie": "jedno zdanie",
  "wymaga_czlowieka": true lub false
}

# PRZYKŁADY
<zgloszenie>W sali 204 nie działa projektor, za 10 minut mam wykład dla 80 osób!!!</zgloszenie>
{"kategoria": "SPRZET", "priorytet": "WYSOKI", "uzasadnienie": "Awaria projektora tuż przed zajęciami grupowymi.", "wymaga_czlowieka": false}

<zgloszenie>Nie mogę się zalogować, wpisuje hasło i nic.</zgloszenie>
{"kategoria": "KONTO", "priorytet": "SREDNI", "uzasadnienie": "Problem z logowaniem jednego użytkownika, brak informacji o blokadzie.", "wymaga_czlowieka": false}

<zgloszenie>Coś się zepsuło, proszę naprawić.</zgloszenie>
{"kategoria": "INNE", "priorytet": "NISKI", "uzasadnienie": "Zgłoszenie bez opisu problemu, wymaga doprecyzowania.", "wymaga_czlowieka": true}

# DANE
<zgloszenie>
Od wczoraj nie moge sie polaczyc z VPN z domu, wyskakuje blad 809. Potrzebuje dostepu do serwera z danymi do jutra rana, bo oddaje projekt.
</zgloszenie>
"""
