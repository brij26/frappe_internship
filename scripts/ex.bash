#!/bin/bash
# This is example shell script
# In this i will ask the user about his name and his current age
# Than i will print name and age of the user and also print In which Year he will or he was become 50 year old

YEAR=$(date +%Y)
read -p "What is Your Name? :" NAME
read -p "What is Your Age? :" AGE
echo "Name : $NAME"
echo "Age : $AGE"
let X=50-$AGE
let ANS=$YEAR+$X
echo In $ANS you become 50 year old
