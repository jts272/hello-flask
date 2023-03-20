# hello-flask

A walkthrough project built using the Flask framework.

## General workflow

1. `pip3 install Flask`
2. Setup `run.py` (see `run.py` file. It is commented.)
   - imports
   - create Flask class instance
   - setup ports and debug mode, using 'os' import
   - `python run.py`
   - open `localhost:PORT` in your web browser
3. Create 'templates' directory - HTML files go in here
4. Bind routes to the appropriate `@app.route` decorators
   - provide Jinja template expressions to nav hrefs `{{url_for('function')}}`
5. Use template inheritance to create a `base.html`, which other pages can use
   for repeated elements

## Templates

`{{}}` = expression, outputting something onto the screen, like a href
`{%%}` = flow control, such as loops or if statements.

### Template inheritance usage

#### In `base.html`:

```
{% block content %} {% endblock %}
```

Used as a placeholder for where other pages' html will reside. In other words,
it looks like a regular html file with the Jinja templates interspersed.

#### In the html files that are using the base:

```
{% extends "base.html" %} {% block content %}
<h1>My HTML is here!</h1>
{% endblock %}
```

Note 'content' in the Jinja template can be named anything.

### Using StartBootstrap source files

In this project, [Clean Blog 5.0.10](https://github.com/startbootstrap/startbootstrap-clean-blog/tree/v5.0.10)
is used.

By examining the source `index.html`, we can see which scripts and stylesheets
are linked. From here, we simply convert these relative links to the Jinja
`{{url_for()}}` format.

By copying the entire content inside the `<body>` tags of the source file to our
project `base.html`, we can then spin off relevant sections to their
corresponding html template files.

Don't forget that even inline style background image sources must be updated to
follow the Jinja method.

### for loops in templates

If a list is supplied as an argument for a view function, it can be printed
directly, or even iterated through.

Syntax:

```
{% for 'variable' in 'list' %}
<p>{{'variable'}}</p>
{% endfor %}
```

Notice the different use of statement and expression syntax `{{}}` and `{%%}`

This will create new `<p>` tags in html, each with the content from the list.

### Using JSON in Python

`import json`

Example of accessing the 'name' property of the second object in a JSON file:

`{{json_file[1]["name"]}}`

### Using JSON data in a for loop in HTML

The `'iterable'` is supplied as an argument in the view return statement.

```
{% for 'object' in 'iterable' %}

  <h3>{{object.name}}</h3>
  <p>{{object.description}}</p>
  <img src="{{object.image_path}} alt="" class="" />

{% endfor %}
```

### Working with forms in Flask

In this example code, the html for the form is used from the Clean Blog template
from StartBootstrap. This is designed to work with the supplied JavaScript from
the template's source files. However, in this application, we are using our own
custom methods to handle the form process. In general:

#### HTML

1. Copy the form html from the template (Clean Blog)
2. Add the "POST" method to the form
3. Add "name" attributes to the input elements

#### Python

4. Add `methods=["GET", "POST"]` to the view's route decorator
5. Import `request` from `flask`
6. We can now access the `request.form` object

### Heroku CLI setup

1. Create new App on Heroku
2. `npm install -g heroku`
3. `heroku login`

- This will open a browser verification link outside of the CLI when MFA is
  enabled.

4. `heroku apps` will list apps for the logged in user

- Rename apps with `heroku apps:rename current-app-name --app new-app-name`

5. Select `Open app` on the Heroku dashboard to see the Heroku URL. This can be
   copied directly from the Heroku app 'Settings' tab.

#### Pushing to Heroku

6. Check `git status` and `git remote -v`

- Expect status to be up to date and for only the `origin` branch to be
  present in the verbose remote log.

7. `git remote add heroku https://git.heroku.com/your-app-name.git`
8. Confirm new remote status with `git remote -v`
9. `git push -u heroku main`

- This will fail as Heroku cannot detect a default language.

10. `pip3 freeze --local > requirements.txt` This creates the `requirements.txt`
    so that Heroku can see the Python dependencies.
11. The `requirements.txt` in the root directory shows Heroku that this is a
    Python application. `git push -u heroku main` will now deploy the application
    to Heroku with the necessary dependencies (Python, Flask etc.) The app still
    requires a `Procfile` to fully deploy without error.
12. Create the Procfile for Heroku with `echo web: python run.py > Procfile`
