#!/bin/bash

set -e
set -x

DIR=`pwd`

rm -f package.zip

zip package.zip app.py users.py

cd venv/lib/python2.7/site-packages/
zip -g -r9 $DIR/package.zip *

cd $DIR
aws lambda update-function-code --function alexaFindMyIphone --zip-file fileb://package.zip
