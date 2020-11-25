class Translation(object):
    START_TEXT = """<b>Hello, My Name Is 𝗛𝗢𝗧𝗦𝗧𝗔𝗥 𝗙𝗟𝗜𝗫 𝗕𝗢𝗧 😎.\n\nI'm A 𝗛𝗢𝗧𝗦𝗧𝗔𝗥 𝗨𝗣𝗟𝗢𝗔𝗗 𝗕𝗢𝗧 Which Can Download Videos From Hotstar\n\nSend Me A 𝗩𝗮𝗹𝗶𝗱 <u>𝗛𝗼𝘁𝘀𝘁𝗮𝗿 𝗨𝗥𝗟 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗟𝗶𝗻𝗸</u> & I'll Upload It To Telegram As A Streamble Video Or Document, See /Help For More Information\n\n❌ 𝗗𝗥𝗠 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦 Are Impossible To Download, Only Free Hotstar Contents Can Be Downloaded With This Bot.\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots For More Exciting Bots</b>"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>Plan:</b> Free User!. \n<b>Unlimited Plan</b>"
    FORMAT_SELECTION = "<b>📌 Thumbnail Link :</b> <b><a href='{}'>Set Temporary Thumbnail</a></b> \n\nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\n\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """\n𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 © @FlixBots @Entclass"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗜𝗻𝘁𝗼 𝗠𝘆 𝗦𝗲𝗿𝘃𝗲𝗿 𝗡𝗼𝘄 ⚠️</b> \n\n<code>Please Wait Uploading Will Start Soon...</code>"
    UPLOAD_START = "<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗧𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗡𝗼𝘄 📁..</b>"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "<b>Downloaded in {} seconds.<b/>\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗨𝘀𝗶𝗻𝗴 𝗧𝗵𝗶𝘀 𝗦𝗲𝗿𝘃𝗶𝗰𝗲, 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBot & @Entclass 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗔𝗺𝗮𝘇𝗶𝗻𝗴 𝗕𝗼𝘁𝘀</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>Downloaded in {} seconds.</b> \n<b>Thanks For Using This Free Service, Subscribe To @FlixBots & @Entclass For More Amazing Bots</b> \n<b>Uploaded in {} seconds.</b>"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗩𝗶𝗱𝗲𝗼/𝗙𝗶𝗹𝗲 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗜𝘀 𝗦𝗮𝘃𝗲𝗱. 𝗧𝗵𝗶𝘀 𝗜𝗺𝗮𝗴𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗨𝘀𝗲𝗱 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗡𝗲𝘅𝘁 𝗨𝗽𝗹𝗼𝗮𝗱 📁."
    DEL_ETED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗖𝗹𝗲𝗮𝗿𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ❌."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media Cleared Succesfully ❌."
    SAVED_RECVD_DOC_FILE = "𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 📁."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: <a href='https://t.me/SpEcHlDe/599'>{}</a>
Expires on: {}"""
    HELP_USER = """<b><u>🍁 𝗛𝗼𝘄 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗛𝗼𝘁𝘀𝘁𝗮𝗿 𝗙𝗶𝗹𝗲𝘀 𝗙𝗿𝗼𝗺 𝗕𝗼𝘁 🍁</u></b>
 
1. <b>Send Custom Thumbnail if required (It Will Be Saved Permanently) 📫

2. Send Your Hotstar link & select desired option.</b>

<b>𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots For More Exciting Bots</b>"""
    BANNED_USER_TEXT = """Hi **{}!!!**, Congratulations 😂 You Are Now Banned"""
    ABOUT_USER = """<b>○ My Name : 𝗛𝗢𝗧𝗦𝗧𝗔𝗥 𝗙𝗟𝗜𝗫 𝗕𝗢𝗧</b>
<b>○ Creator :</b> <a href='https://t.me/iggie/'>Iggie</a>
<b>○ Credits :</b> <code>Everyone in this journey</code>
<b>○ Language :</b> <a href='https://docs.pyrogram.org/'>Python3</a>
<b>○ Library :</b> <code>Pyrogram asyncio 0.16.1</code>
<b>○ Source Code :</b> <a href='https://t.me/NOSOURCECODE/'>👉 CLICK HERE 👈</a>
<b>○ Server :</b> <code>Heroku</code>
<b>○ Build Status :</b> <code>V5 [+0.4]</code>"""
