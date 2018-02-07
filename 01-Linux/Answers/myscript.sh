#!/bin/bash

find -type f -exec cksum {} \; > cksums
cut -d ' ' -f1 cksums | sort | uniq -d > dupes
while read d; do echo "---"; grep $d cksums | cut -d ' ' -f 2-; done < dupes
rm cksums
rm dupes
