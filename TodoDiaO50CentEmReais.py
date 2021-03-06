from logging import log
from os import environ
import random

from Imagem import Imagem
from Twitter import Bot
from CotacaoDolar import Cotacao

# chaves de acesso da API / usu谩rio do bot
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

# emojis felizes/tristes
emojisFelizes = ["馃槉", "馃榿", "馃槃", "馃コ", "馃槏", "馃グ", "馃樆", "馃槅", "馃構", "馃", "馃槈", "馃ぉ", "馃お", "馃ぃ"]
emojisTristes = ["馃槶", "馃槩", "馃槥", "馃檨", "馃樋", "馃挬", "馃樉", "馃槨", "馃槹", "馃槳", "馃樀", "馃槯", "馃", "馃樀"]

#acessar a api do twitter
bot = Bot(consumer_key, consumer_secret, access_token, access_token_secret)
api = bot.authenticate()

# acessar o json com a cotacao do dolar e salvar o valor da cotacao com o momento da atualizacao
cotDolar = Cotacao("https://economia.awesomeapi.com.br/last/USD-BRL")
dolar = cotDolar.retornarValorDolar()
dataCotacao = cotDolar.retornarData()

# verificar se o dolar subiu e guardar novo valor
dolarAntes = float(bot.pegarUltimoValorDolar(api))
dolarMudou = False
dolarAumentou = False
if (round(dolar, 2) != round(dolarAntes, 2)):
    dolarMudou = True
    if (dolar > dolarAntes):
        dolarAumentou = True
    elif (dolar < dolarAntes):
        dolarAumentou = False
else:
    dolarMudou = False

# criar/sobrescrever a imagem MeioDolar.jpg
img = Imagem()
img.CriarImagemAlterada(dolar)

# se o dolar tiver mudado, preparar a legenda e a imagem e publicar o tweet
if (dolarMudou):
    if (dolarAumentou):
        legenda = "O d贸lar subiu " + random.choice(emojisTristes) + "\n\nValor do d贸lar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    else:
        legenda = "O d贸lar caiu " + random.choice(emojisFelizes) + "\n\nValor do d贸lar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    bot.publicar(api, "ImagensCriadas/MeioDolar.jpg", legenda)
    print("Postou!")
else:
    print("D贸lar n茫o mudou!")