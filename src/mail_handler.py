import os
from email.message import EmailMessage
import ssl
import smtplib
from typing import List

EMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_SMTP_PORT = 465


class MailHandler:
    html_templates_path = "html-templates/"

    def __init__(self, email_sender:str, email_password :str, email_receiver: List[str], format: str = "html") -> None:
        self.email_sender = email_sender
        self.email_password = email_password
        self.email_receiver = email_receiver
        self.format = format
        self.subject = None
        self.body = None

    def _send_email(
        self,
    ) -> None:
        """
        Sends an email with the specified parameters.

        Args:
            sender (str): The email address of the sender.
            password (str): The password of the sender's email account.
            receivers (List[str]): A list of receiver email addresses.
            subject (str): The subject of the email.
            body (str): The body of the email.
            format (str): The format of the email body.
            attachment_path (str): The path to the file to be attached (default is None).
        """
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_receiver
        em["Subject"] = self.subject
        em.set_content(self.body, self.format)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT, context=context
        ) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())

        print("Email sent successfully!")


    def send_html_email(
        self, subject:str, html_path: str = None
    ) -> None:

        self.subject = subject
        self.body
        html_path

        if not all([self.email_sender, self.email_password, self.email_receiver]):
            raise ValueError("Email sender, password, and receiver email must be set.")

        html_file_path = os.path.join(html_path)

        # Read the HTML template from the file
        with open(html_file_path, "r") as file:
            self.body = file.read()


        self._send_email()
