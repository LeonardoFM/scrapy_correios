# Scrapy Correios (blazilian post office) with Python Selenium

Fom http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm the class Correios inside scrapy_correios file return the localization and the respective zip range for some 
location (UF) given.

## Requirements
 
 - python 3.9 https://www.python.org/downloads/
 - Firefox browser
 - geckodriver https://github.com/mozilla/geckodriver/releases/tag/v0.27.0
 - Selenium

## Install in Windows

 - First to clone this project we need the Git https://gitforwindows.org/
 - Link to install python3 https://python.org.br/instalacao-windows/
 - and set the global variable Path with geckodriver.exe location
 - Install Selenium with pip

    pip install -r requirements.txt

## Install in Linux

 - Git to start

    sudo apt-get install git # Ubuntu

or

    sudo pacman -Sy git # Arch linux

 - Install the webdriver Ubuntu

    tar -xvf geckodriver-v_.__._-linux64.tar.gz # extract

    chmod +x geckodriver # to excecute

    sudo mv geckodriver /usr/local/bin/ # move to the right place

or in Arch linux using yaourt
   
   yaourt -s geckodriver # Arch linux

 - Finally Selenium

   pip install -r requirements.txt

## Running

Basically we start with some webdriver to instantiate Correios class. Start the navigate method and then the search, which populate data statment inside the class. For one location the class Correios has search_data method and for a list the search_group_data method should be used. 

 *In the main file we have an example how to run the scrapy_correios code using Correios class.*

    python main.py

## Run the tests

Inside project folder with Linux SO the command line is:

    python -m unittest test/test_correio_scrapy.py