"""Flask API Server for Indian Market Price Scanner

This API server provides HTTP endpoints to access the price scanner functionality
and can be deployed to Render, Heroku, Railway, or any cloud platform.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Demo data representing scanned results
DEMO_DEALS = [
    {
        "id": "deal_001",
        "product_name": "Realme 12 Pro Plus",
        "marketplace": "Amazon",
        "original_price": 32999,
        "discounted_price": 23999,
        "discount_percentage": 27.3,
        "url": "https://amazon.in/realme-12-pro",
        "timestamp": "2026-05-03T14:00:00Z"
    },
    {
        "id": "deal_002",
        "product_name": "Samsung Galaxy A55",
        "marketplace": "Flipkart",
        "original_price": 44999,
        "discounted_price": 28999,
        "discount_percentage": 35.6,
        "url": "https://flipkart.com/samsung-a55",
        "timestamp": "2026-05-03T14:05:00Z"
    },
    {
        "id": "deal_003",
        "product_name": "iPhone 15 (Refurbished)",
        "marketplace": "Amazon",
        "original_price": 79900,
        "discounted_price": 59999,
        "discount_percentage": 24.9,
        "url": "https://amazon.in/iphone-15",
        "timestamp": "2026-05-03T14:10:00Z"
    },
    {
        "id": "deal_004",
        "product_name": "OnePlus 12R",
        "marketplace": "Myntra",
        "original_price": 39999,
        "discounted_price": 26999,
        "discount_percentage": 32.5,
        "url": "https://myntra.com/oneplus-12r",
        "timestamp": "2026-05-03T14:15:00Z"
    },
    {
        "id": "deal_005",
        "product_name": "Sony WH1000XM5 Headphones",
        "marketplace": "Flipkart",
        "original_price": 29990,
        "discounted_price": 19999,
        "discount_percentage": 33.3,
        "url": "https://flipkart.com/sony-wh1000xm5",
        "timestamp": "2026-05-03T14:20:00Z"
    },
    {
        "id": "deal_006",
        "product_name": "MacBook Air M2",
        "marketplace": "Croma",
        "original_price": 119900,
        "discounted_price": 89999,
        "discount_percentage": 24.9,
        "url": "https://croma.com/macbook-air-m2",
        "timestamp": "2026-05-03T14:25:00Z"
    }
]


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Indian Market Price Scanner API',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/deals', methods=['GET'])
def get_deals():
    """Get all deals from latest scan
    
    Query parameters:
    - threshold: Filter items below this discount percentage (default: 80)
    - marketplace: Filter by specific marketplace (optional)
    - limit: Maximum number of results (default: 50)
    """
    threshold = request.args.get('threshold', 80, type=float)
    marketplace = request.args.get('marketplace', None)
    limit = request.args.get('limit', 50, type=int)
    
    # Filter deals
    filtered_deals = DEMO_DEALS
    
    if marketplace:
        filtered_deals = [d for d in filtered_deals if d['marketplace'].lower() == marketplace.lower()]
    
    # Apply threshold filter
    filtered_deals = [d for d in filtered_deals if d['discount_percentage'] >= (100 - threshold)]
    
    # Limit results
    filtered_deals = filtered_deals[:limit]
    
    return jsonify({
        'total_deals': len(filtered_deals),
        'scan_timestamp': datetime.utcnow().isoformat(),
        'deals': filtered_deals
    }), 200


@app.route('/api/deals/<deal_id>', methods=['GET'])
def get_deal(deal_id):
    """Get details for a specific deal"""
    deal = next((d for d in DEMO_DEALS if d['id'] == deal_id), None)
    
    if not deal:
        return jsonify({'error': 'Deal not found'}), 404
    
    return jsonify(deal), 200


@app.route('/api/scan', methods=['POST'])
def start_scan():
    """Start a new price scan
    
    Request body (JSON):
    {
        "marketplaces": ["amazon", "flipkart"],
        "threshold": 80
    }
    """
    data = request.get_json() or {}
    
    return jsonify({
        'status': 'queued',
        'scan_id': f'scan_{int(datetime.utcnow().timestamp())}',
        'message': 'Scan queued. In production, this would start a background task.',
        'estimated_duration': '5-10 minutes',
        'timestamp': datetime.utcnow().isoformat()
    }), 202


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get API status and metadata"""
    return jsonify({
        'service_name': 'Indian Market Price Scanner API',
        'version': '1.0.0',
        'status': 'operational',
        'supported_marketplaces': [
            'Amazon', 'Flipkart', 'Myntra', 'AJIO', 'Croma', 'Meesho', 'eBay India'
        ],
        'endpoints': {
            'health': '/api/health',
            'deals': '/api/deals',
            'deal_detail': '/api/deals/<deal_id>',
            'scan': '/api/scan',
            'status': '/api/status'
        },
        'documentation': 'https://github.com/srinivasdrmf/indian-market-price-scanner',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API documentation"""
    return jsonify({
        'message': 'Welcome to Indian Market Price Scanner API',
        'description': 'Scan Indian e-commerce platforms for products below 80% of original price',
        'quick_start': {
            'get_all_deals': 'GET /api/deals',
            'filter_by_discount': 'GET /api/deals?threshold=80',
            'filter_by_marketplace': 'GET /api/deals?marketplace=amazon',
            'get_deal_details': 'GET /api/deals/deal_001',
            'check_health': 'GET /api/health',
            'get_status': 'GET /api/status'
        },
        'example_response': DEMO_DEALS[0]
    }), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
