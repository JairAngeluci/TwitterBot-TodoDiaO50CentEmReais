from logging import log
from Imagem import Imagem
from Twitter import Bot
from CotacaoDolar import Cotacao
from os import environ
import random

# chaves de acesso da API / usuário do bot
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

# emojis felizes/tristes
emojisFelizes = ["😊", "😁", "😄", "🥳", "😍", "🥰", "😻", "😆", "😋", "🤑"]
emojisTristes = ["😭", "😢", "😞", "🙁", "🥺", "😿", "💩", "😾", "😡", "😰"]

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
        legenda = "O dólar subiu " + random.choice(emojisTristes) + "\n\nValor do dólar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    else:
        legenda = "O dólar caiu " + random.choice(emojisFelizes) + "\n\nValor do dólar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    bot.publicar(api, "ImagensCriadas/MeioDolar.jpg", legenda)
    print("Postou!")
else:
    print("Dólar não mudou!")