class Correios:
    """ Correios page objects
    """
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
        self.uf = 'f1col'
        self.btn_search = 'btn2'
        self.results = 'ctrlcontent'

        self.id = 0
        self.data = {}

    def __repr__(self):
        """ return JSONL representation
        """
        rt = ''
        for d in self.data:
            rt += f"'id':{self.data[d]['id']},'localidade': {self.data[d]['localidade']},'faixa de cep': {self.data[d]['faixa de cep']}\n"
        return rt

    def _get_limits(self) -> tuple:
        text = self.driver.find_element_by_class_name(self.results).text
        text = text.split('\n')
        data_range = text[4].split('de')
        total = int(data_range[-1])
        ini, end = data_range[0].split('a')
        ini = int(ini)
        step = int(end)
        return ini, total, step

    def _get_all_lines_data(self, all_in_page) -> bool:
        try:
            #  to extract a line from all data in page
            data_line = all_in_page.pop()
            data_line = data_line.text.split(' ')
            name = ''
            for i, word in enumerate(data_line):
                w = word.split('-')
                if len(w) > 1:
                    zip_code = f'{word} a {data_line[i+2]}'
                    try:
                        # avoid duplication data
                        self.data[name]
                        return True

                    except:
                        self.id += 1
                        self.data.update(
                            {name: {'id': self.id, 'localidade': name, 'faixa de cep': zip_code}})
                        return True
                else:
                    name += f'{w[0]} '
            # end of data needed (only zip range)
            return False

        except:
            # pop not possible
            return False

    def navigate(self):
        self.driver.get(self.url)

    def search_data(self, uf=''):
        """ This search and populate data
        """
        # select the UF
        self.driver.find_element_by_xpath(
            f"//select[@class='{self.uf}']/option[text()='{uf}']").click()
        # search in page
        self.driver.find_element_by_class_name(self.btn_search).click()

        # all pages navigation
        ini, total, step = self._get_limits()
        for i in range(ini, total, step):

            all_in_page = self.driver.find_elements_by_xpath(f"//tr")

            lines = True
            while lines:
                lines = self._get_all_lines_data(all_in_page)

            try:
                # go to the next page
                nx = self.driver.find_element_by_partial_link_text("Próxima")
                nx.click()
            except:
                ...

    def search_group_data(self, group):
        """ all search list are concatenate in one group data
        """
        for g in group:
            self.search_data(g)
            self.driver.get(self.url)
