import os

from obraz import generuj_obraz

# staly przewodnik stylu (po angielsku - FLUX najlepiej rozumie angielski).
# Tlumaczenie: Minimalistyczna plaska ikona w stylu grafiki wektorowej,
# grube zaokraglone kontury, paleta granatowo-biala z jednym pomaranczowym
# akcentem, biale tlo, bez tekstu, bez cieni, kompozycja wysrodkowana.
# Podmiot:
STYL = (
    "Minimalist flat icon in vector graphic style, thick rounded "
    "outlines, navy blue and white palette with a single orange "
    "accent, white background, no text, no shadows, centered "
    " composition. Subject: "
)
# zmienne podmioty serii (laptop z otwartym terminalem,
# chmura obliczeniowa, klucz API)
PODMIOTY = ["a laptop with an open terminal window", "a computing cloud", "an API key"]
os.makedirs("out", exist_ok=True)
for i, podmiot in enumerate(PODMIOTY, start=1):
    print(f"[{i}/{len(PODMIOTY)}] {podmiot}...")
    generuj_obraz(STYL + podmiot, f"out/ikona_{i}.png")
