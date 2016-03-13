#!/bin/sh
# deployment script run by Viper server after push

echo "Starting deploy script"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


#requirements
pip install -r $DIR/requirements.txt

# database
python $DIR/manage.py migrate

# static files
echo "yes" | python $DIR/manage.py collectstatic
