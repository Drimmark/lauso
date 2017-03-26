import json, re

from functools import wraps

from flask import current_app, request, Response
from jose import jwt, JWTError


def authorization_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        errors = {
            'error': []
        }
        if request.headers.get('Authorization') is None:
            errors['error'].append('Authorization required')
            return Response(response=json.dumps(errors),
                            status=401,
                            mimetype="application/json")

        auth = re.search('Bearer (.*)', request.headers['Authorization'])
        if auth is None:
            errors['error'].append('Authorization header not properly set')
            return Response(response=json.dumps(errors),
                            status=400,
                            mimetype="application/json")

        token = auth.group(1)
        try:
            jwt.decode(token, current_app.config['SECRET'], algorithms='HS512')
        except JWTError as error:
            errors['error'].append(str(error))
            return Response(response=json.dumps(errors),
                            status=401,
                            mimetype="application/json")

        return func(*args, **kwargs)
    return decorated_view
