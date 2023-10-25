from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name)

class ScraperController:
    @app.route('/index', methods=['GET'])
    def index():
        search_term = request.args.get('search_term', '').replace(' ', '+')

        jumia_url = "https://www.jumia.co.ke/phones-tablets/"
        jambo_url = "https://www.jamboshop.com/category/Mobile-Phones/2"
        shopit_url = "https://shopit.co.ke/electronics/"
        jiji_url = "https://jiji.co.ke/mobile-phones"
        jumia_url_game = "https://www.jumia.co.ke/video-games/"
        jiji_url_games = "https://jiji.co.ke/videogames"

        jumia_products = scrape_jumia(jumia_url)
        jumia_games = scrape_jumia_games(jumia_url_game)
        jiji_games = scrape_jiji_games(jiji_url_games)
        jiji_products = scrape_jiji(jiji_url)

        return jsonify({
            'jumia': jumia_products,
            'jumia_game': jumia_games,
            'jiji': jiji_products,
            'jiji_games': jiji_games
        })

    def scrape_jumia(jumia_url):
        result = []
        response = requests.get(jumia_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd'):
            img = item.select('a.core div.img-c img.img')[0]['data-src']
            title = item.select('.core .info h3.name')[0].text
            price = item.select('.core .info div.prc')[0].text.strip()
            link = "https://jumia.co.ke" + item.select('.core')[0]['href']

            result.append({'title': title, 'price': price, 'img': img, 'link': link})

        return result

    def scrape_jumia_games(jumia_url_game):
        result = []
        response = requests.get(jumia_url_game)
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd'):
            img = item.select('a.core div.img-c img.img')[0]['data-src']
            title = item.select('.core .info h3.name')[0].text
            price = item.select('.core .info div.prc')[0].text.strip()
            link = "https://jumia.co.ke" + item.select('.core')[0]['href']

            result.append({'title': title, 'price': price, 'img': img, 'link': link})

        return result

    def scrape_jiji(jiji_url):
        result = []
        response = requests.get(jiji_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.b-list-advert__gallery__item.js-advert-list-item'):
            img = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__img__wrapper.b-list-advert-base__img__wrapper--one-image .b-list-advert-base__img.js-list-advert-base-img .h-flex-center.h-width-100p.h-height-100p.h-overflow-hidden img')[0]['src']
            title = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__data .b-list-advert-base__data__inner .b-list-advert-base__data__header .b-list-advert-base__data__title .qa-advert-list-item-title.b-list-advert-base__item-title .b-advert-title-inner.qa-advert-title.b-advert-title-inner--div')[0].text
            price = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__data .b-list-advert-base__data__inner .b-list-advert-base__data__header div.b-list-advert__price.h-mt-3 div.qa-advert-price')[0].text.strip()
            link = "https://jiji.co.ke" + item['href']

            result.append({'img': img, 'title': title, 'price': price, 'link': link})

        return result

    def scrape_jiji_games(jiji_url_games):
        result = []
        response = requests.get(jiji_url_games)
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.b-list-advert__gallery__item.js-advert-list-item'):
            img = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__img__wrapper.b-list-advert-base__img__wrapper--one-image .b-list-advert-base__img.js-list-advert-base-img .h-flex-center.h-width-100p.h-height-100p.h-overflow-hidden img')[0]['src']
            title = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__data .b-list-advert-base__data__inner .b-list-advert-base__data__header .b-list-advert-base__data__title .qa-advert-list-item-title.b-list-advert-base__item-title .b-advert-title-inner.qa-advert-title.b-advert-title-inner--div')[0].text
            price = item.select('.b-list-advert-base.qa-advert-list-item.b-list-advert-base--gallery .b-list-advert-base__data .b-list-advert-base__data__inner .b-list-advert-base__data__header div.b-list-advert__price.h-mt-3 div.qa-advert-price')[0].text.strip()
            link = "https://jiji.co.ke" + item['href']

            result.append({'img': img, 'title': title, 'price': price, 'link': link})

        return result

if __name__ == '__main__':
    app.run(debug=True)
