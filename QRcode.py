#simple way to create QRCode
import qrcode as qr
img = qr.make("Kire Opodhartoni!")
img.save("Secret_Message.png")

