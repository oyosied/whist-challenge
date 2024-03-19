#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./scale_apps.sh <number_of_instances>"
    exit 1
fi

docker-compose -f ../docker-compose.yaml up -d --scale app=$1
