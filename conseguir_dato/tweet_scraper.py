# Twint no funciona
# TODO: (WILL) add tweepy for more efficient scraping

import asyncio
from datetime import date, timedelta, datetime
import json

from twscrape import API, gather
from twscrape.logger import set_log_level

MESES = 6
API_LIMITA = 2

async def scrape(tema, ubicación):
    api = API()

    # agrega cuentas
    # await api.pool.add_account("user1", "pass1", "u1@example.com", "mail_pass1")
    await api.pool.add_account("@Guiller90734051", "Interpreta", "interpretawilltweet1@gmail.com", "Interpreta")
    await api.pool.add_account("@Guiller90734052", "Interpreta", "interpretawilltweet2@gmail.com", "Interpreta")
    await api.pool.add_account("@Guiller90734053", "Interpreta", "interpretawilltweet3@gmail.com", "Interpreta")
    await api.pool.add_account("@gueirllmo23", "Interpreta", "gueirllmo23@gmail.com", "Interpreta")
    await api.pool.add_account("@Guiller90734055", "Interpreta", "interpretawilltweet5@gmail.com", "Interpreta")
    await api.pool.add_account("@ahugeazhow19980", "Interpreta", "ajaxus929@gmail.com", "Interpreta")
    await api.pool.login_all()

    inicio = date.today() - timedelta(MESES * 30)
    hoy = date.today()
    
    # Hace query
    q = f"{tema} since:{inicio} until:{hoy}"
    print (q)
    resultas = []
    async for tweet in api.search(q, limit=API_LIMITA):
        # rep es httpx.Response object
        # print(rep.status_code, rep.json())
        """Preocupación potencial: todos los tweets más recientes son del mismo bot
        """
        # Comprobar la relevancia de la ubicación
        if (ubicación.upper() in tweet.rawContent.upper() or ubicación.upper() in tweet.user.location.upper()):
            resultas.append ((tweet.id, tweet.user.username, tweet.rawContent))
    
    now = datetime.now()
    with open(f'db/{tema}-{now}.json', "w") as outfile:
        json.dump(resultas, outfile)

    return resultas

# asyncio.run(scrape(tema))
