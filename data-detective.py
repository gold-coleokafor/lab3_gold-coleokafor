import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    clean_tweets = []
    bad_rows = 0
    for tweet in tweets:
        missing_text = tweet.get('Text')
        if missing_text is None or missing_text.strip() == '':
            bad_rows += 1
            continue  

        if tweet.get('Likes') == '' or tweet.get('Likes') is None:
            tweet['Likes'] = 0
            bad_rows += 1
        if tweet.get('Retweets') == '' or tweet.get('Retweets') is None:
            tweet['Retweets'] = 0
            bad_rows += 1

        try:
            tweet['Likes'] = int(tweet['Likes'])
            tweet['Retweets'] = int(tweet['Retweets'])
        except ValueError:
            print(f"Bad row due to invalid data types: {tweet}")
            bad_rows += 1
            continue  

        clean_tweets.append(tweet)

    print(f"Fixed or removed {bad_rows} bad rows.")
    return clean_tweets  

def find_viral_tweet(tweets):
    viral = 0
    if len(tweets) == 0:
        print("Error: This list is empty. No tweets to search.")
        return None
    viral = tweets[0]
    for tweet in tweets:
        if tweet['Likes'] > viral['Likes']:
            viral = tweet
    print(f"Username: {viral['Username']} | Likes: {viral['Likes']} | Text: {viral['Text']}")
    return viral

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    if len(tweets) == 0:
            print("Error: This list is empty. No tweets to search.")
            return None
    position = range(0, len(tweets))
    for i in position:
        index = i
        for j in range(i + 1, len(tweets)):
            if tweets[j]['Likes'] > tweets[index]['Likes']:
                index = j
        tweets[i], tweets[index] = tweets[index], tweets[i]
    return tweets

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    keyword = keyword.strip().lower()
    if keyword == "":
        print("Error: The keyword is empty.")
        return None
    matching_tweets = []
    for tweet in tweets: 
        if keyword in tweet['Text'].lower():
            matching_tweets.append(tweet)
    print(f"Found {len(matching_tweets)} tweets.")
    for tweet in matching_tweets:
        print(f"Username: {tweet['Username']} | Likes: {tweet['Likes']} | Text: {tweet['Text']}")
    if len(matching_tweets) == 0:
            print(f"No tweets found for this search: {keyword}")
    return matching_tweets


if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    # Call your functions here to complete the quests!
clean_dataset = clean_data(dataset)
len(clean_dataset)
find_viral_tweet(clean_dataset)
sorted_liked_tweets = custom_sort_by_likes(clean_dataset)
top_10 = sorted_liked_tweets[:10]

print("--- Top 10 Most Liked Tweets ---")
for rank, tweet in enumerate(top_10, start=1):
    print(f"{rank}. Username: {tweet['Username']} | Likes: {tweet['Likes']} | Text: {tweet['Text']}")
search_word = input("Enter a search word (e.g., Python): ")
search_tweets(clean_dataset, search_word)