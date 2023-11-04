import qrcode as qr
from PIL import Image

qrc = qr.QRCode(version=1,error_correction = qr.constants.ERROR_CORRECT_H,
                box_size = 100 , border = 5,)

qrc.add_data("Something Important!")
qrc.make(fit = True)
img = qrc.make_image(fill_color = "green",back_color = "white")
img.save("Important_message.png")