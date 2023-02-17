from flask import Flask, request, send_file
import qrcode

app = Flask(__name__)


@app.route('/api/qr_code', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url')
    if not url:
        return 'No URL provided.', 400

    # Create the QR code image using the qrcode library
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the image to a temporary file and send it back as the API response
    img_path = 'qr_code.png'
    img.save(img_path)
    return send_file(img_path, mimetype='image/png', as_attachment=True, download_name='qr_code.png')


if __name__ == '__main__':
    app.run()
