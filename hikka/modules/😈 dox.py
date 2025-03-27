#meta developer: @Python_Javs
#meta developer: @Hikka_Python
from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class Doox(loader.Module):
    """докс модуль 😈"""
    strings = {'name': '😈 Dox'}

    @loader.command(alias='докс')
    async def dox(self, message):
        """[реплай] - пробить человека разроботчик @Python_Javs """
        dox_msg = [
            "🐍 <b>запрашываю Infomasion...</b>", 
            "🐍 <b>фыйлы найдены, п0лучаю инф0рмацию...</b>", 
            "🐍 <b>озникла ошыбка перезаписуваю файлы</b>"
            ]
        doox = random.choice(dox_msg)
        await utils.answer(message, doox)
        await sleep(2)
        zapros_msg = [
            "😀 <b> обрабляем </b> <code>[ 3% ] </code>",
            "🟢 <b>исправляю ошыбки и нахожу файлы"
            ]
        zapros = random.choice(zapros_msg)    
        await utils.answer(message, zapros)
        await sleep(1)
        await utils.answer(message, "🔄 <b>ищем информацию  </b> <code> [ 7% ]")
        await sleep(1)
        await utils.answer(message, "😶‍🌫️ <b>обрабатуем запрос..</b> <code> [ 13% ]</code>")
        await sleep(1)
        await utils.answer(message, "♻️ <b>обрабатую информвцию...</b> <code> [ 17% ]</code>")
        await sleep(1.5)
        await utils.answer(message, "😰 <b>0брᴀбᴀтываювᴀю инф0рмᴀцию...</b> <code> [ 24% ]</code>")
        await sleep(1)
        await utils.answer(message, "💿 <b>Ysкоряю процᴇss</b> <code> [ 37% ]</code>")
        await sleep(1)
        await utils.answer(message, "💿 <b>Ysкоряю процᴇss</b> <code> [ 53% ]</code>")
        await sleep(1)
        await utils.answer(message, "💿 <b>процесс</b> <code> [ 78% ]</code>")
        await sleep(1)
        await utils.answer(message, "💾 <b>Инф0рмᴀция нᴀйдᴇʜᴀ</b> <code> [ 94% ]</code>")
        await sleep(0.6)
        await utils.answer(message, "👾 <b>вывожу...</b> <code> [ 100% ]</code>")
        possible_numbers = [ 380478632145, 70948036940, 60123654805, 5466821658, 6262626325, 3838339333, 833828483, 819283748, 3829444678, 79236932583, 79230352252, 79236785664
        ]
        random_number = random.choice(possible_numbers)

        countries = ["Иран", "Россия", "США", "Ирак", "Бразылия", "Казастан", "Вылыко брытания", "Молдова", "Польща", "Египет", "Азия", "китай", "Япония"]
        regions = ["Вагнерская область", "Москва", "Калифорния"]
        operators = ["Телепузик", "Мегафон", "Билайн", "Error", "Nymos", "Darknet", "Darkness", "Водафон", "Киевстар", "Лайф"]
        names = ["узбекистан", "Eбу собак", "ебусь в очко", "Шлюха", "Хуесос", "Далбаёб", "Конченый", "Идиот", "клаьал"]
        addresses = ["Россия, Санкт-Петербург", "Украина, параша","Город Омск, улица Куйбышева 77, Третий этаж 105 квартира", "Ничего больше не придумала"]
        birth_dates = ["14.01.2005 (19 лет)", "16.06.6666 (ченахуй)", "14.08.8 (пасхалко)", "сегодня","помер 3 года назад", "никогда не рождался", "05.05.05 (20 лет)", "00.00.-8456 (10 000+ лет)", "34 год до н.э", "01.01.1488 (хз)", "777.07.17 (7 лет)"]
        viewers_counts = [0, 1000, 5000, 837, 364, 63, 7, 8, 37, 928, 1488, 666, 999, 333, 9999, 78942267, 7777777, 666666, 333, 22, 1, 4444, 55555, 88888888, 100000, 53793467, 345, 234, 223, 2023, 69, 52, 1, 57899753]
        reputations_positive = [0, 10, 383, 47, 3633, 99993, 77383, 100, 200, 837, 364, 63, 7, 8, 37, 928, 1488]
        reputations_negative = [100, 383, 395, 849, 48593, 999999999999, 200, 300, 3357, 4572, 344, 468, 678, 789, 3345, 34672]
        social_marks = ["🙄 Ноунейм (0)", "🤔 Известный (1)", "🌐 Проверенный! (2)", "🛡️ Деффер (3)", "📛 Скамер (4)", "🐷 Хохол (5)", "💎 𝐕𝐈𝐏 (6)", "🇷🇺 Бог (7)", "😎 Уважаемый (8)", "💩 Безмамышь (9)", "🔰 Сильнейший (10)", "💻 Программист (11)", "🤫🧏 Сигма (12)", "🤰 Шлюха (13)", "💸 Бизнесмен (14)", "🐒 Квадробобер (Квадробер) (15)"]
        comments_counts = [100, 500, 729, 374, 203, 748, 28, 0, 73, 9542, 9999588, 4578, 335, 356, 478, 789, 753, 3457]

        random_birth_date = random.choice(birth_dates)
        viewers_count = random.choice(viewers_counts)
        reputation = f"({random.choice(reputations_positive)})👍 ({random.choice(reputations_negative)})👎"
        social_mark = random.choice(social_marks)
        comments_count = random.choice(comments_counts)

        result_message = (
            f"🐠️\n<b>├ Номер:</b> <code>{random_number}</code>\n"
            f"<b>🌎 Страна:</b> <code>{random.choice(countries)}</code>\n"
            f"<b>🪽 Регион:</b> <code>{random.choice(regions)}</code>\n"
            f"<b>📱 Оператор:</b> <i>{random.choice(operators)}</i>\n\n"
            f"💎 <b>Возможные имена:\n└</b>  <i>{random.choice(names)}</i>\n\n"
            f"🎚 <b>Возможные адреса:</b> \n<i>{random.choice(addresses)}</i>\n\n"
            f"🎆 <b>Дата рождения:</b> <code>{random_birth_date}</code>\n\n"
            f"🫂 <b>Интересовались:</b> <code>{viewers_count}</code> человек\n"
            f"👁 <b>Репутация:</b> <i>{reputation}</i>\n"
            f"💬 <b>Социальная метка:</b> <code>{social_mark}</code>\n"
            f"🕸 <b>Комментариев:</b> <code>{comments_count}</code>"
        )

        await sleep(2)
        await utils.answer(message, result_message)
