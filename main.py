import os, time, schedule, smtplib, imaplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

def send_email(receiver_email, subject, body):
    sender_email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("EMAIL_PASSWORD")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.example.com", 587)  #Note: replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, sender_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

def read_emails():
    sender_email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("EMAIL_PASSWORD")

    try:
        mail = imaplib.IMAP4_SSL("imap.example.com")  #Note: replace with your IMAP server
        mail.login(sender_email, password)
        mail.select("inbox")
        date = (datetime.now() - timedelta(1)).strftime("%d-%b-%Y") #Note: last 24 hours
        result, data = mail.search(None, f'(SINCE "{date}")')

        if result == "OK":
            for num in data[0].split():
                result, msg_data = mail.fetch(num, "(RFC822)")
                if result == "OK":
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])
                            email_subject = msg["subject"]
                            email_from = msg["from"]
                            email_date = msg["date"]
                            email_body = ""
                            if msg.is_multipart():
                                for part in msg.walk():
                                    if part.get_content_type() == "text/plain":
                                        email_body = part.get_payload(decode=True).decode()
                                        break
                            else:
                                email_body = msg.get_payload(decode=True).decode()
                            print(f"From: {email_from}")
                            print(f"Subject: {email_subject}")
                            print(f"Date: {email_date}")
                            print(f"Body: {email_body}")
                            print("-" * 50)
        mail.logout()
    except Exception as e:
        print(f"Error: {e}")

def prompt_send_email():
    receiver_email = input("Enter recipient's email: ")
    subject = input("Enter subject: ")
    body = input("Enter email content: ")
    send_email(receiver_email, subject, body)

def main():
    while True:
        choice = input("Do you want to (R)ead emails or (S)end an email? (R/S): ").strip().upper()
        if choice == "R":
            read_emails()
        elif choice == "S":
            prompt_send_email()
        else:
            print("Invalid choice, please choose again.")

#Example: schedule a job daily at a specific time
schedule.every().day.at("08:00").do(lambda: send_email("receiver_email@example.com", "Daily Report", "This is the daily report."))
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
        main()