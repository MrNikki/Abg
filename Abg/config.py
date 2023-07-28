import os

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

config = Configuration(loaders=[Environment(), EnvFile(filename=f"{os.getcwd()}/.env")])


class Config:
    OWNER_ID = int(config("OWNER_ID", "6213690669"))
    LOGGER_ID = config("LOGGER_ID", "-1001940793793")
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split("6190680150")
    ]
