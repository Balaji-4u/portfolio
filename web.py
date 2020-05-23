import os
from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# print(dir(page_name))


# @app.route('/')
# def hello_world():
#     return render_template("index.html")

@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as file:
        name = data["username"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        db = file.write(f"\n{name},{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as file1:
        name = data["username"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(file1, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
        # csv_writer.write


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            _name = data["username"]
            print(_name)
        # #mylist = []
        # for key, value in data.items():

            return redirect('./thankyou.html')
        except:
            return "data was not saved in the database, please resubmit it."
        # return "Thank you for submitting the details. I will review your requirement and will respond you in 2 days!"
        # print(data)
    else:
        return "something went wrong!"

###
# @app.route('/<username>/<int:post_id>/<path:subpath>/')
# def show_user(username=None, post_id=None, subpath=None):
#     return render_template("index.html", name=username, post_id=post_id, subpath=subpath)


# @ app.route('/about.html')
# def about_me():
#     return render_template("about.html")


# @app.route('/favicon.ico')
# def fav_ico():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
