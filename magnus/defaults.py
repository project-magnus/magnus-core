NAME = 'magnus'

# CLI settings
LOG_LEVEL = 'WARNING'

# Interaction settings
TRACK_PREFIX = 'MAGNUS_TRACK_'
PARAMETER_PREFIX = 'MAGNUS_PRM_'

# STATUS progression
# For Branch, CREATED -> PROCESSING -> SUCCESS OR FAIL
# For a step, CREATED -> TRIGGERED ->  PROCESSING -> SUCCESS OR FAIL
CREATED = 'CREATED'
PROCESSING = 'PROCESSING'
SUCCESS = 'SUCCESS'
FAIL = 'FAIL'
TRIGGERED = 'TRIGGERED'

# Node and Command settings
COMMAND_TYPE = 'python'
NODE_SPEC_FILE = 'node_spec.yaml'
COMMAND_FRIENDLY_CHARACTER = '%'

# Default services
DEFAULT_EXECUTOR = {
    'type': 'local'
}
DEFAULT_RUN_LOG_STORE = {
    'type': 'buffered'
}
DEFAULT_CATALOG = {
    'type': 'file-system'
}
DEFAULT_SECRETS = {
    'type': 'do-nothing'
}

# Map state
MAP_PLACEHOLDER = 'map_variable_placeholder'

# Dag node
DAG_BRANCH_NAME = 'dag'

# RUN settings
RANDOM_RUN_ID_LEN = 6
MAX_TIME = 86400  # 1 day in seconds

# User extensions
USER_CONFIG_FILE = 'magnus-config.yaml'

# Executor settings
ENABLE_PARALLEL = False

# RUN log store settings
LOG_LOCATION_FOLDER = '.run_log_store'

# Dag node
DAG_BRANCH_NAME = 'dag'

# Data catalog settings
CATALOG_LOCATION_FOLDER = '.catalog'
COMPUTE_DATA_FOLDER = 'data'

# Secrets settings
DOTENV_FILE_LOCATION = '.env'

# AWS settings
AWS_REGION = 'eu-west-1'

# SEc
