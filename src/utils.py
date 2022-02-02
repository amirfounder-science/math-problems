from flask import jsonify


def responsify(problem, solution):
    body = {
        'problem': problem,
        'solution': solution
    }

    response = jsonify(body)
    response.status = 200

    return response