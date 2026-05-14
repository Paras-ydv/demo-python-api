from flask import Blueprint, request, jsonify

export_bp = Blueprint('export', __name__)

@export_bp.route('/export', methods=['POST'])
def handle_export():
    data = request.get_json()
    return jsonify({
        'success': True,
        'message': f"Processed: {data.get('name')}"
    })

@export_bp.route('/export/<id>', methods=['GET'])
def get_export(id: str):
    return jsonify({
        'id': id,
        'data': 'sample data'
    })
# auto-commit: 1778735992354