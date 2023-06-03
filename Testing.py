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

class TestUGD:
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Edge()
        yield 
        self.driver.quit()
    
    def test_buscador(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://ugd.edu.ar/')
        self.driver.maximize_window()
        input = self.driver.find_element(By.ID, 'mod-search-searchword')
        input.send_keys('Ingeniería')
        input.send_keys(Keys.RETURN)
        wait.until(EC.url_changes)
        label = self.driver.find_element(By.CLASS_NAME, 'highlight')
        assert 'Ingeniería' in label.get_attribute('innerHTML')

    def test_english(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://ugd.edu.ar/')
        self.driver.maximize_window()
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="btn dropdown-toggle"]')
        button.click()
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/en/"]')
        button.click()
        wait.until(EC.url_changes)
        university=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/en/"]')
        studies=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/en/studies"]')
        students=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/en/incoming-students"]')
        contact=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/en/sedes"]')
        #Assert Home o University?
        assert 'Home' in university.get_attribute('innerHTML') and 'Studies' in studies.get_attribute('innerHTML') and 'Students' in students.get_attribute('innerHTML') and 'Contact' in contact.get_attribute('innerHTML')

class TestCampus:
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Edge()
        yield 
        self.driver.quit()
    
    def test_buscador(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://campusvirtual.ugd.edu.ar/')
        self.driver.maximize_window()
        input = self.driver.find_element(By.ID, 'username')
        input.send_keys('CREDENCIALES CORRECTAS')
        input = self.driver.find_element(By.ID, 'password')
        input.send_keys('CREDENCIALES CORRECTAS')
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Ingresar"]')
        button.click()
        wait.until(EC.url_changes)
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[title="Todos los Cursos"]')
        button.click()
        wait.until(EC.url_changes) 
        self.driver.execute_script("window.scrollTo(500, document.body.scrollHeight);")
        input = self.driver.find_element(By.ID, 'navsearchbox')
        input.send_keys('gestion de calidad')
        input.send_keys(Keys.RETURN)
        wait.until(EC.url_changes)
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="https://campusvirtual.ugd.edu.ar/moodle/course/view.php?id=64"]')
        button.click()
        wait.until(EC.url_changes)
        assert "GESTION DE LA CALIDAD Y AUDITORIA" in self.driver.title

    def test_aviso(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://campusvirtual.ugd.edu.ar/')
        self.driver.maximize_window()
        input = self.driver.find_element(By.ID, 'username')
        input.send_keys('CREDENCIALES CORRECTAS')
        input = self.driver.find_element(By.ID, 'password')
        input.send_keys('CREDENCIALES CORRECTAS')
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Ingresar"]')
        button.click()
        wait.until(EC.url_changes)      
        assert self.driver.find_element("xpath","//*[text()[contains(., 'no deberá registrar deuda luego del día 10 de cada mes')]]")

    def test_footer(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://campusvirtual.ugd.edu.ar/')
        self.driver.maximize_window()
        input = self.driver.find_element(By.ID, 'username')
        input.send_keys('CREDENCIALES CORRECTAS')
        input = self.driver.find_element(By.ID, 'password')
        input.send_keys('CREDENCIALES CORRECTAS')
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Ingresar"]')
        button.click()
        wait.until(EC.url_changes)      
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button=self.driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.ugd.edu.ar/la-universidad/alumnos/horarios-de-catedra"]')
        button.click()
        wait.until(EC.new_window_is_opened)
        chwd = self.driver.window_handles
        self.driver.switch_to.window(chwd[1])
        wait.until(EC.url_changes)
        assert 'Horarios de cátedra' in self.driver.title  

    def test_error_credenciales(self, setup):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://campusvirtual.ugd.edu.ar/')
        self.driver.maximize_window()
        input = self.driver.find_element(By.ID, 'username')
        input.send_keys('CREDENCIAL ERRONEA')
        input = self.driver.find_element(By.ID, 'password')
        input.send_keys('CREDENCIAL ERRONEA')
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Ingresar"]')
        button.click()
        wait.until(EC.url_changes) 
        assert self.driver.find_element(By.ID, 'loginerrormessage')
