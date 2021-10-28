#!/bin/sh

echo "Flush the manage.py command it any"

while ! python ./app/manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python ./app/manage.py migrate  2>&1; do
  echo "Migration is in progress status"
  sleep 3
done
python ./app/manage.py loaddata ./app/recipes/fixtures/initial_data.json
echo "Django docker is fully configured successfully."


exec "$@"