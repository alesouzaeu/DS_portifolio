import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('rd_classification_model.pkl', 'rb'))

region_to_onehot = {'Australia and New Zealand' : np.array([1,0,0,0,0,0,0,0,0,0]),
                    'Central and Eastern Europe' : np.array([0,1,0,0,0,0,0,0,0,0]),
                    'Eastern Asia' : np.array([0,0,1,0,0,0,0,0,0,0]),
                    'Latin America and Caribbean' : np.array([0,0,0,1,0,0,0,0,0,0]),
                    'Middle East and Northern Africa' : np.array([0,0,0,0,1,0,0,0,0,0]),
                    'North America' : np.array([0,0,0,0,0,1,0,0,0,0]),
                    'Southeastern Asia' : np.array([0,0,0,0,0,0,1,0,0,0]),
                    'Southern Asia' : np.array([0,0,0,0,0,0,0,1,0,0]),
                    'Sub-Saharan Africa' : np.array([0,0,0,0,0,0,0,0,1,0]),
                    'Western Europe' : np.array([0,0,0,0,0,0,0,0,0,1])
                   }

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/verificar', methods=['POST'])          # recebe a requisição, coleta os dados a partir dos requests, esses dados compõe as variáveis em uma amostra de teste e faz a predição.
def verificar():
	sexo = request.form['gridRadiosSexo']
	dependentes = request.form['dependentes']
	casado = request.form['gridRadiosCasado']
	trabalho_conta_propria = request.form['gridRadiosTrabalhoProprio']
	rendimento = request.form['rendimento']
	educacao = request.form['educacao']
	valoremprestimo = request.form['valoremprestimo']
	teste = np.array([[sexo,casado,dependentes,educacao,trabalho_conta_propria,rendimento,valoremprestimo]])

# Na função acima temos todos os atributos que foram usados para treinar o modelo.	
	print(":::::: Dados de Teste ::::::")
	print("Sexo: {}".format(sexo))
	print("Numero de Dependentes: {}".format(dependentes))
	print("Casado: {}".format(casado))
	print("Educacao: {}".format(educacao))
	print("Trabalha por conta propria: {}".format(trabalho_conta_propria))
	print("Rendimento: {}".format(rendimento))
	print("Valor do emprestimo: {}".format(valoremprestimo))
	print("\n")

# Fazendo a predição:
	classe = model.predict(teste)[0]
	print("Classe Predita: {}".format(str(classe)))
# Mostrar na aplicação qual foi o retorno do modelo
	return render_template('template.html',classe=str(classe))


if __name__ == "__main__":
        port = int(os.environ.get('PORT', 5500))
        app.run(host='0.0.0.0', port=port)