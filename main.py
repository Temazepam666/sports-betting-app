from web_scraper import WebScraper
from ml_model import MLModel
from chatbot import ChatBotInterface

def main():
    scraper = WebScraper()
    model = MLModel()
    chatbot = ChatBotInterface(model)
    data = scraper.scrape_data()
    model.train(data)
    chatbot.start()

if __name__ == "__main__":
    main()
