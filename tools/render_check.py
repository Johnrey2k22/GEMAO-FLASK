from MyFlaskapp import create_app
from flask import render_template_string
app = create_app()
with app.test_request_context('/'):
    tpl = open('MyFlaskapp/authentication/templates/login.html','r',encoding='utf-8').read()
    html = render_template_string(tpl)
    for line in html.splitlines():
        if 'static' in line:
            print(line.strip())
