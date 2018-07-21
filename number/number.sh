#!/bin/bash

make build > build.log
docker run -it --rm bsdnumber python bsdnumber/converter.py "$@"
