#!/usr/bin/env bash
./install_python3_venv.sh pure ${1} "pep8"
./install_python3_venv.sh django ${1} "django autopep8 pytest"

