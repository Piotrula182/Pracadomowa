from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    total = a + b
    prediction = 1 if total > 5.8 else 0

    return jsonify({
        "features": {"a": a, "b": b},
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
