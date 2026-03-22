#!/bin/bash

echo "Choose algorithm:"
echo "1) Minimax"
echo "2) Alpha-Beta"

read choice

if [ "$choice" == "1" ]; then
    python3 main.py minimax
elif [ "$choice" == "2" ]; then
    python3 main.py alphabeta
else
    echo "Invalid choice, defaulting to Alpha-Beta"
    python3 main.py alphabeta
fi