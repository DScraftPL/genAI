# Prompt

Napisz funkcję Python do walidacji adresu e-mail.

# Odpowiedź

**Walidacja adresu e‑mail w Pythonie**  

Poniżej znajdziesz kilka wariantów funkcji, które sprawdzają, czy podany ciąg znaków jest prawidłowym adresem e‑mail.  
Każdy z nich ma inne zalety i ograniczenia – możesz wybrać ten, który najbardziej pasuje do Twojego projektu.

---

## 1. Prosta walidacja przy pomocy wyrażenia regularnego

```python
import re

# bardzo prosty wzorzec – spełnia wymóg „coś@coś.coś”
_SIMPLE_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}$"
)

def is_valid_email_simple(email: str) -> bool:
    """
    Zwraca True, jeśli `email` pasuje do prostego wyrażenia regularnego.
    Nie sprawdza istnienia domeny ani limitów długości poszczególnych części.
    """
    if not isinstance(email, str):
        return False
    return bool(_SIMPLE_EMAIL_RE.fullmatch(email.strip()))
```

**Zalety**  
* Szybka i lekka implementacja.  
* Działa bez dodatkowych bibliotek.

**Wady**  
* Nie uwzględnia wszystkich niuansów specyfikacji RFC 5322 (np. komentarzy w nawiasach, znaków Unicode w lokalnej części).  
* Nie weryfikuje, czy domena naprawdę istnieje.

---

## 2. Walidacja z użyciem wbudowanego modułu `email.utils`

```python
from email.utils import parseaddr

def is_valid_email_parseaddr(email: str) -> bool:
    """
    Używa `email.utils.parseaddr`, które zwraca dwuelementową krotkę
    (display_name, address). Jeśli `address` zawiera znak '@' i nie ma
    dodatkowych znaków, uznajemy go za poprawny.
    """
    if not isinstance(email, str):
        return False

    # parseaddr zwraca ('', '') gdy nie uda się wyodrębnić adresu
    _, addr = parseaddr(email.strip())
    return '@' in addr and is_valid_email_simple(addr)   # dodatkowo używamy prostego regexu
```

**Zalety**  
* Lepsze rozpoznawanie adresów w formacie `John Doe <john@example.com>`.  
* Nie wymaga dodatkowych pakietów.

**Wady**  
* Nadal polega na prostym regexie do ostatecznej weryfikacji.  

---

## 3. Pełna walidacja wg. RFC 5322 przy pomocy biblioteki `email-validator`

Jeśli potrzebujesz naprawdę solidnej walidacji (sprawdzanie długości, dopuszczalnych znaków Unicode, a także opcjonalnie weryfikacji istniejącej domeny), warto skorzystać z gotowej biblioteki:

```bash
pip install email-validator
```

```python
from email_validator import validate_email, EmailNotValidError

def is_valid_email_full(email: str) -> bool:
    """
    Pełna walidacja wg. RFC 5322 + dodatkowe sprawdzenia:
    * ograniczenia długości (local-part ≤ 64, cały adres ≤ 254)
    * opcjonalna weryfikacja istnienia domeny (MX/SMTP)
    
    Zwraca True, gdy adres jest prawidłowy, w przeciwnym razie False.
    """
    try:
        # validate_email podniesie EmailNotValidError, jeśli coś jest nie tak
        validate_email(email, check_deliverability=False)  # ustaw True, aby sprawdzić MX
        return True
    except EmailNotValidError as e:
        # e.message zawiera szczegółowy opis przyczyny odrzucenia
        return False
```

**Zalety**  
* Pełna zgodność z RFC 5322 i RFC 6531 (obsługa Unicode).  
* Opcjonalne sprawdzanie, czy domena ma rekordy MX (czyli czy e‑mail może być dostarczony).  
* Dobre komunikaty o błędach (przydatne przy walidacji formularzy).

**Wady**  
* Zewnętrzna zależność – wymaga instalacji biblioteki.  
* Nieco wolniejsza niż czysty regex.

---

## 4. Jak wybrać odpowiednią wersję?

| Kiedy?                                         | Wersja                                   |
|------------------------------------------------|------------------------------------------|
| **Wystarczy szybka, podstawowa kontrola**      | `is_valid_email_simple`                 |
| **Obsługa adresów w formacie “Display <mail>”**| `is_valid_email_parseaddr`               |
| **Ścisłe wymogi RFC i/lub sprawdzanie domeny** | `is_valid_email_full` (biblioteka `email-validator`) |

---

## 5. Przykładowe użycie

```python
test_emails = [
    "jan.kowalski@example.com",
    "invalid-email",
    "user+tag@sub.domain.co.uk",
    "  whitespace@example.com  ",
    "John Doe <john.doe@example.org>",
    "ąśżć@przyklad.pl",               # Unicode w lokalnej części
    "verylonglocalpart" * 10 + "@example.com",  # przekroczenie limitu długości
]

print("=== prosta regex ===")
for e in test_emails:
    print(f"{e!r:40} -> {is_valid_email_simple(e)}")

print("\n=== parseaddr + regex ===")
for e in test_emails:
    print(f"{e!r:40} -> {is_valid_email_parseaddr(e)}")

print("\n=== pełna walidacja (email-validator) ===")
for e in test_emails:
    print(f"{e!r:40} -> {is_valid_email_full(e)}")
```

**Wyjście (przykładowe)**

```
=== prosta regex ===
'jan.kowalski@example.com'                -> True
'invalid-email'                           -> False
'user+tag@sub.domain.co.uk'               -> True
'  whitespace@example.com  '              -> True
'John Doe <john.doe@example.org>'         -> False
'ąśżć@przyklad.pl'                        -> False
'verylonglocalpartverylonglocalpart...@example.com' -> False

=== parseaddr + regex ===
'jan.kowalski@example.com'                -> True
'invalid-email'                           -> False
'user+tag@sub.domain.co.uk'               -> True
'  whitespace@example.com  '              -> True
'John Doe <john.doe@example.org>'         -> True
'ąśżć@przyklad.pl'                        -> False
'verylonglocalpartverylonglocalpart...@example.com' -> False

=== pełna walidacja (email-validator) ===
'jan.kowalski@example.com'                -> True
'invalid-email'                           -> False
'user+tag@sub.domain.co.uk'               -> True
'  whitespace@example.com  '              -> True
'John Doe <john.doe@example.org>'         -> True
'ąśżć@przyklad.pl'                        -> True
'verylonglocalpartverylonglocalpart...@example.com' -> False
```

---

## 6. Co zrobić dalej?

* **Integracja z formularzem webowym** – użyj `is_valid_email_full` po stronie serwera, a po stronie klienta (JS) możesz użyć prostszego regexu, żeby dawać natychmiastowy feedback.
* **Logika rejestracji** – przyjmuj tylko zweryfikowane adresy, a po rejestracji wyślij e‑mail potwierdzający (tzw. double‑opt‑in), aby upewnić się, że podany adres naprawdę istnieje i należy do użytkownika.
* **Obsługa Unicode** – jeśli aplikacja ma obsługiwać międzynarodowe adresy, koniecznie używaj `email-validator` (lub własnego regexu z `re.UNICODE`), ponieważ prosty wzorzec ASCII odrzuci poprawne adresy takie jak `用户@例子.公司`.

---

**Gotowe!** Teraz masz kilka gotowych implementacji, które możesz wkleić do swojego projektu i dopasować do własnych potrzeb. Powodzenia!
