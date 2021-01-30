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

adafruit/actions-ci-circuitpython-libs
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython Datetime <https://github.com/adafruit/Adafruit_CircuitPython_datetime>`_
* `Adafruit CircuitPython Requests <https://github.com/adafruit/Adafruit_CircuitPython_Requests>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

BloomSky Account
================
This library is only usefule to owners of BloomSky Weather Stations.
Get you Bloomsky API Key from your Bloomsky Dashboard.
https://dashboard.bloomsky.com/

Usage Example
=============
::
    ## Join Network
    wifi.radio.connect(secrets["ssid"], secrets["password"])
    # Setup Requests
    radio = wifi.radio
    pool = socketpool.SocketPool(radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())
    bloomsky_client = circuitpython_bloomsky.BloomSkyAPIClient(
    requests, api_key=secrets["bloomsky_key"]
    )
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

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Acknowledgements
================
The core idea for this library and the mapping idea and function came from
https://github.com/tylerdave/bloomsky-api and was heavily reworked for this
library.


Installing from PyPI
====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project circuitpython_bloomsky/>`_. To install for current user:

.. code-block:: shell

    pip3 install circuitpython-bloomsky

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-bloomsky

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-bloomsky
