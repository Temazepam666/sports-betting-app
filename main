from web_scraper import WebScraper
from ml_model import MLModel
from chatbot import ChatBot

def main():
    # Initialize components
    scraper = WebScraper()
    model = MLModel()
    chatbot = ChatBot(model)

    # Scrape data
    data = scraper.scrape_data()

    # Train model
    model.train(data)

    # Start chatbot
    chatbot.start()

if __name__ == "__main__":
    main()
