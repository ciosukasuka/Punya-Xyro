# Credits: XYROOOO
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>

from config import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, FORCE_SUB_CHANNEL_5, FORCE_SUB_CHANNEL_6
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_4 and not FORCE_SUB_CHANNEL_5 and not FORCE_SUB_CHANNEL_6:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_4 and not FORCE_SUB_CHANNEL_5 and not FORCE_SUB_CHANNEL_6:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4 and FORCE_SUB_CHANNEL_5:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ5", url=client.invitelink5),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4 and FORCE_SUB_CHANNEL_5 and FORCE_SUB_CHANNEL_6:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ5", url=client.invitelink5),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ5", url=client.invitelink6),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_4 and not FORCE_SUB_CHANNEL_5 and not FORCE_SUB_CHANNEL_6:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4 and FORCE_SUB_CHANNEL_5:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ5", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_4 and FORCE_SUB_CHANNEL_5 and FORCE_SUB_CHANNEL_6:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ4", url=client.invitelink4),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ5", url=client.invitelink5),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ6", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    
