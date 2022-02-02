from typing import Callable
from src.http_exceptions import throw_not_found
from src.problems_service import *
from src.app import app
from src.utils import responsify


@app.route('/problems/<subject>')
def get_problem(subject: str):

    subject = subject.replace('-', '_')

    global_namespace = globals()

    builder_fn_name: str
    builder_fn: Callable

    builder_fn_name = 'build_{}_problem'.format(subject)
    builder_fn = global_namespace.get(builder_fn_name)

    if builder_fn is None:
        message: str
        message = 'No problem for subject: {}'.format(subject)

        throw_not_found(message)

    p, s = builder_fn()

    return responsify(p, s)
