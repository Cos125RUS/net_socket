#! /bin/bash

python3 server.py >> logs/sys_error.txt 2>&1 &
pid=$!
echo $pid > pid.txt