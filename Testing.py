import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time 

class TestTranslate:
    #Traductor de google
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()

    def test_traduccion_correcta(self, setup):
        #Verificar que el traductor de google realice una traducción correcta del español al inglés.
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
        #Verificar la misma traducción del punto anterior pero utilizando el teclado virtual.
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
        #Verificar que no se permita ingresar más de 5000 caracteres.
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')
        str = ''
        for i in range(500):             
            str = str + "aaaaaaaaaa"
        input.send_keys(str) #Enviamos una cadena de 5000 caracteres compuesta por el caracter a
        input.send_keys("b") #En la posicion 5001 mandamos el caracter 'b', que no debería poder ser ingresado.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        span =self.driver.find_element(By.CSS_SELECTOR, 'span[jsname="qKMVIf"]') #Recuperamos el contador de caracteres
        compare =self.driver.find_element(By.CLASS_NAME, 'D5aOJc') #Recuperamos el string
        assert not "b" in compare.get_attribute('innerHTML') and '5.000' in span.get_attribute('innerHTML') 
        #^^^^^^La cantidad de caracteres debe ser 5000 y b no debe aparecer en la cadena

    def test_traductor_contador(self, setup):    
        #Verificar que el contador de caracteres ingresados en la traductor de google sea la correcta.
        self.driver.get("https://translate.google.com.ar/?hl=es&sl=es&tl=en&op=translate")
        self.driver.maximize_window()
        span =self.driver.find_element(By.CSS_SELECTOR, 'span[jsname="qKMVIf"]')
        input1 =self.driver.find_element(By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')
        input1.send_keys("Hola Mundo, mi nombre es el destructor de mundos")
        assert '48' in span.get_attribute('innerHTML')  

class TestYoutube:
    #Youtube
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()
    
    def test_watchlist(self, setup):
        #Ingresar con una cuenta válida, verificar que al agregar un video a la lista de “Ver más tarde”, este video se agregue efectivamente a la lista
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.youtube.com")
        self.driver.maximize_window()
        #Acceder a la cuenta:
        button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading "]')
        button.click()
        wait.until(EC.url_changes)
        input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        input.send_keys('CREDENCIALES CORRECTAS')
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
        button.click()
        input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
        input.send_keys('CREDENCIALES CORRECTAS')
        button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
        button.click()
        #Redirigir al Home
        time.sleep(3) #Se espera este tiempo porque a veces la página termina de cargar antes de que carguen todos los elementos.
        video = self.driver.find_element(By.ID, 'video-title')
        video.click()
        #Ir a un video
        wait.until(EC.url_changes)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button "]')))
        button.click()
        padre = self.driver.find_element(By.CSS_SELECTOR, 'tp-yt-paper-listbox[id="items"]')
        hijos = padre.find_elements(By.CSS_SELECTOR, 'yt-formatted-string[class="style-scope ytd-menu-service-item-renderer"]')
        for hijo in hijos:  #Buscar el botón Guardar en el submenú
            if 'Guardar' in hijo.get_attribute('innerHTML'):
                hijo.click()
                break            
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'yt-formatted-string[title="Ver más tarde"]')))
        button.click()
        titulo = self.driver.title #Guardamos el titulo del video
        time.sleep(15) #Se espera este tiempo porque a veces youtube tarda en agregar un video a "Ver más tarde"
        self.driver.get('https://www.youtube.com/playlist?list=WL')
        wait.until(EC.url_changes)
        time.sleep(2) #Se espera este tiempo porque a veces la página termina de cargar antes de que carguen todos los elementos.
        video = self.driver.find_element(By.CSS_SELECTOR, 'a[class="yt-simple-endpoint style-scope ytd-playlist-video-renderer"]')
        print(video.get_attribute('innerHTML'))
        assert titulo[-8] in video.get_attribute('innerHTML')  
        #Titulo[-8] Es porque se borra el - Youtube que aparece al final del título

    def test_modo_oscuro(self, setup):
        #Verificar que se active exitosamente la opción de Aspecto oscuro.
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

class TestUGD:
    #Página de la UGD
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()
    
    def test_buscador(self, setup):
        #Verificar que el buscador funciona correctamente, en el texto de los resultados se debe encontrar por lo menos una vez la palabra buscada. 
        #Comprobar para al menos el primer resultado obtenido.
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
        #Verificar que al cambiar al idioma a inglés, el menú superior se encuentre correctamente traducido
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
        assert 'Home' in university.get_attribute('innerHTML') and 'Studies' in studies.get_attribute('innerHTML') and 'students' in students.get_attribute('innerHTML') and 'Contact' in contact.get_attribute('innerHTML')

class TestCampus:
    #Campus virtual
    @pytest.fixture

    def setup(self):
        self.driver = webdriver.Chrome()
        yield 
        self.driver.quit()
    
    def test_buscador(self, setup):
        #Ingresar con una cuenta válida, ir a Todos los cursos, ingresar al aula de la materia a partir del buscador, 
        #utilizando las palabras “gestion de calidad”. Verificar que se ingresa correctamente al aula virtual correspondiente.
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
        #Verificar que al ingresar con un usuario válido, se visualice el mensaje que contenga el siguiente texto
        # “..no deberá registrar deuda luego del día 10 de cada mes.“.. en alguna parte de la página.
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
        final = self.driver.find_element("xpath","//*[text()[contains(., 'no deberá registrar deuda luego del día 10 de cada mes')]]")
        if final == None: #Si no encontró un elemento que contenga el texto 'no deberá registrar deuda luego del día 10 de cada mes':
            res = False
        else:   #Si lo encuentra:
            res = True
        assert res

    def test_footer(self, setup):
        #Verificar que, al ingresar con un usuario válido, el link del footer “Horario de cátedra” redirige a la página correcta.
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
        button=self.driver.find_element(By.XPATH, '//a[text() = "Horario de Cátedra"]')
        button.click()
        wait.until(EC.new_window_is_opened)
        chwd = self.driver.window_handles
        self.driver.switch_to.window(chwd[1])
        wait.until(EC.url_changes)
        assert 'Horarios de cátedra' in self.driver.title  

    def test_error_credenciales(self, setup):
        #Verificar que al intentar iniciar sesión con credenciales inválidas se visualice un mensaje de error. 
        #Verificar también que el mensaje de error se encuentre correctamente escrito.
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
        msj= self.driver.find_element(By.ID, 'loginerrormessage')        
        assert 'Datos erróneos, por favor inténtelo de nuevo. Recuerde que el usuario se bloquea al adeudar la cuota el día 17 del mes vigente o más cuotas' in msj.get_attribute('innerHTML')