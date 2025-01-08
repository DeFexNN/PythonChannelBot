# Telegram Ban Bot

This Telegram bot allows channel administrators to ban and unban users by their Telegram ID. The bot supports the following features:

1. **Channel Setup**: The `/setchannel <channel_username>` command allows you to set the channel username where the bot will operate.
2. **Ban Users**: The `/ban <user_id>` command allows you to ban a user by their Telegram ID.
3. **Unban Users**: The `/unban <user_id>` command allows you to unban a user by their Telegram ID.
4. **Admin Rights Check**: The bot checks if the user executing the command is an administrator of the channel with ban/unban rights.

The bot must be added as an administrator of the channel to work correctly.

## Installation

1. **Get the bot token** from @BotFather on Telegram.
2. **Insert the bot token** into the `BOT_TOKEN` variable in the `ban_bot.py` file.
3. **Add the bot as an administrator** to your channel.

## Dependencies

1. Open the command line.
2. Navigate to the bot's folder.
3. Run the command: `python dependencies.py`.
4. Wait for the message "Dependencies installed successfully."

## Running the Bot

1. Open the command line.
2. Navigate to the bot's folder.
3. Run the command: `python ban_bot.py`.
4. Wait for the message "Bot started."

## Usage

1. **Set the channel username**:
    ```
    /setchannel <channel_username>
    Example: /setchannel @mychannel
    ```

2. **Ban a user**:
    ```
    /ban <user_id>
    Example: /ban 123456789
    ```

3. **Unban a user**:
    ```
    /unban <user_id>
    Example: /unban 123456789
    ```

4. **How to get a user's ID**:
    - Forward the user's message to the bot @getmyid_bot.
    - Use the bot @username_to_id_bot.

## Stopping the Bot

1. Press `Ctrl+C` in the command line.
2. Wait for the message "Bot stopped."

## Notes

- The bot must be an administrator of the channel.
- You need administrator rights to ban and unban users.
- In case of an error, the bot will report the reason.
- The bot checks if you have administrator rights to execute commands.
