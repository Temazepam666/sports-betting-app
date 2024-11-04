from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatBotInterface:
    def __init__(self, ml_model):
        self.bot = ChatBot('SportsBot')
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        self.trainer.train('chatterbot.corpus.english')
        self.ml_model = ml_model

    def start(self):
        print("ChatBot is ready to make predictions. Type 'exit' to stop.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            features = self.extract_features(user_input)
            prediction = self.ml_model.predict(features)
            response = f'Prediction: {prediction}'
            print(f'Bot: {response}')

    def extract_features(self, user_input):
        # Implement your feature extraction logic here
        features = [0, 0]  # Replace with actual logic
        return features
