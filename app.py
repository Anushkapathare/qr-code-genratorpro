from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            img = qrcode.make(url)
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            return send_file(buffer, mimetype="image/png", as_attachment=True, download_name="qr_code.png")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
