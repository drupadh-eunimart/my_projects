from flask import jsonify

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            return jsonify(success=False)
    wrapper.__name__ = func.__name__
    return wrapper