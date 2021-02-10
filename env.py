from typing import Dict

from starlette.config import Config

config = Config(".env")

_ENV = config("ENV", cast=str, default="development")

_DEVELOPMENT: Dict = {
    "uvicorn": {
        "host": "0.0.0.0",
        "port": 5000,
        "log_level": "info",
        "debug": True,
        "reload": True,
    }
}

_STAGING: Dict = {
    "uvicorn": {
        "host": config("HOST", cast=str, default="127.0.0.1"),
        "port": config("PORT", cast=int, default=5000),
        "log_level": "info",
        "debug": True,
        "reload": True,
    }
}

_PRODUCTION: Dict = {
    "uvicorn": {
        "host": config("HOST", cast=str, default="127.0.0.1"),
        "port": config("PORT", cast=int, default=5000),
        "log_level": "info",
        "debug": False,
        "reload": True,
    }
}


def server_options() -> Dict:
    if _ENV == "development":
        options = _DEVELOPMENT["uvicorn"]
    elif _ENV == "staging":
        options = _STAGING["uvicorn"]
    elif _ENV == "production":
        options = _PRODUCTION["uvicorn"]
    else:
        raise ValueError("Invalid Environment")
    return options
