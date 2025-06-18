import argparse
import json
import urllib.request
from urllib.parse import urlencode


def fetch_models(search: str | None = None, limit: int = 10):
    """Fetch model metadata from Hugging Face."""
    params = {"limit": limit}
    if search:
        params["search"] = search
    url = "https://huggingface.co/api/models?" + urlencode(params)
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


def format_model(model: dict) -> str:
    """Return a formatted string for a single model."""
    lines = [f"Model: {model.get('modelId')}"]
    likes = model.get('likes')
    if likes is not None:
        lines.append(f"Likes: {likes}")
    downloads = model.get('downloads')
    if downloads is not None:
        lines.append(f"Downloads: {downloads}")
    last = model.get('lastModified')
    if last:
        lines.append(f"Last Modified: {last}")
    tags = model.get('tags')
    if tags:
        lines.append(f"Tags: {', '.join(tags)}")
    return "\n  ".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="List Hugging Face models")
    parser.add_argument('-q', '--query', help='search query for models')
    parser.add_argument('-l', '--limit', type=int, default=10, help='number of models to list')
    args = parser.parse_args()

    models = fetch_models(args.query, args.limit)
    for m in models:
        print(format_model(m))
        print('-' * 40)


if __name__ == '__main__':
    main()
