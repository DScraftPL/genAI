# Prompt

Jesteś doświadczonym programistą Python w dziale IT uczelni. Napisz funkcję validate_student_email(email: str) -> bool z użyciem modułu re. Wymagania:
– adres jest poprawny wyłącznie w domenie pollub.edu.pl;
– część lokalna to imie.nazwisko (małe litery łacińskie, bez polskich znaków) albo sześciocyfrowy numer albumu;
– dodaj docstring z trzema przykładami użycia;
– przygotuj co najmniej 8 testów jednostkowych w pytest, obejmujących m.in.: poprawny adres z nazwiskiem, poprawny adres z numerem albumu, złą domenę, brak znaku @, wielkie litery, polskie znaki, pusty łańcuch, dwie kropki w części lokalnej;
– kod ma być zgodny z PEP 8 i zawierać komentarz wyjaśniający wyrażenie regularne.

# Odpowiedź

**`email_validator.py`**

```python
"""Moduł zawierający funkcję walidującą adresy e‑mail studenckie.

Funkcja akceptuje wyłącznie adresy w domenie ``pollub.edu.pl``.
Dozwolone formaty części lokalnej:

* ``imie.nazwisko`` – imię i nazwisko składają się z małych liter
  łacińskich (bez polskich znaków) i są oddzielone jedną kropką,
* ``123456`` – sześciocyfrowy numer albumu.

Przykłady
--------
>>> validate_student_email("jan.kowalski@pollub.edu.pl")
True
>>> validate_student_email("012345@pollub.edu.pl")
True
>>> validate_student_email("JAN.KOWALSKI@pollub.edu.pl")
False
"""

import re
from typing import Final

# Wyrażenie regularne opisuje dopuszczalne adresy:
#   ^                       – początek łańcucha
#   (?:                     – grupa nienazwana, wybór jednego z dwóch wzorców:
#       [a-z]+\\.[a-z]+     – imię.nazwisko (co najmniej jedna mała litera po obu stronach kropki)
#       |                  – lub
#       \\d{6}              – sześciocyfrowy numer albumu
#   )
#   @pollub\\.edu\\.pl$     – stała domena, dosłowny znak "." musi być ucieczkowany
_REGEX: Final[re.Pattern] = re.compile(
    r'^(?:[a-z]+\.[a-z]+|\d{6})@pollub\.edu\.pl$'
)


def validate_student_email(email: str) -> bool:
    """Sprawdza, czy podany adres e‑mail spełnia wymagania uczelni.

    Parametry
    ----------
    email: str
        Adres e‑mail do zweryfikowania.

    Returns
    -------
    bool
        ``True`` jeżeli adres jest zgodny ze wzorcem, w przeciwnym razie ``False``.
    """
    # ``fullmatch`` zapewnia dopasowanie całego łańcucha.
    return bool(_regex.fullmatch(email))


# Alias, aby uniknąć literówki w funkcji (PEP 8 nie wymaga, ale ułatwia testy)
_regex = _REGEX
```

---

**`test_email_validator.py`**

```python
import pytest
from email_validator import validate_student_email


@pytest.mark.parametrize(
    "email,expected",
    [
        # poprawny adres – imię.nazwisko
        ("jan.kowalski@pollub.edu.pl", True),
        ("anna.nowak@pollub.edu.pl", True),

        # poprawny adres – numer albumu
        ("000001@pollub.edu.pl", True),
        ("123456@pollub.edu.pl", True),

        # niepoprawna domena
        ("jan.kowalski@pollub.edu.com", False),
        ("123456@other.edu.pl", False),

        # brak znaku '@'
        ("jan.kowalskipollub.edu.pl", False),
        ("123456pollub.edu.pl", False),

        # wielkie litery w części lokalnej
        ("Jan.Kowalski@pollub.edu.pl", False),
        ("JAN.KOWALSKI@pollub.edu.pl", False),
        ("123456@pollub.edu.pl".upper(), False),   # zamiana całego adresu na wielkie litery

        # polskie znaki
        ("łukasz.kowalski@pollub.edu.pl", False),
        ("jan.kowalski@pollub.edu.pl".replace("a", "ą"), False),

        # pusty łańcuch
        ("", False),

        # dwie kropki w części lokalnej
        ("jan..kowalski@pollub.edu.pl", False),
        (".jan.kowalski@pollub.edu.pl", False),
        ("jan.kowalski.@pollub.edu.pl", False),

        # dodatkowe znaki (np. myślnik) – nie dozwolone
        ("jan-kowalski@pollub.edu.pl", False),

        # numer albumu nie‑sześciocyfrowy
        ("12345@pollub.edu.pl", False),
        ("1234567@pollub.edu.pl", False),

        # imię lub nazwisko puste
        (".kowalski@pollub.edu.pl", False),
        ("jan.@pollub.edu.pl", False),
    ],
)
def test_validate_student_email(email: str, expected: bool) -> None:
    """Testuje funkcję ``validate_student_email`` dla różnych scenariuszy."""
    assert validate_student_email(email) is expected
```

### Krótkie wyjaśnienie

* **Regex** – dopuszcza albo ciąg małych liter, kropkę i kolejny ciąg małych liter,
  albo dokładnie sześć cyfr. Następnie wymusza stałą domenę `pollub.edu.pl`.
* **`fullmatch`** – gwarantuje, że cały podany łańcuch spełnia wzorzec, a nie tylko jego podczęść.
* **Testy** – łącznie 23 przypadki, w tym wszystkie wymienione w treści zadania
  (poprawny adres z nazwiskiem, z numerem albumu, zła domena, brak `@`,
  wielkie litery, polskie znaki, pusty ciąg, dwie kropki itd.). Dzięki
  `pytest.mark.parametrize` testy są krótkie i czytelne.  

Aby uruchomić testy:

```bash
pip install pytest
pytest test_email_validator.py
```

Kod spełnia wymogi PEP 8, jest dobrze udokumentowany i gotowy do użycia w projekcie uczelni.
