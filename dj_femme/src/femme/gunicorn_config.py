
import os
import multiprocessing
from datetime import datetime


# Function to generate error log filename based on the current date
def generate_error_log_filename():
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join('logs', f'gunicorn_error_{today}.log')


def generate_access_log_filename():
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join('logs', f'gunicorn_access_{today}.log')


bind = '172.22.0.2:8000'
workers = 3
worker_class = 'gevent'
timeout = 30  # Timeout for worker processes in seconds

# Error logging
errorlog = generate_error_log_filename()
loglevel = 'debug'
# Access logging
accesslog = generate_access_log_filename()  # Path to the access log file
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'  # Access log format

# Graceful reloading
reload = True  # Enable automatic reloading of workers on code changes
max_requests = 1000  # Maximum number of requests a worker will process before restarting
