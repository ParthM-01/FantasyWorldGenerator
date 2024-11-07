import requests

url = "http://127.0.0.1:5000/generate"
prompt_data = {
    "prompt": "In the heart of the enchanted forest, a hidden castle lay cloaked in shadows.",
    "max_length": 150
}

response = requests.post(url, json=prompt_data)
if response.status_code == 200:
    print("Generated Text:", response.json()["generated_text"])
else:
    print("Error:", response.status_code, response.text)
