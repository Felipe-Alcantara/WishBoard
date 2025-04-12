COMO INICIAR O PROJETO WISHLIST

1. ATIVAR O AMBIENTE VIRTUAL:
   - No Windows:
     venv\Scripts\activate
   - No Linux/Mac:
     source venv/bin/activate

2. INSTALAR DEPENDÊNCIAS (se ainda não instaladas):
   - Comando:
     pip install -r requirements.txt

3. CONFIGURAR O BANCO DE DADOS:
   - Criar as migrações:
     python manage.py makemigrations
   - Aplicar as migrações:
     python manage.py migrate

4. CRIAR SUPER USUÁRIO (opcional, para acessar o admin):
   - Comando:
     python manage.py createsuperuser

5. INICIAR O SERVIDOR:
   - Comando:
     python manage.py runserver

6. ACESSAR O PROJETO:
   - No navegador, abra:
     http://127.0.0.1:8000
   - Para acessar o admin (se criou superusuário):
     http://127.0.0.1:8000/admin

NOTAS:
- O banco de dados usado é SQLite, já configurado no projeto.
- O projeto está configurado para desenvolvimento local.
- A porta padrão do servidor é 8000.