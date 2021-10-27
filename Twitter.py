import tweepy
import re

class Bot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def publicar(self, api, imagem, legenda):
        api.update_with_media(filename=imagem, status=legenda)

    def pegarUltimoValorDolar(self, api):
        tweet = api.user_timeline(id = api.me().id, count = 1)[0].text
        valor = re.search(r"[0-9]*\.[0-9]*", tweet).group()
        return valor