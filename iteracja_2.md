# Prompt

Napisz funkcję Python walidującą studencki adres e-mail. Adres jest poprawny wyłącznie w domenie pollub.edu.pl. Funkcja ma używać wyrażeń regularnych i zwracać True lub False. Dodaj testy jednostkowe dla przypadków: adres poprawny, zła domena, brak znaku @, pusty łańcuch znaków.

# Odpowiedź

**Rozwiązanie**  

```python
import re
import unittest

# -------------------------------------------------
# Funkcja walidująca studencki adres e‑mail
# -------------------------------------------------
def is_student_email(address: str) -> bool:
    """
    Sprawdza, czy podany ciąg jest poprawnym studenckim adresem e‑mail
    w domenie ``pollub.edu.pl``.

    Zasady:
    * przed „@” dopuszczalne są litery, cyfry, kropka, podkreślenie i myślnik
      (typowy zestaw znaków w adresach uczelnianych);
    * po „@” musi dokładnie wystąpić domena ``pollub.edu.pl``;
    * nie dopuszczamy dodatkowych pod‑domen (np. ``mail.pollub.edu.pl``).

    Zwraca:
        True  – jeśli adres spełnia wszystkie warunki,
        False – w przeciwnym razie.
    """
    if not address:                     # szybka odrzucenie pustego ciągu
        return False

    # ^                     – początek łańcucha
    # [A-Za-z0-9._%+-]+     – przynajmniej jeden dozwolony znak przed "@"
    # @                     – znak „@”
    # pollub\.edu\.pl$      – dokładna domena, koniec łańcucha
    pattern = r'^[A-Za-z0-9._%+\-]+@pollub\.edu\.pl$'

    return re.fullmatch(pattern, address) is not None


# -------------------------------------------------
# Testy jednostkowe
# -------------------------------------------------
class TestStudentEmailValidator(unittest.TestCase):
    def test_correct_address(self):
        self.assertTrue(is_student_email('jan.kowalski123@pollub.edu.pl'))

    def test_wrong_domain(self):
        self.assertFalse(is_student_email('jan.kowalski123@other.edu.pl'))
        self.assertFalse(is_student_email('jan.kowalski123@pollub.com'))

    def test_missing_at(self):
        self.assertFalse(is_student_email('jan.kowalski123pollub.edu.pl'))
        self.assertFalse(is_student_email('jan.kowalski123 pollub.edu.pl'))

    def test_empty_string(self):
        self.assertFalse(is_student_email(''))


# -------------------------------------------------
# Uruchomienie testów (jeśli plik jest uruchamiany bezpośrednio)
# -------------------------------------------------
if __name__ == '__main__':
    unittest.main()
```

### Dlaczego tak?

| Element | Uzasadnienie |
|---------|--------------|
| `re.fullmatch` | Zapewnia dopasowanie **całego** ciągu, a nie tylko fragmentu. |
| `[A-Za-z0-9._%+\-]+` | Dopuszcza najczęściej spotykane znaki w uczelnianych loginach (litery, cyfry, kropka, podkreślenie, myślnik, znak „+” i „%”). |
| `pollub\.edu\.pl` | Dokładna domena, wymuszona przez `\.` (kropka jest znakiem specjalnym w regexie). |
| `if not address` | Natychmiast odrzuca pusty ciąg – w przeciwnym razie regex zwróciłby `None`, ale lepiej zrobić to jawnie i szybciej. |
| `unittest` | Standardowy moduł testowy w Pythonie, pozwala na automatyczną weryfikację wszystkich scenariuszy. |

Po zapisaniu powyższego kodu w pliku (np. `email_validator.py`) można go uruchomić poleceniem:

```bash
python email_validator.py
```

i zobaczyć, że wszystkie testy przechodzą pomyślnie.
