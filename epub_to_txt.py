import os
from ebooklib import epub
from bs4 import BeautifulSoup

# Directory where EPUB files are stored
input_dir = 'books_epub'
# Directory to save converted text files
output_dir = 'books_txt'

os.makedirs(output_dir, exist_ok=True)

def convert_epub_to_txt(epub_path, txt_path):
    book = epub.read_epub(epub_path)
    content = []

    for item in book.get_items():
        # Check if the item is of type application/xhtml+xml (most text content in EPUB files is of this type)
        if item.get_type() == 9:  # 9 corresponds to 'application/xhtml+xml' in EbookLib
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            content.append(soup.get_text())

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

# Loop through EPUB files and convert each one
for filename in os.listdir(input_dir):
    if filename.endswith('.epub'):
        epub_path = os.path.join(input_dir, filename)
        txt_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        convert_epub_to_txt(epub_path, txt_path)
        print(f"Converted {filename} to text format.")

print("All EPUB files converted to TXT format.")
