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
