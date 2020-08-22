"""General utility functions."""

import typing
from datetime import date, datetime


def json_serial(obj: typing.Any) -> typing.Any:
    """JSON serializer for objects not serialisable by default json code.

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


def chunks(lst: list, n: int) -> list:
    """Yield successive n-sized chunks from list.

    Args:
        lst (list): List to chunk up
        n (int): Number of elements to have in each chunk

    Yields:
        Iterator[list]: Chunks of size n
    """
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def extend_dictionary(base_dict: dict, extender_dict: dict, key_name: str) -> dict:
    """Adds keys from one dictionary to another.

    Args:
        base_dict (dict): Base dictionary to be extended
        extender_dict (dict): Dictionary whose keys will extend base
        key_name (str): The key to be added to base

    Returns:
        dict: Base dictionary plus additional key
    """
    base_dict[key_name] = extender_dict
    return base_dict
