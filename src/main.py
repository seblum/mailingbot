import os
from .mail_handler import MailHandler


def main():
    mail_handler = MailHandler(email_sender=os.getenv("EMAIL_SENDER"),email_password=os.getenv("EMAIL_PASSWORD"),email_receiver=os.getenv("EMAIL_RECEIVER"))
    mail_handler.send_html_email(subject="[Update] Bilanzen",html_path=os.getenv("HTML_PATH"))


if __name__ == "__main__":
    main()