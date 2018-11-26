#!/usr/bin/env bash

 ps -ef | egrep "tensor|my_tf" | grep -v grep  | awk '{print $2}' | xargs kill -9
