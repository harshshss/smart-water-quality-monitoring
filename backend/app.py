from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Static water quality data for Northeast Indian areas
water_quality_data = {
    "Guwahati": {
        "area": "Guwahati",
        "turbidity": 4.2,
        "ph": 7.1,
        "tds": 145,
        "status": "Good"
    },
    "Shillong": {
        "area": "Shillong",
        "turbidity": 2.8,
        "ph": 6.9,
        "tds": 120,
        "status": "Excellent"
    },
    "Imphal": {
        "area": "Imphal",
        "turbidity": 5.1,
        "ph": 7.3,
        "tds": 180,
        "status": "Good"
    },
    "Kohima": {
        "area": "Kohima",
        "turbidity": 3.5,
        "ph": 7.0,
        "tds": 135,
        "status": "Good"
    },
    "Aizawl": {
        "area": "Aizawl",
        "turbidity": 3.2,
        "ph": 6.8,
        "tds": 110,
        "status": "Excellent"
    },
    "Agartala": {
        "area": "Agartala",
        "turbidity": 6.8,
        "ph": 7.4,
        "tds": 220,
        "status": "Fair"
    },
    "Itanagar": {
        "area": "Itanagar",
        "turbidity": 4.7,
        "ph": 7.2,
        "tds": 160,
        "status": "Good"
    },
    "Gangtok": {
        "area": "Gangtok",
        "turbidity": 2.1,
        "ph": 6.7,
        "tds": 95,
        "status": "Excellent"
    }
}

@app.route('/api/areas', methods=['GET'])
def get_areas():
    """Get list of all available areas"""
    areas = list(water_quality_data.keys())
    return jsonify({"areas": areas})

@app.route('/api/water-quality/<area>', methods=['GET'])
def get_water_quality(area):
    """Get water quality data for a specific area"""
    if area in water_quality_data:
        return jsonify(water_quality_data[area])
    else:
        return jsonify({"error": "Area not found"}), 404

@app.route('/api/water-quality', methods=['GET'])
def get_all_water_quality():
    """Get water quality data for all areas"""
    return jsonify(water_quality_data)

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"message": "Smart Water Quality Monitoring API is running", "status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
