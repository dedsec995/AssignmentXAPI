import os,os.path,time,string,random,json,requests,sys
from PIL import Image, ImageDraw, ImageFont
from flask import *
from werkzeug.utils import secure_filename
from assignmentx import AssignmentX
# UPLOAD_FOLDER = "/home/dedsec995/mysite/uploads/"
UPLOAD_FOLDER = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/uploads/"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "ipynb", "ttf"}


# new instance of flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# index routing
@app.route("/")
def index():

    return "Your Welcomed By The UAV Nibbas !!!!"


# Assignment routing
@app.route("/api/assignmentx", methods=["GET", "POST"])
def GetMeAssigmentX():

    json = request.get_json()
    print(json)
    if len(json['name']) == 0:
        return jsonify({'error': 'invalid input'})
    name = json["name"]
    session["name"] = name
    opacity = int(json["opacity"])
    session["opacity"] = opacity
    lol = json["color1"]
    h = lol.lstrip("#")
    a = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
    a = a + (opacity,)
    session["color1"] = a
    lol2 = json["color2"]
    h2 = lol2.lstrip("#")
    a2 = tuple(int(h2[i : i + 2], 16) for i in (0, 2, 4))
    a2 = a2 + (opacity,)
    session["color2"] = a2
    
    session["wtext"] = json["wtext"]
    
    session["opage"] = json["opage"]
    
    session["sfont"] = json["sfont"]

    name = AssignmentX(session.get("opacity",None),session.get("color1",None),session.get("color2",None),session.get("wtext",None),session.get("opage",None),session.get("sfont",None))
    name.initiateX(UPLOAD_FOLDER)
    path = name.get_path()

    for file in request.files.getlist("file"):
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(path, filename))
    name.assignmentx()
    session["path1"] = name.get_path1()
    session["directoryName"] = name.directoryName
    return jsonify({"name": json["name"],"opacity": json["opacity"],"color1": json["color1"],"color2": json["color2"],"wtext": json["wtext"],"opage": json["opage"],"sfont": "Sucessful"})
    # return render_template("next.html", name=session.get("name",None))

        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


# @app.route("/next.html", methods=["GET", "POST"])
# def next():
#     return render_template("next.html", name=session.get("name",None))


# @app.route("/about", methods=["GET", "POST"])
# def about():
#     return render_template("about.html")


# @app.route("/pptc", methods=["GET", "POST"])
# def pptc():
#     return render_template("pptc.html")


# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     return render_template("contact.html")


# @app.route("/output")
# def output():
#     # path = "info.xlsx"
#     # path = "sample.txt"
#     try:
#         return send_file(
#             "{}.pdf".format(os.path.join(session.get("path1",None), session.get("directoryName",None))),
#             as_attachment=True,
#         )
#     except:
#         return send_file(
#             "{}.txt".format("D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/essentials/error"),
#             as_attachment=True,
#         )


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    except:
        app.run(host="0.0.0.0", debug=True)
