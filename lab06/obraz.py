import base64
import io
import os
import sys
import requests
from dotenv import load_dotenv
from PIL import Image

# poprawne wyswietlanie polskich znakow w konsoli Windows
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
KONTO = os.getenv("CF_ACCOUNT_ID")
TOKEN = os.getenv("CF_API_TOKEN")
# model generowania obrazow w Cloudflare Workers AI (darmowy limit dzienny)
MODEL_OBRAZU = "@cf/black-forest-labs/flux-1-schnell"
URL = f"https://api.cloudflare.com/client/v4/accounts/{KONTO}/ai/run/{MODEL_OBRAZU}"
# FLUX najlepiej rozumie prompty po angielsku.
# Tlumaczenie: Fotorealistyczne zdjecie rudego kota spiacego na stercie
# starych ksiazek w bibliotece uniwersyteckiej. Cieple popoludniowe
# swiatlo z wysokiego okna, kadr z poziomu blatu, zblizenie,
# plytka glebia ostrosci.
PROMPT_SCENY = (
    "Photorealistic photo of a ginger cat sleeping on a pile of "
    "old books in a university library. Warm afternoon light from "
    "a high window, shot from desk level, close-up, shallow depth"
    "of field."
)


def generuj_obraz(prompt, plik_wy):
    """Generuje obraz z opisu sceny i zapisuje go do PNG.
    Zwraca True, gdy obraz zostal zapisany."""
    if not KONTO or not TOKEN:
        print("Brak CF_ACCOUNT_ID lub CF_API_TOKEN w pliku .env")
        return False
    try:
        r = requests.post(
            URL,
            headers={"Authorization": f"Bearer {TOKEN}"},
            json={"prompt": prompt, "steps": 4},
            timeout=120,
        )
    except requests.RequestException as e:
        print(f"Brak polaczenia z Cloudflare: {e}")
        return False
    if r.status_code != 200:
        # np. 401/403 - token, 429 - wyczerpany dzienny limit
        print(f"Blad {r.status_code}: {r.text[:300]}")
        return False
    # odpowiedz: {"result": {"image": "<obraz zakodowany w base64>"}, ...}
    dane = base64.b64decode(r.json()["result"]["image"])
    Image.open(io.BytesIO(dane)).save(plik_wy)
    print("Zapisano", plik_wy)
    return True


if __name__ == "__main__":
    os.makedirs("out", exist_ok=True)
    # A: prompt ogolny - decyzje podejmuje model
    generuj_obraz("cat in a library", "out/kot_ogolny.png")
    # B: pelny opis sceny (anatomia promptu obrazowego)
    generuj_obraz(PROMPT_SCENY, "out/kot_scena.png")
