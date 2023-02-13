

from Rwood import db 

import datetime


class Reporters(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(length=200))
    email= db.Column(db.String(length=100))
    contact= db.relationship('Contact',backref= "reporters")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Contact(db.Model):
     id=db.Column(db.Integer(), primary_key=True)
     name=db.Column(db.String(length=100))
     account_name=db.Column(db.String(length=100))
     birthdate=db.Column(db.Date)
     
     rest_birthday_email=db.Column(db.String(length=100))
     contact_owner=db.Column(db.String(length=100))
     reports_to=db.Column(db.String(length=100))
     department=db.Column(db.String(length=100))
     last_stay_in_touch_save_date= db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

     lead_source=db.Column(db.String(length=100))
     account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
     report_id = db.Column(db.Integer, db.ForeignKey('reporters.id'))

     contact_info= db.relationship('ContactInformation', backref='contact')
     contact_address=db.relationship('ContactAddressInformation', backref='contact')
     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


    #  @property
    #  def next_birthday(self):
    #     today = datetime.datetime.now()
    #     next_birthday = self.birthdate.replace(year=today.year)
    #     if next_birthday < today:
    #         next_birthday = next_birthday.replace(year=today.year + 1)
    #     return next_birthday

     




class ContactInformation(db.Model):
     id=db.Column(db.Integer(), primary_key=True)
     email=db.Column(db.String(length=100))
     mobile=db.Column(db.String(length=100))
     phone=db.Column(db.String(length=100))
     home_phone=db.Column(db.String(length=100))
     other_phone=db.Column(db.String(length=100))
     fax=db.Column(db.String(length=100))
     contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class ContactAddressInformation(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    mailing_address=db.Column(db.String(length=100))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)





