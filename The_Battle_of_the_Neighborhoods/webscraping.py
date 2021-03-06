import time
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json

# 1. Grabbing the HTML Content from the URL
url = "https://pt.wikipedia.org/wiki/Lista_dos_distritos_de_São_Paulo_por_população"


option = Options()
#option.headless = True
driver = webdriver.Firefox(options=option)
driver.get(url)


#PIP: 
    #pip install requests
    #pip install pandas 
    #pip install lxml
    #pip install beautifulsoup
    #pip install selenium


""" #To Search and click the button
#driver.find_element(By.XPATH, "html body main form div#painel_form_consulta.container div div#formulario.form div.campos div.campo.col-7.required div.controle").send_keys('São Paulo, SP')
#river.find_element(By.XPATH, "html body main form div#painel_form_consulta.container div div#formulario.form div.campos div.campo.col-1 div.botoes button#btn_pesquisar.primario").click()
"""

#Table- The Dataset

element = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/table[2]")
html_content = element.get_attribute('outerHTML')

# 2.Parsing the HTML content - BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')


# 3. Extructuring the content into a Data Frame - Pandas

df_full = pd.read_html(str(table)) [0]
df = df_full[['Distrito','População 2010']]
df.columns = ['Districts','Population']

# 5. Converting and saving the Data like a JSON Archieve
df.to_json('df_sp.json')

#js = json.dumps(df)
#fp = open('df.js', 'w')
#fp.write(js)
#fp.close()

time.sleep(10)


driver.quit()

