import os

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "qwen/qwen3.8-27b"  # rozumowanie wyłączone (reasoning_effort='none')
MODEL_LOKALNY = "llama3.1"  # model lokalny (Ollama)

ZADANIA = {
    "A - zlozonosc algorytmu": (
        "Wyznacz złożoność czasową poniższego kodu:\n"
        "for i in range(n):\n"
        "    for j in range(i):\n"
        "        op()"
    ),
    "B - zadanie tekstowe": (
        "Do pracowni zamówiono 4 zestawy po 6 "
        "komputerów. Pięć komputerów okazało się "
        "wadliwych i je zwrócono, a następnie "
        "domówiono połowę liczby zwróconych "
        "(zaokrąglając w górę). Ile komputerów "
        "trafiło ostatecznie do pracowni?"
    ),
}

WARIANTY = {
    "bez CoT": "Podaj samą odpowiedź, bez wyjaśnień.",
    "zero-shot CoT": (
        "Myślmy krok po kroku. Na końcu "
        "podaj odpowiedź w osobnej linii "
        "w formacie: ODPOWIEDŹ: ..."
    ),
}

for nazwa, tresc in ZADANIA.items():
    print(f"\n\n{'#' * 64}")
    print(f"### ZADANIE {nazwa}")
    print("#" * 64)
    for opis, dopisek in WARIANTY.items():
        prompt = f"{tresc}\n{dopisek}"
        print(f"\n--- wariant: {opis} ---")
        try:
            r = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=800,
                reasoning_effort="none",
            )
            print(r.choices[0].message.content.strip())  # type: ignore
            tok_wy = r.usage.completion_tokens  # type: ignore
            print(f">>> tokeny wyjsciowe: {tok_wy}")
        except APIError as e:
            # np. blad 429 (limit zapytan) lub problem z kluczem
            print(f"[Blad Groq API] {e}")
            # awaryjne uzycie modelu lokalnego (Ollama)
            lok = ollama.generate(
                model=MODEL_LOKALNY,
                prompt=prompt,
                options={"temperature": 0.0, "num_predict": 800},
            )
            print(f"--- odpowiedz modelu lokalnego: {MODEL_LOKALNY} ---")
            print(lok["response"].strip())
            print(f">>> tokeny wyjsciowe: {lok['eval_count']}")
