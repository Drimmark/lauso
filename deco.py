import json

from flask import request, Response


def validate_input(model):
    def wrap(func):
        def decorated_view(*args, **kwargs):
            errors = {
                'errors': [],
                'fields': []
            }
            body = request.get_json(silent=True)
            if not type(body) is dict:
                errors['errors'].append('Body must be a json object')
                return Response(response=json.dumps(errors),
                                status=404,
                                mimetype="application/json")
            attributes = [attr
                          for attr in model.__mapper__.column_attrs
                          if not attr.expression.nullable and not attr.expression.primary_key]
            for attr in attributes:
                if attr.key not in body.keys():
                    errors['errors'].append('Field %s is required' % attr.key)
                    errors['fields'].append(attr.key)

            if len(errors['errors']) > 0:
                return Response(response=json.dumps(errors),
                                status=404,
                                mimetype="application/json")

            return func(*args, **kwargs)
        return decorated_view
    return wrap
