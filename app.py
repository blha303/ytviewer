#!/usr/bin/env python3
from flask import *
from youtube_dl import YoutubeDL
from requests import get

app = Flask(__name__)
dlobj = YoutubeDL()
def getinfo(id):
    return dlobj.extract_info("http://youtu.be/{}".format(id), download=False, extra_info={"quiet": True})

@app.route("/")
def index():
    return redirect("https://github.com/blha303/ytviewer")

@app.route("/fmt/<id>")
def formats(id):
    return jsonify({"formats": sorted([f["format"] for f in getinfo(id)["formats"]])})

@app.route("/v/<id>")
@app.route("/v/<id>/<fmt>")
def vid(id, fmt=None):
    info = {f["format_id"]:f for f in getinfo(id)["formats"]}
    if fmt:
        if not fmt in info:
            return jsonify({"error": "That video doesn't have that format code. Go to /fmt/{} to see available format codes or omit the code to use the default".format(id), "code": 400})
        url = info[fmt]["url"]
    else:
        url = info["22" if "22" in info else "18"]["url"]
    req = get(url, stream=True)
    return Response(stream_with_context(req.iter_content(chunk_size=128)),
                    content_type=req.headers['content-type'])

if __name__ == "__main__":
    app.run(debug=True, port=53627, host="0.0.0.0")
