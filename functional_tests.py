from selenium import webdriver
#browser = webdriver.Firefox()
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('http://localhost:8000')
assert 'Django' in browser.title