import os
from dotenv import load_dotenv
from groq import APIError, Groq

# wczytanie klucza z pliku .env do zmiennej srodowiskowej
load_dotenv()
# odczyt klucza API z pliku .env
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise SystemExit(
        'Nie znaleziono klucza. Sprawdz, czy plik .env znajduje sie w tym katalogu i czy zawiera GROQ_API_KEY.')

client = Groq(api_key=api_key)
response_1 = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {'role': 'system', 'content': 'Odpowiadaj zwiezle, w jezyku polskim.'},
        {'role': 'user', 'content': 'Witaj! Kim jesteś? Opisz krótko swoje możliwości.'},
    ],
    temperature=0.0,
    max_tokens=1000,
)

response_2 = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {'role': 'system', 'content': 'Odpowiadaj zwiezle, w jezyku polskim.'},
        {'role': 'user', 'content': 'Witaj! Kim jesteś? Opisz krótko swoje możliwości.'},
    ],
    temperature=0.7,
    max_tokens=1000,
)

response_3 = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {'role': 'system', 'content': 'Odpowiadaj zwiezle, w jezyku polskim.'},
        {'role': 'user', 'content': 'Witaj! Kim jesteś? Opisz krótko swoje możliwości.'},
    ],
    temperature=1.5,
    max_tokens=1000,
)

print("# ZADANIE 1")
print("## TEMPERATURE 0.0")
print(response_1.choices[0].message.content)
print("## TEMPERATURE 0.7")
print(response_2.choices[0].message.content)
print("## TEMPERATURE 1.5")
print(response_3.choices[0].message.content)

print("# ZADANIE 2")
print("'koniec' konczy interakcje")

input_prompt = input("Zapytaj modelu:")

while(input_prompt != 'koniec'):
    try:
        response_input = client.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=[
                {'role': 'system', 'content': 'Odpowiadaj zwiezle, w jezyku polskim.'},
                {'role': 'user', 'content': input_prompt},
            ],
            temperature=1.5,
            max_tokens=1000,
        )

        print(response_input.choices[0].message.content)
        input_prompt = input("Zapytaj modelu:")
    except APIError:
        print("Blad API")

print("# ZADANIE 3")

input_prompt = "Wyjaśnij mi, krótko, jak działa ChatGPT"

response_tech = client.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=[
                {'role': 'system', 'content': 'Jesteś ekspertem technicznym, ale nie lubisz odpowiadać na pytania.'},
                {'role': 'user', 'content': input_prompt},
            ],
            temperature=1.5,
            max_tokens=1000,
        )

response_teacher = client.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=[
                {'role': 'system', 'content': 'Jesteś nauczycielem, który tłumaczy cierpliwie i prostym językiem skomplikowane zagadnienia.'},
                {'role': 'user', 'content': input_prompt},
            ],
            temperature=1.5,
            max_tokens=1000,
        )

print("## ODP TECH EXPERT:")
print(response_tech.choices[0].message.content)
print()

print("## ODP NAUCZYCIEL:")
print(response_teacher.choices[0].message.content)
print()

print("## USAGE TECH EXPERT:")
print(response_tech.usage)

print("## USAGE NAUCZYCIEL:")
print(response_teacher.usage)