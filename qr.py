import qrcode

"""
Genera un código QR para conectarse a una red WiFi.

:param ssid: Nombre de la red WiFi (SSID).
:param password: Contraseña de la red WiFi.
:param protocol: Tipo de seguridad (WPA, WPA2, WEP o ninguno).
"""


def create_qr(ssid: str, password: str, protocol: str):
    qr_name = input('Nombre para identificar la imagen qr: ')
    wifi_data = f'WIFI:T:{protocol};S:{ssid};P:{password};;'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'{qr_name}.png')


if __name__ == '__main__':
    ssid = input('Introduce el nombre de tu red WiFi (SSID): ')
    password = input('Introduce la contraseña de tu red WiFi: ')
    protocol = input('Introduce el tipo de seguridad (WPA/WPA2/WEP/NONE): ')
    create_qr(ssid, password, protocol)
