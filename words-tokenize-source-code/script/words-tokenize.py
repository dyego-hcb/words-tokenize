import nltk
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')

def tokenize_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_input:
            lines = file_input.readlines()
            text = ''
            for line in lines:
                if line.endswith('-\n'):
                    text += line.strip()[:-1]
                else:
                    text += line.strip() + ' '
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(text)
            return tokens
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

def save_output(tokens, output_path='./output/out.txt'):
    try:
        with open(output_path, 'w', encoding='utf-8') as file_output:
            for token in tokens:
                file_output.write(str(token) + '\n')
        print("Saída salva com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar a saída: {e}")

file_path = './input/in.txt'
output_path = './output/out.txt'

tokens = tokenize_file(file_path)

if tokens is not None:
    save_output(sorted(tokens), output_path)
