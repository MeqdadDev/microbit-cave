---
title: "DHT11 Sensor"
description: "Read temperature and humidity from a DHT11 sensor."
tags:
  - Sensors
  - Intermediate
level: Intermediate
board: "V2 (tested)"
parts:
  - "micro:bit V2"
  - "DHT11 temperature & humidity sensor"
  - "Jumper wires"
source:
  - "microbit_tools/DHT11 Sensor/dht11-mbit-v2-example.py"
  - "microbit_tools/DHT11 Sensor/dht11.py"
libraries:
  - "microbit_tools/DHT11 Sensor/dht11.py"
wiring:
  - part: "DHT11"
    pins:
      DATA: "P0 (also tested on P1 and P2)"
      VCC: 3V
      GND: GND
---

## What you'll build

Measure temperature and humidity with the low-cost DHT11 and scroll both readings.

The DHT11 measures 0–50 °C (±2 °C) and 20–80 % relative humidity (±5 %) and sends readings over a single digital pin.

## Wiring

<!-- wiring -->

## Code

=== "Example"

    ```python title="dht11-mbit-v2-example.py" linenums="1"
    --8<-- "microbit_tools/DHT11 Sensor/dht11-mbit-v2-example.py"
    ```

=== "dht11.py (library)"

    ```python title="dht11.py" linenums="1"
    --8<-- "microbit_tools/DHT11 Sensor/dht11.py"
    ```

## How it works

`DHT11(pin0).read()` triggers a measurement and decodes the sensor's 40-bit reply into `(temperature, humidity)`.
The readings scroll as `T 23.0C` and `H 41.0%` so you can tell them apart.

Reading a DHT11 sometimes fails with a `DataError` (bad checksum or a missing bit). That's normal, so the example
shows `?` and tries again. Any other error, like a sensor that doesn't answer or an unsupported pin,
scrolls its message so you know what to fix.
The `dht11.py` driver is by Phil Hall (MIT License).

## Try this next

- Log readings with [Data Logging](../microbit/09-data-logger.md).
- Show readings on the [OLED screen](oled-screen.md).
- Sound a buzzer when humidity goes above a threshold.
