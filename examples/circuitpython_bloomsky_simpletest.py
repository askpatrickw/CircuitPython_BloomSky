#
# SPDX-License-Identifier: Unlicense
import socketpool
import ssl
import wifi

import adafruit_requests
import circuitpython_bloomsky

# Get secrets
try:
    from secrets import secrets
except ImportError:
    print("Secrets are kept in secrets.py, please add them there!")
    raise

## Join Network
print("Joining Network")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print(f"ip: {wifi.radio.ipv4_address}")
print(f"hostname: {wifi.radio.hostname}")

# Setup Requests
radio = wifi.radio
pool = socketpool.SocketPool(radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


bloomsky_client = circuitpython_bloomsky.BloomSkyAPIClient(
    requests, api_key=secrets["bloomsky_key"]
)


bloomsky_report = bloomsky_client.get_data()
print(bloomsky_report.device)   # Device Details and Media
print(bloomsky_report.indoor)   # Indoor Data if Available
print(bloomsky_report.sky)      # Sky Weather Station Data
print(bloomsky_report.storm)    # Storm rain and wind gauge
