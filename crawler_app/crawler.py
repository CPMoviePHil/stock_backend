import requests
from bs4 import BeautifulSoup
from crawler_app.models import PCHStock
from datetime import datetime
from django.utils import timezone


class Crawler:
    def get_html(self):
        url = "http://pchome.megatime.com.tw/stock/sto1/ock4/sid1101.html"
        r = requests.post(url, {
            'is_check': 1,
        })
        web_content = r.text
        soup = BeautifulSoup(web_content, 'html.parser')
        main_div = soup.find(id="mainprice")
        tables = main_div.findAll('table')
        table1 = self.parse_table(tables[0].find('tbody'))
        self.save_to_table(table1)
        table2 = self.parse_table(tables[1].find('tbody'))
        self.save_to_table(table2)

    @staticmethod
    def parse_table(table_body) -> list:
        rows = table_body.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data

    @staticmethod
    def save_to_table(table: list):
        for index, item in enumerate(table):
            if index != 0:
                PCHStock.objects.create(
                    stock_name=item[0],
                    buy_price=item[1],
                    sell_price=item[2],
                    average_buy_price=item[3],
                    average_sell_price=item[4],
                    net_buy=item[5],
                    stock_date=datetime.now().strftime("%Y/%m/%d"),
                    create_datetime=datetime.now(tz=timezone.utc),
                )




