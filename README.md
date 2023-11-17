# Unlike-Tweets-X (Unfavorite)

**This script can be used to delete the whole liked tweets(favorited tweets)**

As Elmo restricted access to Twitter's APIs, many tools that did the same job doesn't work anymore, without registering a developer account at X/Twitter.

However, this small script does not depend on those restricted APIs. There is no need to register a developer account nor is it necessary to pay for API access. Only a few manual steps need to be carried out by the user, these steps are explained in detail below.

## Preparation

1. Request an archive of your data at X/Twitter. This archive will be available for download after a few days (mine took like 2 days). If your data is ready for download, you'll receive a notification in your Twitter-App or via E-mail. ![Request Twitter archive at X](doc/archive.png)
2. Once your archive has been downloaded, you need to extract the ZIP-Archive on your disk. You'll need the file called `like.js` that is included in the archive. It includes every favorites(liked tweets) including the corresponding tweet-ID.
3. To enable this python script to unfavorite posts with the tweet-IDs from your archive, you must provide session information as well, otherwise the python script will not be able to authorize. The easiest way is to get them from your browser:
   1. Edge/Chrome: Log into X/Twitter as you used to do before. Then open developer tools by pressing `Ctrl-Shift-i`. Now switch to the *Network* tab of the Developer Tools and click on any request to show the headers. ![Copy & Paste session headers at twitter.com](doc/session.png) Just copy and paste every request header after "Accept", including the values that are redacted in this example. It is important to copy the following headers: *Cookie*, *X-Csrf-Token* and *Authorization*. But in doubt, just copy & paste all the request headers to a file on your hard-drive, e. g. `request-headers.txt`.
   2. Firefox: Probably the same as above, PR welcome
   3. burp suite: Just record a twitter-browser session and copy from client request headers.
4. Check that your `request-headers.txt` is formatted correctly. You should remove some newlines that may be there by accident after copy&paste. You can also just copy&paste the values of the following three headers - a minimal request-headers-file could look like this:
```
Authorization: Bearer AAAAAAAAAAAAAAAAAAAAANR[...]
X-Csrf-Token: b0a38[...]
Cookie: [...] _twitter_sess=BAhD[...]; auth_token=24fa[...]
```

## Run

After you've received your twitter archive and edited a request-header file for a current session (as explained above), we can call our script:

```
de-x.py like.js request-headers.txt
```

## Background

If you know the tweet-id, you can delete the corresponding tweet by calling an API with that specific ID. So the first and most important step is to get a list of all tweets (and thus tweet-ids) that shall be deleted. You can do this, using twitter-APIs, but these APIs are restricted and you have to pay for it. Even if you pay for it, there are quite a few limitations and you might not be able to gather a list of all of your tweets.

Thus, it is easier to simply request an archive of all favorited tweets that you have liked so far. This dataset includes all meta-data and, of course, also the tweet-id we are looking for in the first place. You don't have to pay for it, it is complete and machine readable: win.

The archive contains a file called `like.js` which is basically a JSON encoded data structure, a list of all of your tweets.

Twitter's `UnfavoriteTweet` API is not restricted, and can be called without registering a developer account at X. Using this approach, you can at least unfavorite around 500 tweets in roughly 15 min (*).

(*) Unlike the DELETETWEET API used by Thorsten Schröder's de-x script, rate-limit is implemented in the UNFAVORITETWEET API.  As a chrishenninger's comment in another alike project; X's UnfavoriteTweet endpoint has rate limiting: ~500 tweets in a ~15 minutes https://gist.github.com/aymericbeaumet/d1d6799a1b765c3c8bc0b675b1a1547d?permalink_comment_id=4694790#gistcomment-4694790 

## Conclusion

Here is opinion from original creator [Thorsten Schroeder](https://github.com/devio) of this tool and i completely agree this opinion:


>There is no *One Click Delete Everything* tool available and it never will. This is due to Twitter's massive restrictions on using their APIs to control your own data. Of course, they would like to keep your data. Forever. However, If you don't want your data being archived at Twitter until global heat finally also kills all machines on planet earth, you should spend some time and effort to delete them - free of charge. Maybe it is possible to build a *One Click Delete Everything* tool using this approach, and maybe it is even user-friendly. I know, the one above is not user friendly, but hopefully this readme is, and hopefully it enables your daughter/neighbor/friend to assist with deleting stuff from the Internet that you don't want to see there anymore. In my opinion, everyone should have the right and the opportunity to delete their own content from the Internet without problems, without barriers and without paying money; regardless of their origin.

