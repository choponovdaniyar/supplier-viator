from . import  script
from . import  to_excel
from loguru import  logger

def run():
    script.get_html()
    logger.debug("[start] <saving>")
    to_excel.to_excel()
    logger.debug("[finish] <saving>")