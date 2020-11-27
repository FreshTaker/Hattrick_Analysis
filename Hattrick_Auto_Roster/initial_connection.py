"""This is used for the first connection by a user.

callback_uri = Need to change
"""

from credentials import consumer_key, consumer_secret

print(consumer_key)
print(consumer_secret)
# OAuth Endpoints from API Documentation:
request_token_url = 'https://chpp.hattrick.org/oauth/request_token.ashx'
authorization_base_url = 'https://chpp.hattrick.org/oauth/authorize.aspx'
access_token_url = 'https://chpp.hattrick.org/oauth/access_token.ashx'

# 2. Fetch a request token:
from requests_oauthlib import OAuth1Session
oauth = OAuth1Session(client_key=consumer_key, client_secret=consumer_secret, callback_uri='www.github.com/FreshTaker')
fetch_response = oauth.fetch_request_token(request_token_url)
print(fetch_response)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
print(resource_owner_key, resource_owner_secret)

#3 Redirect user to Hattrick for authorization:
authorization_url = oauth.authorization_url(authorization_base_url)
print('Please go here and authorize: ' + str(authorization_url))

#4 Get authorization verifier code from callback url:
redirect_response = input('Past the full redirect URL here: ')
oauth.parse_authorization_response(redirect_response)

#5 Fetch the access token:
oauth.fetch_access_token(access_token_url)

#6 Fetch a protected resource:
api_url = 'https://chpp.hattrick.org/chppxml.ashx'
r = oauth.get(api_url, parameter='file=managercompendium&version=1.3')
print(r.content)