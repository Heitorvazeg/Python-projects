from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("https://www.workana.com/pt/jobs?category=it-programming&language=pt")

    time.sleep(5)

    projetos = driver.find_elements(By.CSS_SELECTOR, ".project-title a")[:10]

    with open("projetos.txt", "w", encoding="utf-8") as arquivo:
        for i, projeto in enumerate(projetos):
            titulo  = projeto.text.strip()
            link = projeto.get_attribute("href")
            arquivo.write(f"{i}. {titulo} {link}\n")

except:
    print("erro ao executar script!")

finally:
    driver.quit()