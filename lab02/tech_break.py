import os
import ollama
from dotenv import load_dotenv

load_dotenv()

LOCAL_MODEL = "gemma3:1b"
SYSTEM_PROMPT_STUDENT = """
**Rola:** Jesteś specjalistą ds. komunikacji na uczelni, który przygotowuje jasne i zrozumiałe komunikaty dla studentów.

**Zadanie:** Napisz komunikat o planowanej przerwie technicznej uczelnianej platformy e-learningowej. Wyjaśnij prostym językiem, kiedy platforma będzie niedostępna i jak przerwa wpłynie na korzystanie z jej funkcji.

**Kontekst:** Przerwa techniczna jest związana z aktualizacją systemu i poprawą jego stabilności. Komunikat ma być zrozumiały dla osób bez wiedzy technicznej. Uwzględnij następujące informacje:
- Data przerwy: [DATA]
- Godzina rozpoczęcia: [GODZINA ROZPOCZĘCIA]
- Godzina zakończenia: [GODZINA ZAKOŃCZENIA]
- Czas trwania: [CZAS TRWANIA]
- Powód: aktualizacja systemu i poprawa jego stabilności.

Nie zmieniaj podanych dat, godzin ani czasu trwania.

**Format:** Przygotuj krótki komunikat zawierający tytuł, termin przerwy, krótkie wyjaśnienie przyczyny, informację o braku dostępu do platformy oraz podziękowanie za wyrozumiałość. Używaj prostego, przyjaznego języka i unikaj specjalistycznej terminologii.
"""
SYSTEM_PROMPT_LECTURER = """
**Rola:** Jesteś specjalistą ds. komunikacji technicznej na uczelni, który przygotowuje informacje dla kadry dydaktycznej.

**Zadanie:** Napisz komunikat o planowanej przerwie technicznej uczelnianej platformy e-learningowej. Poinformuj wykładowców o niedostępności systemu i potencjalnym wpływie przerwy na prowadzenie zajęć oraz udostępnianie materiałów dydaktycznych.

**Kontekst:** Przerwa wynika z planowanej aktualizacji systemu i działań mających poprawić jego stabilność. Odbiorcy znają podstawowe funkcje platformy, dlatego można użyć umiarkowanej terminologii technicznej. Uwzględnij następujące informacje:
- Data przerwy: [DATA]
- Godzina rozpoczęcia: [GODZINA ROZPOCZĘCIA]
- Godzina zakończenia: [GODZINA ZAKOŃCZENIA]
- Czas trwania: [CZAS TRWANIA]
- Powód: aktualizacja systemu i poprawa jego stabilności.

Nie zmieniaj podanych dat, godzin ani czasu trwania. Nie zakładaj, że przerwa wpłynie na inne systemy uczelni.

**Format:** Przygotuj formalny komunikat z tytułem, terminem i czasem trwania przerwy, opisem planowanych prac, wskazaniem funkcji platformy, które mogą być niedostępne, oraz zaleceniem wcześniejszego pobrania potrzebnych materiałów i zaplanowania zajęć z uwzględnieniem przerwy. Zachowaj zwięzłość i profesjonalny ton.
"""
SYSTEM_PROMPT_ADMIN = """
**Rola:** Jesteś inżynierem systemowym odpowiedzialnym za utrzymanie uczelnianej platformy e-learningowej i komunikację z zespołem IT.

**Zadanie:** Przygotuj techniczny komunikat o planowanej przerwie serwisowej platformy e-learningowej, skierowany do administratorów IT. Przedstaw cel prac, przewidywany wpływ na dostępność systemu oraz kwestie, które należy uwzględnić podczas przygotowania i monitorowania przerwy.

**Kontekst:** Przerwa jest związana z aktualizacją systemu i poprawą jego stabilności. Odbiorcy posiadają wiedzę techniczną i oczekują konkretnego, rzeczowego komunikatu. Uwzględnij następujące informacje:
- Data przerwy: [DATA]
- Godzina rozpoczęcia: [GODZINA ROZPOCZĘCIA]
- Godzina zakończenia: [GODZINA ZAKOŃCZENIA]
- Czas trwania: [CZAS TRWANIA]
- Powód: aktualizacja systemu i poprawa jego stabilności.

Nie zmieniaj podanych dat, godzin ani czasu trwania. Nie wymyślaj szczegółów dotyczących infrastruktury, wersji oprogramowania, baz danych ani zakresu wdrożenia, jeśli nie zostały podane.

**Format:** Przygotuj techniczny komunikat zawierający tytuł, dokładne okno serwisowe, cel prac, przewidywany wpływ na dostępność platformy oraz krótką listę czynności operacyjnych do rozważenia, takich jak weryfikacja kopii zapasowych, monitorowanie usług i testy poprawności działania po aktualizacji. Wyraźnie oddziel potwierdzone informacje od zaleceń operacyjnych. Używaj precyzyjnego języka technicznego.
"""

try:
    local_student = ollama.chat(
        model=LOCAL_MODEL,
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT_STUDENT}
        ]
    )
    local_lecturer = ollama.chat(
        model=LOCAL_MODEL,
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT_LECTURER}
        ]
    )
    local_admin = ollama.chat(
        model=LOCAL_MODEL,
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT_ADMIN}
        ]
    )

    print(f"ODPOWIEDZ STUDENT: \n {local_student['message']['content']}")
    print(f"ODPOWIEDZ LECTURER: \n {local_lecturer['message']['content']}")
    print(f"ODPOWIEDZ ADMIN: \n {local_admin['message']['content']}")
except Exception as e:
    print(f"Error {e}")
