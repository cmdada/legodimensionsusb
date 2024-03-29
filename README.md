# Lego USB smooth color cycling

## Overview
This Python script allows you to smoothly cycle colors on a Lego USB Pad. It uses USB communication to control the colors displayed on the pad.

## Prerequisites
- Python3 and pip3

- Lego USB Pad (only tested with a wii u one)

## Setup
1. Connect your Lego USB Pad to your computer.
2. Install the required Python library:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Adjust the USB device information in the script if necessary (idVendor, idProduct).

## Usage
Run the script to smoothly cycle colors on the Lego USB Pad. The colors transition between the specified start and end colors repeatedly.

```bash
sudo python3 pulse.py
```

## Configuration
- Modify the `start_color` and `end_color` variables in the script to set the initial and target colors.
- Adjust the `transition_duration` variable to control the duration of each color transition (its not seconds i just dont want to fix it)

## License
This project is licensed under the [GPL-3.0](LICENSE).

## Acknowledgments
- https://github.com/VincentXE/Lego-Dimensions-Pad-Scripts for the init stuff
