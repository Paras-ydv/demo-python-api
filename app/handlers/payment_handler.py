from flask import Blueprint, request, jsonify

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['POST'])
def handle_payment():
    data = request.get_json()
    return jsonify({
        'success': True,
        'message': f"Processed: {data.get('name')}"
    })

@payment_bp.route('/payment/<id>', methods=['GET'])
def get_payment(id: str):
    return jsonify({
        'id': id,
        'data': 'sample data'
    })
# auto-commit: 1778586657197