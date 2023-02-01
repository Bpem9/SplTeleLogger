# SplTeleLogger

Hello and welcome to repository of telegram logging python script within the Splunk "okroshka" app.  
Script is based on "telethon==1.26.1" python library. 

0.**A pile of absolutly important information**

Some important credentials collected to main script from environmental variables provided with load_dotenv() and .env file, that was deleted for security reasons. So It is necessary for tester to create ```.env``` file near ```config.py``` file, and it must include all essential credentials you get from:   
• API_ID and API_HASH - Telegram API credentials  
• SESSION_STRING - Telegram session name, using for login to telegram account without SMS authentification. Obtainable with telethon lib by theese <a name="https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions">Instructions</a>  
• TEST_CHANNEL_NAME - Well, just the name of the public channel planning to be tested

1.**Asked questions**  
**"How collected data can help the Security team in case of Security Incidents?"**
- Collected data helping security team to recieve essential information about the incidents like so: its time and date, guilty user/client id, that will be useful for the investigation to go on and reduce the consequences of theese incidents and prevent them from happening in future.  
**"Can we collect any additional data to enrich collected events?"**
- Definitely, yes. As a developer, I'm deciding what information I'll collect from telegram app. I guess, logs from other important security apps are customizable too.  
**"What uses cases / correlations / alerts the Security team can make using the collected data?"**
- There are many correlations might be installed, for example: correlation between amount of failed loggings in account. Or correlation of amount of messages at a time period. We can even develop an alert that starts each time created message(in case we are monitoring telegram chat/channel) includes some pre-setted regex expressions or files.  
**"Any additional thoughts you consider relevant"**
- The IT Security is a big industry with many different details, themes, scopes and the fact that information leaks are still happening means that there always some space to improve.   
