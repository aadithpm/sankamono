import requests
import constants
from bs4 import BeautifulSoup
from datetime import date


def get_lost_sectors_scrapper():
    tid_req_data = requests.get(constants.tid_url)
    tid_bs4_data = BeautifulSoup(
        tid_req_data.text,
        'lxml'
    )
    print(tid_bs4_data.prettify())


def get_lost_sectors_daily(embedder):
    embed = embedder(
        title=f'Lost Sectors - {date.today().strftime("%d/%m/%Y")}',
        description=f'Master and Legend Lost Sector data from {constants.tid_url}',
        color=constants.embed_color
    )
    return embed
