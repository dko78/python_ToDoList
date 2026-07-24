from pathlib import Path

contents = [
    "All carrots are to be sliced longitudinally.",
    "The carrots were reportedly sliced.",
    "The slicing process was well presented."
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

base = Path(__file__).resolve().parent.parent / "Files"
base.mkdir(parents=True, exist_ok=True)

for filename, content in zip(filenames, contents):
    with open(base / filename, "w", encoding="utf-8") as f:
        f.write(content)