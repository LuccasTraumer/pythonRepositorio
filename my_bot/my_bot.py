import tweepy
import time
import random
print('this is my twitter bot ')

CONSUMER_KEY = '****'
CONSUMER_SECRET = '****'

ACESS_KEY = '****'
ACESS_SECRET = '****'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACESS_KEY,ACESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search,q="#FalaProgramadores",
                           lang="pt", since="2019-10-01").items()

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


def mostra():
    for tweet in tweets:
        print(tweet.text)
while True:
    #retweet_Mensionado()
    mostra()
    time.sleep(30)