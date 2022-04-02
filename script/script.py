#selenium, loguru, fake_useragent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from loguru import logger
from fake_useragent import UserAgent

from os.path import abspath
import time

from .config import USER_LOGIN, USER_PASSWORD


def get_html():
    settings = webdriver.FirefoxOptions()
    settings.set_preference("general.useragent.override", UserAgent().random)
    browser = webdriver.Firefox(executable_path=abspath('geckodriver.exe'), options=settings)

    try:
        url = "https://supplier.viator.com/"
        browser.get(url)
        logger.debug("[finish] <opening a web-page [{url}]> ".format(url=url))
        time.sleep(3)

        email = browser.find_element("css selector", "input")
        email.send_keys(USER_LOGIN)
        logger.debug("[finish] <input e-mail [{email}]> ".format(email=USER_LOGIN))
        time.sleep(3)

        try:
            button = browser.find_element("css selector", "button")
            button.send_keys(Keys.ENTER)
        except ElementNotInteractableException as e:
            pass
        finally:
            logger.debug("[finish] <push button>")
        time.sleep(3)

        password = browser.find_elements("css selector", "input")[-1];
        password.send_keys(USER_PASSWORD)
        logger.debug("[finish] <input password [{password}]>".format(email='*'*len(USER_PASSWORD)))
        time.sleep(3)

        button = browser.find_element("css selector", "button")
        button.send_keys(Keys.ENTER)
        logger.debug("[finish] <push button>")
        time.sleep(3)

        browser.get("https://supplier.viator.com/products")
        body = browser.find_element("css selector", "body")
        logger.debug("[finish] <opening a web-page [{url}]> ".format(url=url))
        time.sleep(3)

        # 1 итерация = +20 позиции, длину цикла надо настраивать вручную
        logger.debug("[start] <get product data> ")
        for x in range(110):
            body.send_keys(Keys.END)
            with open("result.html", "w", encoding="utf-8") as f:
                f.write(browser.pag_source)
            logger.debug("[finish] <save in html [it={it}]> ".format(it=x))
            time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        browser.quit()