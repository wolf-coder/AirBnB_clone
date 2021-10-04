#!/bin/bash

read -p 'Type your Username: ' USR
read -p 'Type your PAssword: ' PSSWD
read -p 'Type your Repository link : ' Repo

echo "check this line and execute it"
echo git remote set-url origin https://$USR:$PSSWD@github.com/$USR/$Repo.git
