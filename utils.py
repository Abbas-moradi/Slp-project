from kavenegar import *

def send_otp_code(phone, code):
    try:
        api = KavenegarAPI('2F77537067544365733452714E42516D69344B6176456854354732787363716B4B7848316F5165525155553D')
        params = { 'sender' : '1000010000808',
                   'receptor': phone,
                   'message' :f'سایت گفتار درمانی کشاورز\n :کد تایید شما {code}' }
        print(params)
        response = api.sms_send( params)
    except APIException as e:
        print(e)
    except HTTPException as h:
        print(h)