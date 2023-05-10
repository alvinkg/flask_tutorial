# Flask Tutorial

## Basics

### Install using the requirements.txt

pip install -r requirements.txt

### Using grep to build requirements.txt

pip freeze | grep -i flask >> requirements.txt

### Tutorial 1

- How to build a flask app
- How to do a redirect with flask mtd redirect
- How to use url_for in redirect
- How to pass parameters encoded to your redirect

### Tutorial 2

- How to use render_template
  - create templates directory
  - create template html file
  - call render_template mtd to render html file
- How to pass parameters to template
  - add placeholders inside {{}} in html file
  - hard code param values in backend
- How to run pythonic logic in html
  - use {% %} to wrap code

## Tutorial 5

Sessions

- 'permanent' sessions
  - Your data can last as long as your browser's page is open by default
  - If you are redirected to another page all your data will need to be redirected by code
  - The alternative is to store data on the server for the duration of your session, that is as long as your browser is open
  - To keep your session data after the browser is closed, define the session lifetime
- permanent sessions lifetime
  - We can define the session lifetime to make them last longer than the browser lifetime
- secret key
  - We need to define a secret key if when we store session data on the server
  - app.secretkey


- Steps
  - import session from flask
  - set up session data when method = 'POST' from form
  - check if there is data is the session under the key
  -   

## References

[video](https://www.youtube.com/watch?v=mqhxxeeTbu0)
