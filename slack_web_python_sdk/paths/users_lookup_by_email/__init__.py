# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slack_web_python_sdk.paths.users_lookup_by_email import Api

from slack_web_python_sdk.paths import PathValues

path = PathValues.USERS_LOOKUP_BY_EMAIL