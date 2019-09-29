from flask import Flask, jsonify
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import scale

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    #json_ = request.json
    query_df = pd.DataFrame(data)
    
    X_test_scale=scale(query_df)

    prediction = model.predict(X_test_scale)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
     model = joblib.load('logistic_few_variables.pkl')
    
     app.run(port=8080)