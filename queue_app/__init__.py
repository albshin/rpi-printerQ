from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)

from queue_app.updater import update_printer
app.config.from_object('config')

@app.before_first_request
def init():
    update_printer()
    print("Setting up auto updater.")
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(update_printer, 'cron', minute='*/1')

@app.route('/')
def index():
    return render_template('index.html')
