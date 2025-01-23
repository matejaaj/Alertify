# Alertify

Script is designed to check if a file is available at a specified URL and send an email notification if the file is found. It is **mandatory** to  know the exact URL of a file. For example, I used it for student scholarship application results since it's location followed a specific pattern.


## How to use

### 1. Prepare the configuration file 
Open the `config.ini`file and fill it out with your details. Below is a sample configuration:
```ini
[SMTP]
server = smtp.gmail.com  # SMTP server for sending emails
port = 587               # Port for SMTP server
email = YOUR_EMAIL       # Your email address (used for sending notifications)
password = YOUR_PASSWORD # Your email password or app-specific password

[URL]
file_path = url.txt      # Path to a file containing the URL to be monitored

[RECIPIENT]
email = RECIPIENT_EMAIL  # Email address where notifications will be sent
subject = File Found!    # Subject of the notification email
body = The file is available at:  # Email body prefix
```

**Important**: For Gmail, you have to use app-specific password if two factor authentication is enabled.

### 2. Add the URL to `url.txt`
**Note**:  URLs are stored in `url.txt` because certain URLs (e.g those in Serbian Cyrilic) may not parse corectly when included in `config.ini` file.

### 3. Set up periodic execution.
To make the script run periodically, you need to set up a task scheaduler based on your operating system:
- **Windows**: Use Task Scheduler. Create a new task and configure it to run the script (`.py` file) at your desired interval.
- **Linux**: Use `cron`. Open the crontab with `crontab -e` and add a line like this to scheadule the script:
```bash
*/30 * * * * /usr/bin/python3 /path/to/script.py

