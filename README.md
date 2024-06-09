# EmailRep
 
A Basic CLI email interaction tool utilizing the schedule, smtplib, imaplib & email python modules, allowing you to read emails from a specific inbox as well as send them to a specified destination. 

## Installation & Configuration

1. Clone the repository:
   ```
   git clone https://github.com/Original-Lily/EmailRep.git
   ```

2. For security reasons, your email and password are kept outside of this script, so ensure you set environment variables for these values:
   ```
   export SENDER_EMAIL="YourEmail@example.com"
   export EMAIL_PASSWORD="YourPassword"
   ```

3. Configure Email Server Settings, to do this, replace the following placeholders in the script with your actual email details:
   ```
   smtp.example.com: Your email provider's SMTP server.
   imap.example.com: Your email provider's IMAP server.
   ```

4. Run the program via:
   ```
   python main.py
   ```
   
# Usage

   ```
   Do you want to (R)ead emails or (S)end an email? (R/S): S
   Enter recipient's email: recipient@example.com
   Enter subject: Test Email
   Enter email content: This is a test email.
   Email sent successfully

   Do you want to (R)ead emails or (S)end an email? (R/S): R
   From: sender@example.com
   Subject: Meeting Reminder
   Date: Mon, 8 Jun 2023 10:00:00 -0700
   Body: This is a reminder for our meeting.
   ```
