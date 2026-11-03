import json
import os

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "qwen/qwen3.8-27b"  # rozumowanie wyłączone (reasoning_effort='none')
MODEL_LOKALNY = "llama3.1"  # model lokalny (Ollama)

OGLOSZENIA = [
    (
        "Firma NetSoft z Lublina poszukuje studenta na "
        "praktyki jako junior tester. Mile widziane: "
        "Python i SQL. Wymiar: 2 dni w tygodniu."
    ),
    (
        "Praktyki wakacyjne w dziale IT szpitala "
        "wojewódzkiego - wsparcie helpdesk, wymagana "
        "znajomość systemu Windows. Pełny etat w lipcu."
    ),
    (
        "Startup Medi42 (praca zdalna) przyjmie "
        "praktykanta do zespołu frontend: React oraz "
        "TypeScript. Elastyczne godziny."
    ),
]

POLA = "firma, miasto, stanowisko, technologie (lista), wymiar"

# WARIANT NAIWNY (zero-shot): luzna instrukcja, bez slowa "wylacznie"
# i bez przykladow. Model czesto opakowuje JSON w blok ```json albo
# dodaje komentarz, przez co json.loads sie wywala.
PROMPT_ZERO = (
    "Wyodrębnij z ogłoszenia dane: " + POLA + ". "
    "Jeśli danej brak, wpisz null. "
    "Podaj wynik w formacie JSON.\n"
    'Ogłoszenie: """{tekst}"""'
)

PROMPT_FEW = (
    "Zamieniasz ogłoszenia o praktykach na obiekty "
    "JSON z polami: " + POLA + ". Jeśli danej brak, "
    "wpisz null. Zwracaj wyłącznie JSON.\n"
    'Ogłoszenie: """Biuro projektowe KOMPAS (Lublin) '
    "szuka praktykanta do działu GIS; wymagany "
    'QGIS; 3 dni w tygodniu."""\n'
    'JSON: {"firma": "KOMPAS", "miasto": "Lublin", '
    '"stanowisko": "praktykant GIS", "technologie": '
    '["QGIS"], "wymiar": "3 dni w tygodniu"}\n'
    'Ogłoszenie: """Zdalne praktyki w zespole DevOps '
    'firmy CloudPol: Docker, Linux."""\n'
    'JSON: {"firma": "CloudPol", "miasto": null, '
    '"stanowisko": "praktykant DevOps", '
    '"technologie": ["Docker", "Linux"], '
    '"wymiar": null}\n'
    'Ogłoszenie: """{tekst}"""\n'
    "JSON:"
)


def wyodrebnij(prompt):
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=200,
            reasoning_effort="none",
        )
        return r.choices[0].message.content
    except APIError as e:
        # np. blad 429 (limit zapytan) lub problem z kluczem
        print(f"[Blad Groq API] {e}")
    # awaryjne uzycie modelu lokalnego (Ollama)
    lok = ollama.generate(
        model=MODEL_LOKALNY,
        prompt=prompt,
        options={"temperature": 0.0, "num_predict": 200},
    )
    return lok["response"]


for nazwa, szablon in [("zero-shot", PROMPT_ZERO), ("few-shot", PROMPT_FEW)]:
    print(f"\n\n{'#' * 64}")
    print(f"### WARIANT {nazwa}")
    print("#" * 64)
    poprawne = 0
    for i, tekst in enumerate(OGLOSZENIA, start=1):
        odp = wyodrebnij(szablon.replace("{tekst}", tekst))
        # UWAGA: celowo NIE usuwamy blokow ```json ani prozy wokol JSON.
        # Chcemy zobaczyc, ktory wariant zwraca czysty, parsowalny JSON,
        # a ktory psuje parsowanie dodatkowymi znacznikami/tekstem.
        assert odp is not None
        odp = odp.strip()
        try:
            json.loads(odp)
            status = "OK"
            poprawne += 1
        except json.JSONDecodeError:
            status = "BLAD PARSOWANIA"
        print(f"\nogloszenie {i}: {status}")
        print(odp)
    print(f"\n>>> Parsowalne odpowiedzi: {poprawne} z {len(OGLOSZENIA)}")
