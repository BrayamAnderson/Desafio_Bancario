# numeros = {"Teste maior":{"numero": 1,"braco": "grande","perna": "Precisa melhorar"}}

# def testando(nome = "Brayam"):
#     # for numero in numeros:
    
#     print(f"Realizando teste {nome}")
    
#     return testando

# def mundo():
#     print("Ola mundo!")

# print(mundo())


# import selenium
# selenium.__version__

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)


# def abrindo_studeo():
#     driver.get("https://studeo.unicesumar.edu.br/#!/access/login")
#     driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("201317175")
#     driver.find_element('xpath','//*[@id="password"]').send_keys("Brayan@7")

#     driver.find_element('xpath','//*[@id="login-form-studeo"]/div[3]/form/div[3]/div/button').click()

# abrindo_studeo()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

def abrindo_studeo():
    driver.get("https://studeo.unicesumar.edu.br/#!/access/login")

    # Espera até que o campo de usuário esteja visível
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    username_input.send_keys("201317175")

    # Localiza e preenche a senha
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password_input.send_keys("Brayan@7")

    # Clica no botão de login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form-studeo"]/div[3]/form/div[3]/div/button'))
    )
    login_button.click()

    fechar_anuncio = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/ui-view/ui-view/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/button'))
    )
    fechar_anuncio.click()


    fale_mediador = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/ui-view/ui-view/div[1]/div/div[1]/div[1]/div/ul/li/uni-messenger/div/a'))
    )
    fale_mediador.click()


# Chama a função para abrir o Studeo e fazer login
# abrindo_studeo()

def abrindo_youtube():
    driver.get("https://www.youtube.com/")
    driver.find_element('xpath','//*[@id="search"]').send_keys("Selenium com python #11")

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="search"]'))
    )
    username_input.send_keys("Olá Maelly")


abrindo_youtube()
