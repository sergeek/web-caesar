from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->

      <form method="post">

        <label>
            Rotate by: 
            <input type="text" name="rot" value="0"/>
        </label>
        <textarea type="text" name="text">{0}</textarea>
        <button>Submit</button>
        

      </form> 


    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = int(request.form['rot'])
    encrypt_text = str(request.form['text'])

    caesar_text = rotate_string(encrypt_text, rotate_by)

    return form.format(caesar_text)


@app.route("/")
def index():
    return form.format("")

app.run()

