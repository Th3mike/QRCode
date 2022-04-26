import qrcode
import shutil
import os
import os.path

def gerar():
    data = "https://marciolacerda.netlify.app/"

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5) 
    qr.add_data(data) 
    qr.make(fit = True) 
    img = qr.make_image(fill_color = 'black', back_color = 'white') 
    img.save('./img/QRCode.png')

    print('QR Code gerado com sucesso!')