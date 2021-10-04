#!/bin/bash

# read -p 'Type the file name ' File_name

read -p  'type your commit message : ' Commit

git add $1
git commit -m "${Commit}"
git push