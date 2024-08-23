#!/bin/bash

install -m755 servod.py /usr/local/bin/servod
install -m644 pyservod.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable pyservod.service

#test -e /dev/servoblaster || mkfifo /dev/servoblaster && chmod 666 /dev/servoblaster
#test -e /dev/servoblaster-cfg || mkfifo /dev/servoblaster-cfg && chmod 666 /dev/servoblaster-cfg

