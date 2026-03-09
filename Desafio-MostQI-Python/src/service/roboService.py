from playwright.sync_api import sync_playwright
from core.settings import settings
from utils.util import generateID
import requests
import base64
from datetime import datetime

# Navega até o portal da transparência e obtém os dados
def searchData(cpf, nome, nis, beneficiario):
    screenshot: bytes
    resultado: list

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(settings.SITE_URL)

        page.click("#button-consulta-pessoa-fisica")

        page.fill("#termo", cpf)
        # Caso o parâmetro beneficiario esteja preenchido
        if beneficiario:
            page.fill("#beneficiarioProgramaSocial", beneficiario)

        page.click("text=Consultar")
        page.wait_for_selector("table tbody tr")

        page.click("table tbody tr:first-child a")
        page.wait_for_timeout(3000)

        linhas = page.query_selector_all(".linha-beneficio")

        for linha in linhas:

            programa = linha.query_selector(".programa").inner_text()
            valor = linha.query_selector(".valor").inner_text()
            mes = linha.query_selector(".mes").inner_text()
            municipio = linha.query_selector(".municipio").inner_text()

            resultado.append({
                "programa": programa,
                "valor": valor,
                "mes_referencia": mes,
                "municipio": municipio
            })

        # Print do elemento que contém os resultados
        screenshot = page.screenshot(path="")

        browser.close()

    # Converte o print para base64
    base64_screenshot_string = base64.b64encode(screenshot).decode("utf-8")

    n8nWorkflowRequest(cpf=cpf, nome=nome, nis=nis, beneficiario=beneficiario, resultado=resultado,
                       screenshot_base64=base64_screenshot_string)

def n8nWorkflowRequest(cpf, nome, nis, beneficiario, resultado, screenshot_base64):
    url = settings.WORKFLOW_API

    payload = {
        "id": generateID(),
        "nome": nome,
        "cpf": cpf,
        "nis": nis,
        "beneficiario": beneficiario,
        "resultado": resultado,
        "screenshot": screenshot_base64,
        "data_consulta": datetime.now().isoformat()
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Erro ao enviar para n8n:", response.text)

    return response.json()