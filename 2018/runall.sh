#!/bin/bash
for filename in *.py; do
	python3 $filename &
done
wait
