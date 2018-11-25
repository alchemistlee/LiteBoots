#!/usr/bin/env bash

sh /home/root/start-enzh.sh
echo 'start enzh ! ...'
sleep 6s


sh /home/root/start-zhen.sh
echo 'start zhen ! ...'
sleep 5s

nohup python3 /home/root/LiteBoots/my_tf.py &

echo "start tf_flask !"

tailf nohup.out