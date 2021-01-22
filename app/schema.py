from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length

class CreditCardShema(Schema):
    CreditCardNumber = fields.Str(required=True)
    CardHolder = fields.Str(required=True)
    ExpirationDate = fields.DateTime(required=True,format='%m/%y')
    SecurityCode= fields.Str(required=True,validate=Length(equal=3))
    Amount = fields.Decimal(required=True)

    @validates('CreditCardNumber')
    def checker(self,value):
        if value.isdigit():
            validatelist=[]
            for i in value:
                validatelist.append(int(i))
            for i in range(0,len(value),2):
                validatelist[i] = validatelist[i]*2
                if validatelist[i] >= 10:
                    validatelist[i] = validatelist[i]//10 + validatelist[i]%10
            if sum(validatelist)%10 != 0:
                raise ValidationError("this is not valid card no")
        else:
            raise ValidationError("this is not valid card no")



    @validates('ExpirationDate')
    def is_not_in_past(self,value):
        now = datetime.now()
        if value < now:
            raise ValidationError("past date")
            
    @validates('SecurityCode')
    def is_num(self,value):
        if not value.isdigit():
            raise ValidationError("not a valid no")

    @validates('Amount')
    def is_positive(self,n):
        if not n > 0:
            raise ValidationError("Not a positive number") 



