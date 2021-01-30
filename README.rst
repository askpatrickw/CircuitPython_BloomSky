Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython_bloomsky/badge/?version=latest
    :target: https://circuitpython_bloomsky.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/askpatrickw/CircuitPython_BloomSky/workflows/Build%20CI/badge.svg
    :target: https://github.com/askpatrickw/CircuitPython_BloomSky/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython Wrapper for BloomSky API


Dependencies
============

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython Datetime <https://github.com/adafruit/Adafruit_CircuitPython_datetime>`_
* `Adafruit CircuitPython Requests <https://github.com/adafruit/Adafruit_CircuitPython_Requests>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

BloomSky Account
================
This library is only useful to owners of `BloomSky Weather Stations <https://shop.bloomsky.com/>`_.
Get you Bloomsky API Key from your Bloomsky Dashboard.
https://dashboard.bloomsky.com/

Usage Example
=============

See full working example in the examples folder. The basic structure looks like this, ::

    ## Join Network
    wifi.radio.connect(secrets["ssid"], secrets["password"])

    # Setup Requests
    radio = wifi.radio
    pool = socketpool.SocketPool(radio)
    requests = adafruit_requests.Session(pool,
    ssl.create_default_context())

    # Create Bloomsky client.
    bloomsky_client = circuitpython_bloomsky.BloomSkyAPIClient(
        requests, api_key=secrets["bloomsky_key"]
    )

    # Get data and utilize it in your application.
    # This is the section you would put in your While loop if running
    # repeatedly.
    bloomsky_report = bloomsky_client.get_data()

    print(bloomsky_report.device)
    print(bloomsky_report.indoor)
    print(bloomsky_report.sky)
    print(bloomsky_report.storm)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/askpatrickw/CircuitPython_BloomSky/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

RTD coming soon.

Acknowledgements
================
The basic idea for this library and the concept to rename attributes came from
https://github.com/tylerdave/bloomsky-api and was heavily reworked for this
library.


Installing from PyPI
====================
.. note:: This library is not available on PyPI yet. Stay tuned for PyPI availability,
when or if CircuitPython libraries are supported from there.
