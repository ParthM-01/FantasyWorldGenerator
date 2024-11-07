# Fantasy World Generator

This project is a fine-tuned GPT-2 model that generates fantasy-themed text based on a given prompt.

## Features
- Generates immersive and creative fantasy text based on input prompts.
- Built using Hugging Face’s `transformers` library.

## Requirements
- `transformers`
- `torch`
- `Flask`

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/fantasy-world-generator.git
    cd fantasy-world-generator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

## Usage
Send a POST request to `http://localhost:5000/generate` with a JSON payload containing your prompt:

```json
{
    "prompt": "In the heart of the enchanted forest, a hidden castle lay cloaked in shadows.",
    "max_length": 150
}
