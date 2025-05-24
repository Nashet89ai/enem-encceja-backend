# app.py (Backend Flask)

from flask import Flask
from flask_cors import CORS # Correto: Importa uma vez

# ... outras importações que seu app possa ter (ex: request, jsonify, etc.)
# import os # Exemplo: se usar variáveis de ambiente
# from dotenv import load_dotenv # Exemplo: se usar dotenv para variáveis locais

# Carregue variáveis de ambiente se necessário (para uso local)
# load_dotenv()

# 1. Inicialize seu aplicativo Flask
app = Flask(__name__)

# 2. Configure CORS para permitir requisições do seu frontend
#    Substitua 'https://SEU-NOME-DO-PROJETO.vercel.app' pelo URL REAL do seu frontend no Vercel.
#    Adicione 'http://localhost:PORTA_DO_SEU_FRONTEND' se você também testar localmente.
CORS(app, resources={r"/*": {"origins": [
    "https://enem-encceja-frontend-d2c19wvsg-nevers-projects-4aac9f28.vercel.app",  # <--- ATENÇÃO: SUBSTITUA POR ESTE URL REAL DO SEU FRONTEND NO VERCEL
    "http://localhost:3000",                   # Exemplo: se o seu frontend React/Vue/Angular roda na porta 3000
    "http://127.0.0.1:3000"                    # Adicional para localhost, se necessário
]}})

# --- Suas Rotas e Lógica de Negócios Abaixo ---

@app.route('/')
def home():
    return "Bem-vindo ao backend do ENEM/ENCCEJA!"

# Exemplo de uma rota de API
@app.route('/api/dados')
def get_dados():
    # Aqui você retornaria dados do seu banco de dados, etc.
    return {"mensagem": "Dados do backend"}

# --- Fim das Rotas ---

if __name__ == '__main__':
    # Use o PORT da variável de ambiente, ou a porta 5000 como padrão
    # PORT = os.getenv("PORT", 5000) # Se você usar variáveis de ambiente no Railway/Render
    app.run(debug=True, host='0.0.0.0', port=5000) # host='0.0.0.0' é importante para deploy