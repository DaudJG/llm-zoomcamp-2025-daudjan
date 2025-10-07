from pathlib import Path
import requests, json

DATA_URL = "https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json"
DATA_PATH = Path("01-intro-rag/data/documents.json")

def download_data(url: str = DATA_URL, save_path: Path = DATA_PATH):
    save_path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    docs = response.json()
    save_path.write_text(json.dumps(docs, indent=2))
    print(f"Saved {len(docs)} courses to {save_path.resolve()}")

if __name__ == "__main__":
    download_data()
