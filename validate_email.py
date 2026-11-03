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
