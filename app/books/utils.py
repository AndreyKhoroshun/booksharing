def display(obj, attr, sep='.'):
    if sep in attr:
        attr1, attr2 = attr.split(sep)
        return_value = getattr(getattr(obj, attr1), attr2)
    else:
        return_value = getattr(obj, attr)

    return return_value() if callable(return_value) else return_value
