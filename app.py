from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

app = Flask(__name__)

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict function


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting a JSON request
    features = data.get('features', [])

    if not features:
        return jsonify({'error': 'No features provided'}), 400

    try:
        features = [features]  # Convert to 2D array
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        return jsonify({'prediction': int(prediction[0])})  # Convert NumPy int to Python int
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Home route
@app.route('/')
def home():
    return "Iris Prediction API is Running!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# this is a comment
# this is another comment
