from flask import render_template, request, Blueprint, flash, abort, redirect, url_for,jsonify
from Rwood.contacts.schema import(
    contact_address_schema, contacts_address_schema, contacts_schema,contact_schema, contact_info_schema, contacts_info_schema, rwood_report_schema,rwoods_report_schema
)

from Rwood import db
from Rwood.contacts.models import Contact, ContactInformation, ContactAddressInformation, Reporters
from Rwood.accounts.models import Account
from datetime import datetime
contacts = Blueprint('contacts', __name__)


@contacts.route("/contact")
def contacts_home():

    return render_template('contacts/home.html')




@contacts.route("/allcontacts")
def get_allcontacts():
    all_contacts= Contact.query.all()
    return contacts_schema.dump(all_contacts)

@contacts.route("/allcontacts/info")
def get_allcontacts_info():
    all_contacts_info= ContactInformation.query.all()
    return contacts_info_schema.dump(all_contacts_info)   


@contacts.route("/allcontact/address")
def get_allcontacts_address():
    all_contacts_address= ContactAddressInformation.query.all()
    return contacts_address_schema.dump(all_contacts_address)  


@contacts.route("/rwood_reporter/add", methods=["POST"] )
def add_rwood_reporters():
    name= request.json['name']
    email= request.json['email']

    rwood_reporters = Reporters.query.filter_by(name=name).first()
    if not rwood_reporters:
        

        new_reporters = Reporters(name=name,email=email)
        db.session.add(new_reporters)
        db.session.commit()
    else:
        return f"account_name with {name} is already present"

    
    

 
    
    return rwood_report_schema.jsonify(new_reporters)






@contacts.route("/contact/add", methods=["POST"])
def add_contact():

  
    name=request.json['name']
    account_name =request.json["account_name"]
    birthdate =request.json["birthdate"]
    birthdate_new = datetime.strptime(birthdate, '%Y-%m-%d').date()

    rest_birthday_email =request.json["rest_birthday_email"]
    contact_owner =request.json["contact_owner"]
    reports_to = request.json["reports_to"]
    department =request.json["department"]
    lead_source= request.json["lead_source"]
   

    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        return f'there is no account in {account_name} name'

    
    reporter = Reporters.query.filter_by(name= reports_to).first()
    print(reporter)
    if not reporter:
        return f"there is no rwood reported with this {reports_to}"
        print(reporter)

    new_contact=Contact(
        name=name,account_name=account_name, birthdate=birthdate_new,rest_birthday_email= rest_birthday_email, contact_owner=contact_owner, department=department, lead_source=lead_source,reports_to= reports_to,
        account_id=account.id, report_id = reporter.id
        
        )

    db.session.add(new_contact)
    db.session.commit()
    return contact_schema.jsonify(new_contact)


@contacts.route('/contactinfo/add', methods=['POST'])
def add_contactinfo():
    email= request.json["email"]
    mobile= request.json["mobile"]
    phone= request.json["phone"]
    home_phone= request.json["home_phone"]
    other_phone= request.json["other_phone"]
    fax= request.json["fax"]
    name = request.json["name"]

    contact = Contact.query.filter_by(name=name).first()
    if not contact:
        flash('there is no contact in the name')

    new_contactinfo= ContactInformation(
        email=email,mobile=mobile, phone=phone, home_phone=home_phone, other_phone=other_phone, fax=fax, contact_id = contact.id
    )


    db.session.add(new_contactinfo)
    db.session.commit()

    return contact_info_schema.jsonify(new_contactinfo)








@contacts.route('/contact/address/add', methods=['POST'])
def add_contact_address():
    name = request.json['name']
    mailing_address= request.json['mailing_address']
    contact = Contact.query.filter_by(name=name).first()
    if not contact:
        flash('there is no contact in the name')

    new_contact_address= ContactAddressInformation(mailing_address= mailing_address, contact_id= contact.id)

    db.session.add(new_contact_address)
    db.session.commit()

    return contact_address_schema.jsonify(new_contact_address)









@contacts.route('/contact/update/<id>', methods=['PUT'])
def update_contact(id):

    update_contact = Contact.query.get(id)
    if not update_contact:
        return jsonify({f"message": "update_account not found"}), 404

    name=request.json['name']
    account_name =request.json["account_name"]
    birthdate =request.json["birthdate"]
    birthdate_new = datetime.strptime(birthdate, '%Y-%m-%d').date()

    rest_birthday_email =request.json["rest_birthday_email"]
    contact_owner =request.json["contact_owner"]
    reports_to = request.json["reports_to"]
    department =request.json["department"]
    lead_source= request.json["lead_source"]
   

    account = Account.query.filter_by(account_name=account_name).first()
    if not account:
        return f'there is no account in {account_name} name'

    reporter = Reporters.query.filter_by(name= reports_to).first()
    print(reporter)
    if not reporter:
        return f"there is no rwood reported with this {reports_to}"
       

    update_contact.name= name
    update_contact.account_name=account_name
    update_contact.birthdate= birthdate
    update_contact.birthdate_new= birthdate_new
    update_contact.rest_birthday_mail= rest_birthday_email
    update_contact.contact_owner= contact_owner

    update_contact.reports_to= reports_to
    update_contact.department= department
    update_contact.lead_source= lead_source
    update_contact.account_id= account.id
    update_contact.report_id= reporter.id
    db.session.commit()

    return contact_schema.jsonify(update_contact)




@contacts.route('/contact/updateinfo/<id>', methods=['PUT'])
def update_contactinfo(id):
    contact_info= ContactInformation.query.get(id)
    if not contact_info:
        return f'There is no contact_info in this ID-{id}'

    
    email= request.json["email"]
    mobile= request.json["mobile"]
    phone= request.json["phone"]
    home_phone= request.json["home_phone"]
    other_phone= request.json["other_phone"]
    fax= request.json["fax"]
    name = request.json["name"]

    contact = Contact.query.filter_by(name=name).first()
    if not contact:
        flash('there is no contact in the name')


    contact_info.email=email
    contact_info.mobile=mobile
    contact_info.phone=phone
    contact_info.home_phone= home_phone
    contact_info.other_phone= other_phone
    contact_info.fax= fax
    contact_info.contact_id= contact.id
    db.session.commit()
    


    return contact_info_schema.jsonify(contact_info)


@contacts.route('/contact/update/address/<id>', methods=['PUT'])
def update_contact_address(id):
    update_address= ContactAddressInformation.query.get(id)
    if not update_address:
        return jsonify(f'there is no address info with this ID-{id}')

    name = request.json['name']
    mailing_address= request.json['mailing_address']

    contact = Contact.query.filter_by(name=name).first()
    if not contact:
        flash('there is no contact in the name')    

    update_address.name= name
    update_address.mailing_address= mailing_address
    db.session.commit()
    return contact_address_schema.jsonify(update_address)



@contacts.route('/contact/delete/<id>', methods=['DELETE'])
def delete_contact(id):
    contact_delete= Contact.query.get(id)
    if not contact_delete:
        return jsonify(f' There is no contact with in the given query ID-{id}')

    db.session.delete(contact_delete)
    db.session.commit()

    return jsonify(f"ID- {id} with contact has been deleted successfully")


@contacts.route('/contactinfo/delete/<id>', methods=['DELETE'])
def delete_contact_info(id):
    contactinfo_delete= ContactInformation.query.get(id)
    if not contactinfo_delete:
        return jsonify(f' There is no contact information with in the given query ID-{id}')

    db.session.delete(contactinfo_delete)
    db.session.commit()

    return jsonify(f"ID- {id} with contact information has been deleted successfully")



@contacts.route('/contactaddress/delete/<id>', methods=['DELETE'])
def delete_contact_address(id):
    contactaddress_delete= ContactAddressInformation.query.get(id)
    if not contactaddress_delete:
        return jsonify(f' There is no contact address with in the given query ID-{id}')

    db.session.delete(contactaddress_delete)
    db.session.commit()

    return jsonify(f"ID- {id} with contact address has been deleted successfully")