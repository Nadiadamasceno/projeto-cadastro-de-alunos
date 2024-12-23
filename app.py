from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados SQLite
def conectar_db():
    conn = sqlite3.connect('alunos.db')
    return conn

# Criar a tabela e popular com dados iniciais (se necessário)
def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            media REAL,
            status TEXT DEFAULT "ativo"
        )
    ''')
    conn.commit()
    conn.close()

# Função para popular a tabela com alunos iniciais
def popular_tabela():
    alunos_iniciais = [
        {"nome": "Lucas Almeida", "idade": 20, "media": 8.5, "status": "Ativo"},
        {"nome": "Ana Clara", "idade": 22, "media": 9.2, "status": "Inativo"},
        {"nome": "João Pedro", "idade": 19, "media": 7.8, "status": "Inativo"},
        {"nome": "Mariana Silva", "idade": 23, "media": 8.0, "status": "Inativo"},
        {"nome": "Pedro Henrique", "idade": 21, "media": 7.5, "status": "Ativo"},
        {"nome": "Camila Rocha", "idade": 18, "media": 9.0, "status": "Inativo"},
        {"nome": "Rafael Santos", "idade": 24, "media": 6.8, "status": "Ativo"},
        {"nome": "Gabriela Nunes", "idade": 20, "media": 8.7, "status": "Inativo"},
        {"nome": "Bruno Costa", "idade": 22, "media": 7.9, "status": "Inativo"},
        {"nome": "Isabela Ferreira", "idade": 19, "media": 9.5, "status": "Ativo"},
        {"nome": "Thiago Pereira", "idade": 21, "media": 6.5, "status": "Inativo"},
        {"nome": "Larissa Lima", "idade": 23, "media": 8.3, "status": "Inativo"},
        {"nome": "Matheus Moura", "idade": 20, "media": 7.0, "status": "Ativo"},
        {"nome": "Fernanda Gomes", "idade": 22, "media": 9.1, "status": "Inativo"},
        {"nome": "Daniela Ramos", "idade": 18, "media": 8.8, "status": "Inativo"},
        {"nome": "Rodrigo Azevedo", "idade": 24, "media": 6.7, "status": "Ativo"},
        {"nome": "Carolina Farias", "idade": 19, "media": 7.6, "status": "Inativo"},
        {"nome": "Henrique Martins", "idade": 21, "media": 9.3, "status": "Inativo"},
        {"nome": "Beatriz Almeida", "idade": 20, "media": 8.4, "status": "Inativo"},
        {"nome": "Eduardo Souza", "idade": 22, "media": 7.8, "status": "Ativo"},
    ]
    
    conn = conectar_db()
    cursor = conn.cursor()

    # Verifica se a tabela já contém alunos antes de inserir
    cursor.execute('SELECT COUNT(*) FROM alunos')
    if cursor.fetchone()[0] == 0:
        for aluno in alunos_iniciais:
            cursor.execute('''
                INSERT INTO alunos (nome, idade, media, status)
                VALUES (?, ?, ?, ?)
            ''', (aluno['nome'], aluno['idade'], aluno['media'], aluno['status']))
        conn.commit()
    conn.close()

# Inicializar banco de dados
criar_tabela()
popular_tabela()

@app.route('/')
def home():
    return render_template('index.html', aluno=None)

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    nome = request.form.get('nome', '').strip()
    id_aluno = request.form.get('id', '').strip()
    aluno = None
    conn = conectar_db()
    cursor = conn.cursor()
    if id_aluno:
        cursor.execute('SELECT * FROM alunos WHERE id = ?', (id_aluno,))
    elif nome:
        cursor.execute('SELECT * FROM alunos WHERE nome LIKE ?', (f'%{nome}%',))
    aluno = cursor.fetchone()
    conn.close()
    return render_template('index.html', aluno=aluno)
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    media = request.form['media']
    
    # Conectar ao banco de dados e inserir o novo aluno
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO alunos (nome, idade, media)
        VALUES (?, ?, ?)
    ''', (nome, idade, media))
    conn.commit()
    conn.close()

    # Após o cadastro, redirecionar para a página principal (ou uma página de sucesso)
    return render_template('index.html', aluno=None)
@app.route('/editar', methods=['POST'])
def editar():
    # Obtém os dados do formulário
    id_aluno = request.form['id']
    nova_idade = request.form.get('nova-idade')
    nova_media = request.form.get('nova-media')
    novo_status = request.form.get('novo-status')

    conn = conectar_db()
    cursor = conn.cursor()

    # Atualiza os campos apenas se valores foram fornecidos
    if nova_idade:
        cursor.execute('UPDATE alunos SET idade = ? WHERE id = ?', (nova_idade, id_aluno))
    if nova_media:
        cursor.execute('UPDATE alunos SET media = ? WHERE id = ?', (nova_media, id_aluno))
    if novo_status:
        cursor.execute('UPDATE alunos SET status = ? WHERE id = ?', (novo_status, id_aluno))
    
    conn.commit()
    conn.close()

    # Redireciona para a página inicial após salvar as alterações
    return render_template('index.html', aluno=None)

if __name__ == '__main__':
    app.run(debug=True)
