import os
import time

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

load_dotenv()

MODEL_ZEWNETRZNY = "openai/gpt-oss-120b"
MODEL_LOKALNY = "llama3.1"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPTY = [
    "Przygotuj analizę transportu produktów mrożonych w mieście.",
    """
Przygotuj analizę miejskiego transportu produktów mrożonych samochodem Toyota Proace City Long bez agregatu chłodniczego. Trasa trwa 6 godzin i obejmuje 100 adresów. Przy każdym adresie drzwi przestrzeni ładunkowej są otwarte przez 20 sekund. Temperatura otoczenia wynosi 15°C. Produkty mają początkowo -22°C i muszą zachować temperaturę nie wyższą niż -18°C. Produkty są przewożone w pojemnikach EPS 12 l z jednym wkładem PCM o temperaturze przemiany fazowej -21°C. Oblicz łączny czas otwarcia drzwi, oceń główne ryzyka cieplne i zaproponuj usprawnienia.
""".strip(),
    """
ROLA:
Jesteś inżynierem logistyki i chłodnictwa projektującym transport ostatniej mili dla mrożonej żywności.

ZADANIE:
Wykonaj wstępną analizę organizacyjną i cieplną przewozu oraz oceń, czy przyjęta koncepcja wymaga dalszych badań przed wdrożeniem.

KONTEKST:
Projekt dotyczy miejskiej dystrybucji produktów mrożonych w systemie e-commerce. Samochód nie ma agregatu chłodniczego, a podstawową ochronę zapewniają indywidualne pojemniki EPS z wkładami PCM.

DANE:
###
Pojazd: Toyota Proace City Long 2025
Czas trasy: 6 godzin
Liczba adresów: 100
Średni czas jednego otwarcia drzwi: 20 sekund
Temperatura otoczenia: 15°C
Temperatura początkowa produktu: -22°C
Najwyższa dopuszczalna temperatura produktu: -18°C
Opakowanie: pojemnik EPS 12 l
Wkład chłodzący: jeden wkład PCM, temperatura przemiany fazowej -21°C
###

FORMAT:
1. Krótko opisz problem.
2. Oblicz łączny czas otwarcia drzwi w sekundach i minutach oraz jego udział procentowy w czasie trasy.
3. W tabeli wskaż źródła dopływu ciepła, ich możliwe skutki i sposoby ograniczenia.
4. Wymień dane brakujące do pełnego bilansu cieplnego.
5. Podaj pięć konkretnych zaleceń organizacyjnych lub technicznych.
6. Zakończ jednoznacznym wnioskiem, czy na podstawie podanych danych można potwierdzić utrzymanie temperatury -18°C przez całą trasę.

Nie wymyślaj brakujących parametrów. Wyraźnie oddziel obliczenia od założeń i ocen jakościowych. Użyj prostego języka technicznego.
""".strip(),
]

DOKUMENTACJA = [
    (
        "1",
        "Brak danych liczbowych, limitu temperatury, rodzaju pojazdu i formatu odpowiedzi.",
        "Dodano dane trasy, temperatury, pojazd, opakowanie i wymagane obliczenia.",
    ),
    (
        "2",
        "Brak jasno określonej roli, listy brakujących danych i zakazu wymyślania parametrów.",
        "Dodano pełną strukturę promptu, delimitery, kolejność odpowiedzi i regułę niewymyślania danych.",
    ),
    (
        "3",
        "Brak istotnych braków w strukturze promptu.",
        "Wersja finalna.",
    ),
]


def uruchom_groq(prompt):
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=MODEL_ZEWNETRZNY,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=1400,
    )
    czas = time.perf_counter() - start
    return response.choices[0].message.content, czas


def uruchom_ollama(prompt):
    start = time.perf_counter()
    response = ollama.chat(
        model=MODEL_LOKALNY,
        messages=[{"role": "user", "content": prompt}],
    )
    czas = time.perf_counter() - start
    return response["message"]["content"], czas


for numer, prompt in enumerate(PROMPTY, start=1):
    print(f"\n{'=' * 64}\nITERACJA {numer}\n{'=' * 64}")
    print(f"PROMPT:\n{prompt}\n")
    try:
        odpowiedz, czas = uruchom_groq(prompt)
        print(f"ODPOWIEDŹ {MODEL_ZEWNETRZNY}:\n{odpowiedz}")
        print(f"Czas odpowiedzi: {czas:.2f} s")
    except APIError as blad:
        print(f"[Błąd Groq API] {blad}")
    except Exception as blad:  # noqa: BLE001
        print(f"[Błąd modelu zewnętrznego] {blad}")

print(f"\n{'=' * 64}\nTABELA ITERACJI\n{'=' * 64}")
print("Iteracja | Zidentyfikowane braki | Zmiana wprowadzona w prompcie")
for iteracja, braki, zmiana in DOKUMENTACJA:
    print(f"{iteracja} | {braki} | {zmiana}")

print(f"\n{'=' * 64}\nTEST FINALNEGO PROMPTU NA MODELU LOKALNYM\n{'=' * 64}")
try:
    odpowiedz, czas = uruchom_ollama(PROMPTY[-1])
    print(f"ODPOWIEDŹ {MODEL_LOKALNY}:\n{odpowiedz}")
    print(f"Czas odpowiedzi: {czas:.2f} s")
except Exception as blad:  # noqa: BLE001
    print(f"[Błąd modelu lokalnego] {blad}")
