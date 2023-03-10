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
