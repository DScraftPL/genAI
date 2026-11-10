import json
import os
import sys
from dotenv import load_dotenv
from groq import Groq
from pptx import Presentation

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
TEMAT = "Bezpieczne korzystanie z kluczy API"
PROMPT_KONSPEKTU = (
    'Przygotuj konspekt prezentacji edukacyjnej pt. "'
    + TEMAT
    + '" dla studentów I roku informatyki. Zwróć WYŁĄCZNIE '
    "poprawny JSON, bez żadnego innego tekstu, o strukturze: "
    '{"tytul": "...", "slajdy": [{"tytul": "...", '
    '"punkty": ["...", "..."], "notatka": "..."}]}. '
    "Dokładnie 6 slajdów; 3-4 zwięzłe punkty i 2-zdaniowa "
    "notatka prelegenta na slajd. Zakres: czym jest klucz API, "
    "typowe błędy (klucz w kodzie, publiczne repozytorium), "
    "dobre praktyki (.env, .gitignore, unieważnianie), "
    "podsumowanie."
)
# etap 1: konspekt z modelu (kontrakt JSON, niska temperatura)
r = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": PROMPT_KONSPEKTU}],
    temperature=0.2,
    max_tokens=3000,
    reasoning_effort="low",
    include_reasoning=False,
)
tekst = r.choices[0].message.content.strip()
konspekt = json.loads(tekst)  # walidacja kontraktu
print("Slajdów w konspekcie:", len(konspekt["slajdy"]))
# etap 2: budowa pliku PPTX z konspektu
prezentacja = Presentation()
# slajd tytułowy (układ 0: tytuł + podtytuł)
slajd = prezentacja.slides.add_slide(prezentacja.slide_layouts[0])
slajd.shapes.title.text = konspekt["tytul"]
slajd.placeholders[1].text = "Generatywna sztuczna inteligencja i prompt engineering"
# slajdy treści (układ 1: tytuł + lista punktów)
for dane in konspekt["slajdy"]:
    slajd = prezentacja.slides.add_slide(prezentacja.slide_layouts[1])
    slajd.shapes.title.text = dane["tytul"]
    pole = slajd.placeholders[1].text_frame
    pole.text = dane["punkty"][0]
    for punkt in dane["punkty"][1:]:
        pole.add_paragraph().text = punkt
    # notatka prelegenta
    slajd.notes_slide.notes_text_frame.text = dane["notatka"]

os.makedirs("out", exist_ok=True)
prezentacja.save("out/prezentacja.pptx")
print("Zapisano out/prezentacja.pptx")
