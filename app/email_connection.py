from imap_tools import MailBox, AND
from setup.config import Config
from db.connection import Session, engine
from db.models import EmailStore
from datetime import datetime

session = Session(bind=engine)

def access_inbox():
    with MailBox(Config.EMAIL_HOST).login(Config.EMAIL_USER, Config.EMAIL_PASS, Config.EMAIL_FOLDER) as mb:

        existing_email_array = []

        for msg in mb.fetch(AND(seen=False), mark_seen=True, reverse=False):
            source_email = msg.from_

            if source_email == Config.SOURCE_EMAIL:

                target_email = msg.to[0]
                print(target_email)

                if target_email not in existing_email_array:

                    email_exists = check_email_exists(target_email)

                    if email_exists:
                        print("Email id duplicated")
                        existing_email_array.append(target_email)
                    else:
                        create_record(target_email, msg.date)

                else:
                    print("Email id duplicated")

        print("Process completed")

def split_email(email: str):
    return email.split('@')

def check_email_exists(email: str):
    return session.query(EmailStore).filter(EmailStore.email_id == email).first() is not None

def create_record(target_email: str, date):
    email_detail = split_email(target_email)

    new_email_info = EmailStore(
        email_id=target_email,
        username=email_detail[0],
        domain_name=email_detail[1],
        received_date=date,
        created_date=datetime.now()
    )

    session.add(new_email_info)
    session.commit()