from flask import Flask, render_template, request, redirect
from blockchain import Blockchain

app = Flask(__name__)
diary = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=diary.chain)

@app.route('/add', methods=['POST'])
def add():
    entry = request.form['entry']
    last = diary.get_last_block()
    diary.create_block(entry, last['hash'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
