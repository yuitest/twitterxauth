# twitterxauth

a thin wrapper for xAuth with Twitter API 1.1

## usage

```
import twitterxauth
access_token, access_token_secret = twitterxauth.get_oauth_tokens(
    'YourXAuthConsumerKey',
    'YourXAuthConsumerKeySecret',
    'user_twitter_screen_name',
    'user_password',
)
```
