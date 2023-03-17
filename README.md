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
