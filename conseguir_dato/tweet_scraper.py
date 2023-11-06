# Twint no funciona
# TODO: (WILL) use second account to try tweepy for location data

import asyncio
from datetime import date, timedelta
import json

from twscrape import API, gather
from twscrape.logger import set_log_level

async def scrape():
    api = API()

    # agrega cuentas
    # await api.pool.add_account("user1", "pass1", "u1@example.com", "mail_pass1")
    await api.pool.add_account("@Guiller90734051", "Interpreta", "interpretawilltweet1@gmail.com", "Interpreta")
    await api.pool.add_account("@Guiller90734052", "Interpreta", "interpretawilltweet2@gmail.com", "Interpreta")
    await api.pool.login_all()

    inicio = date.today() - timedelta(6 * 30)
    hoy = date.today()
    tema = 'Mujer migrante en Colombia'
    
    # Hace query
    q = f"{tema} since:{inicio} until:{hoy}"
    print (q)
    resultas = []
    async for tweet in api.search(q, limit=2):
        print ('here')
        # rep es httpx.Response object
        # print(rep.status_code, rep.json())
        # print (type(rep.json()))
        resultas.append ([tweet.id, tweet.user.username, tweet.rawContent])
    print (resultas)
    
    with open("db/sample.json", "w") as outfile:
        json.dump(resultas, outfile)

asyncio.run(scrape())
