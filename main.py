from datetime import datetime
import os

from apscheduler.schedulers.background import BlockingScheduler
import dotenv

from enums import EnvironmentVariable
import mail.mailer as mailer

dotenv.load_dotenv()

scheduler = BlockingScheduler()
trigger_date_time = datetime.now().replace(
    hour=int(os.getenv(EnvironmentVariable.TRIGGER_HOUR)),
    minute=0,
    second=0,
    microsecond=0,
)
scheduler.add_job(
    mailer.generate_email, "interval", days=1, start_date=trigger_date_time
)
# scheduler.add_job(mailer.generate_email)
scheduler.add_job(mailer.run_mails)
scheduler.start()
