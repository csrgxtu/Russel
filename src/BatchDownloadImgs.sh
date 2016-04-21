#!/usr/bin/env bash
input="../data/links.csv"
output="../data/fail.csv"

cd "../data"
while IFS= read -r var
do
  wget "$var" -q
  OUT=$?
  if [ $OUT -eq 0 ];then
    echo "$var Success"
  else
    echo "$var Fail"
    echo "$var" >> "$output"
  fi
  sleep 1
done < "$input"
