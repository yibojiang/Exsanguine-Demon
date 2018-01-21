#!/usr/bin/env bash

# watchmedo shell-command \
#     --patterns="*.py;*.txt" \
#     --recursive \
#     --command='echo "${watch_src_path}"' \
#     .

watchmedo shell-command \
    --patterns="*.dat" \
    --recursive \
    --command='`pwd`/Tools/lipsync.sh "${watch_src_path}"' \
    `pwd`/Sounds/Characters