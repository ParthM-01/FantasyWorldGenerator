import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# Set the file paths
dataset_path = 'preprocessed_fantasy_texts.txt'
model_name = 'gpt2'  # Using the base GPT-2 model

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Set pad token to end-of-sequence token

# Create a dataset for training
def load_dataset(file_path, tokenizer, block_size=128):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    inputs = tokenizer(text, return_tensors="pt", max_length=block_size, truncation=True)
    return TextDataset(tokenizer=tokenizer, file_path=file_path, block_size=block_size)

train_dataset = load_dataset(dataset_path, tokenizer)

# Define data collator for padding
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False,
)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./fantasy_gpt2_model",
    overwrite_output_dir=True,
    num_train_epochs=1,  # Adjust for more training if desired
    per_device_train_batch_size=1,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the fine-tuned model
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_save_path = "./fantasy_gpt2_model"
model_name = 'gpt2'  # Replace with the model name if using a different one

# Load the base GPT-2 model and tokenizer, if not loaded already
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Save the fine-tuned model and tokenizer
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(model_save_path)

print(f"Model and tokenizer saved to {model_save_path}")