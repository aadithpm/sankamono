import constants
import re
import requests
from bs4 import BeautifulSoup
from datetime import date


def get_lost_sectors_scrapper():
    tid_req_data = requests.get(constants.tid_url)
    tid_bs4_data = BeautifulSoup(
        tid_req_data.text,
        'lxml'
    )

    sectors_data = tid_bs4_data.find_all(
        'div',
        class_='eventCardContainer',
        id=re.compile("bl_lost_sector*")
    )

    print(sectors_data.prettify())
    # Legend

    # Master
    return {
        'legend':
        {
            'title': 'test1'
        },
        'master':
        {
            'title': 'test2'
        }
    }


def get_lost_sectors_daily(embedder):
    embed = embedder(
        title=f'Lost Sectors - {date.today().strftime("%d/%m/%Y")}',
        description=f'Master and Legend Lost Sector data from {constants.tid_url}',
        color=constants.embed_color
    )

    sectors = get_lost_sectors_scrapper()

    # Legend LS

    embed.add_field(
        name=f'{sectors["legend"]["title"]} - {constants.legend_pl}',
        value=sectors["legend"]
    )

    # Master LS

    embed.add_field(
        name=f'{sectors["master"]["title"]} - {constants.master_pl}',
        value=sectors["master"]
    )

    return embed
