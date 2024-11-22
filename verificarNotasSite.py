import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.system('cls')
raConta = input('Digite o RA da sua conta do Portal ENIAC: ')
senhaConta = input('Digite a senha da sua conta do Portal ENIAC: ')
os.system('cls')
decisao = int(input('Qual curso você deseja acessar?\n1\tGamificação\n2\tInteração Humano-Computador\n3\tRealidade Virtual e Aumentada\n\nDigite o número da matéria que deseja saber: '))
driver = webdriver.Edge()
driver.get('https://eniac-edu.grupoa.education/plataforma/auth/signin?returnUrl=%2F')
driver.set_window_size(1920, 1080)
os.system('cls')
print("Carregando informações, aguarde um instante...")

try:
    def logar():
        time.sleep(3)
        ra = driver.find_element(By.ID, '47')
        ra.click()
        ra.clear()
        ra.send_keys(f"{raConta}")

        senha = driver.find_element(By.ID, '52')
        senha.click()
        senha.clear()
        senha.send_keys(f"{senhaConta}")

        continuar = driver.find_element(By.CLASS_NAME, 'v-btn__content')
        continuar.click()
        time.sleep(3)
    
    def verNotas():
        wait = WebDriverWait(driver, 30)
        disciplinas = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-v-a14e34a4]")))
        disciplinas.click()
        time.sleep(3)
        global decisao
        if decisao == 1:
            gamificacao = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="discipline-Gamificação (EMI3-INFO)"]')))
            gamificacao.click()
        elif decisao == 2:
            ihc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="discipline-Interação Humano - Computador (EMI3-INFO)"]')))
            ihc.click()
        elif decisao == 3:
            realidade = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="discipline-Realidade Virtual e Aumentada (EMI3-INFO)"]')))
            realidade.click()
        time.sleep(3)
        gradeNotas = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Grade de Notas"]')))
        gradeNotas.click()
        time.sleep(3)
        elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "v-chip__content")))
        notas = [element.text for element in elements]
        exercicios = notas[0]
        desafios = notas[1]
        prova = notas[2]
        driver.quit()
        os.system('cls')
        desafios = float(desafios.replace(',', '.'))
        media = (float(exercicios)*0.2)+(desafios*0.3)+(float(prova)*0.5)
        print(f'Você tirou {exercicios} nos exercícios do portal, {desafios} nos desafios e {prova} na prova! Além disso, sua média final foi {media}. Parabéns pelo seu esforço e dedicação! 🤗')

    logar()
    verNotas()
    
except Exception as err:
    print(f'Algo deu errado. Erro: {err}')