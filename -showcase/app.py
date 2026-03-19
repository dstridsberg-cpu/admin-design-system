from flask import Flask, render_template, redirect, send_from_directory
import os

BASE = os.path.dirname(os.path.dirname(__file__))  # project root
app = Flask(__name__, template_folder='templates', static_folder=BASE, static_url_path='/static')

@app.route('/')
def showcase():
    return render_template('showcase.html', section='all')

@app.route('/atoms')
def atoms():
    return redirect('/#atoms')

@app.route('/molecules')
def molecules():
    return redirect('/#molecules')

@app.route('/organisms')
def organisms():
    return redirect('/#organisms')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
