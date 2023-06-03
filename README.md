# the-friendly-mailer

This masterpiece is able to give someone you love a nice headstart into the day. 
It sends a mail with...
- a nice greeting
- a weather report for the next 5 days
- funny gifs of animals
on a daily basis. 

# Set it up!
You need a machine which runs permanently in order to send mails every day. 
I use my raspberry I already had up and running. 

Configure a fresh mail account you want to use as a sender and get the SMTP information of the provider. 

Create an `.env` file in the project root with the following content (fill your specs):
````
AUTHOR = author
LOG_LEVEL = INFO
EMAIL_USERNAME_STRATO = username
EMAIL_PASSWORD_STRATO = password
EMAIL_SENDER_ADDRESS = account@yourmailprovider.com
TRIGGER_HOUR = 8
````

Create a content.json file in the config dir with the following content (fill your specs):
```json
{
  "name": "Linus",
  "email": "receiver@anothermailprovider.com",
  "subjects": [
    "Your subject 1",
    "Your subject 2"
  ],
  "greetings": [
    "Hello my love,",
    "What's up mate?!",
    "Ho ho ho!"
  ],
  "bodies": [
    "You are just the best!", 
    "You rock! \n\n So just rock on! =)",
    "You are the sunshine that brightens my world and I can't imagine a life without your love. "
  ],
  "closings": [
    "With love\nAngelina",
    "Love\nAngelina"
  ]
}
```

Clone this repository and fill all the necessary information into the docker-compose.yml file. 
Call `docker compose up -d` and voilà, you're done! 
