import logging

# Plugin imports
from plugin.rubicon_plugin import RubiconPlugin

# Max connections for bid requests allowed for the process
MAX_CONNS = 100
# Amount of connections for event notification allowed for the process
MAX_EVENT_CONNS = 10

# Endpoint list containing tuples for the DSPs (endpoint, expected_qps) where :
#  - endpoint should be a string 'host:port'
#  - expected_qps is the amount of qps expected for the endpoint
ENDPOINT_LIST = [
    ('localhost:80', 1),
]

# Event endpoint :
# - endpoint should be a string 'host:port'
EVENT_ENDPOINT = 'localhost:9876'

# Balance time out indicating the period in seconds 
# to balance connections
BALANCE_TO = 3

# Check connections time out indicating the period in
# seconds to verify if a connection attempt was successfull
CHECK_CONNS_TO = 1

# Log level should be one of :
# - logging.DEBUG
# - logging.INFO
# - logging.WARNING
# - logging.ERROR
LOG_LEVEL = logging.DEBUG

# Parameter plugin
PARAMETER_PLUGIN = RubiconPlugin

# RTB request template filename
TEMPLATE_FILENAME = 'templates/request.template'
