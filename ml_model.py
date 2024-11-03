import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class MLModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, data):
        # Convert data to DataFrame
        df = pd.DataFrame(data, columns=['feature1', 'feature2', 'label'])

        # Preprocess data
        X = df[['feature1', 'feature2']]
        y = df['label']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        self.model.fit(X_train, y_train)

        # Evaluate model
        accuracy = self.model.score(X_test, y_test)
        print(f'Model Accuracy: {accuracy * 100:.2f}%')

    def predict(self, features):
        return self.model.predict([features])
