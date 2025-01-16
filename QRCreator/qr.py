import qrcode

"""
Generates a QR code to connect to a WiFi network.

param ssid: Name of the WiFi network (SSID).
:param password: Password of the WiFi network.
:param protocol: Security type (WPA, WPA2, WEP or none).
"""

def validate_input(prompt: str, is_protocol: bool = False) -> str:
    valid_protocols = ["WPA", "WPA2", "WEP", "NONE"]
    while True:
        value = input(prompt).strip()
        if is_protocol:
            value = value.upper()
            if value in valid_protocols:
                return value
            print(f"Invalid protocol. Please choose one of the following: {', '.join(valid_protocols)}.")
        elif value:
            return value
        else:
            print("This field cannot be empty. Please enter a valid value.")

def create_qr(ssid: str, password: str, protocol: str):
    qr_name = validate_input('Name to identify the QR image: ')
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
    print(f"QR Code saved as: {qr_name}.png")

if __name__ == '__main__':
    while True:
        ssid = validate_input('Enter the name of your WiFi network (SSID): ')
        password = validate_input('Enter the password of your WiFi network: ')
        protocol = validate_input('Enter your WiFi network security type (WPA/WPA2/WEP/NONE): ', is_protocol=True)
        create_qr(ssid, password, protocol)
        retry = input('Enter “y” to create another QR code, enter to exit: ').strip().lower()
        if retry != 'y':
            break
