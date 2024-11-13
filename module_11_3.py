def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")],
        'module': obj.__class__.__module__
    }
    return info


number_info = introspection_info(42)
print(number_info)