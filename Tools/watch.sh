#!/usr/bin/env bash

# watchmedo shell-command \
#     --patterns="*.py;*.txt" \
#     --recursive \
#     --command='echo "${watch_src_path}"' \
#     .

watchmedo shell-command \
    --patterns="*.dat;*.fbx" \
    --recursive \
    --command='`pwd`/Tools/run.sh "${watch_src_path}"' \
    `pwd`