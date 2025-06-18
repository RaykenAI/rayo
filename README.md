# Rayo Model Listing Utility

This repository contains a simple script to retrieve and list models from the [Hugging Face](https://huggingface.co) hub.

## Usage

```bash
python list_models.py --query gpt --limit 5
```

The script will display details for each matching model, including likes, downloads, last modification date and tags.

## Requirements

The script relies only on the Python standard library. Internet access is required at runtime to query the Hugging Face API.
