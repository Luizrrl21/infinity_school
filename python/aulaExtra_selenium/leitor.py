#Bibliotecas
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyttsx3

#Limpando terminal
# os.system('cls')

#Configuração
opcoes = Options()
opcoes.add_experimental_option("detach", True)

#Browser
navegador = webdriver.Chrome(ChromeDriverManager().install()) #Abrir navegador com configuração Ativada
navegador.maximize_window() #Máximizar tela
navegador.get("https://ge.globo.com/futebol/brasileirao-serie-a/") #Abrir site

#Paragrafos
paragrafo1 = navegador.find_element(By.XPATH, '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong')
paragrafo2 = navegador.find_element(By.XPATH, '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[2]/td[2]/strong')

#Narração
narrador = pyttsx3.init()
narrador.setProperty("rate", 250)
narrador.say("O líder do campeonato é o:")
narrador.say(paragrafo1.text)
narrador.say("O vice é o")
narrador.say(paragrafo2.text)
narrador.runAndWait()
