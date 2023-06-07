import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time 

""" class TestTranslate:
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
        assert '48' in span.get_attribute('innerHTML')   """



class TestYoutube:
    #No anda
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()
    
    def test_watchlist(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.youtube.com")
        self.driver.maximize_window()
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading "]')
        button.click()
        wait.until(EC.url_changes)
        input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        input.send_keys('credenciales validas')
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
        button.click()
        input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
        input.send_keys('credenciales validas')
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
        button.click()
        time.sleep(3) 
        video = self.driver.find_element(By.ID, 'video-title')
        video.click()
        wait.until(EC.url_changes)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button "]')))
        button.click()
        padre = self.driver.find_element(By.CSS_SELECTOR, 'tp-yt-paper-listbox[id="items"]')
        hijos = padre.find_elements(By.CSS_SELECTOR, 'yt-formatted-string[class="style-scope ytd-menu-service-item-renderer"]')
        for hijo in hijos:
            if 'Guardar' in hijo.get_attribute('innerHTML'):
                hijo.click()
                #time.sleep(5)
                break            
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'yt-formatted-string[title="Ver más tarde"]')))
        button.click()
        titulo = self.driver.title
        print (titulo)
        time.sleep(15)
        self.driver.get('https://www.youtube.com/playlist?list=WL')
        wait.until(EC.url_changes)
        time.sleep(2)
        video = self.driver.find_element(By.CSS_SELECTOR, 'a[class="yt-simple-endpoint style-scope ytd-playlist-video-renderer"]')
        print(video.get_attribute('innerHTML'))
        assert titulo[-8] in video.get_attribute('innerHTML') 

    def test_modo_oscuro(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.youtube.com")
        self.driver.maximize_window()
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Configuración"]')
        button.click()
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Aspecto")]')))
        button.click()
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[(text()="Tema oscuro")]')))
        button.click()
        wait.until(EC.url_changes)
        time.sleep(3)
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Configuración"]')
        button.click()
        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="style-scope ytd-toggle-theme-compact-link-renderer"]')))
        assert 'Oscuro' in button.get_attribute('innerHTML')