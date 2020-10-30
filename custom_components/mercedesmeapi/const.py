"""
Mercedes Me APIs

Author: G. Ravera

For more details about this component, please refer to the documentation at
https://github.com/xraver/mercedes_me_api/
"""
# Software Parameters
NAME = "Mercedes Me API"
DOMAIN = "mercedesmeapi"
VERSION = "0.2"
TOKEN_FILE = ".mercedesme_token"
CREDENTIAL_FILE = ".mercedesme_credentials"
RESOURCES_FILE = ".mercedesme_resources"
REDIRECT_URL = "https://localhost"
SCOPE = "mb:vehicle:mbdata:fuelstatus%20mb:vehicle:mbdata:vehiclestatus%20mb:vehicle:mbdata:vehiclelock%20offline_access"
URL_OAUTH_BASE = "https://id.mercedes-benz.com/as"
URL_OAUTH_AUTH = URL_OAUTH_BASE + "/authorization.oauth2?response_type=code"
URL_OAUTH_TOKEN = URL_OAUTH_BASE + "/token.oauth2"
URL_RES_PREFIX = "https://api.mercedes-benz.com/vehicledata/v2"
#UPDATE_SIGNAL = "mercedesmeapi_update"

# File Parameters
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CONF_VEHICLE_ID = "vehicle_id"
