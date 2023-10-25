import requests
from bs4 import BeautifulSoup

class ScraperController:
    def index(self):
        search_term = request.args.get('search_term', '').replace(' ', '+')
        jumia_url = "https://www.jumia.co.ke/phones-tablets/"
        jambo_url = "https://www.jamboshop.com/category/Mobile-Phones/2"
        shopit_url = "https://shopit.co.ke/electronics/"
        jiji_url = "https://jiji.co.ke/mobile-phones"
        jumia_url_game = "https://www.jumia.co.ke/video-games/"
        jiji_url_games = "https://jiji.co.ke/videogames"
        
        games = self.scrape_jumia_games(jumia_url_game)
        games2 = self.scrape_jiji_games(jiji_url_games)
        prod = self.scrape_jumia(jumia_url)
        prod3 = self.scrape_jiji(jiji_url)
        
        return {
            'jumia': prod,
            'jiji': prod3,
            'jumia_game': games,
            'jiji_games': games2
        }

    def scrape_jumia(self, jumia_url):
        result = []
        response = requests.get(jumia_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd')
        for item in items:
            # Scrape item details
            result.append(item.text.strip())
        return result

    def scrape_jumia_games(self, jumia_url_game):
        result = []
        response = requests.get(jumia_url_game)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd')
        for item in items:
            # Scrape item details
            result.append(item.text.strip())
        return result

    def scrape_jiji_games(self, jiji_url_games):
        result = []
        response = requests.get(jiji_url_games)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd')
        for item in items:
            # Scrape item details
            result.append(item.text.strip())
        return result

    def scrape_jiji(self, jiji_url):
        result = []
        response = requests.get(jiji_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.select('.aim.row.-pbm .-pvs.col12 .card.-fh .-paxs.row._no-g._4cl-3cm-shs .prd._fb.col.c-prd')
        for item in items:
            # Scrape item details
            result.append(item.text.strip())
        return result