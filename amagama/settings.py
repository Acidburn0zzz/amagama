# Global config

DEBUG = False
ENABLE_WEB_UI = True
ENABLE_DATA_ALTERING_API = True


# Database config

DB_NAME = "amagama"
DB_USER = "usuario"
DB_PASSWORD = "usuario"
DB_HOST = "localhost"
DB_PORT = "5432"


# Database pool config

DB_MIN_CONNECTIONS = 2
DB_MAX_CONNECTIONS = 20


# Levenshtein config

MAX_LENGTH = 1000
MIN_SIMILARITY = 70
MAX_CANDIDATES = 5
