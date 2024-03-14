# ХОРОШИЙ КОД ДОКУМЕНТИРУЕТ САМ СЕБЯ
# или "хороший код будет понятен и без любой документации"

# Пример «спагетти-кода», в котором одна функция выполняет несколько задач
async def process_messages(messages, do_async):
    for message in messages:
        try:
            user_id = message['user']['id']
            user = db_conn.get('user', 'id=={}'.format(user_id))
            user.messages = user.messages + '\n' + message['text']
            user.save()
            if do_async:
                await db_conn.write_async(
                    'message',
                    {'text': message['text'], 'user_id': message['user']['id']}
                )
            else:
                db_conn.write(
                    'message',
                    {'text': message['text'], 'user_id': message['user']['id']}
                )
            return 200, 'OK'
        except DatabaseException as exc:
            return 400, str(exc)