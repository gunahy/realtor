import os
import urllib.request
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from main.models import Announce

URL = 'https://www.avito.ru/tyumen/kvartiry/prodam-ASgBAgICAUSSA8YQ?p=1'
BASE_DIR = r'..\static\avito'
SOURCE = 'https://www.avito.ru'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

def convert_date(datestr):
    months = {
        'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04',
        'мая': '05', 'июня': '06', 'июля': '07', 'августа': '08',
        'сентября': '09', 'октября': '10', 'ноября': '11', 'декабря': '12',
        }

    date_str = datestr.split(' ')
    time = datestr[3].split(':')
    return datetime(int(date_str[2]), int(months[date_str[1]]), int(date_str[0]),
                    int(time[0]), int(time[1]), int(time[2]))


def get_html(url):
    html = requests.get(url, HEADERS)
    return html.text


def split_address_for_dirname(address):
    dirs = address.split()
    dirname = '\\'.join(dirs)
    return f'{BASE_DIR}\\{dirname}'


def download_images_from_url(html, dirname):
    soup = BeautifulSoup(html, 'html.parser')
    photos = soup.find_all('img', class_='large-picture-img')

    for img in photos:
        url = img['src']
        name = str(url.split('/')[-1])
        urllib.request.urlretrieve(url, os.path.join(dirname, name))


def get_page_content():
    soup = BeautifulSoup(get_html(URL), 'html.parser')
    ad_list = soup.find('div', class_='snippet-list')
    ad_items = ad_list.find('div', class_='item_table')

    ad_reference = []
    for i, ad in enumerate(ad_items):
        try:
            title = ad.find('h3', class_='snippet-title').text.strip()
        except:
            title = ''
        try:
            row_url = ad.find('a', class_='snippet-link')['href']
            url = f'{SOURCE}{row_url}'
        except:
            url = ''
        try:
            address = ad.find('span', class_='item-address__string').text.strip()
            dirname = split_address_for_dirname(address)
        except:
            address = ''
            dirname = r'..\static\avito\tmp'
        try:
            district = ad.find('span', class_='item-address-georeferences-item__content').text.strip()
        except:
            district = ''
        try:
            price = ad.find('span', class_='snippet-price').text.strip()
            price = float(price.split('  ')[0].replace(' ', ''))
        except:
            price = 0
        try:
            published = ad.find('div', class_='snippet-date-info')['data-tooltip']
        except:
            published = ''
        try:
            images_html = ad.find('ul', class_='item-slider-list')
            download_images_from_url(images_html, dirname)
        except:
            pass

        new_ad = Announce.objects.get_or_create(
            title=title,
            address=address,
            district=district,
            images_path=dirname,
            url=url,
            price=price,
            #published_date=published,
            source=SOURCE,
        )
        if new_ad[1]:
            ad_reference.append(new_ad[0])
    #return ad_reference


def main():
    print(get_page_content())


if __name__ == '__main__':
    main()
