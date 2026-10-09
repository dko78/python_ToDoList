from pathlib import Path
import os
from pathlib import Path

contents = [
    "All carrots are to be sliced longitudinally.",
    "The carrots were reportedly sliced.",
    "The slicing process was well presented."
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

print("Trenutni radni folder (cwd):", os.getcwd())
print("Folder gdje je skripta:", Path(__file__).resolve().parent)
print("Apsolutna putanja skripte:", Path(__file__).resolve())

# Čita se ovako:
# Path(__file__) -> putanja trenutne .py datoteke
# .resolve() -> pretvori u punu apsolutnu putanju
# .parent.parent -> idi dva nivoa gore
# / "Files" -> dodaj podfolder Files
# Dakle base postaje putanja do Files foldera.

# zatim:
# base.mkdir(parents=True, exist_ok=True) -> kreiraj taj folder (i roditelje ako trebaju), bez greške ako već postoji.

base = Path(__file__).resolve().parent.parent / "Files"
print('Base je:', base)
base.mkdir(parents=True, exist_ok=True)

for filename, content in zip(filenames, contents):
    with open(base / filename, "w", encoding="utf-8") as f:
        f.write(content)