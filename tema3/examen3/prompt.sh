#!/bin/bash
if [ "$#" -ne 1 ]; then
   echo "Usage: prompt.sh <uo>" >&2
else
   PS1="\t|"$1"@\w$ "
fi

