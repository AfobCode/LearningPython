import json
import sys

#filename = input('Enter the name of the file: ')
filename = sys.argv[1]
tweet_num = int(input('Which tweet number you want to see: '))
user_path = input('Enter the path (i.e: user/id): ')

path = user_path.split('/')
tweet_count = 0

# Open the file and save only the tweet of interest
try: 
    with open(filename) as json_file: 
        for line in json_file:
            if len(line) > 1: tweet_count +=1
            if tweet_count == tweet_num: 
                tweet = json.loads(line)
                break
except:
    print('File not found, unable to read')


for i in range(len(path)):
    try:
        tweet = tweet[path[i]]
    except:
        print(f'Unable to reach {path[i]} in {tweet}')

print(tweet)