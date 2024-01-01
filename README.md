## Tokenizar e Salvar Arquivos de Texto

Este repositório contém um script em Python que tokeniza e salva o conteúdo de arquivos de texto.

### Requisitos

- Python 3.x
- Biblioteca NLTK (incluída no pacote `nltk`)

### Estrutura do Diretório

- A pasta **[Código Fonte da Tokenização de Palavras](./words-tokenize-source-code/)** contém as entradas e saídas usadas no projeto criado, bem como o código fonte em si.
- Na pasta **[Script](./words-tokenize-source-code/script/)**, você encontrará o código fonte do projeto.

### Instalação

O pacote `nltk` é geralmente instalado usando o pip:

pip install nltk

Se encontrar um erro durante a instalação, pode ser necessário baixar e instalar manualmente os dados necessários para o tokenizador `punkt`:

python -m nltk.download('punkt')

### Uso

1. Coloque o(s) arquivo(s) de texto de entrada no diretório `./input`.

2. Para tokenizar e salvar todos os arquivos em `./input`, execute o seguinte comando:

python words-tokenize.py

3. Para tokenizar e salvar arquivos específicos, modifique a variável `file_path` dentro da função `save_output()` em `words-tokenize.py`.

4. A saída tokenizada será salva no diretório `./output`, com cada arquivo nomeado com base no nome original do arquivo de entrada.

### Explicação do Script

O script utiliza duas funções principais:

1. `tokenize_file(file_path)`: Lê o conteúdo do arquivo especificado, substitui caracteres de nova linha por espaços e tokeniza o texto usando a classe `RegexpTokenizer()` da biblioteca `nltk`. O tokenizador divide o texto em palavras individuais com base nos limites das palavras.

2. `save_output(tokens)`: Escreve as palavras tokenizadas em um arquivo de saída com o mesmo nome de base do arquivo de entrada, preservando a extensão original do arquivo. Cada token é escrito em uma linha separada.

### Notas

- O script assume que os arquivos de texto de entrada estão codificados em UTF-8.
- O script remove automaticamente caracteres de nova linha do texto de entrada e salva os tokens no diretório `./output` com o mesmo nome de arquivo.
- Se desejar salvar os tokens em um formato ou diretório diferente, modifique a função `save_output()` conforme necessário.

***

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

### Usage

1. Place the input text file(s) in the `./input` directory.

2. To tokenize and save all files in `./input`, run the following command:
python words-tokenize.py

3. To tokenize and save specific files, modify the `file_path` variable within the `save_output()` function in `words-tokenize.py`.

4. The tokenized output will be saved in the `./output` directory, with each file named based on the original input file name.

### Script Explanation

The script utilizes two main functions:

1. `tokenize_file(file_path)`: Reads the contents of the specified file, replaces newline characters with spaces, and tokenizes the text using the `RegexpTokenizer()` class from the `nltk` library. The tokenizer splits the text into individual words based on word boundaries.

2. `save_output(tokens)`: Writes the tokenized words to an output file with the same base filename as the input file, preserving the original file extension. Each token is written to a separate line.

### Notes

- The script assumes the input text files are in UTF-8 encoding.
- The script automatically removes newline characters from the input text and saves the tokens in the `./output` directory with the same filename.
- If you want to save the tokens in a different format or directory, modify the `save_output()` function accordingly.