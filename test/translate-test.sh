#!/usr/bin/env bash

SERVER=127.0.0.1
PORT=5000
WORD="hello"

API_LIST=$(grep "app.route('/translate" my_tf.py | awk -F \' '{print $2}')
for API in ${API_LIST[*]};do
  URL="${SERVER}:${PORT}$API?in=${WORD}"
  echo ${URL}
  curl ${URL}
done
