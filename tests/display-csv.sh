#!/bin/sh

cat "$1" | column -s, -t | less -#2 -N -S
