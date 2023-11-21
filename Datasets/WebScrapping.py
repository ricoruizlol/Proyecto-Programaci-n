import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


class ClaroShopScraper:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--window-size=1020,1200")
        self.browser = webdriver.Chrome(service=self.service, options=self.options)
        self.data = {"Producto": [], "Comentarios": [], "Precio": [], "Tipo de envio": [], "Descuento": [], "Precio anterior": []}

    def lanzar_pagina(self):
        self.browser.get("https://www.claroshop.com/")
        time.sleep(5)

    def click_productos_gamer(self):
        menu = self.browser.find_element(By.XPATH, "//*[@id='__next']/div[1]/header/div[1]/div[2]/div/nav[2]/ul[1]/li[3]/a")
        menu.click()
        time.sleep(5)

    def scraper_html(self):
        for _ in range(10):
            segunda_pagina = self.browser.find_element(By.XPATH, "//*[@id='root']/main/section[2]/div/div[2]/ul/li[11]/a")
            segunda_pagina.click()
            time.sleep(2)
            soup = BeautifulSoup(self.browser.page_source, "html.parser")
            lista_divs = soup.find_all(name="div", attrs={"class": "contDataCard"})

            for i in lista_divs[1:]:
                self.extraer_datos(i)

    def extraer_datos(self, div):
        producto = div.find("h3", attrs={"class": "h4"})
        comentarios = div.find("p", attrs={"class": "comments"})
        precio = div.find("p", attrs={"class": "precio1"})
        tipo_envio = div.find("p", attrs={"class": "fullFilment"})
        descuento = div.find("span", attrs={"class": "discoutnCard"})
        precio_anterior = div.find("span", attrs={"class": "textUnderline"})

        self.data["Producto"].append(producto.text)
        self.data["Comentarios"].append(comentarios.text if comentarios else "")
        self.data["Precio"].append(precio.text if precio else "")
        self.data["Tipo de envio"].append(tipo_envio.text if tipo_envio else "Normal")
        self.data["Descuento"].append(descuento.text if descuento else "" )
        self.data["Precio anterior"].append(precio_anterior.text if precio_anterior else "")

    def guardar_csv(self, filename="ClaroShop.csv"):
        data_df = pd.DataFrame(self.data)
        data_df.to_csv(filename)

    def cerrar_navegador(self):
        self.browser.close()

# bloque para lanzar el scraper
if __name__ == "__main__":
    scraper = ClaroShopScraper()
    scraper.lanzar_pagina()
    scraper.click_productos_gamer()
    scraper.scraper_html()
    scraper.guardar_csv()
    scraper.cerrar_navegador()
