"""
lambda_handler.py
Method for starting intelbridge from a lambda function
"""

import sys
import logging
from intelbridge.intelbridge import IntelBridge
from util.util import start_log

def lambda_handler(event, context):
    """Initializes and starts intel bridge object
    returns: N/A
    """
    start_log()
    logging.info("Intel Bridge main routine starting...")
    intelbridge = IntelBridge()
    intelbridge.start()
    return