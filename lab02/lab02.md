# Sprawozdanie 

## Generatywna sztuczna inteligencja i Prompt Engineering

## Lab 02 

## Samodzielne zadania:

### Ćwiczenie 2.1

gpt-oss-120b:
```
Transformer to architektura sieci neuronowej, która pozwala modelom językowym efektywnie przetwarzać tekst. Zamiast czytać słowa kolejno, jak w tradycyjnych rekurencyjnych sieciach, transformer jednocześnie patrzy na wszystkiesłowa w zdaniu i ocenia, które z nich są ze sobą powiązane, używając mechanizmu uwagi (attention). Dzięki temu potrafi lepiej rozumieć kontekst i generować płynne, spójne odpowiedzi, a jednocześnie jest szybki w trenowaniu na dużych zbiorach danych. Ta struktura jest podstawą popularnych modeli, takich jak GPT‑3 czy BERT.
```

gemma3:
```
Wyobraź sobie, że model językowy uczy się czytać i rozumieć tekst, analizując wzorce w danych. Transformer to nowa technika, która pomaga mu to zrobić.  Zamiast skupiać się na jednym punkcie, transformer analizuje **wszystkie** słowa w zdaniu jednocześnie, co pozwala mu na lepsze zrozumienie kontekstu.  Dzięki temu model może lepiej przewidywać, co będzie dalej pisać - w efekcie tworzy bardziej spójne i sensowne teksty.
```

llama3.1:
```
Pewnie znałeś już takie modele jak Word2Vec czy BERT, ale Transformer to kolejna generacja modeli, która odniosła ogromny sukces, zwłaszcza w dziedzinie rozumienia tekstu. Jest to model językowy, który działa nieco inaczej niżte z poprzednich generacji. Zamiast korzystać z wewnętrznej reprezentacji słów w postaci wektorów, Transformer używa "pamięci" do przechowywania i aktualizowania reprezentacji. Pozwala to na bardziej efektywne wykorzystanie dostępnych danych i poprawę ogólnej jakości wyników.
```

ChatGPT: 
```
Transformer to architektura sieci neuronowej wykorzystywana w nowoczesnych modelach językowych, takich jak ChatGPT, która pozwala analizować tekst i rozumieć zależności między jego słowami. Jego najważniejszym mechanizmem jest attention (mechanizm uwagi), dzięki któremu model potrafi określić, które słowa w danym kontekście są najważniejsze dla interpretacji pozostałych. Transformer przetwarza słowa równolegle, co pozwala mu uczyć się efektywnie na dużych zbiorach tekstu. Na podstawie poznanych wzorców model może następnie przewidywać kolejne słowa i generować spójne odpowiedzi.
```

| Kryterium | gpt-oss-120b | gemma3 | llama3.1 | chatGPT | 
| - | - | - | - | - |
| Poprawność merytoryczna | 4 | 3 | 2 | 5 | 
| Zgodność z limitem długości (3-4 zdania) | 5 | 5 | 5 | 5 |
| Dostosowanie języka do odbiorcy | 4 | 3 | 3 | 5 |
| Poprawność językowa (polszczyzna) | 3 | 3 | 3 | 3 |
| Czas odpowiedzi [s] | 0.91 | 18.24 | 25.83 | 1 |

P: Który model poradził sobie najlepiej i dlaczego? Czy niższa jakość
odpowiedzi modelu lokalnego jest w tym zadaniu akceptowalna, biorąc pod uwagę
prywatność danych i brak kosztów?

Model lokalny wykonywał się zdecydowanie dłużej, w porównaniu z modelami chmurowymi - jest to spowodowane możliwościami obliczeniowymi. Brak kosztów i prywatność danych to wielka zaleta, ale wymaga to odpowiedniego sprzętu do uruchomienia. 

### Ćwiczenie 2.2 

```
ODPOWIEDZ STUDENT: 
 **Komunikat: Przerwa Techniczna na Platformie E-Learningowej**

**Dzień:** [DATA]

**Czas:** Zaczynamy od [GODZINA ROZPOCZĘCIA] i planujemy zakończyć o [GODZINA ZAKOŃCZENIA]

**Przyчина:**  Aby poprawić, zwiększyć bezpieczeństwo i wydajność naszej platformy e-learningowej, potrzebujemy aktualizacji.  Dzięki tym zmianom, chcemy zapewnić, aby wszyscy studenci mieli łatwy dostęp do materiałów i mogli korzystać z naszych narzędzi.

**Co oznacza to dla Was?**

Od [GODZINY ROZPOCZĘCIA] do [GODZINY ZAKOŃCZENIA] platforma e-learningowa nie będzie dostępna.  To oznacza, że nie będziemy mogli:

*   Otwierać i przeglądać materiały edukacyjne.
*   Uczestniczyć w kursach online.
*   Przejrzeć testy i quizy.

**Jak to się rozwiąże?**

Nasze technicy pracują ciężko, aby naprawić problem.  Więc, bardzo proszę o cierpliwość, aby wszystko poszło dobrze.

**Dziękujemy za zrozumienie i wyrozumiałość!**

Z poważaniem,

Zespół [Nazwa Uczelni]
ODPOWIEDZ LECTURER: 
 **Komunikat o Planowanej Przerwie Technicznej**

**Do:** Kadra Dydaktyczna

**Od:** [Twoje Imię/Nazwa] – Specjalista ds. Komunikacji Technicznej

**Data:** [DATA]

**Temat: Planowana Przerwa Techniczna – Aktualizacja Systemu E-Learning**

Wážení kolegovia,

s ohromující situací, je s velkou mírou smutku, že musíme připomenout, že będziemy v následujících dnech vyhlásit plánovanou przerwę technickou pro platformę e-learningową, s cílem zlepšit její stabilitu a bezpieczeństwo.

**Data:** Przerwa rozpocznie się [DATA] a zakończy się [GODZINA ZAKOŃCZENIA].

**Doba:** Przerva bude trvat [CZAS TRWANIA] hodin.

**Účel:** Tato aktualizace systému má za úkol zameřit běžící problémy a zjednodušit interakce s platformou.  Realizujeme důkladnou aktualizaci, která zahrnuje optimalizaci výkonu a vylepšení uživatelského rozhraní.

**Funkce Platformy Potřeby Obnovení:**

W průběhu této výzvy budou nedostupnější některé klíčové funkce platformy, včetně aktualizace zobrazení, plánování seminářů a úpravy zasílání materiálů.  Přesněji řečeno:

*   Některé funkce, jako je například [KONKRETNE UŻYTKOWANIE] a [INNE UŻYTKOWANÉ FUNKCJE], budou vyžadovat okamžité zobrazení a přístup.
*   Sestavení a zobrazení rozsáhlých seznamů a prezentací nebude možné.

**Dopłady:**

Prosíme Vás o pozornou pozornost na následující:

*   Předběžné načtení, dohledání a přizpůsobení potřebných materiálů a předpřipravených prezentací.
*   Kontrola a úprava plánů a rozvrhů předchozích seminářů a úvodů.
*   Zajistěte, aby byly všechny zadané materiály a přístup k platformě dostupné do [DATUM] pro všechny požadované osoby.

Vaše spolupráce a pochopení jsou pro nás zásadní. V případě jakýchkoliv dotazů nebo sazených otázek se nebojte kontaktovat mě na [ADRESZA E-MAILA] nebo [NUMERO] nebo se obraťte přímo na vedení oddělení, které zprostředkuje práci na této platformě.

S pozdravem,

[Twoje Imię/Nazwa]
Specjalista ds. Komunikací Technicznej

ODPOWIEDZ ADMIN: 
 **Komunikat o Przerwie Serwisowej**

**Temat:** Przerwa serwisowa - Aktualizacja Systemu E-learningowego

**Do:** Administratorzy IT

**Data:** [DATA]

**Godzina rozpoczęcia:** [GODZINA ROZPOCZĘCIA]
**Godzina zakończenia:** [GODZINA ZAKOŃCZENIA]
**Czas trwania:** [CZAS TRWANIA]

**Cel prac:**

Przedstawienie technicznego komunikatu informującego o planowanej przerwie serwisowej, która umożliwi aktualizację systemu e-learningowego oraz poprawę jego stabilności, z uwzględnieniem wpływu na dostępność platformy do użytkowników.

**Przewidywany wpływ na dostępność platformy:**

Przerwa serwisowa na Platformie E-learningowej zakończy się przerywem dostępu do wszystkich modułów.  W związku z tym, użytkownicy będą mieli ograniczony dostęp do platformy do:

*   **Wprowadzenia i przeglądania materiałów:** Brak możliwości interakcji z materiałami.
*   **Uczestnictwa w ćwiczeniach:** Brak możliwości uczestnictwa w ćwiczeniach.
*   **Możliwości moderowania:**  Ograniczony dostęp do moderowania materiałów.
*   **Funkcji diagnostycznych:**  Zazwyczaj brak możliwości przeprowadzenia diagnozy.

Projektujemy minimalny czas przerwania dostępu, który pozwoli na usunięcie problemów programowych, które zidentyfikowaliśmy w procesie aktualizacji. 

**Kluczowe czynności operacyjne do rozważenia:**

1.  **Weryfikacja Kopii Zapasowych:** Upewnij się, że kopie zapasowe wszystkich głównych modułów i danych użytkowników są w pełni testowane i dostępne.
2.  **Monitorowanie Usług:**  Utrzymuj stały monitoring usług wszystkich komponentów systemu (np. serwer, baza danych, komponenty oprogramowania).  Zwróć szczególną uwagę na kluczowe usługi związane z platformą (np. usługi raportowania, integracja z systemami zewnętrznymi).
3.  **Testy Poprawności Działania:** Przeprowadź testy poprawności działania wszystkich aktualizowanych komponentów systemu.  W celu weryfikacji, czy dane użytkowników są prawidłowo przekazywane.
4.  **Testy Integracyjne:**  Przeprowadź testy integracyjne między głównymi modułami platformy (np. moduł komunikacji z systemami zewnętrznymi).
5.  **Ustawienie Alarmów:**  Ustaw alarmy w systemie monitoringowym, aby w razie problemów, automatycznie uruchomić procedury odzyskiwania.
6.  **Komunikacja z Użytkownikami:** Przesyłanie poufnych komunikatów z informacją o przerywie, co najmniej 24 godziny przed rozpoczęciem.

**Uwaga:**  Przerwa serwisowa będzie trwała około [CZAS TRWANIA] godzin.  W przypadku wystąpienia problemów, zespół IT będzie na bieżąco monitorował sytuację i w razie potrzeby poddaje się zmianom planu.

```

### Ćwiczenie 2.3 

```
# ROLA
Jesteś asystentem badawczym specjalizującym się w przeglądach literatury
naukowej z dziedziny informatyki. Pracujesz precyzyjnie i nie domyślasz się
informacji, których nie ma w tekście.

# KONTEKST
Użytkownik pisze przegląd literatury do pracy dyplomowej. Z każdego
abstraktu potrzebuje ustrukturyzowanych danych, które trafią do tabeli
porównawczej.

# ZADANIE
Przeanalizuj abstrakt podany w sekcji DANE i wyodrębnij z niego informacje
zgodnie ze schematem z sekcji FORMAT.

# ZASADY
1. Korzystaj WYŁĄCZNIE z informacji zawartych w abstrakcie.
2. Jeśli informacji brak, wpisz "nie_podano". Nie zgaduj i nie uzupełniaj
   wiedzą ogólną.
3. Wartości liczbowe (metryki, rozmiary zbiorów) przepisuj dokładnie.
4. Pole "dowod" musi zawierać dosłowny fragment abstraktu (max 20 słów)
   uzasadniający pole "wyniki".
5. Odpowiadaj po polsku, ale terminy techniczne i nazwy własne zostaw
   w oryginale.
6. Zwróć wyłącznie obiekt JSON, bez komentarza i bez znaczników markdown.

# FORMAT
{
  "cel": "jedno zdanie",
  "metoda": "jedno zdanie",
  "dane": "nazwa/opis zbioru danych lub 'nie_podano'",
  "wyniki": "kluczowy wynik, z liczbami jeśli podano",
  "ograniczenia": "wymienione ograniczenia lub 'nie_podano'",
  "dowod": "dosłowny cytat z abstraktu",
  "pewnosc": "wysoka | srednia | niska"
}

# PRZYKŁAD
Abstrakt: "We propose a CNN-based classifier for detecting pneumonia in
chest X-rays. Trained on 5,856 images from the Kermany dataset, the model
achieves 92.4% accuracy. Limited to pediatric patients."
Odpowiedź:
{
  "cel": "Wykrywanie zapalenia płuc na zdjęciach rentgenowskich klatki piersiowej.",
  "metoda": "Klasyfikator oparty na konwolucyjnej sieci neuronowej (CNN).",
  "dane": "Zbiór Kermany, 5856 obrazów",
  "wyniki": "Dokładność (accuracy) 92,4%",
  "ograniczenia": "Ograniczenie do pacjentów pediatrycznych",
  "dowod": "the model achieves 92.4% accuracy",
  "pewnosc": "wysoka"
}

# DANE
Abstrakt:
"""
{{WKLEJ_ABSTRAKT}}
"""
```