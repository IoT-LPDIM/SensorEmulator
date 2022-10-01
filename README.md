# Sensor emulator

## Overview

This is a simple python emulator for the [sensor board](https://pycom.io/) whidh is unfortunaly unavailable.
The sensor reading is simulated by a random value for each data point.
The data is then sent to the backend, which is a set of 2 [cloud functions](https://github.com/IoT-LPDIM/CloudFunctions) hosted on [Google Cloud Platform](https://cloud.google.com/).