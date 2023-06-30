#! /bin/bash

python3 main.py >> logs/sys_error.txt 2>&1 &
pid=$!
echo $pid > pid.txt