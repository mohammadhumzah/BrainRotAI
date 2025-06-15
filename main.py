from flask import Flask, render_template, request
import uuid     # Give unique filenames to uploaded files
from werkzeug.utils import secure_filename      # For uploading files in flask
import os

UPLOAD_FOLDER = 'user_uploads'      # location of folder to which it is uploaded to
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app = Flask(__name__)
app.config[ 'UPLOAD_FOLDER'] = UPLOAD_FOLDER           # set the folder path where uploaded files will be saved in Flask app

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods= ["GET", "POST"])
def create():
    myid = uuid.uuid1()     # uuid1 creates id based on time of uploads so its unique
    # If user is uploading an image/images
    if request.method == "POST":
        print (request.files.keys())        # To access uploaded files
        rec_id = request.form.get("uuid")   # used to get input values (like text etc.) from an HTML <form> submitted via POST.
        desc= request.form.get("text")
        input_files = []     # List to store the names of uploaded files
        
        for key, value in request.files.items():
            print(key,value)

    # Upload a file using file.save.os from flask documentation
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)       # secure_filename cleans the filename

                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))    # Join the upload folder path with filename and save it to that location
                input_files.append(file.filename)
                print(file.filename)
     # Capture the description and save it to a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
                f.write(desc)
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")
        
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")  # List all reels in the static/reels directory
    return render_template("gallery.html", reels=reels)

app.run(debug=True)