from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data_nascimento = request.form.get('data_nascimento')

        if data_nascimento:
            data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
            idade = datetime.now().year - data_nascimento.year
            return render_template('index.html', idade=idade)
        else:
            return render_template('index.html', idade=None)
    else:
        return render_template('index.html', idade=None)


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
