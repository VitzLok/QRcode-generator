Segue o **README.md** do projeto em **português** e **inglês**:

---

# Gerador de QR Code com Validação de Website  
**QR Code Generator with Website Validation**

Este projeto é uma aplicação Python que gera um QR Code para um link de website fornecido pelo usuário. Antes de gerar o QR Code, o programa valida o link para garantir que seja um website válido e acessível.  
**This project is a Python application that generates a QR Code for a website link provided by the user. Before generating the QR Code, the program validates the link to ensure it is a valid and accessible website.**

---

## 🚀 Funcionalidades | Features

- Valida se o link inserido é uma URL válida.  
  **Validates if the input is a valid URL.**
- Verifica se o website é acessível (responde com código de status 200).  
  **Checks if the website is accessible (responds with status code 200).**
- Gera um QR Code para o link validado.  
  **Generates a QR Code for the validated link.**
- Salva o QR Code como um arquivo de imagem (`qrcode.png`) no diretório atual.  
  **Saves the QR Code as an image file (`qrcode.png`) in the current directory.**

---

## 🛠️ Requisitos | Requirements

- Python 3.6 ou superior | **Python 3.6 or later**  
- As seguintes bibliotecas Python | **The following Python libraries**:  
  - `qrcode`  
  - `validators`  
  - `requests`

---

## 📦 Instalação | Installation

1. **Clone o repositório | Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Crie um ambiente virtual (opcional) | Create a virtual environment (optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências | Install dependencies**:
   ```bash
   pip install qrcode validators requests
   ```

---

## 🖥️ Uso | Usage

1. Execute o programa | **Run the program**:
   ```bash
   python main.py
   ```

2. Insira uma URL quando solicitado | **Enter a website URL when prompted**:
   ```
   Cole aqui seu link de site: https://www.example.com
   ```

3. Se a URL for válida e o website for acessível | **If the URL is valid and the website is accessible**:
   - Um QR Code será gerado.  
     **A QR Code will be generated.**
   - O QR Code será salvo como `qrcode.png` no diretório atual.  
     **The QR Code is saved as `qrcode.png` in the current directory.**
   - Uma mensagem de sucesso será exibida:  
     **A success message is displayed**:
     ```
     Site válido. Gerando QRcode...
     QR Code gerado com sucesso e salvo como 'qrcode.png'!
     ```

4. Se a URL for inválida ou o website estiver inacessível | **If the URL is invalid or the website is inaccessible**:
   - Uma mensagem de erro será exibida:  
     **An error message is displayed**:
     ```
     Site inválido. Tente novamente com um link acessível.
     ```

---

## 🧰 Estrutura do Código | Code Structure

- **`main.py`**: Contém toda a lógica para validar o website e gerar o QR Code.  
  **Contains the entire logic for validating the website and generating the QR Code.**
  - **Funções | Functions**:
    - `website_acessivel(url)`: Valida o formato da URL e verifica se o website é acessível.  
      **Validates the URL format and checks if the website is accessible.**
  - **Lógica | Logic**:
    - Solicita uma URL ao usuário.  
      **Requests a URL from the user.**
    - Valida a URL.  
      **Validates the URL.**
    - Gera e salva o QR Code se a URL for válida.  
      **Generates and saves a QR Code if the URL is valid.**

---

## 🐛 Solução de Problemas | Troubleshooting

### Problemas Comuns | Common Issues
1. **`ModuleNotFoundError: No module named 'requests'`**:
   - Instale as bibliotecas necessárias | **Install the required libraries**:
     ```bash
     pip install requests validators qrcode
     ```

2. **Website considerado inválido | Website is considered invalid**:
   - Certifique-se de que a URL começa com `http://` ou `https://`.  
     **Ensure the URL starts with `http://` or `https://`.**
   - Verifique se o website é acessível no navegador.  
     **Verify that the website is accessible in your browser.**

---

## 📜 Licença | License

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.  
**This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.**

---
