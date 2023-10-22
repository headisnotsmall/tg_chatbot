import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram bot token (replace with your actual bot token)
TOKEN = "your_token"

# Store the last known public IP address
last_public_ip = ""

# Function to get the public IP address
def get_public_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    data = response.json()
    return data["ip"]

# Function to send the IP address when the /getip command is used
def send_ip(update: Update, context: CallbackContext):
    global last_public_ip
    current_public_ip = get_public_ip()

    if current_public_ip != last_public_ip:
        last_public_ip = current_public_ip
        update.message.reply_text(f"Your current public IP address is: {current_public_ip}")
    else:
        update.message.reply_text("Your public IP address has not changed.")

# Main function to start the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("getip", send_ip))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
