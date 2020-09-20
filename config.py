TOKEN = "NzU2NTE4ODUzMDcyMTI1OTgy.X2TBFg.sS2J4FZW4I3c9hur4H5jD76Sw_4"

GENERAL = '''Префикс: >

Список всех команд: 
wow - чтобы стать клоуном;
coinflip - орел либо решка
ping - узнать пинг бота
helpme - показать это сообщение
age - узнать как долго ты на сервере (не учитывает перезаходы)

Используйте 
help <Category>
для более подробного описания каждого раздела 
'''
MOD = '''Префикс: >

Только для модеров:
clear (количество) - удалить последние (количество) сообщений
kick @чувачок (причина) - кик
ban @чувачок (причина) - бан
unban имячувачка#1234 - разбанить
'''


def help(category=None):
    if category == "general":
        return GENERAL
    if category == "mod":
        return MOD