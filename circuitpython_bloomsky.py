# SPDX-FileCopyrightText: Copyright (c) 2021 Patrick Walters
#
# SPDX-License-Identifier: MIT
"""
`circuitpython_bloomsky`
================================================================================

CircuitPython Wrapper for BloomSky API


* Author(s): Patrick Walters

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit CircuitPython Datetime Library
  https://github.com/adafruit/Adafruit_CircuitPython_datetime
* Adafruit CircuitPython Requests Library
  https://github.com/adafruit/Adafruit_CircuitPython_Requests
"""

from adafruit_datetime import datetime, timedelta

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/askpatrickw/CircuitPython_BloomSky.git"

BLOOMSKY_API_URL = "https://api.bloomsky.com/api/skydata/"
CLIENT_HEADERS = {"User-Agent": "CircuitPython-Bloomsky/{0}".format(__version__)}


class BLOOMSKY_REPORT():
    """
    Bloomsky Report Class represents data from the Bloomsky API.
    DEVICE is the Sky's non-wx and available media data.
    SKY is the base weather station.
    STORM is the add-on rain and wind gauge.
    """

    _sky_device_mapping = [
        ("ALT", "altitude"),
        ("CityName", "city_name"),
        ("DST", "is_dst"),
        ("DeviceID", "device_id"),
        ("DeviceName", "device_name"),
        ("FullAddress", "full_address"),
        ("LAT", "latitude"),
        ("LON", "longitude"),
        ("NumOfFavorites", "favorites_count"),
        ("NumOfFollowers", "followers_count"),
        ("PreviewImageList", "preview_images"),
        ("RegisterTime", "registered_timestamp"),
        ("Searchable", "is_searchable"),
        ("StreetName", "street_name"),
        ("UTC", "utc_offset"),
        ("VideoList", "video_urls"),
    ]
    _sky_wx_mapping = [
        ("DeviceType", "device_type"),
        ("Humidity", "humidity"),
        ("ImageTS", "image_timestamp"),
        ("ImageURL", "image_url"),
        ("Luminance", "luminance"),
        ("Night", "is_night"),
        ("Pressure", "pressure"),
        ("Rain", "is_raining"),
        ("TS", "data_timestamp"),
        ("Temperature", "temperature"),
        ("UVIndex", "uv_index"),
        ("Voltage", "voltage"),
    ]
    _storm_mapping = [
        ("24hRain", "24_hour_rain"),
        ("RainDaily", "rain_daily"),
        ("RainRate", "rain_rate"),
        ("SustainedWindSpeed", "sustained_wind_speed"),
        ("UVIndex", "uv_index"),
        ("WindDirection", "wind_direction"),
        ("WindGust", "wind_gust"),
    ]

    def __init__(self, response_json):
        self.json = response_json
        self._data = [self._rename_keys(device) for device in self.json]
        self._humanreadable_timestamps()
        self.device = self._data[0]["device"]
        self.indoor = self._data[0]["indoor"]
        self.sky = self._data[0]["sky"]
        self.storm = self._data[0]["storm"]

    @classmethod
    def _rename_keys(cls, response_json):
        """
        Changes keys to user friendly and python style names
        :param json the response_json is a list of a single dict
        :return: updated list
        """
        remapped_data = {}
        remapped_data["device"] = {}
        for old_name, new_name in cls._sky_device_mapping:
            remapped_data["device"][new_name] = response_json.get(old_name)
        remapped_data["sky"] = {}
        for old_name, new_name in cls._sky_wx_mapping:
            remapped_data["sky"][new_name] = response_json["Data"].get(old_name)
        indoor = response_json.get("Point", {})
        remapped_data["indoor"] = {
            "humidity": indoor.get("Humidity"),
            "temperature": indoor.get("Temperature"),
        }
        remapped_data["storm"] = {}
        for old_name, new_name in cls._storm_mapping:
            remapped_data["storm"][new_name] = response_json["Storm"].get(old_name)
        return remapped_data

    def _humanreadable_timestamps(self):
        """
        Update datetime fields to human readable format.
        """
        for device in self._data:
            device["device"]["is_dst"] = bool(device["device"]["is_dst"])
            offset_hours = device["device"]["utc_offset"]
            device["sky"]["data_timestamp"] = self._timestamp_to_iso_format(
                device["sky"]["data_timestamp"], offset_hours
            )
            device["sky"]["image_timestamp"] = self._timestamp_to_iso_format(
                device["sky"]["image_timestamp"], offset_hours
            )
            device["sky"]["uv_index"] = int(device["sky"]["uv_index"])
            device["device"]["registered_timestamp"] = self._timestamp_to_iso_format(
                device["device"]["registered_timestamp"], offset_hours
            )

    @staticmethod
    def _timestamp_to_iso_format(timestamp, offset_hours=0):
        """
        Converts a timestamp to an iso format and adjusts for the sensing devices
        timezone
        """
        offset_adjusted_dt = datetime.fromtimestamp(timestamp) - timedelta(
            hours=abs(offset_hours)
        )
        return offset_adjusted_dt.isoformat()

    def __repr__(self):
        return "{0}".format(self.json)


class BloomSkyAPIClient():
    """ A client for interacting with the BloomSky API """

    def __init__(self, requests, api_key=None, api_url=BLOOMSKY_API_URL):
        self.api_key = api_key
        self.api_url = api_url
        self._http = requests
        self._headers = {"Authorization": self.api_key}

    @staticmethod
    def _create_headers(io_headers):
        """Creates http request headers."""
        headers = CLIENT_HEADERS.copy()
        headers.update(io_headers)
        return headers

    def get_data(self, intl_units=False):
        """Retrieves Data from Bloomsky API"""
        _url = self.api_url
        if intl_units:
            _url = "{}?unit={}".format(_url, intl_units)
        response = self._http.get(_url, headers=self._create_headers(self._headers))
        return BLOOMSKY_REPORT(response.json())
