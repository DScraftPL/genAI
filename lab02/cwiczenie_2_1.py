import os
import sys
import time

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

MODEL_ZEWNETRZNY = "openai/gpt-oss-120b"
MODELE_LOKALNE = ("llama3.1", "gemma3:1b")

PROMPT = (
    "Jesteś ekspertem od sztucznej inteligencji. "
    "Wyjaśnij w 3-4 zdaniach, czym jest transformer "
    "w kontekście modeli językowych. Użyj prostego języka, "
    "zrozumiałego dla studenta pierwszego roku informatyki."
)


def uruchom_groq():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=MODEL_ZEWNETRZNY,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0.7,
        max_tokens=1000,
    )
    czas = time.perf_counter() - start
    return response.choices[0].message.content, czas


def uruchom_ollama(model):
    start = time.perf_counter()
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
    )
    czas = time.perf_counter() - start
    return response["message"]["content"], czas


wyniki = []

try:
    odpowiedz, czas = uruchom_groq()
    wyniki.append((MODEL_ZEWNETRZNY, odpowiedz, czas))
except APIError as blad:
    print(f"[Błąd Groq API] {blad}")
except Exception as blad:
    print(f"[Błąd modelu {MODEL_ZEWNETRZNY}] {blad}")

for model in MODELE_LOKALNE:
    try:
        odpowiedz, czas = uruchom_ollama(model)
        wyniki.append((model, odpowiedz, czas))
    except Exception as blad:
        print(f"[Błąd modelu {model}] {blad}")

for model, odpowiedz, czas in wyniki:
    print(f"\n=== {model} ===")
    print(odpowiedz)
    print(f"Czas odpowiedzi: {czas:.2f} s")

czasy = {model: czas for model, _, czas in wyniki}
print(
    "Czas odpowiedzi [s];"
    f"{czasy.get(MODEL_ZEWNETRZNY, 0):.2f};"
    f"{czasy.get('llama3.1', 0):.2f};"
    f"{czasy.get('gemma3:1b', 0):.2f};-"
)
