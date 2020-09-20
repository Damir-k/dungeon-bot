import discord
from discord.ext import commands

general = '''```Префикс: >

Общедоступные команды:
    wow - чтобы стать клоуном
    coinflip - орел либо решка
    ping - узнать пинг бота
    help (категория) - показать информацию по категориям
    age - узнать как долго ты на сервере (не учитывает перезаходы)

Категории: General, ModOnly, DevOnly```
'''

devonly = '''```Префикс: >

Модуль DevOnly:
    load (модуль) - загрузить модуль (Эту команду невозможно отключить)
    unload (модуль) - отключить модуль и все его команды
    reload (модуль) - перезагрузить модуль и все его команды

Заметка: команда reload может перезагрузить модуль DevOnly в том числе```
'''

modonly = '''```Префикс: >

Модуль ModOnly:
    clear (количество) - удалить последние (количество) сообщений
    kick @чувачок (причина) - кик
    ban @чувачок (причина) - бан
    unban имячувачка#1234 - разбанить```
'''

class Help(commands.Cog):

    def __init__(self, client):
        client.remove_command("help")
        self.client = client

    @commands.command(aliases=["helpme"])
    async def help(self, ctx, category="general"):
        category = category.lower()
        if category == "general":
            await ctx.send(general)
        elif category == "modonly":
            await ctx.send(modonly)
        elif category == "devonly":
            await ctx.send(devonly)


def setup(client):
    client.add_cog(Help(client))