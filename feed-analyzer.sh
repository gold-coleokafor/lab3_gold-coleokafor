#!/bin/bash

FILE="twitter_dataset.csv"
if [ ! -f "$FILE" ]; then
   echo "File $FILE not found"
   echo "This application accepts only twitter_dataset.csv. Place it in the same folder as feed-analyzer.sh."
   exit 1
fi

echo "---Top 5 Most Active Users---"

grep -E '^[0-9]+,' "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -nr | head -n 5



