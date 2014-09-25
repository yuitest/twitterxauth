# coding: utf8
import oauth2
import urllib
import urlparse
from collections import namedtuple


OAuthTokens = namedtuple(
    'OAuthTokens', ('access_token', 'access_token_secret'))


def get_oauth_tokens(
    consumer_key, consumer_secret, screen_name, password,
    API_URL='https://api.twitter.com/oauth/access_token',
):
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    client = oauth2.Client(consumer)
    client.add_credentials(screen_name, password)
    client.set_signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    resp, token = client.request(
        API_URL, method='POST', body=urllib.urlencode({
            'x_auth_mode': 'client_auth',
            'x_auth_username': screen_name,
            'x_auth_password': password,
        }))
    parsed_token = dict(urlparse.parse_qsl(token))
    return OAuthTokens(
        parsed_token['oauth_token'],
        parsed_token['oauth_token_secret'],
    )
