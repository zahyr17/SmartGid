from flask import Flask, jsonify, request

app = Flask(__name__)

# Namunaviy ma'lumotlar
locations = [
    {"id": 1, "name": "Talabalar parki", "category": "park", "target": "student"},
    {"id": 2, "name": "Qimmatbaho restoran", "category": "restoran", "target": "general"},
]

@app.route('/api/locations', methods=['GET'])
def get_locations():
    user_type = request.args.get('type', 'general')
    filtered = [loc for loc in locations if loc['target'] == user_type or loc['target'] == 'general']
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(port=8000, debug=True)