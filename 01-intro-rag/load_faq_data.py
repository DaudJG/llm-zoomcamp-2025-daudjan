from pathlib import Path
from typing import Any, List, Dict
import requests
import json

DATA_URL: str = "https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json"
DATA_PATH = Path(__file__).resolve().parent / "data" / "documents.json"


def download_data(url: str = DATA_URL, save_path: Path = DATA_PATH) -> None:
    """
    Downloads JSON data from the given URL and saves it locally.

    Args:
        url (str): The URL of the JSON data to download.
        save_path (Path): The local path where the file will be saved.

    Raises:
        requests.HTTPError: If the HTTP request fails.
        json.JSONDecodeError: If the response is not valid JSON.
    """
    save_path.parent.mkdir(parents=True, exist_ok=True)

    response: requests.Response = requests.get(url)
    response.raise_for_status()

    docs: List[Dict[str, Any]] = response.json()
    save_path.write_text(json.dumps(docs, indent=2), encoding="utf-8")
    """
    # .write_text() is a method on a Path object that hides the file-handling ceremony
    # it is a short hand for:
        with open(save_path, "w", encoding="utf-8") as f:
             f.write(json.dumps(docs, indent=2))
    """


    print(f"Saved {len(docs)} items to {save_path.resolve()}")


if __name__ == "__main__":
    download_data()
