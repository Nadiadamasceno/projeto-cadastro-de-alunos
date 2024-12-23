# 📚 Gerenciamento de Alunos

Este é um sistema simples de gerenciamento de alunos, que permite realizar operações como cadastro, edição, pesquisa e visualização de informações. Desenvolvido com *Flask* no backend, utiliza *SQLite* como banco de dados e HTML/CSS para o frontend.

---

## ✨ Recursos Principais

- *📋 Cadastro de Alunos*: Adicione alunos com informações como nome, idade e média.
- *✏️ Edição de Dados*: Atualize a idade, média e status de um aluno.
- *🔍 Pesquisa*: Encontre alunos pelo nome ou pelo ID.
- *🗄️ Banco de Dados*: Informações armazenadas em um banco SQLite para fácil persistência.
- *🖥️ Frontend*: Interface simples e intuitiva com HTML, CSS e integração de templates Flask.

---

## 🛠️ Tecnologias Utilizadas

- *Python (Flask)*: Desenvolvimento do backend.
- *SQLite*: Banco de dados relacional leve.
- *HTML5 e CSS3*: Criação da interface do usuário.

---

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

- Python 3.7 ou superior
- Virtualenv (opcional, mas recomendado)

### 🧩 Passos para Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciamento-alunos.git
   cd gerenciamento-alunos
   ```

2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install flask
   ```

4. Inicialize o banco de dados:
   O script cria automaticamente a tabela `alunos` e popula o banco com dados iniciais ao rodar o aplicativo.

5. Execute o servidor:
   ```bash
   python app.py
   ```

6. Acesse a aplicação no navegador:
   Abra [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para interagir com o sistema.

---

## 📂 Estrutura do Projeto

```
/
├── app.py                 # Arquivo principal do Flask
├── alunos.db              # Banco de dados SQLite
├── static/
│   └── css/
│       └── style.css      # Estilos da aplicação
├── templates/
│   └── index.html         # Template HTML principal
```

---

## ⚙️ Funcionalidades

### 📋 Cadastro de Alunos
Formulário para inserir informações como nome, idade e média.

### ✏️ Edição de Dados
Atualize campos específicos de um aluno utilizando o ID.

### 🔍 Pesquisa
Busque alunos utilizando o nome ou ID.

### 📄 Visualização
Exiba os detalhes do aluno encontrado em uma interface limpa.

---

## 🖼️ Capturas de Tela

![cadastro de alunos](https://github.com/user-attachments/assets/c268c403-2867-474b-9413-1b535bdb79ad)

![Editar alunos](https://github.com/user-attachments/assets/1f273ceb-3196-4926-bd19-fd88e58555c2)

![Pesquisa de Alunos](https://github.com/user-attachments/assets/3cca927e-8f91-48bd-8354-897041953bf5)




---

## 🤝 Contribuindo

Se desejar contribuir com o projeto:

1. Faça um fork do repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciamento-alunos.git
   ```

2. Crie uma branch com sua feature:
   ```bash
   git checkout -b minha-feature
   ```

3. Commit suas mudanças:
   ```bash
   git commit -m "Adiciona nova feature"
   ```

4. Faça o push para a branch:
   ```bash
   git push origin minha-feature
   ```

5. Abra um Pull Request.

---

## 📝 Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.


