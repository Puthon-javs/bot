import datetime
import logging
import time

from telethon.tl.types import Message

from .. import loader, main, utils

logger = logging.getLogger(__name__)


class CendPing(loader.Module):

    strings = {
        "name": "⌛️ CendPing",
        "uptime": "🕷️<b>Uptime</b>",
        "com": "{} <code>{}</code> <b>ms</b>\n{}",
        "modulesupports": "Модуль поддерживает значения {time} и {uptime}",
        "pingmsg": "Тут вы можете изменить ответное сообщения команды"
    }

    strings_ru = {
        "name": "CendPing",
        "uptime": "🕷️ <b>Аптайм</b>",
        "com": "{} <code>{}</code> <b>мс</b>\n{}",
        "modulesupports": "Модуль поддерживает значения {time} и {uptime}",
        "pingmsg": "Тут вы можете изменить ответное сообщения команды"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_message",
                "no",
                doc=lambda: self.strings("modulesupports"),
            ),
            loader.ConfigValue(
                "ceping_message",
                "🕷️ <b>Ping:</b>",
                lambda: self.strings("cepingmsg"),
            ),
            loader.ConfigValue(
                "timezone",
                "0",
                lambda: "use 1, -1, -3 etc. to correct the server time on {time}",
            ),
        )

    def _render_ping(self):
        offset = datetime.timedelta(hours=self.config["timezone"])
        tz = datetime.timezone(offset)
        time2 = datetime.datetime.now(tz)
        time = time2.strftime("%H:%M:%S")
        uptime = utils.formatted_uptime()
        return (
            self.config["custom_message"].format(
                time=time,
                uptime=uptime,
            )
            if self.config["custom_message"] != "no"
            else (f'{self.strings("uptime")}: <b>{uptime}</b>')
        )

    @loader.command(command="p", aliases=["ping"])
    async def ceping(self, message: Message):
        """- разроботчик @Python_Javs"""
        ceping = self.config["ceping_message"]
        start = time.perf_counter_ns()
        message = await utils.answer(message, "🕷️")
        try:
            await utils.answer(
                message,
                self.strings("com").format(
                    ceping,
                    round((time.perf_counter_ns() - start) / 10**6, 3),
                    self._render_ping(),
                ),
            )
        except TypeError:
            await utils.answer(
                message,
                "Invalid number on .config -> cenping -> timezone, pls update it",
            )
