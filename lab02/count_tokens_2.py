import os
import time

import ollama
from dotenv import load_dotenv
from groq import APIError, Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# nazwy modeli w jednym miejscu - latwiej je podmienic, gdy dostawca
# wycofa model (patrz uwaga pod skryptem)
MODEL = "openai/gpt-oss-120b"
MODEL_LOKALNY = "llama3.1"
PROMPT = (
    "Jesteś ekspertem od sztucznej inteligencji. Wyjaśnij w 3-4 zdaniach, "
    "czym jest transformer w kontekście modeli językowych. Użyj prostego "
    "języka, zrozumiałego dla studenta pierwszego roku informatyki."
)


def wypisz_tokeny(prompt_tok, completion_tok, czas):
    """Wypisuje zuzycie tokenow i szybkosc generowania."""
    if prompt_tok is None or completion_tok is None:
        print("Tokeny: brak danych o zuzyciu")
        return
    razem = prompt_tok + completion_tok
    tps = completion_tok / czas if czas > 0 else 0
    print(f"Tokeny: prompt={prompt_tok}, odpowiedz={completion_tok}, razem={razem}")
    print(f"Szybkosc: {tps:.1f} tokenow/s (wliczajac opoznienie sieci/ladowania)")


# --- model zewnetrzny: Groq (API) ---
print(f"=== {MODEL} (model zewnetrzny) ===")
try:
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0.7,
        max_tokens=1000,
    )
    t_groq = time.perf_counter() - start
    print(response.choices[0].message.content)
    print(f"Czas odpowiedzi: {t_groq:.2f} s")

    usage = response.usage
    wypisz_tokeny(usage.prompt_tokens, usage.completion_tokens, t_groq)

    # gpt-oss to model "rozumujacy" - tokeny rozumowania wliczaja sie do
    # completion_tokens (i do limitu max_tokens), jesli API je raportuje
    details = getattr(usage, "completion_tokens_details", None)
    reasoning = getattr(details, "reasoning_tokens", None) if details else None
    if reasoning:
        print(f"  w tym tokeny rozumowania: {reasoning}")
except APIError as e:
    # np. blad 429 (przekroczony limit zapytan) lub problem z kluczem/siecia
    print(f"[Blad Groq API] {e}")
    print("Pomijam Groq i przechodze do modelu lokalnego.")

# --- model lokalny: Ollama ---
print(f"\n=== {MODEL_LOKALNY} (model lokalny) ===")
try:
    start = time.perf_counter()
    local = ollama.chat(
        model=MODEL_LOKALNY, messages=[{"role": "user", "content": PROMPT}]
    )
    t_llama = time.perf_counter() - start
    print(local["message"]["content"])
    print(f"Czas odpowiedzi: {t_llama:.2f} s")

    # Ollama zwraca liczniki tokenow w polach prompt_eval_count / eval_count
    wypisz_tokeny(local.get("prompt_eval_count"), local.get("eval_count"), t_llama)
except Exception as e:
    # np. serwer Ollama nie dziala lub brak pobranego modelu
    print(f"[Blad Ollama] {e}")
    print(
        f"Upewnij sie, ze serwer Ollama dziala i model {MODEL_LOKALNY} "
        f"jest pobrany (ollama pull {MODEL_LOKALNY})."
    )
