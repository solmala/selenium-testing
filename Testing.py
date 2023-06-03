import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTranslate:
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()

    def test_traduccion_correcta(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        input1 =self.driver.find_element(By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')
        input1.send_keys("Hola mundo, mi nombre es el destructor de mundos")
        traduciendo=self.driver.find_element(By.CLASS_NAME, 'xsPT1b')
        wait.until(EC.visibility_of(traduciendo))
        wait.until_not(EC.visibility_of(traduciendo))
        input2 =self.driver.find_element(By.CLASS_NAME, 'ryNqvb')
        assert "Hello world, my name is the destroyer of worlds" in input2.get_attribute('innerHTML')

    def test_traduccion_teclado_virtual(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        teclado = self.driver.find_element(By.CLASS_NAME, 'ita-kd-icon-button')
        teclado.click()
        wait.until_not(EC.invisibility_of_element((By.ID, 'kbd')))
        string="Hola mundo, mi nombre es el destructor de mundos"
        for i in range(len(string)):
            if string[i] == ' ':
                button = self.driver.find_element(By.ID, 'K32')
                button.click()
            elif string[i] == ',':
                button = self.driver.find_element(By.ID, 'K188')
                button.click()
            else:
                if string[i].isupper():
                    button = self.driver.find_element(By.ID, 'K16')
                    button.click
                num = ord(string[i].lower())-32
                id = 'K' + str(num)
                button = self.driver.find_element(By.ID, id)
                button.click()
        traduciendo=self.driver.find_element(By.CLASS_NAME, 'xsPT1b')
        wait.until(EC.visibility_of(traduciendo))
        wait.until_not(EC.visibility_of(traduciendo))
        input2 =self.driver.find_element(By.CLASS_NAME, 'ryNqvb')
        assert "Hello world, my name is the destroyer of worlds" in input2.get_attribute('innerHTML')

    def test_traductor_5000caracteresMax(self, setup):
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')
        str = ''
        for i in range(500):  
            str = str + "aaaaaaaaaa"
        input.send_keys(str)
        input.send_keys("b")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        span =self.driver.find_element(By.CSS_SELECTOR, 'span[jsname="qKMVIf"]')
        compare =self.driver.find_element(By.CLASS_NAME, 'D5aOJc')
        assert not "b" in compare.get_attribute('innerHTML') and '5.000' in span.get_attribute('innerHTML') 

    def test_traductor_contador(self, setup):    
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        span =self.driver.find_element(By.CSS_SELECTOR, 'span[jsname="qKMVIf"]')
        input1 =self.driver.find_element(By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')
        input1.send_keys("Hola Mundo, mi nombre es el destructor de mundos")
        assert '48' in span.get_attribute('innerHTML')  