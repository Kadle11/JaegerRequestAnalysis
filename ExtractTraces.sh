#!/bin/bash


docker logs --since $2 $1 2>&1 | grep -Po '"trace-id":"[a-z0-9]+"'  > TMP_Logs
sed -i 's/trace-id//g' TMP_Logs
cat TMP_Logs | grep -Po "[a-z0-9]+" | sort -u  | grep -Po "[a-z0-9]+" > TraceLogs

rm TMP_Logs

python3 retrieveJSON.py

rm TraceLogs
