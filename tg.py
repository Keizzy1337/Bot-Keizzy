from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Ваша дата обновления
update_date = "12.12.2024"
clumsy_kwizzy = "Твой Clumsy - скоро..."
kwizzysaturn = "Скачать Saturn Mod - скоро..."
channel_url = "https://t.me/+XsV7HFU6Nw83YzBi"

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Узнать дату обновы", callback_data='get_date')],
        [InlineKeyboardButton("Скачать Clumsy", callback_data='clumsy')],
        [InlineKeyboardButton("Скачать SaturnMod", callback_data='kwizzy_saturn')],
        [InlineKeyboardButton("Перейти в MetroShop по низким ценам", url=channel_url)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Добро пожаловать! Нажмите любую кнопку ниже', reply_markup=reply_markup)

# Обработчик нажатий на кнопки
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'get_date':
        await query.edit_message_text(text=f"Дата: {update_date}")
    elif query.data == 'clumsy':
        await query.edit_message_text(text=f"{clumsy_kwizzy}")
    elif query.data == 'kwizzy_saturn':
        await query.edit_message_text(text=f"{kwizzysaturn}")

# Основной метод запуска бота
def main() -> None:
    # Ваш токен бота
    application = ApplicationBuilder().token("7668833815:AAGFDBuJo8YFoCz8uwiIX1C7dROoIyoxZQY").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
