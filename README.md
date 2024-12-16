### README: Gerador de QR Code com Interface Gráfica  

---

#### 📌 **Descrição do Projeto**  

Este é um aplicativo em Python que permite criar QR Codes a partir de URLs válidos e acessíveis. Ele conta com uma interface gráfica simples e intuitiva construída com `tkinter`. Com as atualizações mais recentes, o usuário pode:  

- Validar se o link é acessível antes de gerar o QR Code.  
- Escolher a pasta e o nome do arquivo para salvar o QR Code gerado.  
- Visualizar o QR Code diretamente na interface do aplicativo.  

---

#### 🛠️ **Funcionalidades**  

1. **Validação de URLs:**  
   - O programa verifica se o link fornecido é válido e acessível antes de gerar o QR Code.  
   - Utiliza as bibliotecas `validators` e `requests`.  

2. **Escolha Personalizada do Local e Nome do Arquivo:**  
   - O usuário pode selecionar onde salvar o QR Code e definir um nome personalizado para o arquivo, usando o diálogo gráfico `filedialog.asksaveasfilename`.  

3. **Interface Gráfica Intuitiva:**  
   - Construída com `tkinter`, inclui:  
     - Campo para entrada de URLs.  
     - Botão para gerar o QR Code.  
     - Área para exibição do QR Code gerado.  

4. **Feedback ao Usuário:**  
   - Mensagens informativas notificam sobre erros, ações bem-sucedidas ou operações canceladas.  

---

#### 🧰 **Pré-requisitos**  

- **Python 3.8 ou superior**  
- Bibliotecas adicionais:  
  - `qrcode`  
  - `validators`  
  - `requests`  
  - `Pillow`  

---

#### 📦 **Instalação**  

1. **Clone este repositório:**  
   ```bash  
   git clone https://github.com/VitzLok/QRcode-generator.git  
   cd QRcode-generator  
   ```  

2. **Instale as dependências:**  
   ```bash  
   pip install qrcode validators requests pillow  
   ```  

3. **Execute o programa:**  
   ```bash  
   python main.py  
   ```  

---

#### 🚀 **Como Usar**  

1. Insira um link válido no campo de texto.  
2. Clique no botão **Gerar QR Code**.  
3. Escolha a pasta e o nome do arquivo onde o QR Code será salvo.  
4. Visualize o QR Code diretamente na interface do aplicativo.  
5. Encontre o QR Code salvo na pasta especificada.  

---

#### 🎨 **Estrutura do Código**  

- **Validação de URL:** Garante que o link fornecido é acessível antes de gerar o QR Code.  
- **Criação do QR Code:** Utiliza a biblioteca `qrcode` para criar o código.  
- **Interface Gráfica:**  
  - Gerenciada por componentes do `tkinter`.  
  - O `filedialog` permite selecionar diretório e nome do arquivo.  
  - O `Pillow` redimensiona e exibe o QR Code na interface.  

---

#### 📂 **Funcionalidades Futuras**  

- Personalização do QR Code (cor, tamanho, formato).  
- Suporte a múltiplos idiomas.  
- Histórico de QR Codes gerados.  

---

#### 🖊️ **Contribuição**  

Fique à vontade para contribuir:  

1. Faça um fork do repositório.  
2. Crie uma branch para suas alterações:  
   ```bash  
   git checkout -b minha-feature  
   ```  
3. Envie um pull request.  

---

#### 🧑‍💻 **Autor**  

- **Perfil no GitHub:** [VitzLok](https://github.com/VitzLok)  
- **Contato:** vitordev1409@gmail.com  

---

#### ⚖️ **Licença**  

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.  

_______________________________________________________________

### README: QR Code Generator with Graphical Interface


#### 📌 **Project Description**  

This is a Python application that allows users to create QR Codes from valid and accessible URLs. It features a simple and intuitive graphical interface built with `tkinter`. With recent updates, users can:  

- Validate if the URL is accessible before generating the QR Code.  
- Choose the folder and filename for saving the generated QR Code.  
- View the generated QR Code directly in the application interface.  

---

#### 🛠️ **Features**  

1. **URL Validation:**  
   - The program checks if the provided URL is valid and accessible before generating the QR Code.  
   - Implements libraries like `validators` and `requests`.  

2. **Custom Location and Filename Selection:**  
   - Users can choose where to save the QR Code and set a custom file name using the `filedialog.asksaveasfilename` graphical dialog.  

3. **Intuitive Graphical Interface:**  
   - Built with `tkinter`, the interface includes:  
     - An input field for URLs.  
     - A button to generate the QR Code.  
     - A section to display the generated QR Code.  

4. **User Feedback:**  
   - Informative messages notify users about errors, successful actions, or canceled operations.  

---

#### 🧰 **Prerequisites**  

- **Python 3.8 or higher**  
- Additional libraries:  
  - `qrcode`  
  - `validators`  
  - `requests`  
  - `Pillow`  

---

#### 📦 **Installation**  

1. **Clone this repository:**  
   ```bash  
   git clone https://github.com/VitzLok/QRcode-generator.git  
   cd QRcode-generator  
   ```  

2. **Install dependencies:**  
   ```bash  
   pip install qrcode validators requests pillow  
   ```  

3. **Run the program:**  
   ```bash  
   python main.py  
   ```  

---

#### 🚀 **How to Use**  

1. Enter a valid URL in the text field.  
2. Click the **Generate QR Code** button.  
3. Select the folder and specify the filename for the QR Code.  
4. View the QR Code directly in the application interface.  
5. Find the saved QR Code in the specified folder.  

---

#### 🎨 **Code Structure**  

- **URL Validation:** Ensures the link is valid and accessible before creating the QR Code.  
- **QR Code Generation:** Utilizes the `qrcode` library to generate the QR Code.  
- **Graphical Interface:**  
  - Managed by `tkinter` components.  
  - `filedialog` supports directory and filename selection.  
  - `Pillow` resizes and displays the QR Code in the application.  

---

#### 📂 **Future Features**  

- Customization of QR Code appearance (e.g., color, size, and format).  
- Multi-language support.  
- History of generated QR Codes.  

---

#### 🖊️ **Contributing**  

Feel free to contribute:  

1. Fork the repository.  
2. Create a branch for your feature:  
   ```bash  
   git checkout -b my-feature  
   ```  
3. Submit a pull request.  

---

#### 🧑‍💻 **Author**  

- **GitHub Profile:** [VitzLok](https://github.com/VitzLok)  
- **Contact:** vitordev1409@gmail.com  

---

#### ⚖️ **License**  

This project is licensed under the MIT License. See the `LICENSE` file for details.  