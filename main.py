import time

from apscheduler.schedulers.background import BackgroundScheduler
import dotenv

import mailer

dotenv.load_dotenv()


scheduler = BackgroundScheduler()
# scheduler.add_job(mailer.generate_email, trigger="interval", minutes=2)
scheduler.add_job(mailer.generate_email)
scheduler.add_job(mailer.run_mails)
scheduler.start()
time.sleep(5)
