#!/usr/bin/env bash
echo `pwd`
# echo '`pwd`/Tools/run.sh "${watch_src_path}"'
# /cygdrive/c/Users/yibojiang/Documents/Projects/Psycho
# watchmedo shell-command --patterns="*.dat;*.fbx" --recursive --command='/cygdrive/c/Users/yibojiang/Documents/Projects/Psycho/Tools/run.sh "${watch_src_path}"' /cygdrive/c/Users/yibojiang/Documents/Projects/Psycho
# watchmedo shell-command --patterns="*.py;*.txt" --recursive --command='echo "${watch_src_path}"' .
watchmedo shell-command --patterns="*.dat;*.fbx" --recursive --command='/Tools/run.sh "${watch_src_path}"' .