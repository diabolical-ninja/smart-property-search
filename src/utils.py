from datetime import date, datetime


def json_serial(obj):
    """JSON serializer for objects not serialisable by default json code

    Args:
        obj (any): Object that JSON cannot serialise

    Raises:
        TypeError: Message indicating that object of type "X" is not supported

    Returns:
        (Any): Serialised object
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serialisable" % type(obj))


def chunks(lst, n):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def extend_dictionary(base_dict, extender_dict, key_name):
    """Adds keys from one dictionary to another"""
    base_dict[key_name] = extender_dict
    return base_dict
