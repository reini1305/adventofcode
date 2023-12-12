#!/bin/bash
for filename in *.py; do
	pypy3 $filename & 
done
wait
