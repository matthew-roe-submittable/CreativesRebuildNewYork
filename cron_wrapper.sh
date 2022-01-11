#!/bin/bash

date

echo "Creatives Rebuild New York starting"

# mail -s 'Creatives Rebuild New York starting' jesse.finneman@submittable.com <<< 'The Creatives Rebuild New York process is beginning'

# echo "Subject: Creatives Rebuild New York  running" | sendmail -v jesse.finneman@submittable.com

docker run CreativesRebuildNewYork:latest

date

echo "Creatives Rebuild New York finished"

# mail -s 'Creatives Rebuild New York  ran' jesse.finneman@submittable.com <<< 'The Creatives Rebuild New York process ended'

# echo "Subject: Creatives Rebuild New York complete" | sendmail -v jesse.finneman@submittable.com