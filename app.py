# app.py (Backend Flask)
from flask_cors import CORS
# ...

# Substitua ' https://github.com/Nashet89ai/enem-encceja-frontend' pelo URL real do seu frontend no Vercel
CORS(app, resources={r"/*": {"origins": "https://seu-frontend-vercel-url.vercel.app"}})