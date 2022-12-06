from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import glob
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def get_local_path():
        current_dir = os.path.dirname(os.path.realpath(__file__))
        return current_dir

class BaseTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.page_load_strategy = 'normal'
        cls.driver = WebDriver(options = options)
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        print("../recetario/media/images")
        files = glob.glob(get_local_path()+"\..\\recetario\media\images\*.jpg")
        print("Removiendo archivos creados de pruebas...")
        for f in files:
            os.remove(f)
        cls.driver.quit()

    #Test para cargar el sitio y crear una receta
    def test_CargaPagina(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3\n")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"success-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))

    #Test para crear y ver una receta
    def test_VerReceta(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3\n")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"success-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))
        
        ## Acceso a la información de la sopaipilla
        ActionChains(self.driver).click(self.driver.find_element(By.ID, "verRecetas")).perform()
        wait.until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        wait.until(EC.presence_of_element_located((By.NAME,'verReceta')))
        texto = self.driver.find_element(By.NAME,"verReceta")
        assert texto.text == "Ver Receta"
        ActionChains(self.driver).click(texto).perform()
        texto2 = self.driver.find_element(By.ID,"MENU_PREPARACION")
        assert texto2.text == "Preparacion:"
    
    #Test para crear y actualizar el valor de una receta
    def test_ActualizarReceta(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3\n")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"success-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))
        ## Ver la receta
        ActionChains(self.driver).click(self.driver.find_element(By.ID, "verRecetas")).perform()
        wait.until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        wait.until(EC.presence_of_element_located((By.NAME,'verReceta')))
        texto = self.driver.find_element(By.NAME,"verReceta")
        assert texto.text == "Ver Receta"
        ActionChains(self.driver).click(texto).perform()
        texto2 = self.driver.find_element(By.ID,"MENU_PREPARACION")
        assert texto2.text == "Preparacion:"
        ## Editar la receta
        ActionChains(self.driver).click(self.driver.find_element(By.ID,"editarReceta")).perform()
        page = self.driver.find_element(By.ID,"EDITAR_RECETA")
        assert page.text == "Editar Receta"
        nombre2 = self.driver.find_element(By.NAME,"nombreReceta")
        nombre2.send_keys("2") 
        file2 = self.driver.find_element(By.NAME, "imagenReceta")
        file2.send_keys(get_local_path()+"\sopaipilla.jpg")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(page).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"success-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))
        # Ver la receta
        ActionChains(self.driver).click(self.driver.find_element(By.ID, "verRecetas")).perform()
        wait.until(EC.presence_of_element_located((By.ID,'explanation')))
        nombre3 = self.driver.find_element(By.ID, "NOMBRE_RECETA")
        assert nombre3.text == "Sopaipilla2"
    
    #Test para crear y eliminar una receta
    def test_eliminarReceta(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3\n")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"success-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))
        ## Ver la receta
        ActionChains(self.driver).click(self.driver.find_element(By.ID, "verRecetas")).perform()
        wait.until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        wait.until(EC.presence_of_element_located((By.NAME,'verReceta')))
        texto = self.driver.find_element(By.NAME,"verReceta")
        assert texto.text == "Ver Receta"
        ActionChains(self.driver).click(texto).perform()
        texto2 = self.driver.find_element(By.ID,"MENU_PREPARACION")
        assert texto2.text == "Preparacion:"
        ## Eliminar la receta
        ActionChains(self.driver).click(self.driver.find_element(By.ID, "eliminarReceta")).perform()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"

    #Test de caso incorrecto, cuando no se ingresan en el formato deseado los ingredientes
    def test_AddRecetaIncorrectaING(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina Huevos Zapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3\n")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ROBOT")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"failed-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
    
    #Prueba caso incorrecto, cuando no se agregan correctamente los pasos
    def test_AddRecetaIncorrectaPasos(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1 Paso2 Paso3")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ROBOT")
        imagen = self.driver.find_element(By.NAME, "imagenReceta")
        imagen.send_keys(get_local_path()+"\sopaipilla.jpg")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.visibility_of_element_located((By.ID,"failed-alert")))
        wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))

    #Prueba de caso fallido, para cuando una receta no tiene imagen
    def test_AddRecetaIncorrectaImg(self):
        wait = WebDriverWait(self.driver, 15)
        ## Creacion de la sopaipilla
        self.driver.get(self.live_server_url)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'explanation')))
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll.text == "Ver recetas"
        button1 = self.driver.find_element(By.ID,"anadirReceta")
        ActionChains(self.driver).move_to_element(poll).click(button1).perform()
        menu = self.driver.find_element(By.ID,'MENU_ADDRECETA')
        assert menu.text == "Añadir receta"
        nombre = self.driver.find_element(By.NAME, "nombreReceta") 
        nombre.send_keys("Sopaipilla")
        ingredientes = self.driver.find_element(By.NAME, "ingredientes")
        ingredientes.send_keys("Harina\nHuevos\nZapallo")
        pasos = self.driver.find_element(By.NAME, "pasos")
        pasos.send_keys("Paso1\nPaso2\nPaso3")
        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("ROBOT")
        buttonadd = self.driver.find_element(By.ID, "BOTON_ADD_RECETA")
        
        element = wait.until(EC.invisibility_of_element_located((By.ID,"failed-alert")))
        ActionChains(self.driver).click(buttonadd).perform()
        wait.until(EC.invisibility_of_element_located((By.ID,"success-alert")))

    
