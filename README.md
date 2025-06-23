<h1 align="center">📦 ScanFlux</h1>
<p align="center">
Sistema moderno de <strong>rastreamento e inventário de produtos</strong> com leitura de etiquetas via câmera ou imagem, utilizando <code>Python</code>, <code>OpenCV</code>, <code>PyQt5</code> e <code>SQLite</code>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/python-3.10+-yellow" />
</p>

---

## 📸 Visão Geral

O **ScanFlux** é um sistema desktop completo para controle de inventário em ambientes industriais ou logísticos. Com ele, você pode:

✅ Ler etiquetas de produto e endereço via **câmera ao vivo**  
📁 Ler códigos diretamente de **imagens**  
📦 Consultar produtos por localização ou nome  
📝 Realizar e atualizar inventários diretamente na base de dados  
🧠 Interface moderna com **PyQt5**

---

## 🧩 Estrutura do Projeto

ScanFlux/
├── controller/
│ ├── leitor.py # Leitura de etiquetas (câmera e imagem)
│ └── controle_estoque.py # Lógica de inventário e consulta
├── models/
│ ├── conexao.py # Conexão SQLite
│ └── consulta.py # Operações SQL
├── views/
│ └── main.py # Interface gráfica com PyQt5
├── interface.ui # Layout Qt Designer
├── Img/ # Imagens usadas na UI
└── estoque.db # Banco de dados (gerado automaticamente)

---

## 💻 Tecnologias

- 📦 Python 3.10+
- 🎨 PyQt5
- 🔍 Pyzbar (decodificador de QR/Barras)
- 📷 OpenCV
- 🧠 SQLite3

---

## 🚀 Como Rodar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/ScanFlux.git
cd ScanFlux
2. Instale as dependências
Crie o arquivo requirements.txt com o conteúdo abaixo, ou rode:

bash
Copiar código
pip install pyqt5 opencv-python pyzbar numpy
3. Execute a aplicação
bash
Copiar código
python views/main.py
A interface será exibida com botões de leitura, consulta e inventário.

🔍 Leitura de Etiquetas
▶️ Leitura por Câmera

from controller.leitor import Leitor
leitor = Leitor()
dados = leitor.ler_codigo_barras_camera()

🖼️ Leitura por Imagem

dados = leitor.ler_codigo_barras_imagem("Img/exemplo.jpg")
🛠️ Banco de Dados
O banco estoque.db é criado automaticamente com as seguintes tabelas:

produto(id_produto, cod_produto, nome_produto)
endereco(id_endereco, cod_endereco)
estoque(id_estoque, id_produto, id_endereco, quantidade)
As chaves estrangeiras garantem integridade entre produtos, endereços e o estoque.

📌 Funcionalidades
Função	Descrição
Leitor de câmera	Leitura ao vivo de etiquetas para produto e endereço
Leitor de imagem	Leitura de códigos em imagens (PNG, JPG, etc.)
Consulta	Mostra produtos em um endereço ou localiza um produto específico
Inventário	Atualiza quantidade de um item no banco após escaneamento
Interface intuitiva	Desenvolvida com Qt Designer para facilitar o uso em operação real

🛡️ Licença
Este projeto está licenciado sob os termos da MIT License.

🤝 Contribuição
Contribuições são bem-vindas! Para sugerir melhorias, abra uma issue ou envie um pull request.

👨‍💻 VitorSilva06


