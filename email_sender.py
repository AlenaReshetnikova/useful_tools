import smtplib
from email.mime.text import MIMEText


def send_email(to, subject, message):
    msg = MIMEText(message, TEXT_TYPE, "utf-8")
    msg["From"] = FROM_EMAIL
    msg["Subject"] = subject
    msg["To"] = to
    smtp = smtplib.SMTP(SERVER, 587)
    smtp.starttls()
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


SERVER = "smtp.yandex.ru"
PORT = 465
LOGIN = ""  # put mail login here
PASSWORD = ""  # put password here
FROM_EMAIL = "player.flute@yandex.ru"
TEXT_TYPE = "plain"
if __name__ == "__main__":
    send_email("12345@mail.ru", "Папочке", "Любимому папочке, от лучшего програмиста ")
