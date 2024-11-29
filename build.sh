#!/bin/bash

rm -fr dist *.egg-info src/*.egg-info
python -m build
