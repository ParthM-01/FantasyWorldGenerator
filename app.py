from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model and tokenizer
model_path = "./fantasy_gpt2_model"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token

# Initialize Flask app
app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    max_length = data.get("max_length", 150)

    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    attention_mask = inputs['attention_mask']
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=attention_mask,
        max_length=max_length,
        temperature=0.6,
        top_k=30,
        top_p=0.85,
        repetition_penalty=1.2,
        do_sample=True
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)