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
