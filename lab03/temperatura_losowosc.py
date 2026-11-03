import os
import sys

from dotenv import load_dotenv
from groq import APIError, Groq

# poprawne wyswietlanie polskich znakow w konsoli Windows

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# nazwy modeli w jednym miejscu - latwiej je podmienic
MODEL = "qwen/qwen3.8-27b"  # rozumowanie wyłączone (reasoning_effort='none')
MODEL_LOKALNY = "llama3.2"  # model zapasowy (Ollama), gdy Groq nie odpowiada
PROMPT = (
    "Podaj pięć zastosowań sztucznej inteligencji w przemyśle. Odpowiedz krótką listą."
)
TEMPERATURY = [0.0, 0.7, 1.5]
PROBY = 3
for temp in TEMPERATURY:
    print(f"\n\n{'#' * 64}")
    print(f"### TEMPERATURE = {temp}")
    print("#" * 64)
    odpowiedzi = []
    for i in range(1, PROBY + 1):
        try:
            r = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": PROMPT}],
                temperature=temp,
                max_tokens=300,
                reasoning_effort="none",
            )
            tekst = r.choices[0].message.content.strip()
            odpowiedzi.append(tekst)

            print(f"\n--- proba {i} ---")
            print(tekst)
        except APIError as e:
            # np. blad 429 (limit zapytan) lub problem z kluczem
            print(f"[Blad Groq API] {e}")
            # brak odpowiedzi z Groq -> awaryjne uzycie modelu lokalnego
            import ollama

            lok = ollama.generate(
                model=MODEL_LOKALNY,
                prompt=PROMPT,
                options={"temperature": temp, "num_predict": 300},
            )
            tekst = lok["response"].strip()
            odpowiedzi.append(tekst)
            print(f"--- proba {i} (model lokalny: {MODEL_LOKALNY})---")
            print(tekst)
    unikalne = len(set(odpowiedzi))
    print(f"\n>>> Unikalne odpowiedzi: {unikalne} z {len(odpowiedzi)}")
