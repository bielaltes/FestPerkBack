# Docker
To run the project use:
make
make migrations

If you want to enter the docker image:
docker exec -it festperk bash

# Scripts
To run the scripts:
1. Enter the docker image:
docker exec -it festperk bash
2. Set PYTHONPATH env variable:
export PYTHONPATH=/app/FestPerk/
3. execute desired script:
python /app/FestPerk/api/scripts/desired_script.py

Run create_all.py to fill the local database.