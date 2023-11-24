import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


class ClaroShopScraper:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1020,1200")
        chrome_service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.data = {"Producto": [], "Comentarios": [], "Precio": [], "Tipo de envio": [], "Descuento": [],
                     "Precio anterior": []}

    def lanzar_pagina(self):
        self.browser.get("https://www.claroshop.com/")
        time.sleep(10)  # Tiempo de espera aumentado

    def click_productos_gamer(self):
        menu = self.browser.find_element(By.XPATH,
                                         "//*[@id='__next']/div[1]/header/div[1]/div[2]/div/nav[2]/ul[1]/li[3]/a")
        menu.click()
        time.sleep(10)

    def scraper_html(self):
        for pagina in range(1, 31):
            try:
                if pagina > 1:
                    pagina_xpath = f"//a[@href='/categoria/21827/videojuegos/pagina={pagina}']"
                    siguiente_pagina = WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, pagina_xpath))
                    )
                    siguiente_pagina.click()
                    time.sleep(10)  #tiempo de espere aumentado para dejar que los elementos del html terminen e cargarse

                soup = BeautifulSoup(self.browser.page_source, "html.parser")
                lista_divs = soup.find_all("div", class_="contDataCard")

                for div in lista_divs:
                    self.extraer_datos(div)
            except Exception as e:
                print(f"Error en la página {pagina}: {e}")

    def extraer_datos(self, div):
        producto = div.find("h3", class_="h4")
        comentarios = div.find("p", class_="comments")
        precio = div.find("p", class_="precio1")
        tipo_envio = div.find("p", class_="fullFilment")
        descuento = div.find("span", class_="discoutnCard")
        precio_anterior = div.find("span", class_="textUnderline")

        self.data["Producto"].append(producto.text.strip() if producto else "")
        self.data["Comentarios"].append(comentarios.text.strip() if comentarios else "")
        self.data["Precio"].append(precio.text.strip() if precio else "")
        self.data["Tipo de envio"].append(tipo_envio.text.strip() if tipo_envio else "Normal")
        self.data["Descuento"].append(descuento.text.strip() if descuento else "")
        self.data["Precio anterior"].append(precio_anterior.text.strip() if precio_anterior else "")

    def guardar_csv(self, filename="ClaroShop.csv"):
        data_df = pd.DataFrame(self.data)
        data_df.to_csv(filename, index=False)

    def cerrar_navegador(self):
        self.browser.quit()


if __name__ == "__main__":
    scraper = ClaroShopScraper()
    scraper.lanzar_pagina()
    scraper.click_productos_gamer()
    scraper.scraper_html()
    scraper.guardar_csv()
    scraper.cerrar_navegador()
