from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule

# Configurações do WebDriver (ajustar o caminho do driver)
driver_path = 'caminho_para_seu_webdriver'
driver = webdriver.Chrome(driver_path)

# Função para realizar login e clicar no botão
def login_e_interagir():
    # Abrir o site
    driver.get('https://app.pmovel.com.br/')

    # Localizar e preencher o campo de CPF
    cpf_input = driver.find_element(By.ID, 'email')
    cpf_input.send_keys('02605034798')

    # Localizar e preencher o campo de senha
    senha_input = driver.find_element(By.ID, 'password')
    senha_input.send_keys('Mktrj001@!')
    
    # Enviar o formulário de login
    senha_input.send_keys(Keys.RETURN)
    
    # Esperar o site carregar (tempo ajustável)
    time.sleep(5)

    # Clicar no botão desejado
    botao = driver.find_element(By.ID, 'id_do_botao')
    botao.click()

# Agendar horários diferentes para interagir automaticamente
schedule.every().monday.at("08:00").do(login_e_interagir)
schedule.every().wednesday.at("15:30").do(login_e_interagir)
schedule.every().friday.at("18:45").do(login_e_interagir)

# Loop para manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto
