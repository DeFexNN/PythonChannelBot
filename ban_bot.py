from telegram import Bot, Update
from telegram.ext import Application, CommandHandler
import asyncio

# Вставьте ваш токен бота здесь
BOT_TOKEN = ''
CHANNEL_USERNAME = None  # Юзернейм канала будет установлен пользователем

async def is_admin(bot, chat_id, user_id):
    member = await bot.get_chat_member(chat_id, user_id)
    return member.status in ['administrator', 'creator'] and member.can_restrict_members

async def set_channel(update, context):
    global CHANNEL_USERNAME
    try:
        args = context.args
        if not args:
            await update.message.reply_text("Укажите юзернейм канала (например, @mychannel).")
            return

        CHANNEL_USERNAME = args[0]
        await update.message.reply_text(f"Юзернейм канала установлен: {CHANNEL_USERNAME}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")

async def ban_user(update, context):
    try:
        if CHANNEL_USERNAME is None:
            await update.message.reply_text("Сначала установите юзернейм канала с помощью команды /setchannel.")
            return

        args = context.args
        if not args:
            await update.message.reply_text("Укажите Telegram ID пользователя, которого нужно забанить.")
            return

        user_id = int(args[0])

        # Проверка прав администратора
        bot = Bot(token=BOT_TOKEN)
        if not await is_admin(bot, CHANNEL_USERNAME, update.effective_user.id):
            await update.message.reply_text("У вас нет прав администратора для бана пользователей.")
            return

        # Бан пользователя
        await bot.ban_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

        await update.message.reply_text(f"Пользователь с ID {user_id} успешно забанен!")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")

async def unban_user(update, context):
    try:
        if CHANNEL_USERNAME is None:
            await update.message.reply_text("Сначала установите юзернейм канала с помощью команды /setchannel.")
            return

        args = context.args
        if not args:
            await update.message.reply_text("Укажите Telegram ID пользователя, которого нужно разбанить.")
            return

        user_id = int(args[0])

        # Проверка прав администратора
        bot = Bot(token=BOT_TOKEN)
        if not await is_admin(bot, CHANNEL_USERNAME, update.effective_user.id):
            await update.message.reply_text("У вас нет прав администратора для разбана пользователей.")
            return

        # Разбан пользователя
        await bot.unban_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

        await update.message.reply_text(f"Пользователь с ID {user_id} успешно разбанен!")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")

def main():
    # Настройка бота
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем команду /setchannel
    application.add_handler(CommandHandler("setchannel", set_channel))
    # Добавляем команду /ban
    application.add_handler(CommandHandler("ban", ban_user))
    # Добавляем команду /unban
    application.add_handler(CommandHandler("unban", unban_user))

    # Запускаем бота
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nБот остановлен.")
