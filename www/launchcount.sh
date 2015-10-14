#!/bin/bash

for i in $(ps aux | grep time.py | grep -ve "grep" | awk '{print $2}'); do sudo kill -9 $i; done

/root/time_repo/time.py count $1 $2 