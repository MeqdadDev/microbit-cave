---
title: "Radio Messaging"
description: "Send a message from one micro:bit to another over radio when button A is pressed."
tags:
  - Radio
  - Buttons
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "2 × micro:bit"
source:
  - "microbit/4 radio-sender.py"
  - "microbit/5 radio-receiver.py"
---

## What you'll build

micro:bits can talk to each other wirelessly. Flash the **sender** onto one micro:bit and the **receiver** onto a
second one. Press button A on the sender and the receiver scrolls the message.

## Code

=== "Sender"

    Flash this onto the first micro:bit.

    ```python title="4 radio-sender.py" linenums="1"
    --8<-- "microbit/4 radio-sender.py"
    ```

=== "Receiver"

    Flash this onto the second micro:bit.

    ```python title="5 radio-receiver.py" linenums="1"
    --8<-- "microbit/5 radio-receiver.py"
    ```

## How it works

- `radio.config(group=5)` puts both micro:bits on group 5. Only boards in the **same group** hear each other,
  so the sender and receiver must match.
- `radio.on()` powers up the radio, which is off by default to save battery.
- `radio.send()` broadcasts a string to every micro:bit in range on the same group.
- `radio.receive()` returns the next queued message as a string, or `None` if nothing has arrived.

## Try this next

- Send a different message for button B, and show a different image for each one on the receiver.
- Pick your own group number (0–255) so you don't clash with classmates.
- Add a short `sleep(200)` on the sender so holding the button doesn't flood the radio.
- Reply from the receiver so both boards can chat.
- Use `radio.receive_full()` to read the signal strength and estimate distance.
