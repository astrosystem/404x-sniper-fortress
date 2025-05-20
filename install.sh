#!/bin/bash

echo "Installing 404X Sniper Fortress Bot..."

cd 404x-sniper-fortress

pip install -r requirements.txt

python3 sniper.py --init

echo "Installation complete. You’re now locked and loaded."
