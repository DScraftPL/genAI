import os

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"
# ceny platnej warstwy API w USD za 1 mln tokenow (stan na 2026 r.)
CENA_WE = 0.15
CENA_WY = 0.60
PROMPT = (
    "Jesteś ekspertem od sztucznej inteligencji i doświadczonym "
    "wykładowcą akademickim. Wyjaśnij w 5-6 zdaniach, czym jest "
    "przeuczenie (overfitting) w uczeniu maszynowym. Użyj prostego "
    "języka, zrozumiałego dla studenta pierwszego roku informatyki, "
    "i unikaj zbędnego żargonu matematycznego. Podaj jeden życiowy "
    "przykład, który pomoże zrozumieć to zjawisko, na przykład "
    "porównanie do nauki na pamięć pytań z poprzednich egzaminów. "
    "Na końcu wymień dwie popularne metody zapobiegania przeuczeniu "
    "i opisz każdą jednym krótkim zdaniem. Odpowiedź napisz po "
    "polsku, w formie zwartego tekstu bez nagłówków i wypunktowań, "
    "a nowe pojęcia angielskie podawaj w nawiasach. Zachowaj "
    "rzeczowy, ale przyjazny ton i nie dodawaj żadnych zbędnych "
    "wstępów ani podsumowań."
)
try:
    # wyslanie zadania i odczyt statystyk z pola usage
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0.7,
        max_tokens=1000,
    )
    print(response.choices[0].message.content)
    assert response.usage is not None
    tok_we = response.usage.prompt_tokens
    assert response.usage is not None
    tok_wy = response.usage.completion_tokens
    print(f"Tokeny wejsciowe: {tok_we} | tokeny wyjsciowe: {tok_wy}")
    # szacunkowy koszt pojedynczego zapytania
    koszt = (tok_we * CENA_WE + tok_wy * CENA_WY) / 1_000_000
    print(f"Szacunkowy koszt zapytania: {koszt:.6f} USD")
except APIError as e:
    # np. blad 429 (przekroczony limit zapytan) lub problem z kluczem/siecia
    print(f"[Blad Groq API] {e}")

# porownanie tokenizacji: polski vs angielski
zdania = {
    "PL": "Sztuczna inteligencja zmienia współczesną informatykę.",
    "EN": "Artificial intelligence is changing modern computing.",
}
for jezyk, tekst in zdania.items():
    r = client.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": tekst}], max_tokens=1
    )

    assert r.usage is not None
    print(f"{jezyk}: {r.usage.prompt_tokens} tokenów |{len(tekst)} znaków")

# tokeny w modelu lokalnym (Ollama)
local = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": PROMPT}])
print("Tokeny wejściowe (Ollama):", local["prompt_eval_count"])
print("Tokeny wyjściowe (Ollama):", local["eval_count"])
