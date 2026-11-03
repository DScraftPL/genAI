from validate_email import validate_student_email
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
