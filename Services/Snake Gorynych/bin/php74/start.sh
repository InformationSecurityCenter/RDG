#!/bin/bash
apachectl -D FOREGROUND &
/usr/sbin/sshd -D -o ListenAddress=0.0.0.0