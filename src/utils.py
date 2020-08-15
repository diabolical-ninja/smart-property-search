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


def timestamp_to_epoch(time_string, timezone_offet='+0000'):
    """Converts a timestamp string to epoch time (seconds since midnight 1 Jan 1970)

    Args:
        time_string (str): Timestamp string in ISO8601 format
        timezone_offet (str, optional): Defaults to 0000 (UTC)
                    - Timezone offset
                    - Must be of format (+/-)HHMM

    Returns:
        int: Timestamp in epoch time
    """

    timestamp = f"{time_string}{timezone_offet}"
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    return dt.timestamp()


def chunks(lst, n):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
