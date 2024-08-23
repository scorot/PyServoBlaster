# PyServoBlaster

## Introduction
This project is an attempt to rewrite the [ServoBlaster](https://github.com/richardghirst/PiBits) daemon with Python. [ServoBlaster](https://github.com/richardghirst/PiBits) is a great tool for those how want to control servo motor with a RaspberryPi with accuracy.

Unfortunately, as for August 2024, ServoBlaster do not seem to work on 64bits RaspberryPi OS.

Since my knowledge in C programming and in the RaspberryPi is limited, as long as the time i can spend on it, I decided to rewrite ServoBlaster in Python. This implementation supports only the very basic feature of ServoBlaster.
The main caveat is that this Python implementation uses GPIO API, know to be less accurate, but for my need it is quite sufficient.

The code controlling the servo is inspired from [this tutorial](https://howtoraspberrypi.com/servo-raspberry-pi/) on [howtoraspberrypi.com](https://howtoraspberrypi.com/).

## How is works

This python script runs as a daemon and read commands echoed to /dev/servoblaster just as for the C implementation ServoBlaster.

Currently, it works for only one servo.
Also, only commands in pulse duration are accepted and the pinout servo identification format is not supported (read ServoBlaster [README](https://github.com/richardghirst/PiBits/blob/master/ServoBlaster/README.txt) for details). 


## Installation

Just run the ``install.sh`` script as root and start the service either by rebooting your pi or by typing ``sudo systemctl start pyservod.service``.
Once it is done, there should see a program named ``servod`` running as a service in the background waiting for command echoed to ``/dev/servoblaster``.
