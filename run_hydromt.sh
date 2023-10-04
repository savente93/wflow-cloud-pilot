#! /usr/bin/bash

set -e

size=$1
if [ -z "$size" ]
then
      size=small
elif [ "$size" != "small" ] && [ "$size" != "large" ]
then
    echo "Invalid size: $size"
    exit 1
fi

if [ "$size" = "small" ]
then
    region='{"subbasin": [9.666, 0.4476], "uparea": 100}'
else
    region='{"basin": [4.099565785808807, 51.97582874463458], "strord": 5}'
fi

hydromt build wflow -vv "./wflow_$size" -i wflow-build.ini -r "$region" -d deltares-data-curated.yaml
