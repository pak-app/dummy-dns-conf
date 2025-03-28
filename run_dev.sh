#!/bin/bash

dotenv -f .env.development run python3 main.py
# This script runs the main.py file in a development environment using dotenv to load environment variables from a .env.development file.
# It uses the bash shell to execute the command.
# The `dotenv` command is used to load environment variables from the specified .env file before running the Python script.
# The `-f` option specifies the file to load, and `run` is the command to execute the Python script.
# The `python3` command is used to run the Python script, and `main.py` is the name of the script being executed.