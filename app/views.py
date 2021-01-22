from app import app
from flask import abort
from app.schema import CreditCardShema
from app.payment_services import ProcessPayment
import json


creditcardschema= CreditCardShema()

@app.route("/",methods=["POST"])
def index():
    errors = creditcardschema.validate(request.get_json())
    
    if errors:
        abort(400, str(errors))
    else:
        req=request.get_json()
        amount=req.get('Amount')
        cardno=req.get('CreditCardNumber')
        cardholder=req.get('CardHolder')
        exdate=req.get('ExpirationDate')
        try:
            print("payment started")
            status = ProcessPayment(amount,cardholder)
            print("payment processing started")
            payment_sccess = status.payment()
            if payment_sccess:
                return {"status":"payment successfull"}, 200
            else:
                abort(400)
        except:
            abort(500)
        
    return 'ok'