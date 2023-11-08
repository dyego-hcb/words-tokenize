## Tokenize and Save Text Files

This repository contains a Python script that tokenizes and saves the contents of text files.

### Requirements

- Python 3.x
- NLTK library (included in the `nltk` package)

### Folder Structure

- The **[Words Tokenize Source Code](./words-tokenize-source-code/)** folder contains the inputs and outputs used in the created project, as well as the source code itself.
- In the **[Script](./words-tokenize-source-code/script/)** folder, you will find the source code for the project.

### Installation

The `nltk` package is typically installed using pip:

pip install nltk

If you encounter an error during installation, you may need to manually download and install the required data for the `punkt` tokenizer:

python -m nltk.download('punkt')

python tokenize_and_save.py

### Usage

1. Place the input text file(s) in the `./input` directory.

2. To tokenize and save all files in `./input`, run the following command:
python words-tokenize.py

3. To tokenize and save specific files, modify the `file_path` variable within the `tokenize_file()` function in `tokenize_and_save.py`.

4. The tokenized output will be saved in the `./output` directory, with each file named based on the original input file name.

### Script Explanation

The script utilizes two main functions:

1. `tokenize_file(file_path)`: Reads the contents of the specified file, replaces newline characters with spaces, and tokenizes the text using the `RegexpTokenizer()` class from the `nltk` library. The tokenizer splits the text into individual words based on word boundaries.

2. `save_output(tokens)`: Writes the tokenized words to an output file with the same base filename as the input file, preserving the original file extension. Each token is written to a separate line.

### Notes

- The script assumes the input text files are in UTF-8 encoding.
- The script automatically removes newline characters from the input text and saves the tokens in the `./output` directory with the same filename.
- If you want to save the tokens in a different format or directory, modify the `save_output()` function accordingly.