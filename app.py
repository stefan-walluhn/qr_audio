import os

from flask import Flask, Response, render_template, url_for, request
from qrcode import QRCode
from qrcode.image.svg import SvgPathImage


app = Flask(__name__)


@app.route("/play/<slug>")
def play(slug):
    return render_template('play.html', filename=slug_to_filename(slug))


@app.route("/qr/<slug>")
def qr(slug):
    qr = QRCode(box_size=50, image_factory=SvgPathImage)
    qr.add_data(url_for('play', slug=slug, _external=True))
    qr.make(fit=True)

    svg = qr.make_image()

    return Response(svg.to_string(), mimetype='image/svg+xml')


def slug_to_filename(slug, folder="media", extension="mp3"):
    return os.path.join(folder, ".".join([slug, extension]))
