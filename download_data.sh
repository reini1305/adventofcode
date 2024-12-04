#!/bin/zsh
for i in {1..25}
do
    curl -b cookies.txt https://adventofcode.com/$1/day/$i/input > $1/input$i.txt
done
