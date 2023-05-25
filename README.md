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

Clone this repository and fill all the necessary information into the docker-compose.yml file. 
Call `docker compose up -d` and voilà, you're done! 
