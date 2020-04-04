from tests.framework.webapp import webapp
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class EsikaPageObjects():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = EsikaPageObjects()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def seleccionarCategoria(self, categoria):
        time.sleep(4)
        menu = self.driver.find_element_by_xpath("//div[@id='lbel-03']//a[contains(text(),{})]".format(categoria))
        action = ActionChains(self.driver)
        action.move_to_element(menu)
        action.perform()


    def seleccionarTipo(self, tipo):
        #self.driver.find_element_by_xpath("//li[contains(@class,'yCmsComponent nav__link--secondary')]//a[contains(text(),{})]".format(tipo)).click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/header[1]/nav[3]/div[1]/ul[2]/li[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[6]/a[1]").click()

    def ingresarFichaDelProducto(self, cualquiera):
        self.driver.find_element_by_id("product_productName_{}".format(cualquiera)).click()


    def agregarCantidad(self, cantidad):
        time.sleep(3)
        self.driver.find_element_by_id("pdpAddtoCartInput").clear()
        self.driver.find_element_by_id("pdpAddtoCartInput").send_keys(cantidad)

    def seleccionarAgregarBolsa(self):
        time.sleep(3)
        self.driver.find_element_by_id("addToCartButton").click()

    def seleccionarIrBolsa(self):
        self.driver.find_element_by_id("/html/body/main/div[1]/header/nav[1]/div/div/div[2]/div/ul/li[2]/div/div[2]/div/a/div[2]").click()

    def seleccionarIrPagarPopPup(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='addToCartLayer']/a[1]").click()

    def seleccionarIrPagar(self):
        self.driver.get("https://compra.tiendabelcorp.com/pe/cart/checkout");


    def ingresarComoInvitado(self, invitado):
        time.sleep(3)
        arrInvitado = invitado.split(";")
        self.driver.find_element_by_id("guest.firstName").send_keys(arrInvitado[0])
        self.driver.find_element_by_id("guest.lastName").send_keys(arrInvitado[1])
        self.driver.find_element_by_id("guest.email").send_keys(arrInvitado[2])
        self.driver.find_element_by_id("guest.confirm.email").send_keys(arrInvitado[2])
        self.driver.find_element_by_xpath("//*[@id='guestForm']/div[8]/button").click()

    def ingresarDireccionEnvio(self, envio):
        arrEnvio = envio.split(";")
        select1 = Select(self.driver.find_element_by_xpath("//*[@id='address.regionIsoParent2']"))
        select1.select_by_value(arrEnvio[0])
        time.sleep(1)
        select2 = Select(self.driver.find_element_by_xpath("//*[@id='address.regionIsoParent1']"))
        select2.select_by_value(arrEnvio[1])
        time.sleep(1)
        select3 = Select(self.driver.find_element_by_xpath("//*[@id='address.regionIso']"))
        select3.select_by_value(arrEnvio[2])
        self.driver.find_element_by_id("address.line1").send_keys(arrEnvio[3])
        self.driver.find_element_by_id("address.line2").send_keys(arrEnvio[4])
        self.driver.find_element_by_id("address.referencia").send_keys(arrEnvio[5])
        self.driver.find_element_by_id("address.phone").send_keys(arrEnvio[6])
        time.sleep(1)
        self.driver.find_element_by_id("addressSubmit").click()

esikaPageObjects = EsikaPageObjects.get_instance()