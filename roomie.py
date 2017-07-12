import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('Template.html', koszontes="Hello World")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)