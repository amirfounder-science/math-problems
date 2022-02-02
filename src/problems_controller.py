from src.http_exceptions import throw_not_found
from src.problems_service import *
from src.app import app
from src.utils import responsify


@app.route('/problems/<subject>')
def get_problem(subject: str):

    problem: str
    solution: int | list | str | tuple

    if subject == 'addition':
        problem, solution = build_addition_problem()
        return responsify(problem, solution)

    elif subject == 'subtraction':
        problem, solution = build_subtraction_problem()
        return responsify(problem, solution)

    elif subject == 'multiplication':
        problem, solution = build_multiplication_problem()
        return responsify(problem, solution)

    elif subject == 'division':
        problem, solution = build_division_problem()
        return responsify(problem, solution)

    message: str
    message = 'We currently have no problem generators for subject: {}'.format(
        subject)

    throw_not_found(message)
