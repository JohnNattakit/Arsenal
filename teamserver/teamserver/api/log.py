"""
    This module contains all 'Log' API functions.
"""
from .utils import success_response
from ..models import Log, log

def create_log(params):
    """
    Log an entry (if current log level deems necessary)

    application (required): The application that is requesting to log a message. <str>
    level (required): The log level that the message is at. <str, LOG_LEVELS from config.py>
    message (required): The message to log. <str>
    """
    if params['application'] is None:
        # TODO: Raise error
        pass

    log(params['level'], params['message'], params['application'])
    return success_response()

def list_logs(params):
    """
    Show filtered log entries

    application (optional): The application to filter for. <str>
    since (optional): The timestamp that logs must be newer than. <float>
    include_archived (optional): Should archived messages be included (default=False). <boolean>
    """
    logs = Log.list(
        params.get('include_archived', False),
        params.get('application'),
        params.get('since', 0))

    return success_response(logs=[entry.document for entry in logs])
