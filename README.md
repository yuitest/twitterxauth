# twitterxauth

a thin wrapper for xAuth with Twitter API 1.1

## Installation

```ShellSession
$ pip install twitterxauth
```

or

```ShellSession
$ pip install git+https://github.com/yuitest/twitterxauth.git
```

## Usage

```python
import twitterxauth
access_token, access_token_secret = twitterxauth.get_oauth_tokens(
    'YourXAuthConsumerKey',
    'YourXAuthConsumerKeySecret',
    'user_twitter_screen_name',
    'user_password',
)
```

