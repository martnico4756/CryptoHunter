
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime, timezone

SOURCES = {
    "Binance Learn & Earn":
        "https://academy.binance.com/en/learn-and-earn",
}

KEYWORDS = [
    "learn and earn",
    "reward",
    "rewards",
    "quiz",
    "campaign",
]

def inspect(name, url):
    print(f"\nFuente: {name}")
    print(f"Enlace oficial: {url}")

    request = Request(
        url,
        headers={"User-Agent": "CryptoHunter/1.0"}
    )

    try:
        with urlopen(request, timeout=20) as response:
            html = response.read(500000).decode(
                "utf-8", errors="ignore"
            ).lower()

        matches = [word for word in KEYWORDS if word in html]
        print("Palabras encontradas:",
              ", ".join(matches) if matches else "ninguna")
        print("IMPORTANTE: verificar la campaña manualmente.")

    except (HTTPError, URLError, TimeoutError, OSError) as error:
        print("No se pudo revisar automáticamente:", error)

print("=== CRYPTOHUNTER ===")
print("Informe:", datetime.now(timezone.utc).isoformat())

for name, url in SOURCES.items():
    inspect(name, url)

print("\nEste programa busca pistas de recompensas.")
print("No mina Bitcoin ni garantiza ganancias.")
print("Nunca ingreses contraseñas ni claves privadas.")
