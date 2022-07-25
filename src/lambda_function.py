import json
from requests_oauthlib import OAuth1Session
import requests

def lambda_handler(event, context):

    body = event['body']
    input = json.loads(body)
    print(event)
    consumer_key = '49AXDOb49BPjG9ztDipL80lEY'
    consumer_secret = 'xxG5zyyuhwO0VcfNQ6u3MhQpV4zVoT3KuQ0U1YeC1q9fk55wb6'
    print(input)

    payload = {"text": input['event']['blocks'][0]['elements'][0]['elements'][1]['text']}
    print(payload)
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print("There may have been an issue with the key or secret you entered.")

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)


#     base_authorization_url = "https://api.twitter.com/oauth/authorize"
#     authorization_url = oauth.authorization_url(base_authorization_url)
#     print("Please go here and authorize: %s" % authorization_url)
#     verifier = input("Paste the PIN here: ")


#     access_token_url = "https://api.twitter.com/oauth/access_token"
#     oauth = OAuth1Session(consumer_key,client_secret=consumer_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret,verifier=verifier)
#     oauth_tokens = oauth.fetch_access_token(access_token_url)

#     access_token = oauth_tokens["oauth_token"]
#     access_token_secret = oauth_tokens["oauth_token_secret"]
    access_token = '1459715092681879557-j4dm92rfRG9Ngdsg47kXZ9OKYC7UGh'
    access_token_secret = 'GeeevgOTz8ODNYVnHZbDzM9WErUSzF0YzSjgRgyfCs34B'


    oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
    )

    response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
    )

    if response.status_code != 201:
        raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    json_response = response.json()
    return json.dumps(json_response)
