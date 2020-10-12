from unittest import TestCase
from selenium import webdriver

from src.scrapy_correios import Correios

class CorreiosFriend(Correios):
    """ This set is used to test private methods only
    """
    def get_limits(self):
        self._get_limits()

    def get_all_lines_data(self, line):
        self._get_all_lines_data(line)

class TestCorreios(TestCase):
    """
        Test Correios class where the methods are defined to get
        zip range informations by location.
    """
    def setUp(self):
        self.url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
        self.results = 'ctrlcontent'

    def test_open_correios_page(self):
        ff = webdriver.Firefox()
        c = Correios(ff)
        self.assertTrue(isinstance(c,Correios))
        ff.close()

    def test_SC_data_limits(self):
        """ Open the search for SC location
        """
        ff = webdriver.Firefox()
        c = CorreiosFriend(ff)
        c.navigate()
        # select the UF
        c.driver.find_element_by_xpath(
            f"//select[@class='f1col']/option[text()='SC']").click()
        # search in page
        c.driver.find_element_by_class_name('btn2').click()
        # data range finded
        c.get_limits()
        # knowed limits: 1,50,322
        self.assertEqual(c.ini,1)
        self.assertEqual(c.total,322)
        self.assertEqual(c.step,50)
        ff.close()

    def test_line_cleanner(self):
        ff = webdriver.Firefox()
        c = CorreiosFriend(ff)
        c.navigate()
        # select the UF
        c.driver.find_element_by_xpath(
            f"//select[@class='f1col']/option[text()='SC']").click()
        # search in page
        c.driver.find_element_by_class_name('btn2').click()
        _in_page = c.driver.find_elements_by_xpath(f"//tr")        
        c.get_all_lines_data(_in_page)
        ff.close()

    def test_get_sc_zip_range(self):
        ff = webdriver.Firefox()
        c = Correios(ff)
        c.navigate()
        c.search_data('SC')
        self.assertGreaterEqual(len(c.data),0)
        self.assertGreaterEqual(c.total,len(c.data))
        ff.close()
    
    def test_two_groups(self):
        g = ['SC', 'RJ']
        ff = webdriver.Firefox()
        c = Correios(ff)
        c.navigate()
        c.search_group_data(g)
        ff.close()