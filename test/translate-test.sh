#!/usr/bin/env bash

SERVER=10.0.3.125
PORT=5000
WORD="hello"

API_LIST=$(grep "app.route('/translate" my_tf.py | awk -F \' '{print $2}' | grep -iv zh)
for API in ${API_LIST[*]};do
  URL="${SERVER}:${PORT}$API?in=${WORD}"
  echo ${URL}
  curl ${URL}
done
