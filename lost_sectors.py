import constants
import re
import requests
from bs4 import BeautifulSoup
from datetime import date


def get_sector_tag_data(tag, tag_class):
    return tag.find(constants.ls_internal_tag, tag_class).contents[0]


def make_sector_entry(ls):
    record = {}
    data = BeautifulSoup(str(ls), 'lxml')

    # Sector, level, modifiers
    # record['level'] = get_sector_tag_data(data, constants.ls_level_tag)
    record['title'] = get_sector_tag_data(data, constants.ls_title_tag)
    record['description'] = get_sector_tag_data(data, constants.ls_description_tag)
    record['powerlevel'] = data.find(
            constants.ls_container_tag,
            class_=constants.ls_powerlevel_tag
        ).contents[0]

    # Rewards
    rewards = data.find_all('p', class_='eventCardRewardName')

    # Formatting
    record['rewards'] = '\n'.join(r.contents[0] for r in rewards)
    record['description'] = record['description'].replace('\n\n', '\n')

    return record


def get_lost_sectors_scrapper():
    tid_req_data = requests.get(constants.tid_url)
    tid_bs4_data = BeautifulSoup(
        tid_req_data.text
    )

    sectors_data = tid_bs4_data.find_all(
        constants.ls_container_tag,
        class_=constants.ls_container_class,
        id=re.compile(constants.ls_bl_regex)
    )

    return [make_sector_entry(sector) for sector in sectors_data]


def get_lost_sectors_daily(embedder):
    embed = embedder(
        title=f'Lost Sectors - {date.today().strftime("%d/%m/%Y")}',
        description=f'Data from {constants.tid_url}',
        color=constants.embed_color
    )

    sectors = get_lost_sectors_scrapper()

    print(sectors)

    for sector in sectors:
        embed.add_field(
            name=f'{sector["title"]} ({sector["powerlevel"]})',
            value=f'**Rewards:**\n{sector["rewards"]}\n**Modifiers:**\n{sector["description"]}'
        )

    return embed
