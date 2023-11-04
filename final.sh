#!/bin/bash

# Check if the 'service-result' directory exists locally, if not, create it
if [ ! -d "bd-a1/service-result" ]; then
  mkdir -p bd-a1/service-result
fi

# Copy output files to the local 'service-result' directory
cp eda-1.txt eda-2.txt eda-3.txt res_dpre.csv vis.png k.txt /bd-a1/service-result/

# Stop the container
docker container stop my-container