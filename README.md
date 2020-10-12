# Scrapy correios with Python Selenium

Fom http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm the class Correios inside scrapy_correios file return the localization and the respective zip range for some UF given.

## Requirements
 
 - python 3.8
 - pip install -r requirements.txt

## Running

Basically we start with some webdriver to instantiate Correios class. We start the navigate method and then the search, which populate data statment inside the class. Only for one UF the class Correios has search_data method and for a UF's list search_group_data method should be used. 

 *In the main file we have an example how to run the scrapy_correios code using Correios class.*

    - python main.py