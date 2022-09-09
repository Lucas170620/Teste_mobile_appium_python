import random

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.config.AppiumCapabilities import capabilites_android
from tests.map.calculatorElements import CalculatorElements

class CalculatorTest:
    def __init__(self):
        self.driver = webdriver.Remote(
            "https://oauth-lucascandidosantos2014-43f24:b1c868df-f165-46f4-a35e-244ddb37a760@ondemand.us-west-1.saucelabs.com:443/wd/hub",
            capabilites_android)
        self.elements = CalculatorElements(self.driver)

    def testar_somar(self,primero_numero,segundo_numero,resultado_esperado):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.elements.btn))
        self.elements.clicar_botao_numero(primero_numero)
        self.elements.btn_sum.click()
        self.elements.clicar_botao_numero(segundo_numero)
        self.elements.btn_equal.click()
        print("Somar {} por {}".format(primero_numero, segundo_numero))
        print(" Resultado Obtido: {}".format(self.elements.mostrarResultado()))
        print(" Resultado Esperado: {}".format(resultado_esperado))

        try:
            assert self.elements.mostrarResultado() == resultado_esperado
            print("Passou")
        except:
            print("Não Passou")

    def testar_subtrair(self,primeiro_valor,segundo_valor,resultado_esperado):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.elements.btn))
        self.elements.clicar_botao_numero(primeiro_valor)
        self.elements.btn_sub.click()
        self.elements.clicar_botao_numero(segundo_valor)
        self.elements.btn_equal.click()
        print("Subtrair {} por {}".format(primeiro_valor, segundo_valor))
        print(" Resultado Obtido: {}".format(self.elements.mostrarResultado()))
        print(" Resultado Esperado: {}".format(resultado_esperado))

        try:
            assert self.elements.mostrarResultado() == resultado_esperado
            print("Passou")
        except:
            print("Não Passou")

    def testar_dividir(self,primeiro_valor,segundo_valor,resultado_esperado):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.elements.btn))
        self.elements.clicar_botao_numero(primeiro_valor)
        self.elements.btn_div.click()
        self.elements.clicar_botao_numero(segundo_valor)
        self.elements.btn_equal.click()
        print("Dividir {} por {}".format(primeiro_valor, segundo_valor))
        print(" Resultado Obtido: {}".format(self.elements.mostrarResultado()))
        print(" Resultado Esperado: {}".format(resultado_esperado))

        try:
            assert self.elements.mostrarResultado() == resultado_esperado
            print("Passou")
        except:
            print("Não Passou")

    def testar_multiplicar(self,primeiro_valor,segundo_valor,resultado_esperado):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.elements.btn))
        self.elements.clicar_botao_numero(primeiro_valor)
        self.elements.btn_mult.click()
        self.elements.clicar_botao_numero(segundo_valor)
        self.elements.btn_equal.click()
        print("Multiplicar {} por {}".format(primeiro_valor,segundo_valor))
        print(" Resultado Obtido: {}".format(self.elements.mostrarResultado()))
        print(" Resultado Esperado: {}".format(resultado_esperado))

        try:
            assert self.elements.mostrarResultado() == resultado_esperado
            print("Passou")
        except:
            print("Não Passou")




    def runAll(self):
        for i in range(10):
            a = random.randint(0,9)
            b = random.randint(0,9)
            self.testar_somar(a,b,str(a+b))
            self.testar_subtrair(a,b,str(a-b))
            self.testar_multiplicar(a,b,str(a*b))
            if b == 0:
                self.testar_dividir(a,b,"Não é possível dividir por zero")
            else:
                self.testar_dividir(a,b,str(a/b))
        self.driver.quit()