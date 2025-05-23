# Garanta que você está na pasta correta e com o venv ativo
cd C:\enem-encceja-backend
venv\Scripts\activate

# Agora o 'dir' deve mostrar app.py, requirements.txt e README.md
dir

# Adicione TODOS os arquivos que devem ir para o GitHub, incluindo o app.py
git add .

# Faça um novo commit
git commit -m "Add missing app.py and ensure all backend files are tracked"

# Envie para o GitHub
git push origin main