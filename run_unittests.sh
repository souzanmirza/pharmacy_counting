#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#

echo "[$(date)]" &>> unit_tests/results.txt
python3 -m unittest discover -v &>> unit_tests/results.txt

read -p "Press enter to continue"