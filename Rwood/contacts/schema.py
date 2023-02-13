from Rwood.contacts.models import Contact, ContactInformation, ContactAddressInformation, Reporters

from flask_marshmallow import Marshmallow


ma= Marshmallow()
class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        include_fk = True



class ContactInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactInformation
        include_fk = True


class ContactAddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactAddressInformation
        include_fk = True


class RwoodReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reporters
        


contact_schema= ContactSchema()
contacts_schema= ContactSchema(many=True)

contact_info_schema= ContactInfoSchema()
contacts_info_schema= ContactInfoSchema(many=True)

contact_address_schema= ContactAddressSchema()
contacts_address_schema= ContactAddressSchema(many=True)


rwood_report_schema= RwoodReportSchema()
rwoods_report_schema= RwoodReportSchema(many=True)