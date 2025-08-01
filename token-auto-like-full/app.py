from flask import Flask, request, render_template, redirect, url_for, session
from config import ADMIN_PASSWORD, load_tokens, load_log_uid, save_tokens, save_log_uid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/like', methods=['GET'])
def like():
    uid = request.args.get('uid')
    if not uid:
        return "Thiếu UID", 400

    tokens = load_tokens()
    log_uid = load_log_uid()

    if uid in log_uid:
        return "UID đã like trước đó", 400

    # Gửi request like
    success = 0
    for token in tokens:
        res = requests.get(f'https://graph.facebook.com/{uid}/likes?access_token={token}')
        if res.status_code == 200:
            success += 1

    if success > 0:
        log_uid.append(uid)
        save_log_uid(log_uid)

    return f"Đã like UID {uid} bằng {success} token."

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    tokens = load_tokens()
    logs = load_log_uid()
    return render_template('admin.html', tokens=tokens, logs=logs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)