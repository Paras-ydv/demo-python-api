from flask import Blueprint, request, jsonify

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['POST'])
def handle_report():
    data = request.get_json()
    return jsonify({
        'success': True,
        'message': f"Processed: {data.get('name')}"
    })

@report_bp.route('/report/<id>', methods=['GET'])
def get_report(id: str):
    return jsonify({
        'id': id,
        'data': 'sample data'
    })
# auto-commit: 1778455759247