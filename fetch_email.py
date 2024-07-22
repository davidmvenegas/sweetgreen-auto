import logging
import imaplib
import email
from email.header import decode_header

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_email_subject(email_user, email_password):
    imap_server = "imap.gmail.com"
    mailbox = "INBOX"

    logging.info("Connecting to the email server")
    try:
        # Connect to the email server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, email_password)
        mail.select(mailbox)
        logging.info("Logged in and mailbox selected")

        # Search for all emails
        status, messages = mail.search(None, "ALL")
        messages = messages[0].split()
        if not messages:
            logging.error("No emails found")
            return None

        logging.info("Fetching the latest email")
        # Fetch the latest email
        latest_email_id = messages[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Decode the email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        logging.info(f"Subject of the latest email: {subject}")
        return subject

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None


# Example usage
def run():
    logging.info("Starting email fetch process")
    try:
        email_user = "testuser"
        email_password = "test1234"
        subject = fetch_email_subject(email_user, email_password)
        if subject:
            logging.info(f"Latest email subject: {subject}")
        else:
            logging.error("Failed to retrieve the email subject")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
