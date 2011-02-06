from flask import request

def negotiate_content(*order):
    types = {'json': 'application/json', 'html': 'text/html'}
    order = order or types.keys()
    return request.accept_mimetypes.best_match(order) or ''
