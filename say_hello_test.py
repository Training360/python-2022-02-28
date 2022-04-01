import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # When
    driver.get("http://127.0.0.1:5500/docs/welcome.html")
    return driver


def test_say_hello(driver: webdriver.Chrome):
    # Beviteli mező lekérdezése
    input_field = driver.find_element_by_id("name-input")
    # Írjuk bele, hogy John Doe
    input_field.send_keys("John Doe")
    # Kérjük le a gombot
    button = driver.find_element_by_id("hello-button")
    # Nyomjuk meg a gombot
    button.click()

    # THEN
    # Lekérjük az üzenetet tartalmazó p tag-et
    paragraph = driver.find_element_by_id("message-p")
    message = paragraph.text
    assert message == "Hello John Doe!"
    