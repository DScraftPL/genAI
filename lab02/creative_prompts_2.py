import os
import time

from dotenv import load_dotenv

load_dotenv()

UZYJ_OLLAMA = False  # True = model lokalny zamiast Groq
MODEL_GROQ = "openai/gpt-oss-120b"
MODEL_OLLAMA = "gemma3:1b"  # zmień na model pobrany w Zadaniu 2.1

if not UZYJ_OLLAMA:
    from groq import Groq

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def zapytaj(prompt: str, max_tokens: int = 3000) -> str:
    messages = [{"role": "user", "content": prompt}]
    if UZYJ_OLLAMA:
        import ollama

        return ollama.chat(model=MODEL_OLLAMA, messages=messages)["message"]["content"]
    r = client.chat.completions.create(
        model=MODEL_GROQ, messages=messages, max_tokens=max_tokens
    )
    return r.choices[0].message.content


PROMPTY = {
    "A - biznes": (
        "Wyjaśnij właścicielowi małej firmy, bez wykształcenia technicznego, "
        "czym jest konteneryzacja aplikacji (Docker) i jakie korzyści biznesowe "
        "daje jej wdrożenie. Użyj codziennej analogii i unikaj żargonu "
        "technicznego. Maksymalnie 100 słów."
    ),
    "B - student": (
        "Wyjaśnij studentowi pierwszego roku informatyki, czym jest kontener "
        "Dockera i czym różni się od maszyny wirtualnej. Użyj podstawowych pojęć "
        "z systemów operacyjnych i podaj jedno przykładowe polecenie docker run. "
        "Około 150 słów."
    ),
    "C - administrator": (
        "Przedstaw doświadczonemu administratorowi systemów zwięzłe porównanie "
        "kontenerów i maszyn wirtualnych na poziomie izolacji zasobów "
        "(przestrzenie nazw, cgroups). Wskaż dwa typowe zastosowania produkcyjne "
        "i jedno ryzyko bezpieczeństwa. Około 150 słów, forma zwięzłych akapitów."
    ),
}

wynik = []
for nazwa, prompt in PROMPTY.items():
    start = time.time()
    odp = zapytaj(prompt)
    czas = time.time() - start
    blok = (
        f"=== WERSJA {nazwa} ===\nPROMPT:\n{prompt}\n\n"
        f"ODPOWIEDŹ ({len(odp.split())} słów, {czas:.1f} s):\n{odp}\n"
    )
    print(blok)
    wynik.append(blok)

with open("wyniki_2_6.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(wynik))
print("Zapisano do wyniki_2_6.txt")
