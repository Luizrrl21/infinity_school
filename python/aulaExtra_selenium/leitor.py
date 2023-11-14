#Bibliotecas
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyttsx3


#Limpando terminal
os.system('cls')

#Configuração
opcoes = Options()
opcoes.add_experimental_option("detach", True)

#Browser
navegador = webdriver.Chrome(options=opcoes) #Abrir navegador com configuração Ativada
navegador.maximize_window() #Máximizar tela
navegador.get("https://www.contosdeterror.site/") #Abrir site

#Selecionar história
leia_mais = navegador.find_element(By.XPATH, '//*[@id="Blog1"]/div[1]/article[2]/div/div/div[4]/div[2]/a') #Inspecionar -> Copy XPATH
leia_mais.click()

#Paragrafos
paragrafo1 = navegador.find_element(By.XPATH, '//*[@id="post-body-4073905748094003101"]/p[10]/span')

#Narração
narrador = pyttsx3.init()
narrador.setProperty("rate", 150)
narrador.say(paragrafo1.text)
narrador.runAndWait()
