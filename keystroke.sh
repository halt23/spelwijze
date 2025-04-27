#!/bin/bash

 read -p "Enter a input file. -> " input_file
sleep 3 # Allows you to posstions your cursor / input field (quite handy c:)
echo "starting.."
while IFS= read -r line
do
    wtype "$line"
    wtype $'\n'  # Press Enter
    sleep 1
done < "$input_file"
