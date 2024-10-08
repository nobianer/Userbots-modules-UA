# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: ExcuseGenerator
# Author: dorotorothequickend
# Commands:
# .excuse
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroExcuseGenerator.png
# meta developer: @nobianermodules

import random

from .. import loader, utils


@loader.tds
class ExcuseGeneratorMod(loader.Module):
    """
    Ваш відданий помічник!
    """

    strings = {
        "name": "ExcuseGenerator",
        "courtesy": "Звернення до людини на ТИ (0), звернення до людини на ВИ (1).",
        "sex": (
            "Звертатися до людини як до чоловічої статі (0), звертатися до людини як до"
            " жіночої статі (1)."
        ),
        "mysex": "Стать того, хто пише відмазку. Чоловіча (0), жіноча (1).",
    }

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue("courtesy", "0", doc=lambda: self.strings("courtesy")),
            loader.ConfigValue("sex", "0", doc=lambda: self.strings("sex")),
            loader.ConfigValue("mysex", "0", doc=lambda: self.strings("mysex")),
        )

    @loader.command()
    async def excuse(self, message):
        """<ім'я> - генерує відмазку."""
        args = utils.get_args_raw(message)
        nameo = [
            "Друг",
            "Товариш",
            "Друже",
            "Приятель",
            "Дорогий друже",
            "Мій найкращий друг",
        ]
        nameowoman = [
            "Дівчина",
            "Моя найкраща подруга",
            "Подруга",
            "Пупсик",
            "Котик",
            "Красуня",
        ]
        hello = [
            "привіт",
            "здрастуй",
            "вітаю",
            "добрий день",
            "добрий вечір",
            "доброго ранку",
            "саламулі гамаджоба",
            "гарного дня",
            "салам алейкум",
            "hello",
            "здарова",
            "алоха",
        ]
        hellovi = [
            "здрастуйте",
            "здрастуй",
            "добрий день",
            "добрий вечір",
            "доброго ранку",
            "гарного дня",
            "гарного вечора",
            "гарного проведення часу",
        ]
        fail = [
            "Літак, у якому я летів, приземлився на запаснику в Новгороді",
            (
                "Я їхав у поїзді, і хтось зірвав стопкран, я різко впав і вдарився"
                " головою, зараз у лікарні"
            ),
            (
                "Я спіймав попутку, її зупинила ГИБДД, і знайшли велику партію"
                " наркотиків. Зараз я під слідством"
            ),
            (
                "Я вийшов з дому, а двері зачинилися, я спробував залізти через"
                " балкон, але впав. Зараз я в травмпункті, йду на поправку"
            ),
            (
                "Я йшов парком, і на мене напав бомж, він вкрав у мене гаманець і ключі"
                " від будинку. Добре, хоч що не зґвалтував"
            ),
            (
                "У мене розвалилося ліжко під час сну, я пошкодив хребет."
                " Зараз іду на одужання"
            ),
            "Я втратив паспорт",
            "Я на похороні був, останній дідусь помер",
            "У мене рак знайшли, я по лікарнях їздив",
            "У мене рак печінки, на жаль, серйозно, я зараз хіміотерапію проходжу",
            "Я втратив усе, що було в портмоне",
            "Мене побили цигани",
            "У мене котик помер, я на похороні",
            "Я в аеропорту, мене депортували",
            "Зламав ногу. Мене поклали в лікарню, відновлююся",
            "Я просто в глушині був",
            "Я просто був не в місті",
            "Мене відправили у справах",
            "Твій банк відхилив переказ",
            "Мій рахунок заблокували",
            "Я загубив ноутбук",
            "У мене зламався комп'ютер",
            "Комп'ютер вибухнув, полагоджу і все зроблю",
            "У мене передозування кофеїну. Я в лікарні",
            "Мене машина збила",
            "Я трохи не встигаю",
            "Я зараз працюю за фрілансом",
            "Скоро стартап окупиться",
            "Бабуся скоро пенсію отримає",
            "Гроші повернув твій банк, пише відмову, перевір номер картки",
            "Платіж на обробці",
            "Платіж відхилено, буду сваритися з банком",
            "Проводжаю сліпу бабусю через дорогу",
            "Зламав хребет",
            "Мої рибки спливли нагору, скоро похорон",
            "Я осліп",
            "Біля мого будинку вбили дівчину, зараз усіх опитують",
            "Мене в армію забрали",
            "У мене кішка народжувала",
            "У мене дочка народила",
            "У мене молоко втекло",
            "У мене квартира згоріла",
            "Я недооцінив завдання",
            "Я недооцінив масштаб завдання",
            "Я зіткнувся з непередбаченими складнощами",
        ]
        failwoman = [
            "Літак, у якому я летіла, приземлився на запаснику в Новгороді",
            (
                "Я їхала в поїзді, і хтось зірвав стопкран, я різко впала і вдарилася"
                " головою, зараз у лікарні"
            ),
            (
                "Я спіймала попутку, її зупинила ГИБДД, і знайшли велику партію"
                " наркотиків. Зараз я під слідством"
            ),
            (
                "Я вийшла з дому, а двері зачинилися, я спробувала залізти через"
                " балкон, але впала. Зараз я в травмпункті, йду на поправку"
            ),
            (
                "Я йшла парком, і на мене напав бомж, він вкрав у мене гаманець і ключі"
                " від будинку. Добре, що хоч не зґвалтував"
            ),
            (
                "У мене розвалилося ліжко під час сну, я пошкодила хребет."
                " Зараз іду на одужання"
            ),
            "Я загубила паспорт",
            "Я на похороні була, останній дідусь помер",
            "У мене рак знайшли, я по лікарнях їздила",
            "У мене рак печінки, на жаль, серйозно, я зараз хіміотерапію проходжу",
            "Я втратила все, що було в портмоне",
            "Мене побили цигани",
            "У мене котик помер, я на похороні",
            "Я в аеропорту, мене депортували",
            "Зламала ногу. Мене поклали в лікарню, відновлююся",
            "Я просто в глушині була",
            "Я просто була не в місті",
            "Мене відправили у справах",
            "Твій банк відхилив переказ",
            "Мій рахунок заблокували",
            "Я загубила ноутбук",
            "У мене зламався комп'ютер",
            "Комп'ютер вибухнув, полагоджу і все зроблю",
            "У мене передозування кофеїну. Я в лікарні",
            "Мене машина збила",
            "Я трохи не встигаю",
            "Я зараз працюю за фрілансом",
            "Скоро стартап окупиться",
            "Бабуся скоро пенсію отримає",
            "Гроші повернув твій банк, пише відмову, перевір номер картки",
            "Платіж на обробці",
            "Платіж відхилено, буду сваритися з банком",
            "Проводжаю сліпу бабусю через дорогу",
            "Зламала хребет",
            "Мої рибки спливли наверх, скоро похорон",
            "Я осліпла",
            "Біля мого будинку вбили дівчину, зараз усіх опитують",
            "Мене в армію забрали",
            "У мене кішка народжувала",
            "У мене дочка народила",
            "У мене молоко втекло",
            "У мене квартира згоріла",
            "Я недооцінила завдання",
            "Я недооцінила масштаб завдання",
            "Я зіткнулася з непередбачуваними складнощами",
        ]
        action = [
            "Я зроблю все",
            "Вишлю частину",
            "Постараюся",
            "Доберуся і все зроблю",
            "Зможу зробити все",
            "Я закінчу",
            "Я дороблю",
            "Я виправлю",
            "Узгоджу все",
            "Поясню все докладніше",
            "Зможу відіслати",
            "Зможу вирішити це питання",
            "Зможу доробити",
            "Зможу закінчити",
            "Зроблю переклад",
            "Перекладу",
            "Приїду",
            "Я особисто зустрінуся з тобою",
            "Я розберуся з цим",
            "Я розгребу це",
            "Вирішу все",
            "Відправлю",
            "Скину",
            "Доїду до дому",
            "Приїду додому",
            "Закрию це питання",
            "Спробую",
            "Давай зустрінемося",
            "Давай готівкою віддам",
            "Все зроблю",
            "Приїду з армії",
        ]
        date = [
            "зараз",
            "завтра",
            "завтра ввечері",
            "завтра вдень",
            "завтра вранці",
            "якнайшвидше",
            "якомога швидше",
            "нарешті",
            "трохи пізніше",
            "пізніше",
            "близько 2 діб",
            "наприкінці тижня",
            "наприкінці місяця",
            "наприкінці дня",
            "до кінця наступного тижня",
            "до завтра",
            "післязавтра",
            "ближче до вечора",
            "ближче до ранку",
            "з ранку",
            "завтра крайній термін",
            "на тижні",
            "через кілька днів",
            "скоро",
            "відразу",
            "зараз, протягом 3-4 днів",
        ]
        general = [
            "Хочу закрити питання якнайшвидше",
            "Сам уже втомився чекати",
            "Я б із радістю вже все зробив",
            "Сам у шоці, що так все вийшло",
            "Сам у шоці, що так все затягується",
            "Сам не очікував таких подій",
            "Треба скоріше вирішити це питання",
            "Треба вже закрити це питання",
            "Треба вже вирішити цю проблему",
            "Я, звичайно, дуже перепрошую, що так вийшло",
        ]
        generalwoman = [
            "Хочу закрити питання якнайшвидше",
            "Сама вже втомилася чекати",
            "Я б із радістю вже все зробила",
            "Сама в шоці, що так все вийшло",
            "Сама в шоці, що так все затягується",
            "Сама не очікувала таких подій",
            "Треба скоріше вирішити це питання",
            "Треба вже закрити це питання",
            "Треба вже вирішити цю проблему",
            "Я, звичайно, дуже перепрошую, що так вийшло",
        ]
        rnh = random.choice(hello)
        rnf = random.choice(fail)
        rna = random.choice(action)
        rnd = random.choice(date)
        rng = random.choice(general)
        if not args and self.config["sex"] == 1:
            args = random.choice(nameowoman)
        if not args and self.config["courtesy"] == 1:
            args = "Уважаемый начальник"
        if self.config["courtesy"] == 1:
            rnh = random.choice(hellovi)
        if not args:
            args = random.choice(nameo)
        if self.config["mysex"] == 1:
            rnf = random.choice(failwoman)
            rng = random.choice(generalwoman)
        await utils.answer(message, f"<b>{args}, {rnh}! {rnf}. {rna} {rnd}. {rng}.</b>")
