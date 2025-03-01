from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    boton_pedir_taxi = (By.CSS_SELECTOR, "button.button.round")
    boton_tarifa_comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    campo_numero_telefono = (By.CLASS_NAME, "np-button")
    agregar_numero_de_telefono = (By.ID, 'phone')
    boton_siguiente_numero_de_telefono = (By.CSS_SELECTOR, ".button.full")
    campo_ingresar_codigo = (By.ID, "code")
    boton_confirmar_codigo = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    click_metodo_de_pago = (By.CSS_SELECTOR, '.pp-button.filled')
    click_agregar_tarjeta = (By.CSS_SELECTOR, '.pp-row.disabled')
    campo_tarjeta_rellenar = (By.ID, 'number')
    campo_nip_rellenar = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    click_para_perder_foco = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[2]')
    boton_agregar_tarjeta = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    boton_cerrar_ventana_emergente = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    obtener_metodo_de_pago = (By.CLASS_NAME, "pp-value-text")
    campo_comentario = (By.ID, "comment")
    slider_manta_y_pañuelos = (By.CSS_SELECTOR, ".slider.round")
    boton_agregar_helado = (By.CLASS_NAME, 'counter-plus')
    obtener_cantidad_de_helados = (By.CLASS_NAME, 'counter-value')
    pedir_taxi = (By.CLASS_NAME, 'smart-button')
    titulo_ventana_emerente = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver
#ingresa desde
    def set_from(self, from_address):
        from_field_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.from_field))
        from_field_element.send_keys(from_address)
        time.sleep(2)

    #ingresa hasta
    def set_to(self, to_address):
        to_field_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.to_field))
        to_field_element.send_keys(to_address)
        time.sleep(2)
#ingresa desde y hasta
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)
        time.sleep(2)
#obtener valor desde
    def get_from(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.from_field)
        ).get_property('value')

    time.sleep(2)
#obtener valor hasta
    def get_to(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.to_field)
        ).get_property('value')

    time.sleep(2)

#click en el boton pedir un taxi
    def set_click_boton_pedir_un_taxi(self):
        pedir = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_pedir_taxi)))
        pedir.click()
        time.sleep(2)
#click en tarifa comfort
    def set_click_boton_comfort(self):
        clickComfort = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_tarifa_comfort)))
        clickComfort.click()
        time.sleep(2)
#obtener valor de boton de tarifa comfort
    def get_boton_comfort(self):
        textoTarifaComfort = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_tarifa_comfort))).text
        return textoTarifaComfort

    time.sleep(2)
#click en el boton numero de telefono
    def set_boton_numero_telefono(self):
        clickNumeroDeTelefono = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_numero_telefono)))
        clickNumeroDeTelefono.click()
        time.sleep(2)
#ingresar numero de telefono
    def set_ingresar_numero_de_telefono(self, numero):
        agregarNumero = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.agregar_numero_de_telefono)))
        agregarNumero.send_keys(numero)
        time.sleep(2)
#Click en el boton siguiente para despeus obtener el codigo
    def set_click_boton_siguiente_numero_telefono(self):
        siguiente = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_siguiente_numero_de_telefono)))
        siguiente.click()
        time.sleep(2)
#obtener codigo
#ingresa el codigo en el campo
    def set_ingresar_codigo(self, codigo):
        ingresarCodigo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_ingresar_codigo)))
        ingresarCodigo.send_keys(codigo)
        time.sleep(2)
#confirmar codigo
    def set_confirmar_codigo(self):
        confirmar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_confirmar_codigo)))
        confirmar.click()
        time.sleep(2)
#obtener numero de telefono
    def get_numero_telefono(self):
        numero = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_numero_telefono)))
        return numero.text

    time.sleep(2)
    def set_proceso_numero_de_telefono_ingresar(self, numero):
        self.set_boton_numero_telefono()
        self.set_ingresar_numero_de_telefono(numero)
        self.set_click_boton_siguiente_numero_telefono()
    def set_codigo_numero_telefono(self, codigo):
        self.set_ingresar_codigo(codigo)
        self.set_confirmar_codigo()
#click en metodo de pago
    def set_click_metodo_pago(self):
        tarjetaCredito = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.click_metodo_de_pago)))
        tarjetaCredito.click()
        time.sleep(2)
#click en agregar tarjeta
    def set_click_agregar_tarjeta_por_favor(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.pp-row.disabled'))).click()
        time.sleep(2)

    #click metodo de pago y campo agregar tarjeta
    def set_clicks_metodo_pago_agregar_tarjeta(self):
        self.set_click_metodo_pago()
        self.set_click_agregar_tarjeta_por_favor()
#ingresar numero de tarjeta en campo numero de tarjeta
    def set_rellenar_campo_tarjeta(self, numeroDeTarjeta):
        ingresarTarjeta = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_tarjeta_rellenar)))
        ingresarTarjeta.send_keys(numeroDeTarjeta)
        time.sleep(2)
#ingresar codigo en el campo codigo
    def set_rellenar_campo_codigo(self, numeroCode):
        ingresarCodigo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_nip_rellenar)))
        ingresarCodigo.send_keys(numeroCode)
        time.sleep(2)
#ingresar campo tarjeta y campo codigo
    def set_rellenar_campos_tarjeta_y_codigo(self, numeroDeTarjeta, numeroCode):
        self.set_rellenar_campo_tarjeta(numeroDeTarjeta)
        self.set_rellenar_campo_codigo(numeroCode)
#obtener valor campo tarjeta
    def get_obtener_campo_tarjeta(self):
        ingresarTarjeta = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_tarjeta_rellenar)))
        return ingresarTarjeta.get_property('value')

    time.sleep(2)
#obtener valor campo codigo
    def get_obtener_campo_codigo(self):
        ingresarCodigo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_nip_rellenar)))
        return ingresarCodigo.get_property('value')

    time.sleep(2)
#Dar click para perder el enfoque
    def set_click_para_derder_el_enfoque(self):
        ckickOtroLado = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.click_para_perder_foco)))
        ckickOtroLado.click()
        time.sleep(2)
#click en agregar tarjeta
    def set_click__boton_agregar_tarjeta(self):
        clickAgregar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_agregar_tarjeta)))
        clickAgregar.click()
        time.sleep(2)
#cerrar ventana <button class="close-button section-close"></button>
    def set_click_cerrar_ventana_emergente(self):
        cerrarVentana = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_cerrar_ventana_emergente)))
        cerrarVentana.click()
        time.sleep(2)
#perder enfoque, agregar tarjeta, cerrar ventana emergente
    def set_clicks_perder_enfoque_agregar_tarjeta_cerrar_ventana(self):
        self.set_click_para_derder_el_enfoque()
        self.set_click__boton_agregar_tarjeta()
        self.set_click_cerrar_ventana_emergente()
#obtener valor de metodo de pago
    def get_obtener_metodo_de_pago(self):
        comprobarTexto = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.obtener_metodo_de_pago)))
        return comprobarTexto.text

    time.sleep(2)
#agregar comentario al conductor
    def set_agregar_comentario(self, message_for_driver):
        agregarComentario = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_comentario)))
        agregarComentario.send_keys(message_for_driver)
        time.sleep(2)
#comprobarComentario
    def get_comprobar_comentario(self):
        comprobarComentario = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.campo_comentario)))
        return comprobarComentario.get_attribute('value')

    time.sleep(2)
#hacer click en manta y pañuelos
    def set_click_manta_y_pañuelos(self):
        clickSlider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.slider_manta_y_pañuelos)))
        clickSlider.click()
        time.sleep(2)
#saber si esta seleccionado el slider
    def get_saber_si_slider_esta_seleccionado(self):
        apretar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']//input[@class='switch-input']")))
        return apretar.is_selected()

    time.sleep(2)
#agregar helado
    def set_agregar_helado(self):
        mashelado = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.boton_agregar_helado)))
        mashelado.click()
        mashelado.click()
        time.sleep(2)
#obtener cantidad de helados
    def get_cantidad_de_helados(self):
        helado = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.obtener_cantidad_de_helados)))
        return helado.text

    time.sleep(2)
#hacer click pedir taxo
    def set_click_pedir_taxi(self):
        pedir = self.driver.find_element(*self.pedir_taxi)
        pedir.click()
#comprobar valor ventana emergente
    def get_comprobar_ventana_emergente_si(self):
        emergente = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.titulo_ventana_emerente)))
        return emergente.text

    time.sleep(2)
#darle tiempo
    def set_tiempo(self):
        nuevaVentana = WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((self.titulo_ventana_emerente), 'El conductor llegará en'))
#el coductor llegara en...
    def get_comprobar_informacion_de_conductor(self):
        otro = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.titulo_ventana_emerente)))
        return otro.text
