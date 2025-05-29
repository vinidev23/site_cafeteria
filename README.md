# ☕ Coffe's - Seu Site de Café com Flask

Um projeto web simples desenvolvido com Flask e MySQL para demonstrar um sistema básico de cadastro, login e acesso a conteúdo restrito.

---

## ✨ Funcionalidades

* **Cadastro de Usuários:** Permite que novos usuários se registrem com e-mail, telefone e senha.
* **Login de Usuários:** Autenticação segura de usuários existentes.
* **Criptografia de Senha:** As senhas são armazenadas de forma segura (hashed) no banco de dados.
* **Sessões de Usuário:** Mantém o usuário logado e restringe o acesso a páginas protegidas.
* **Mensagens Flash:** Feedback visual para o usuário (sucesso no cadastro, erro no login, etc.).
* **Páginas Dinâmicas:** Conteúdo HTML renderizado pelo Flask.
* **Design Responsivo:** (Se aplicável, ajuste esta linha) Layout adaptável para diferentes dispositivos.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * [Python](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/): Microframework web para Python.
    * [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/): Conexão com o banco de dados MySQL.
    * [Werkzeug](https://werkzeug.palletsprojects.com/): Para funções de segurança como hash de senhas.
* **Banco de Dados:**
    * [MySQL](https://www.mysql.com/) (gerenciado via [XAMPP](https://www.apachefriends.org/pt_br/index.html) e [phpMyAdmin](https://www.phpmyadmin.net/)).
* **Frontend:**
    * HTML5
    * CSS3

---

## 🚀 Como Rodar o Projeto Localmente

Siga estes passos para configurar e executar o projeto em sua máquina local:

### Pré-requisitos

* [Python 3.x](https://www.python.org/downloads/) instalado.
* [XAMPP](https://www.apachefriends.org/pt_br/index.html) (ou outro servidor web com MySQL/MariaDB) instalado e rodando.

### 1. Configuração do Banco de Dados

1.  **Inicie o MySQL no XAMPP Control Panel.** (O Apache também pode ser iniciado para acesso ao phpMyAdmin).
2.  Acesse o [phpMyAdmin](http://localhost/phpmyadmin/) no seu navegador.
3.  Crie um novo banco de dados chamado **`meu_site_db`** (tudo minúsculo).
4.  Dentro do banco de dados `meu_site_db`, execute o seguinte código SQL na aba "SQL" para criar a tabela `cadastro`:

    ```sql
    CREATE TABLE IF NOT EXISTS cadastro (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        telefone VARCHAR(15),
        senha VARCHAR(255) NOT NULL,
        data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

### 2. Configuração do Projeto Python

1.  **Clone este repositório** para sua máquina local (ou navegue até a pasta do projeto se já a tiver):

    ```bash
    git clone [https://github.com/SEU_USUARIO/meu_site_cafe_flask.git](https://github.com/SEU_USUARIO/meu_site_cafe_flask.git)
    cd meu_site_cafe_flask # Ou o nome da sua pasta principal
    ```

    *Substitua `SEU_USUARIO` e `meu_site_cafe_flask` pelo seu usuário e nome do repositório no GitHub.*

2.  **Instale as dependências** do Python (certifique-se de estar na pasta raiz do projeto no terminal):

    ```bash
    pip install Flask mysql-connector-python Werkzeug
    ```

    *Se você tiver um arquivo `requirements.txt` gerado, pode usar `pip install -r requirements.txt`.*

3.  **Configure o `app.py`:**

    * Abra o arquivo `app.py`.
    * Localize a seção `DB_CONFIG` e verifique se os detalhes correspondem ao seu MySQL (host, database, user, password).

        ```python
        DB_CONFIG = {
            'host': 'localhost',
            'database': 'meu_site_db',
            'user': 'root',
            'password': '' # Coloque sua senha do MySQL se você tiver uma
        }
        ```

    * **MUITO IMPORTANTE:** Altere a `app.secret_key` para uma string longa e única.

        ```python
        app.secret_key = 'sua_nova_chave_secreta_aqui_e_bem_longa_e_unica_1234567890ABCDEF'
        ```

### 3. Executar o Aplicativo

1.  No terminal, na pasta raiz do projeto (`meu_site_cafe_flask`), execute o aplicativo Flask:

    ```bash
    python app.py
    ```

2.  Abra seu navegador e acesse: `http://localhost:5000/`

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

---

## 📧 Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.

---
