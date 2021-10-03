#!/bin/bash
pip install autoflake autopep8
python $PWD/autoflake.py
flake8
pip uninstall autoflake autopep8