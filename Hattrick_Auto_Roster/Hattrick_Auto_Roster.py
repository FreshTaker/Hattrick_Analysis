
import requests
from requests_oauthlib import OAuth1Session




hattrick = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')

url = 'https://api.twitter.com/1/account/settings.json'
r = hattrick.get(url)



