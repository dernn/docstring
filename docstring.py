# ХОРОШИЙ КОД ДОКУМЕНТИРУЕТ САМ СЕБЯ
# или "хороший код будет понятен и без любой документации"

# «Могу ли я сделать код читабельнее без документации?»

import functools


# Рефакторинг кода
# Созданные атомарные функции можно будет легко переиспользовать в других местах,
# уменьшая общее количество написанного кода.
def catch_db_exceptions(wrapped):
    @functools.wraps(wrapped)
    def wrapper(*args, **kwargs):
        try:
            return wrapped(*args, **kwargs)
        except DatabaseException as exc:
            return 400, str(exc)

    return wrapper


def get_user(user_id):
    return db_conn.get('user', 'id=={}'.format(user_id))


def update_user_messages(user, message):
    user.messages = user.messages + '\n' + message['text']
    user.save()


async def process_message(message, do_async):
    data = {
        'text': message['text'],
        'user_id': message['user']['id']
    }
    if do_async:
        await db_conn.write_async('message', data)
    else:
        db_conn.write('message', data)


# Иногда важно описать, за что отвечают аргументы функции, или просто дать читателю больше контекста
# В таком случае докстроки можно разнести на несколько строк.
# На строчке с первыми кавычками при этом необходимо оставить краткую справку о функции:
@catch_db_exceptions
async def process_messages(messages, do_async):
    """Process each message and update them in the user info.

    You can use this function as a shortcut when you don't care
    about manually specifying parameters for the update and just
    want control over whether or not messages will be processed
    synchronously.

    Parameters
        ----------
        messages : list[Message]
            List of messages
        do_async : bool
            Whether to run the processing asynchronously
    """
    for message in messages:
        user = get_user(message['user']['id'])
        update_user_messages(user, message)
        await process_message(message, do_async)
        return 200, 'OK'


# Докстрока (docstring) для любого задокументированного объекта (модуля, класса, объекта класса или функции)
# доступна через специальный атрибут __doc__
print(functools.wraps.__doc__)
# Таким образом, даже работая из консоли, можно быстро получить документацию к коду
