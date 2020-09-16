from streamlit import st

import joblib

app = Flask(__name__)      # Iniciando a aplicação.

@app.route('/')
def index():
    return render_template('primeiro_app')              # renderizando o um template html

app.run()