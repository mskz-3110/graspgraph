#!/bin/bash

repository="${1:-testpypi}"
python -m twine upload --repository ${repository} dist/*
