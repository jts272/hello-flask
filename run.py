# import 'os' from Python standard library which will be referenced to
# get the app running:
import os

# Required import for handling JSON data, such as in the company about
# details
import json

# import the 'Flask' class:
# Add the render_template function from Flask to render full HTML files
# from the root 'templates' folder:
# request library used to handle form processing:
# flash will display non-permanent messages to the user
from flask import Flask, render_template, request, flash

# import env, only if the system can find our 'env.py' file:
if os.path.exists("env.py"):
    import env
    # This creates the '__pycache__' dir, which can be ignored by Git.

# Create an instance of this class:
# The first arg is the name of the application's module - our package.
# Since we're just using a single module, the built-in Python variable
# '__name__' is used.
# Flask needs this to find templates and static files.
app = Flask(__name__)

# Get the hidden key after app instantiation:
app.secret_key = os.environ.get("SECRET_KEY")


# Route decorator to tell Flask what URL triggers the following function
# When we browse the root directory '/', Flask triggers the following
# function.
@app.route("/")
def index():
    # Text or text in HTML tags can be returned for the browser to
    # render:
    # return "<h1>Hello,</h1> <h2>world!</h2>"

    # Instead of returning text typed in above, we want to render the
    # full template supplied:
    # Flask is looking for a root directory named 'templates'.
    return render_template("index.html")


# This route decorator binds the function or 'view' to the filepath
# provided:
@app.route("/about")
def about():
    # Additional argument provided to the return function. This is a
    # user-defined variable that is accessed with the double curly
    # braces syntax in the html pages, to populate the page title.
    #
    # This is an example of setting data on the server side, and viewing
    # it on the client side.
    #
    # Initialize an empty list for the company JSON data:
    data = []
    # Start a 'with' block for Python to read the JSON file.
    # The file path, read-only mode and new variable name are declared:
    with open("data/company.json", "r", encoding="utf-8") as json_data:
        # Create var to hold the JSON content.
        # This is also supplied as an argument to the return statement,
        # as a variable named 'company'.
        data = json.load(json_data)

    return render_template("about.html", page_title="About", company=data)


# The angled brackets look for data in the url path to pass to the view
# below.
@app.route("/about/<member_name>")
# Create the view, which takes the member_name argument from above:
def about_member(member_name):
    # Create empty object to store the data we want to display later:
    member = {}
    with open("data/company.json", "r", encoding="utf-8") as json_data:
        data = json.load(json_data)
        # Iterate through the data array we have just created:
        for obj in data:
            if obj["url"] == member_name:
                # Give the member object the content of the current loop
                # iteration:
                member = obj

    # Render the specified template and give it the member variable from
    # this function:
    return render_template("member.html", member=member)

# Flask's views all handle GET events by default. Other methods must be
# specified in the route arguments. This allows the contact form to use
# other methods instead of getting a 405 error.


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Test message for posting form:
    # Results appear in the python terminal from running run.py
    if request.method == "POST":
        print("Form posted!")
        # When using the request method of POST, a form object is
        # attached:
        print(request.form)
        # Two different methods for accessing some form data:
        print(request.form.get("name"))
        print(request.form["email"])
        # In the event of the key not being present:
        # get("") = none
        # [""] = throw

        # Call the flash() function to display the flash message:
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# Get the application running:
# '__main__' is the name of the default Module in Python. The if clause
# runs the app with the following arguments.
# Using 'os', get the IP environment variable if it exists, the set
# default.
# Same for PORT (casted as integer). 5000 is a common port used by Flask
# Debug is set to True during development, and False for production!
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False
    )
