import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
model_path = "fantasy_gpt2_model"  # Path to your saved fine-tuned model
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)


tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = model.config.eos_token_id

# Function to generate text
def generate_text(prompt, max_length=150, temperature=0.6, repetition_penalty=1.2):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    attention_mask = inputs['attention_mask']
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=attention_mask,
        min_length=80,
        max_length=max_length,
        temperature=temperature,
        top_k=30,
        top_p=0.85,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )
    
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Post-process to end at the last complete sentence
    if not text.endswith(('.', '!', '?')):
        last_punctuation = max(text.rfind(p) for p in ('.', '!', '?'))
        if last_punctuation != -1:
            text = text[:last_punctuation + 1]
    
    return text

# Test the function
prompt = "As he woke up amidst ashes of the destruction, earth beneath started trembling. With shaken breath, he said: 'So it begins...'"
print(generate_text(prompt))
