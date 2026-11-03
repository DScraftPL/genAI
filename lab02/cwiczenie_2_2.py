import os
import sys

from dotenv import load_dotenv
from groq import APIError, Groq

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

MODEL = "openai/gpt-oss-120b"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPTY = {
    "STUDENCI": """
ROLA:
Jesteś pracownikiem uczelni odpowiedzialnym za komunikację ze studentami.

ZADANIE:
Napisz komunikat dla studentów o planowanej przerwie technicznej platformy e-learningowej.

KONTEKST:
Przerwa rozpocznie się 7 listopada 2026 r. o 22:00 i zakończy 8 listopada 2026 r. o 02:00. Potrwa 4 godziny. Platforma będzie niedostępna z powodu aktualizacji systemu i prac przy bazie danych. Przed przerwą należy zapisać pracę i wylogować się.

FORMAT:
Zwróć wyłącznie gotowy komunikat: tytuł i krótki akapit, maksymalnie 60 słów. Użyj prostego języka, bez szczegółów technicznych. Podaj daty i godziny rozpoczęcia oraz zakończenia przerwy, czas trwania i zalecenie zapisania pracy oraz wylogowania się.
""".strip(),
    "WYKŁADOWCY": """
ROLA:
Jesteś pracownikiem uczelni odpowiedzialnym za wsparcie wykładowców korzystających z platformy e-learningowej.

ZADANIE:
Napisz komunikat dla wykładowców o planowanej przerwie technicznej platformy e-learningowej.

KONTEKST:
Przerwa rozpocznie się 7 listopada 2026 r. o 22:00 i zakończy 8 listopada 2026 r. o 02:00. Potrwa 4 godziny. Platforma będzie niedostępna z powodu aktualizacji systemu i prac przy bazie danych. Przed przerwą należy zapisać pracę i wylogować się.

FORMAT:
Zwróć wyłącznie gotowy komunikat: tytuł i krótki akapit, maksymalnie 90 słów. Użyj formalnego języka i krótko podaj przyczynę przerwy, bez szczegółów administracyjnych. Podaj daty i godziny rozpoczęcia oraz zakończenia przerwy i czas trwania. Przypomnij o wcześniejszym zapisaniu materiałów, wylogowaniu się i uwzględnieniu przerwy przy planowaniu aktywności dydaktycznych.
""".strip(),
    "ADMINISTRATORZY IT": """
ROLA:
Jesteś administratorem uczelnianej platformy e-learningowej informującym zespół IT o pracach serwisowych.

ZADANIE:
Napisz komunikat techniczny dla administratorów IT o planowanej przerwie platformy e-learningowej.

KONTEKST:
Przerwa rozpocznie się 7 listopada 2026 r. o 22:00 i zakończy 8 listopada 2026 r. o 02:00. Potrwa 4 godziny. Platforma będzie niedostępna z powodu aktualizacji systemu i prac przy bazie danych. Przed przerwą należy zapisać pracę i wylogować się.

FORMAT:
Zwróć wyłącznie gotowy komunikat: tytuł i punkty, maksymalnie 130 słów. Użyj technicznego języka. Podaj daty i godziny rozpoczęcia oraz zakończenia przerwy, czas trwania, zakres prac i wpływ na dostępność platformy. Uwzględnij wcześniejsze zapisanie pracy i wylogowanie użytkowników. Zaleć kontrolę logowania i dostępu do kursów po zakończeniu prac. Nie wymyślaj wersji oprogramowania ani dodatkowych prac serwisowych.
""".strip(),
}

for odbiorca, prompt in PROMPTY.items():
    print(f"\n=== {odbiorca} ===")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1000,
            reasoning_effort="low",
        )
        print(response.choices[0].message.content)
    except APIError as blad:
        print(f"[Błąd Groq API] {blad}")
    except Exception as blad:
        print(f"[Błąd] {blad}")
