# Lab 3: The Social Media Data Detective

A small data-analysis project that explores a messy dataset of tweets (`twitter_dataset.csv`). It has two parts:

1. A **Python program** (`data-detective.py`) that cleans the data, finds the most-liked tweet, sorts tweets by Likes with a hand-written algorithm, and searches tweets by keyword.
2. A **Bash script** (`feed-analyzer.sh`) that finds the 5 most active users using a chain of terminal commands.

**Author:** Gold Adaobi Cole-Okafor | **GitHub:** gold-coleokafor

---

## Files in this repository

| File | What it does |
|---|---|
| `data-detective.py` | The Python application (Quests 1 to 4) |
| `feed-analyzer.sh` | Bash script that shows the Top 5 most active users |
| `twitter_dataset.csv` | The dataset (10,000 tweets) |
| `README.md` | This guide |

The CSV has these columns: `Tweet_ID, Username, Text, Retweets, Likes, Timestamp`.

---

## Requirements

- Python 3
- Bash (Linux, macOS, or WSL on Windows)
- **No external libraries.** Only Python's built-in modules `csv`, `sys` and `os` (from the starter code) are used.

---

## How to run

Open a terminal in the project folder. `twitter_dataset.csv` must be in the same folder.

**Python program:**

```bash
python3 data-detective.py
```

The program runs Quests 1 to 3 automatically, then asks you to type a search word for Quest 4. Example input: `Congress`

**Bash script:**

```bash
bash feed-analyzer.sh
```

---

## What each part does

### Quest 1: The Data Auditor (`clean_data`)
Goes through every tweet and cleans it:
- A tweet with **missing or blank Text** is removed.
- A **blank Likes or Retweets** value is replaced with `0`.
- Likes and Retweets are converted from text to whole numbers with `int()`. If a value is not a valid number (for example `"abc"`), that tweet is removed.
- It prints how many bad rows were fixed or removed. Each removed tweet counts as 1, and each blank field that was fixed counts as 1.

### Quest 2: The Viral Post (`find_viral_tweet`)
Loops through the cleaned tweets and keeps track of the one with the highest Likes, then prints its Username, Likes and Text. It does not use `max()`. If several tweets tie, the first one found is kept.

### Quest 3: The Algorithm Builder (`custom_sort_by_likes`)
Sorts the tweets from most Likes to fewest using a hand-written **Selection Sort**. Each round finds the tweet with the most Likes in the unsorted part of the list and swaps it into place. The top 10 are then printed with a rank number. It does not use `.sort()` or `sorted()`. Sorting 10,000 tweets this way can take a few seconds.

### Quest 4: The Content Filter (`search_tweets`)
Asks the user for a search word, then builds a **new list** of every tweet whose Text contains that word (the search ignores capital letters). It prints how many tweets matched, followed by the tweets themselves.

### Shell script: Feed Analyzer (`feed-analyzer.sh`)
Reads `twitter_dataset.csv` and prints the **Top 5 Most Active Users** with this pipeline:

```
grep -E '^[0-9]+,' | cut -d',' -f2 | sort | uniq -c | sort -nr | head -n 5
```

| Command | Job |
|---|---|
| `grep -E '^[0-9]+,'` | Keeps only lines that start a new tweet (a Tweet_ID followed by a comma) |
| `cut -d',' -f2` | Extracts the Username column |
| `sort` | Groups identical usernames together |
| `uniq -c` | Counts each username |
| `sort -nr` | Orders by count, highest first |
| `head -n 5` | Keeps the top 5 |

**Why the `grep` step?** Some tweet texts contain line breaks, so one tweet can take up several lines in the file. Without the filter, pieces of tweet text would be counted as usernames.

---

## Error handling

| Situation | What the program does |
|---|---|
| `twitter_dataset.csv` is missing (Python) | Prints an error message and stops |
| `twitter_dataset.csv` is missing (Bash) | Prints an error message and exits with code `1` |
| Tweet has no Text | The tweet is removed and counted |
| Likes or Retweets is blank | Set to `0` and counted |
| Likes or Retweets is not a number | The tweet is
