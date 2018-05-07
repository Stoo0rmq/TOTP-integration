import pyotp
import pyqrcode

numput = -3
while numput != 0 :
    print(" Hello, please choose and option:\n")
    print(" 1 - Generate QR code with TOTP")
    print(" 2 - Check TOTP")
    print(" 0 - Exit")
    
    numput = input()

    if numput == 1 :
        numb = pyotp.random_base32()
        x = pyotp.totp.TOTP(numb).provisioning_uri("yourmail@mew.com", issuer_name="YourServiceName")
        print (" Your QR is ready")
        url = pyqrcode.create(x)
        big_code = pyqrcode.create(x, error='L', version=27, mode='binary')
        big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        print (" Just in case you would like to check the correctness of the key, this is the code:\n") 
        print(numb)
        big_code.show()
    if numput == 2 :
        print (" Please introduce TOTP including quotation marks \n")
        totpcheck = input()
        totp = pyotp.TOTP(totpcheck)
        print("Current OTP:", totp.now())

