#!/usr/bin/env bash

# watchmedo shell-command \
#     --patterns="*.py;*.txt" \
#     --recursive \
#     --command='echo "${watch_src_path}"' \
#     .

watchmedo shell-command \
    --patterns="*.dat" \
    --recursive \
    --command='./lipsync.sh "${watch_src_path}"' \
    /private/var/ninja/Documents/Projects/Psycho/Sounds/Adam/Story