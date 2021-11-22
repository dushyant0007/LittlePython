import smtplib
import datetime as dt
import random

MY_EMAIL = "rajkumarindia294@gmail.com"
MY_PASSWORD = "12345!@#$%"

now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.weekday())

with open("email.txt") as e_file:
    all_emails = e_file.readlines()

    with open("quotes.txt") as q_file:
        all_quotes = q_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    for email in all_emails:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject : Motivation \n\n {quote} "
            )
