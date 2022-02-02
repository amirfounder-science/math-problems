from datetime import datetime
from flask import abort, jsonify


def throw_not_found(message: str):
    error_response = {
        'timestamp': datetime.isoformat(),
        'error': 'Not Found',
        'error_message': message,
        'status': 404
    }
    
    response = jsonify(error_response)
    response.status = 404

    abort(response)
