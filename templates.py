BASE = r"""<!doctype html>
<html lang="id"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{% block title %}CateringKu{% endblock %}</title>
<style>
:root{--ink:#14213D;--bg:#F7F4EE;--card:#fff;--line:#E7E1D3;--or:#E8590C;--or2:#F4A261;--teal:#1C7C7D;--mut:#6B7280;--red:#D62839;--grn:#2E9E5B}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);min-height:100vh}
a{color:inherit;text-decoration:none}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
.nav{background:linear-gradient(120deg,#0F1B2D,#1E2F52);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 4px 20px rgba(15,27,45,.25)}
.nav .wrap{display:flex;align-items:center;gap:14px;height:64px}
.brand{font-weight:800;font-size:22px;letter-spacing:.3px;display:flex;align-items:center;gap:8px}
.brand span{display:inline-block;animation:bob 2.4s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-4deg)}50%{transform:translateY(-4px) rotate(4deg)}}
.sp{flex:1}.clock{font-size:14px;color:#cfd6e4;font-variant-numeric:tabular-nums}
.bell{position:relative;background:rgba(255,255,255,.12);border:0;color:#fff;width:42px;height:42px;border-radius:50%;font-size:20px;cursor:pointer;transition:.2s}
.bell:hover{background:rgba(255,255,255,.22)}
.bell.ring{animation:ring 1.2s ease-in-out infinite}
@keyframes ring{0%,100%{transform:rotate(0)}10%,30%{transform:rotate(14deg)}20%,40%{transform:rotate(-14deg)}50%{transform:rotate(0)}}
.badge{position:absolute;top:-4px;right:-4px;min-width:20px;height:20px;border-radius:10px;background:var(--red);font-size:12px;font-weight:700;display:none;place-items:center;padding:0 5px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:0;border-radius:10px;padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;transition:transform .15s,box-shadow .15s,background .15s;background:var(--or);color:#fff}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 18px rgba(232,89,12,.3)}
.btn.ghost{background:rgba(255,255,255,.14);color:#fff}.btn.ghost:hover{box-shadow:none;background:rgba(255,255,255,.24)}
.btn.sm{padding:6px 10px;font-size:13px;border-radius:8px}.btn.grn{background:var(--grn)}.btn.red{background:var(--red)}.btn.line{background:#fff;color:var(--ink);border:1px solid var(--line)}
.hero{padding:28px 0 8px}.hero h1{font-size:30px}.hero p{color:var(--mut);margin-top:4px}
.grid{display:grid;gap:16px}.stats{grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin:18px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 2px 10px rgba(20,33,61,.05);animation:up .5s both}
@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.stat{display:flex;gap:14px;align-items:center;transition:transform .2s}.stat:hover{transform:translateY(-4px)}
.stat .ic{width:52px;height:52px;border-radius:14px;display:grid;place-items:center;font-size:26px;background:#FFF1E6}
.stat b{font-size:26px;display:block;line-height:1.1}.stat small{color:var(--mut)}
.alert{border-radius:16px;padding:16px 18px;margin:8px 0;display:flex;gap:12px;align-items:flex-start;animation:up .5s both}
.alert.besok{background:#FFF4E0;border:1px solid #F6C26B}.alert.hari{background:#FDE8EA;border:1px solid #F3A5AD}
.alert .big{font-size:28px;animation:ring 2s ease-in-out infinite}
.alert ul{margin-top:6px;padding-left:18px}
.two{display:grid;grid-template-columns:340px 1fr;gap:16px;align-items:start}
@media(max-width:860px){.two{grid-template-columns:1fr}}
label{font-size:13px;font-weight:700;color:var(--mut);display:block;margin:10px 0 4px}
input,select{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:10px;font-size:15px;background:#fff;color:var(--ink)}
input:focus,select:focus{outline:2px solid var(--or2);border-color:var(--or2)}
.hint{font-size:12px;color:var(--teal);margin-top:6px}
.tools{display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap}.tools input{flex:1;min-width:160px}.tools select{width:auto}
.tbl{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;padding:10px;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.5px;border-bottom:2px solid var(--line)}
td{padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:middle}tr:hover td{background:#FFFBF5}
.chip{padding:4px 10px;border-radius:99px;font-size:12px;font-weight:700;display:inline-block}
.chip.Baru{background:#E6F2F2;color:var(--teal)}.chip.Selesai{background:#E4F5EA;color:var(--grn)}
.tag{margin-left:6px;padding:3px 8px;border-radius:99px;font-size:11px;font-weight:800;color:#fff;animation:pulse 1.6s infinite}
.tag.besok{background:var(--or)}.tag.hari_ini{background:var(--red)}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(232,89,12,.5)}70%{box-shadow:0 0 0 9px rgba(232,89,12,0)}100%{box-shadow:0 0 0 0 rgba(232,89,12,0)}}
.act{display:flex;gap:6px;flex-wrap:wrap}.act form{display:inline}
.empty{text-align:center;color:var(--mut);padding:34px}
.panel{position:fixed;top:70px;right:16px;width:min(360px,calc(100vw - 32px));background:#fff;color:var(--ink);border-radius:16px;box-shadow:0 18px 50px rgba(0,0,0,.25);padding:16px;display:none;z-index:40}
.panel.open{display:block;animation:up .25s both}.panel h4{margin-bottom:8px}.panel li{margin:6px 0 6px 18px;font-size:14px}
#toasts{position:fixed;bottom:18px;right:18px;display:flex;flex-direction:column;gap:10px;z-index:60}
.toast{background:var(--ink);color:#fff;padding:12px 16px;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.3);animation:up .3s both;max-width:320px;font-size:14px}
.toast.ok{background:var(--grn)}.toast.error{background:var(--red)}.toast.warn{background:var(--or)}
.login{min-height:100vh;display:grid;place-items:center;padding:20px;background:radial-gradient(circle at 20% 20%,#2a3f6d,#0F1B2D 60%)}
.login .box{width:min(400px,100%);background:#fff;border-radius:22px;padding:32px;box-shadow:0 30px 80px rgba(0,0,0,.4);animation:up .6s both}
.login h1{font-size:28px}.login .logo{font-size:46px;display:inline-block;animation:bob 2.4s ease-in-out infinite}
.login p{color:var(--mut);margin:4px 0 12px}
</style></head><body>
{% block body %}{% endblock %}
<div id="toasts"></div>
<script>
function toast(m,t){var d=document.createElement('div');d.className='toast '+(t||'');d.textContent=m;document.getElementById('toasts').appendChild(d);setTimeout(function(){d.style.opacity=0;d.style.transition='.4s';setTimeout(function(){d.remove()},400)},4500)}
{% for c,m in get_flashed_messages(with_categories=true) %}toast({{ m|tojson }},{{ c|tojson }});{% endfor %}
</script>
{% block script %}{% endblock %}
</body></html>"""

LOGIN = r"""{% extends "base.html" %}{% block title %}Masuk · CateringKu{% endblock %}
{% block body %}<div class="login"><form class="box" method="post">
<div class="logo">🍱</div><h1>CateringKu</h1><p>Masuk sebagai pemilik / admin catering</p>
<label>Username</label><input name="username" autofocus required>
<label>Password</label><input name="password" type="password" required>
<button class="btn" style="width:100%;margin-top:18px">Masuk</button>
</form></div>{% endblock %}"""

DASH = r"""{% extends "base.html" %}{% block title %}Dashboard · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div><div class="sp"></div>
<div class="clock" id="clock"></div>
<button class="bell {% if notif %}ring{% endif %}" id="bell" title="Pemberitahuan">🔔<span class="badge" id="badge"></span></button>
<a class="btn ghost sm" href="/logout">Keluar ({{ user }})</a></div></div>
<div class="panel" id="panel"><h4>Pemberitahuan</h4><ul id="plist"></ul>
<button class="btn sm line" id="allow" style="margin-top:10px">Aktifkan notifikasi browser</button></div>
<div class="wrap">
<div class="hero"><h1>Halo, {{ user }} 👋</h1><p>Hari ini {{ today }}. Kelola pesanan catering kamu di sini.</p></div>

{% set hari=notif|selectattr('pengingat','equalto','hari_ini')|list %}{% set bsk=notif|selectattr('pengingat','equalto','besok')|list %}
{% if hari %}<div class="alert hari"><div class="big">🚨</div><div><b>{{ hari|length }} pesanan harus disiapkan HARI INI</b><ul>
{% for r in hari %}<li>{{ r.pelanggan }} · {{ r.menu }} · {{ r.jumlah }} porsi</li>{% endfor %}</ul></div></div>{% endif %}
{% if bsk %}<div class="alert besok"><div class="big">🔔</div><div><b>Pengingat: {{ bsk|length }} pesanan catering untuk BESOK</b><ul>
{% for r in bsk %}<li>{{ r.pelanggan }} · {{ r.menu }} · {{ r.jumlah }} porsi</li>{% endfor %}</ul></div></div>{% endif %}

<div class="grid stats">
<div class="card stat"><div class="ic">📦</div><div><b class="count" data-n="{{ stats.total }}">0</b><small>Total pesanan</small></div></div>
<div class="card stat"><div class="ic">🍳</div><div><b class="count" data-n="{{ stats.proses }}">0</b><small>Sedang diproses</small></div></div>
<div class="card stat"><div class="ic">✅</div><div><b class="count" data-n="{{ stats.selesai }}">0</b><small>Selesai</small></div></div>
<div class="card stat"><div class="ic">💰</div><div><b class="count" data-n="{{ stats.pendapatan }}" data-rp="1">0</b><small>Pendapatan (selesai)</small></div></div>
</div>

<div class="two">
<form class="card" method="post" action="/tambah"><h3>➕ Pesanan baru</h3>
<label>Nama pelanggan</label><input name="pelanggan" required>
<label>Menu</label><input name="menu" placeholder="mis. Nasi Box Ayam" required>
<label>Jumlah porsi</label><input name="jumlah" type="number" min="1" required>
<label>Harga per porsi (Rp)</label><input name="harga" type="number" min="0" required>
<label>Tanggal acara</label><input name="tanggal" type="date">
<div class="hint">💡 Diskon 10% otomatis untuk 50 porsi ke atas</div>
<button class="btn" style="width:100%;margin-top:14px">Simpan pesanan</button></form>

<div class="card"><h3 style="margin-bottom:12px">📋 Daftar pesanan</h3>
<form class="tools" method="get"><input name="q" value="{{ q }}" placeholder="Cari pelanggan atau menu...">
<select name="status"><option value="">Semua status</option><option {% if st=='Baru' %}selected{% endif %}>Baru</option><option {% if st=='Selesai' %}selected{% endif %}>Selesai</option></select>
<button class="btn sm">Cari</button></form>
<div class="tbl"><table><tr><th>Pelanggan</th><th>Menu</th><th>Porsi</th><th>Total</th><th>Tanggal</th><th>Status</th><th>Aksi</th></tr>
{% for r in rows %}<tr>
<td><b>{{ r.pelanggan }}</b></td><td>{{ r.menu }}</td><td>{{ r.jumlah }}</td><td>{{ r.total|rupiah }}</td>
<td>{{ r.tanggal_acara|tgl }}{% if r.pengingat %}<span class="tag {{ r.pengingat }}">{{ 'BESOK' if r.pengingat=='besok' else 'HARI INI' }}</span>{% endif %}</td>
<td><span class="chip {{ r.status }}">{{ r.status }}</span></td>
<td><div class="act">
{% if r.status=='Baru' %}<form method="post" action="/status/{{ r.id }}"><button class="btn sm grn">Selesai</button></form>{% endif %}
<a class="btn sm line" href="/edit/{{ r.id }}">Edit</a>
<form method="post" action="/hapus/{{ r.id }}" onsubmit="return confirm('Hapus pesanan ini?')"><button class="btn sm red">Hapus</button></form></div></td>
</tr>{% else %}<tr><td colspan="7" class="empty">Belum ada pesanan. Tambahkan lewat form di samping 🍽️</td></tr>{% endfor %}
</table></div></div></div></div>
{% endblock %}
{% block script %}<script>
document.querySelectorAll('.count').forEach(function(el){var n=+el.dataset.n,rp=el.dataset.rp,t0=performance.now();
function f(v){return rp?'Rp'+Math.round(v).toLocaleString('id-ID'):Math.round(v)}
(function s(t){var p=Math.min((t-t0)/900,1);el.textContent=f(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(s)})(t0)});
function tick(){var d=new Date();document.getElementById('clock').textContent=d.toLocaleDateString('id-ID',{weekday:'long',day:'numeric',month:'long'})+' · '+d.toLocaleTimeString('id-ID')}
tick();setInterval(tick,1000);
var bell=document.getElementById('bell'),panel=document.getElementById('panel'),badge=document.getElementById('badge'),last=-1;
bell.onclick=function(){panel.classList.toggle('open')};
document.getElementById('allow').onclick=function(){if('Notification' in window)Notification.requestPermission().then(function(p){toast(p==='granted'?'Notifikasi browser aktif':'Izin notifikasi ditolak','ok')})};
function cek(){fetch('/api/notifikasi').then(function(r){return r.ok?r.json():null}).then(function(d){if(!d)return;
badge.textContent=d.jumlah;badge.style.display=d.jumlah?'grid':'none';bell.classList.toggle('ring',d.jumlah>0);
var ul=document.getElementById('plist');ul.innerHTML='';
if(!d.items.length){ul.innerHTML='<li>Tidak ada pesanan untuk hari ini atau besok</li>'}
d.items.forEach(function(i){var li=document.createElement('li');li.textContent=(i.kapan==='besok'?'Besok: ':'Hari ini: ')+i.pelanggan+' · '+i.menu+' · '+i.jumlah+' porsi';ul.appendChild(li)});
if(d.jumlah>last&&d.jumlah>0){toast('🔔 '+d.jumlah+' pesanan perlu disiapkan (hari ini / besok)','warn');
if('Notification' in window&&Notification.permission==='granted')new Notification('CateringKu',{body:d.jumlah+' pesanan perlu disiapkan hari ini / besok'})}
last=d.jumlah}).catch(function(){})}
cek();setInterval(cek,30000);
</script>{% endblock %}"""

EDIT = r"""{% extends "base.html" %}{% block title %}Edit pesanan · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div><div class="sp"></div><a class="btn ghost sm" href="/">← Kembali</a></div></div>
<div class="wrap" style="max-width:520px;padding-top:28px"><form class="card" method="post"><h3>✏️ Edit pesanan #{{ p.id }}</h3>
<label>Nama pelanggan</label><input name="pelanggan" value="{{ p.pelanggan }}" required>
<label>Menu</label><input name="menu" value="{{ p.menu }}" required>
<label>Jumlah porsi</label><input name="jumlah" type="number" min="1" value="{{ p.jumlah }}" required>
<label>Harga per porsi (Rp)</label><input name="harga" type="number" min="0" value="{{ p.harga_satuan }}" required>
<label>Tanggal acara</label><input name="tanggal" type="date" value="{{ p.tanggal_acara.isoformat() if p.tanggal_acara else '' }}">
<div style="display:flex;gap:8px;margin-top:16px"><button class="btn" style="flex:1">Simpan perubahan</button><a class="btn line" href="/">Batal</a></div>
</form></div>{% endblock %}"""

TEMPLATES = {"base.html": BASE, "login.html": LOGIN, "dashboard.html": DASH, "edit.html": EDIT}
