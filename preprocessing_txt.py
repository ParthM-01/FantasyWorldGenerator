import os
import re

# Directory where the converted text files are stored
input_dir = 'books_txt'
# Output file to store the preprocessed text
output_file = 'preprocessed_fantasy_texts.txt'

def clean_text(text):
    # Remove unwanted characters and extra whitespace
    text = re.sub(r'\s+', ' ', text)  # Replaces multiple spaces/newlines with a single space
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Removes non-ASCII characters if present
    return text.strip()

def preprocess_text_files(input_dir, output_file):
    all_text = []

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                clean = clean_text(text)
                all_text.append(clean)
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(all_text))

    print(f"Preprocessed text saved to {output_file}")

# Run the preprocessing function
preprocess_text_files(input_dir, output_file)