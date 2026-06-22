import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "http://35.154.1.53:5000")

def test_frontend_sentiment():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "text-input").send_keys("This hotel was amazing")
        driver.find_element(By.ID, "submit-btn").click()
        time.sleep(3)
        result = driver.find_element(By.ID, "result-output").text
        assert result != ""
        assert "POSITIVE" in result or "NEGATIVE" in result or "Confidence" in result
    finally:
        driver.quit()
