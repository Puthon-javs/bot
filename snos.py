# meta developer: @YourNickname
# scope: hikka_only
# scope: hikka_min 1.6.0

from hikkatl.types import Message
from .. import loader, utils
import smtplib
from email.mime.text import MIMEText
import random
import time

@loader.tds
class TelegramComplaintMod(loader.Module):
    """Модуль для отправки жалоб в Telegram"""
    strings = {
        "name": "Telegram",
        "cfg_smtp_server": "SMTP сервер (например: smtp.mailtrap.io)",
        "cfg_smtp_port": "SMTP порт (587 для TLS)",
        "cfg_smtp_user": "SMTP логин",
        "cfg_smtp_pass": "SMTP пароль",
        "complaint_sent": "✅ Жалоба на {} отправлена с {}",
        "error": "❌ Ошибка: {}",
        "args": "❌ Используй: <code>.snos @username [причина]</code>",
        "config_warning": "⚠️ Сначала настрой SMTP в <code>.config TelegramComplaint</code>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "smtp_server",
                "",
                lambda: self.strings["cfg_smtp_server"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "smtp_port",
                587,
                lambda: self.strings["cfg_smtp_port"],
                validator=loader.validators.Integer(minimum=1, maximum=65535),
            ),
            loader.ConfigValue(
                "smtp_user",
                "",
                lambda: self.strings["cfg_smtp_user"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "smtp_pass",
                "",
                lambda: self.strings["cfg_smtp_pass"],
                validator=loader.validators.String(),
            ),
        )

    async def client_ready(self, client, db):
        self._client = client

    @loader.command()
    async def snos(self, message: Message):
        """Отправить жалобу - .snos @username [причина]"""
        if not all([self.config["smtp_server"], self.config["smtp_user"], self.config["smtp_pass"]]):
            await utils.answer(message, self.strings["config_warning"])
            return

        args = utils.get_args_raw(message)
        if not args or not args.startswith("@"):
            await utils.answer(message, self.strings["args"])
            return

        username = args.split()[0]
        reason = " ".join(args.split()[1:]) if len(args.split()) > 1 else random.choice(self.reasons())
        temp_email = f"user{random.randint(100000, 999999)}@example.com"

        try:
            await self._send_complaint(username, reason, temp_email)
            await utils.answer(message, self.strings["complaint_sent"].format(username, temp_email))
        except Exception as e:
            await utils.answer(message, self.strings["error"].format(str(e)))

    def reasons(self):
        return [
            "Распространение спама и рекламы",
            "Оскорбления и угрозы",
            "Распространение запрещенного контента",
            "Мошенничество и обман",
            "Нарушение авторских прав",
            "Фейковый аккаунт",
        ]

    async def _send_complaint(self, username, reason, from_email):
        """Отправка жалобы через SMTP"""
        emails = [
            "abuse@telegram.org",
            "dmca@telegram.org",
            "support@telegram.org",
        ]

        body = f"""Здравствуйте,

Пользователь {username} нарушает правила Telegram:
{reason}

Прошу принять меры.
С уважением,
{from_email}
"""

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = f"Жалоба на {username}"
        msg["From"] = from_email
        msg["To"] = ", ".join(emails)

        try:
            with smtplib.SMTP(self.config["smtp_server"], self.config["smtp_port"], timeout=10) as server:
                server.ehlo()
                if self.config["smtp_port"] == 587:
                    server.starttls()
                    server.ehlo()
                server.login(self.config["smtp_user"], self.config["smtp_pass"])
                server.sendmail(from_email, emails, msg.as_string())
                time.sleep(1)
        except smtplib.SMTPException as e:
            raise Exception(f"SMTP ошибка: {e}")