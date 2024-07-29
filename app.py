from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

def scrape_bianca():
    # Configurar o Selenium com ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Rodar em modo headless
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # URL do site a ser raspado
        url = 'https://bianca.com'
        driver.get(url)
        
        time.sleep(5)  # Esperar a página carregar completamente

        # Exemplo de como encontrar elementos (modifique conforme necessário)
        elements = driver.find_elements(By.TAG_NAME, 'h1')
        data = [element.text for element in elements]
        
        return data
    
    finally:
        driver.quit()

@app.route('/scrape', methods=['GET'])
def scrape():
    try:
        data = scrape_bianca()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
