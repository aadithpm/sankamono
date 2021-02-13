import constants


def get_help_message(embedder):
    embed = embedder(
        title='Sankamono Help',
        color=constants.embed_color
    )

    embed.add_field(
        name='Command list',
        value=constants.help_string
    )

    return embed
