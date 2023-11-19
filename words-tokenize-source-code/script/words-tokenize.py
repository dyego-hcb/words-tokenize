import nltk
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')

def tokenize_file(path_input):
    try:
        with open(path_input, 'r', encoding='utf-8') as file_input:
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
        print(f"Arquivo {path_input} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

def save_output(tokens, path_output='./output/out.txt'):
    try:
        with open(path_output, 'w', encoding='utf-8') as file_output:
            for token in tokens:
                file_output.write(str(token) + '\n')
        print("Saída salva com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar a saída: {e}")

path_input = './input/in.txt'
path_output = './output/out.txt'

tokens = tokenize_file(path_input)

if tokens is not None:
    save_output(sorted(tokens), path_output)
