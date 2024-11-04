import requests
from bs4 import BeautifulSoup

class WebScraper:
    def scrape_data(self):
        url = 'http://site.api.espn.com/apis/site/v2/sports/soccer/{league}/teams'  # Replace with actual URL
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        for item in soup.find_all('div', class_='data-item'):
            data.append({
                'feature1': item.find('span', class_='feature1').text,
                'feature2': item.find('span', class_='feature2').text,
                'label': item.find('span', class_='label').text
            })
        return data
