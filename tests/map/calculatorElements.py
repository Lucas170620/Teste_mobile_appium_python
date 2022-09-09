from appium.webdriver.common.appiumby import AppiumBy

class CalculatorElements:
    def __init__(self,driver):
        self.driver = driver
        self.btn = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_1")
        self.btn_sum = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
        self.btn_sub = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="minus")
        self.btn_div = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="divide")
        self.btn_mult = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiply")
        self.btn_equal = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")

    def mostrarResultado(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final").text

    def clicar_botao_numero(self,numero):
        self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_"+str(numero)).click()
