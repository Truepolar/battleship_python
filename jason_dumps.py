import json

def json_dumps(object):
    json.dumps(object, indent=4, default=lambda x : getattr(x, "__dict__", str))