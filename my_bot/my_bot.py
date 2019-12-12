import tweepy
import time
import random
print('this is my twitter bot ')

CONSUMER_KEY = '3uTGXZn8zXB7MDWZ4Xjs3zBSR'
CONSUMER_SECRET = '3B7mjaKh6fzfQCEtYqjTdj9RSfkADoGMiUuKtKB68ikPFHW6m4'

ACESS_KEY = '1203421137495089154-s593xwKx9yHhH69SoZJzkQl9Q8E0pV'
ACESS_SECRET = 'jshYzMZDQjBotXLKRd0qvbiyIIJ0vdbgyN75GpmBwBV3N'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACESS_KEY,ACESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
nome_Arq = 'ultimoVisto.txt'


def ultimo_visto(nomeArquivo):
    f_read = open(nome_Arq)
    ultimo = int(f_read.read().strip())
    f_read.close()
    return ultimo

def armazenar_Ultimo_Visto(ultimo_id_visualizado, nome_Arq):
    f_write = open(nome_Arq,'w')
    f_write.write(str(ultimo_id_visualizado))
    f_write.close()

def retweet_Mensionado():
    ultimo_id = ultimo_visto(nome_Arq)
    mentions = api.mentions_timeline(ultimo_id,
                                tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) +' - '+ mention.full_text)
        ultimo_id = mention.id
        armazenar_Ultimo_Visto(ultimo_id,nome_Arq)
        if'luccastraumer' in mention.full_text.lower():
            statis = '@' + mention.user.screen_name + ' O MAIS BRABOOO!'
            api.update_status(statis,mention.id)
            api.create_favorite(mention.id)



def favArroba():
    ultimo_id = ultimo_visto(nome_Arq)
    for tweet in api.search(q="luccastraumer", lang="pt", rpp=10):
        mentions = api.mentions_timeline(tweet.id,
                                         tweet_mode='extended')
        for mention in reversed(mentions):
                print(str(mention.id) + ' - ' + mention.full_text)
                ultimo_id = mention.id
                armazenar_Ultimo_Visto(ultimo_id, nome_Arq)
                if 'vai mano' in mention.full_text.lower() and tweet.text.lower():
                    statis = '@' + mention.user.screen_name + ' O MAIS BRABOOO!'
                    api.update_status(statis, mention.id)
                    api.create_favorite(mention.id)
                else:
                    continue

while True:
    #retweet_Mensionado()
    favArroba()
    time.sleep(30)