##
# de-x.py -- delete all your tweets w/o API access
# Copyright 2023 Thorsten Schroeder
#
# Published under 2-Clause BSD License (https://opensource.org/license/bsd-2-clause/)
#
# Please see README.md for more information
##

##
#  Unlike-Tweets-X -- delete all your favorites w/o API access
#  Copyright 2023 Metin Emre Koral
#  Forked and developed from devio's de-x script: (https://github.com/devio/de-x)
#
# Please see README.md for more information
##


import sys
import json
import requests
import random
import time

def get_tweet_ids(json_data):

    result = []
    data = json.loads(json_data)

    for d in data:
        result.append(d['like']['tweetId'])

    return result

def parse_req_headers(request_file):

    sess = {}

    with open(request_file) as f:
        line = f.readline()
        while line:
            try:
                k,v = line.split(':', 1)
                val = v.lstrip().rstrip()
                sess[k] = val
            except:
                # ignore empty lines
                pass

            line = f.readline()

    return sess

def main(ac, av):

    if(ac != 3):
        print(f"[!] usage: {av[0]} <jsonfile> <req-headers>")
        return

    f = open(av[1], encoding='UTF-8')
    raw = f.read()
    f.close()

    # skip data until first '['
    i = raw.find('[')
    ids = get_tweet_ids(raw[i:])

    session = parse_req_headers(av[2])

    for i in ids:
        delete_tweet(session, i)
        # as a chrishenninger's comment in another alike project; X's UnfavoriteTweet endpoint has rate limiting: ~500 tweets in a ~15 minutes https://gist.github.com/aymericbeaumet/d1d6799a1b765c3c8bc0b675b1a1547d?permalink_comment_id=4694790#gistcomment-4694790 

        sleep_time = random.uniform(1, 5)
        time.sleep(sleep_time)


def delete_tweet(session, tweet_id):

    print(f"[*] delete tweet-id {tweet_id}")
    delete_url = "https://twitter.com/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet"
    data = {"variables":{"tweet_id":tweet_id,"dark_request":False},"queryId":"ZYKSe-w7KEslx3JhSIk5LA"}

    # set or re-set correct content-type header
    session["content-type"] = 'application/json'
    r = requests.post(delete_url, data=json.dumps(data), headers=session)
    print(r.status_code, r.reason)
    print(r.text[:500] + '...')

    return


if __name__ == '__main__':

    main(len(sys.argv), sys.argv)
