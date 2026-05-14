from flask import Blueprint, request, jsonify

worker_bp = Blueprint('worker', __name__)

@worker_bp.route('/worker', methods=['POST'])
def handle_worker():
    data = request.get_json()
    return jsonify({
        'success': True,
        'message': f"Processed: {data.get('name')}"
    })

@worker_bp.route('/worker/<id>', methods=['GET'])
def get_worker(id: str):
    return jsonify({
        'id': id,
        'data': 'sample data'
    })
# auto-commit: 1778732331969