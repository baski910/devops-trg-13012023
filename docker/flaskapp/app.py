from flask import Flask<br>
<br>
app = Flask(__name__)<br>
<br>
@app.route('/')<br>
def home():<br>
    return "<h1>Hello world</h1>"<br>
<br>
if __name__ == "__main__":<br>
    app.run(host="0.0.0.0")<br>
