import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
   options = Options()
   options.add_argument('--headless')
   options.add_argument('--no-sandbox') # чтоб Docker пахал
   browser = webdriver.Chrome(options=options)
   # browser = webdriver.Chrome()
   browser.maximize_window()
   browser.implicitly_wait(5)
   yield browser
   browser.close()