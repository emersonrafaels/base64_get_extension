<h1 align="center">
    <img alt="Get Extension Base64" title="#OCRRG" src="./assets/banner.png" />
</h1>

<h4 align="center"> 
	🚧 Get Extension Base64 - 1.0 🚀 em desenvolvimento... 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/emersonrafaels/ocr_rg?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/emersonrafaels/ocr_rg">

  	
  <a href="https://www.linkedin.com/in/emerson-rafael/">
    <img alt="Siga no Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
	
  
  <a href="https://github.com/emersonrafaels/ocr_rg/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/emersonrafaels/ocr_rg">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/emersonrafaels/ocr_rg/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/emersonrafaels/ocr_rg?style=social">
  </a>
</p>


## 💻 Sobre o projeto

📦 **Get Extension Base64** é um projeto que permite **obter a extensão de um arquivo**. Esse projeto é muito útil para a utilização em *API's* que recebem **Base64 como input**.

Atualmente funcionando para:

 1. PNG
 2. JPG
 3. HEIC (formato das imagens do Iphone)
 4. HEIF (formato das imagens do Iphone)
 5. PDF
 6. Docx
 
 ## 🧗‍♂️ Adicional - Conversor de HEIC/HEIF para PNG
 
 O projeto inclui um conversor de arquivos em formato **HEIC/HEIF** para **PNG**.

## 🛠  Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python]

## 🚀 Como executar o projeto

1. **Instalando**: pip install -r requirements.txt
2. **Seguir modelos apresentados no diretório de testes**:

Ex: Executando a **obtenção de extensão**:

```python
import base64
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.base64_encode_decode import image_to_base64, base64_get_extension

input_image = '../fixtures/IMG_4127.HEIC'

# CONVERTENDO PARA BASE64
input_image_base64 = image_to_base64(input_image)

# DECODIFICANDO A BASE64
result_decode = base64.b64decode(input_image_base64.decode())

# OBTENDO A EXTENSÃO
extension = base64_get_extension(result_decode)

print("-"*50)
print("A EXTENSÃO DO ARQUIVO É {}".format(extension))
```
Os **arquivos de teste mostram como realizar a chamada da função para obtenção da extensão**, ao mesmo tempo que **implementam a chamada de funções de conversão de um arquivo para base64 e base64 decodificada**.

Os passos foram:
1) Conversão de um arquivo para base64 (para usar como exemplo)
2) Decodificação da base64
3) Obtenção da extensão do arquivo original (codificado em base64)

## ➊ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas (O download pode ser realizado pela própria página do Python ou Anaconda):
[Python](https://www.anaconda.com/products/individual).

## [≝] Testes
Os testes estão na pasta: **TESTS/***.
Nela é possível verificar os testes disponíveis

## 📝 Licença

Este projeto está sob a licença MIT.

Feito com ❤️ por **Emerson Rafael** 👋🏽 [Entre em contato!](https://www.linkedin.com/in/emerson-rafael/)

[Python]: https://www.python.org/downloads/