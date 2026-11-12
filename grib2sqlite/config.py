"""Shared configuration and logging for grib2sqlite."""

import logging
import os

logger = logging.getLogger("grib2sqlite")
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
formatter = logging.Formatter(
    "{levelname} - {message}",
    style="{",
)
console_handler.setFormatter(formatter)
logger.setLevel("WARNING")  # actually, this is the default anyway

basedir = os.path.dirname(__file__)
# some defaults
default_parameter_list = basedir + "/data/param_list_default.json"
default_station_list = basedir + "/data/station_list_default.csv"
default_sqlite_template = "{MODEL}/{YYYY}/{MM}/FCTABLE_{PP}_{YYYY}{MM}.sqlite"
