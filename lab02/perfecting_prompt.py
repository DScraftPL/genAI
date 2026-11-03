import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"


def zapytaj(prompt: str, max_tokens: int = 4000) -> str:
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    return r.choices[0].message.content


PROMPT_1 = "Napisz funkcję Python do walidacji adresu e-mail."

PROMPT_2 = (
    "Napisz funkcję Python walidującą studencki adres e-mail. Adres jest "
    "poprawny wyłącznie w domenie pollub.edu.pl. Funkcja ma używać wyrażeń "
    "regularnych i zwracać True lub False. Dodaj testy jednostkowe dla "
    "przypadków: adres poprawny, zła domena, brak znaku @, pusty łańcuch znaków."
)

PROMPT_3 = """Jesteś doświadczonym programistą Python w dziale IT uczelni. Napisz funkcję validate_student_email(email: str) -> bool z użyciem modułu re. Wymagania:
– adres jest poprawny wyłącznie w domenie pollub.edu.pl;
– część lokalna to imie.nazwisko (małe litery łacińskie, bez polskich znaków) albo sześciocyfrowy numer albumu;
– dodaj docstring z trzema przykładami użycia;
– przygotuj co najmniej 8 testów jednostkowych w pytest, obejmujących m.in.: poprawny adres z nazwiskiem, poprawny adres z numerem albumu, złą domenę, brak znaku @, wielkie litery, polskie znaki, pusty łańcuch, dwie kropki w części lokalnej;
– kod ma być zgodny z PEP 8 i zawierać komentarz wyjaśniający wyrażenie regularne."""

odpowiedzi = []
for i, prompt in enumerate([PROMPT_1, PROMPT_2, PROMPT_3], start=1):
    odp = zapytaj(prompt)
    odpowiedzi.append(odp)
    print(
        f"\n{'=' * 20} ITERACJA {i} {'=' * 20}\nPROMPT:\n{prompt}\n\nODPOWIEDŹ:\n{odp}"
    )
    with open(f"iteracja_{i}.md", "w", encoding="utf-8") as f:
        f.write(f"# Prompt\n\n{prompt}\n\n# Odpowiedź\n\n{odp}\n")

# --- Krok 6: wyciągnij kod z odpowiedzi iteracji 3 do plików ---
bloki = re.findall(r"```(?:python|py)?\s*\n(.*?)```", odpowiedzi[2], re.DOTALL)
funkcja = next(
    (b for b in bloki if "def validate_student_email" in b and "def test_" not in b),
    None,
)
testy = next((b for b in bloki if "def test_" in b), None)

if funkcja is None and testy:  # model dał wszystko w jednym bloku
    idx = testy.find("def test_")
    funkcja, testy = testy[:idx], "import pytest\n\n" + testy[idx:]
    print("\nUWAGA: kod i testy były w jednym bloku - sprawdź pliki ręcznie.")

if funkcja and testy:
    if "validate_email" not in testy:
        testy = "from validate_email import validate_student_email\n" + testy
    with open("validate_email.py", "w", encoding="utf-8") as f:
        f.write(funkcja)
    with open("test_validate_email.py", "w", encoding="utf-8") as f:
        f.write(testy)
    print("\nZapisano validate_email.py i test_validate_email.py -> uruchom: pytest -v")
else:
    print("\nNie znaleziono kodu w odpowiedzi - zapisz pliki ręcznie z iteracja_3.md.")
