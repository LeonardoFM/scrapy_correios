
from selenium import webdriver
import json
from src.scrapy_correios import Correios

ff = webdriver.Firefox()

c = Correios(ff)
c.navigate()
c.search_group_data(['SC','RJ'])

ff.close()

with open('data_out.jsonl', 'w', encoding='utf8') as f:
    for d in c.data:
        f.write(json.dumps(c.data[d],ensure_ascii=False)+'\n')
    f.close()

import pdb; pdb.set_trace()