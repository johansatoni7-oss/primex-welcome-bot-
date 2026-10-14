
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]

async def welcome(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    change = update.chat_member
    if not change:
        return

    old = change.old_chat_member
    new = change.new_chat_member

    if old.status in ("left", "kicked") and new.status in (
        "member", "administrator"
    ):
        user = new.user

        await change.chat.send_message(
            f"👋 Welcome {user.first_name} to PrimeX Network!\n\n"
            "📜 GROUP RULES\n"
            "1. Respect all members.\n"
            "2. No spam or scam links.\n"
            "3. No unauthorized ads.\n"
            "4. Check prices before payment.\n"
            "5. Contact an admin for help."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        ChatMemberHandler(
            welcome,
            ChatMemberHandler.CHAT_MEMBER
        )
    )

    app.run_polling(
        allowed_updates=["chat_member", "message"]
    )

if __name__ == "__main__":
    main()
