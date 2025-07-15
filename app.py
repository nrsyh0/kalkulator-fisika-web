# app.py
# Kalkulator Fisika Web — Satu File Saja
#
# Fitur:
# 1. Kinematika   : jarak, kecepatan, waktu, percepatan
# 2. Dinamika     : gaya, tekanan, energi kinetik
# 3. Konversi     : energi & tekanan
#
# Jalankan: python app.py
# Buka:    http://127.0.0.1:5000

from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------- HTML BASE ----------
BASE = """
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Kalkulator Fisika</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>body{padding-top:20px}</style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
  <div class="container-fluid">
    <a class="navbar-brand" href="{{ url_for('index') }}">Kalkulator Fisika</a>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="{{ url_for('kinematika') }}">Kinematika</a></li>
        <li class="nav-item"><a class="nav-link" href="{{ url_for('dinamika') }}">Dinamika</a></li>
        <li class="nav-item"><a class="nav-link" href="{{ url_for('konversi') }}">Konversi</a></li>
      </ul>
    </div>
  </div>
</nav>
<div class="container">
  {% block content %}{% endblock %}
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# ---------- HALAMAN BERANDA ----------
INDEX = """
{% extends base %}{% block content %}
<h1 class="text-center">Selamat Datang di Kalkulator Fisika</h1>
<p class="text-center">Gunakan menu di atas untuk mulai perhitungan.</p>
{% endblock %}
"""

# ---------- KINEMATIKA ----------
KINEMATIKA = """
{% extends base %}{% block content %}
<h2>Kalkulator Kinematika</h2>
<form method="POST" class="mb-4">
  <div class="mb-3">
    <label class="form-label">Besaran yang dihitung</label>
    <select name="mode" class="form-select" required>
      <option value="jarak">Jarak (s)</option>
      <option value="kecepatan">Kecepatan (v)</option>
      <option value="waktu">Waktu (t)</option>
      <option value="percepatan">Percepatan (a)</option>
    </select>
  </div>
  <div class="row">
    <div class="col-md-4 mb-3"><input name="s"  step="any" type="number" placeholder="Jarak s (m)" class="form-control"></div>
    <div class="col-md-4 mb-3"><input name="v"  step="any" type="number" placeholder="Kecepatan v (m/s)" class="form-control"></div>
    <div class="col-md-4 mb-3"><input name="t"  step="any" type="number" placeholder="Waktu t (s)" class="form-control"></div>
  </div>
  <div class="row">
    <div class="col-md-6 mb-3"><input name="v1" step="any" type="number" placeholder="Kecepatan awal v1 (m/s)" class="form-control"></div>
    <div class="col-md-6 mb-3"><input name="v2" step="any" type="number" placeholder="Kecepatan akhir v2 (m/s)" class="form-control"></div>
  </div>
  <button class="btn btn-primary" type="submit">Hitung</button>
</form>
{% if result is not none %}
<div class="alert alert-info"><strong>Hasil:</strong> {{ result }}</div>
{% endif %}
{% endblock %}
"""

# ---------- DINAMIKA ----------
DINAMIKA = """
{% extends base %}{% block content %}
<h2>Kalkulator Dinamika</h2>
<form method="POST" class="mb-4">
  <div class="mb-3">
    <label class="form-label">Besaran yang dihitung</label>
    <select name="mode" class="form-select" required>
      <option value="gaya">Gaya (N)</option>
      <option value="tekanan">Tekanan (Pa)</option>
      <option value="energi">Energi Kinetik (J)</option>
    </select>
  </div>
  <div class="row">
    <div class="col-md-4 mb-3"><input name="m"    step="any" type="number" placeholder="Massa m (kg)" class="form-control"></div>
    <div class="col-md-4 mb-3"><input name="a"    step="any" type="number" placeholder="Percepatan a (m/s²)" class="form-control"></div>
    <div class="col-md-4 mb-3"><input name="v"    step="any" type="number" placeholder="Kecepatan v (m/s)" class="form-control"></div>
  </div>
  <div class="row">
    <div class="col-md-6 mb-3"><input name="f"    step="any" type="number" placeholder="Gaya F (N)" class="form-control"></div>
    <div class="col-md-6 mb-3"><input name="area" step="any" type="number" placeholder="Luas A (m²)" class="form-control"></div>
  </div>
  <button class="btn btn-primary" type="submit">Hitung</button>
</form>
{% if result is not none %}
<div class="alert alert-info"><strong>Hasil:</strong> {{ result }}</div>
{% endif %}
{% endblock %}
"""

# ---------- KONVERSI ----------
KONVERSI = """
{% extends base %}{% block content %}
<h2>Konversi Satuan</h2>
<form method="POST" class="mb-4">
  <div class="mb-3">
    <label class="form-label">Jenis Besaran</label>
    <select name="jenis" class="form-select" required>
      <option value="energi">Energi</option>
      <option value="tekanan">Tekanan</option>
    </select>
  </div>
  <div class="row mb-3">
    <div class="col-md-4"><input name="value" step="any" type="number" placeholder="Nilai" class="form-control" required></div>
    <div class="col-md-4">
      <select name="satuan_from" class="form-select" required>
        <optgroup label="Energi">
          <option value="joule">Joule</option><option value="kjoule">kJoule</option>
          <option value="kwh">kWh</option><option value="cal">Kalori</option>
        </optgroup>
        <optgroup label="Tekanan">
          <option value="pa">Pa</option><option value="kpa">kPa</option>
          <option value="bar">Bar</option><option value="atm">Atm</option>
          <option value="mmhg">mmHg</option>
        </optgroup>
      </select>
    </div>
    <div class="col-md-4">
      <select name="satuan_to" class="form-select" required>
        <optgroup label="Energi">
          <option value="joule">Joule</option><option value="kjoule">kJoule</option>
          <option value="kwh">kWh</option><option value="cal">Kalori</option>
        </optgroup>
        <optgroup label="Tekanan">
          <option value="pa">Pa</option><option value="kpa">kPa</option>
          <option value="bar">Bar</option><option value="atm">Atm</option>
          <option value="mmhg">mmHg</option>
        </optgroup>
      </select>
    </div>
  </div>
  <button class="btn btn-primary" type="submit">Konversi</button>
</form>
{% if result is not none %}
<div class="alert alert-info"><strong>Hasil:</strong> {{ result }}</div>
{% endif %}
{% endblock %}
"""

# ---------- ROUTES ----------
@app.route('/')
def index():
    return render_template_string(INDEX, base=BASE)

# --- KINEMATIKA ---
@app.route('/kinematika', methods=['GET', 'POST'])
def kinematika():
    res = None
    if request.method == 'POST':
        mode = request.form['mode']
        try:
            if mode == 'jarak':      # s = v * t
                v = float(request.form['v']); t = float(request.form['t'])
                res = v * t
            elif mode == 'kecepatan':# v = s / t
                s = float(request.form['s']); t = float(request.form['t'])
                res = s / t
            elif mode == 'waktu':    # t = s / v
                s = float(request.form['s']); v = float(request.form['v'])
                res = s / v
            elif mode == 'percepatan':# a = (v2 - v1)/t
                v1 = float(request.form['v1']); v2 = float(request.form['v2']); t = float(request.form['t'])
                res = (v2 - v1) / t
        except (ValueError, ZeroDivisionError):
            res = "Input tidak valid"
    return render_template_string(KINEMATIKA, base=BASE, result=res)

# --- DINAMIKA ---
@app.route('/dinamika', methods=['GET', 'POST'])
def dinamika():
    res = None
    if request.method == 'POST':
        mode = request.form['mode']
        try:
            if mode == 'gaya':       # F = m * a
                m = float(request.form['m']); a = float(request.form['a'])
                res = m * a
            elif mode == 'tekanan':  # P = F / A
                f = float(request.form['f']); area = float(request.form['area'])
                res = f / area
            elif mode == 'energi':   # Ek = ½ m v²
                m = float(request.form['m']); v = float(request.form['v'])
                res = 0.5 * m * v ** 2
        except (ValueError, ZeroDivisionError):
            res = "Input tidak valid"
    return render_template_string(DINAMIKA, base=BASE, result=res)

# --- KONVERSI ---
@app.route('/konversi', methods=['GET', 'POST'])
def konversi():
    res = None
    if request.method == 'POST':
        jenis = request.form['jenis']
        try:
            val = float(request.form['value'])
            sf  = request.form['satuan_from']
            st  = request.form['satuan_to']
            if jenis == 'energi':
                faktor = {'joule':1, 'kjoule':1e3, 'kwh':3.6e6, 'cal':4.184}
            else:  # tekanan
                faktor = {'pa':1, 'kpa':1e3, 'bar':1e5, 'atm':101325, 'mmhg':133.322}
            res = val * faktor[sf] / faktor[st]
        except (ValueError, KeyError, ZeroDivisionError):
            res = "Input tidak valid"
    return render_template_string(KONVERSI, base=BASE, result=res)

# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)
