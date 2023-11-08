import nltk
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')

def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as fileInput:
        text = fileInput.read()
        text = text.replace('\n', ' ')
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        return tokens
    
def save_output(tokens):
    with open('./output/out.txt', 'w', encoding='utf-8') as fileOutput:
        for token in tokens:
            fileOutput.write(str(token) + '\n')

file_path = './input/in.txt'
tokens = tokenize_file(file_path)
save_output(sorted(tokens))
