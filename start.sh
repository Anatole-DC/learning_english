#!/bin/bash

echo "STARTING THE SERVERS..."

# Prepare the exit of the program in order to make sure all the server instances are killed
set -e
trap cleanup 0 1 2 3 6 15
cleanup() {
    pgrep -P $$ | xargs kill
    exit 1
}

source ./server/venv/bin/activate

python ./server/main.py &
yarn --cwd ./frontend serve