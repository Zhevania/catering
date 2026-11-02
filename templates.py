BASE = r"""<!doctype html>
<html lang="id"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{% block title %}CateringKu{% endblock %}</title>
<style>
:root{--ink:#14213D;--bg:#F7F4EE;--card:#fff;--line:#E7E1D3;--or:#E8590C;--or2:#F4A261;--teal:#1C7C7D;--mut:#6B7280;--red:#D62839;--grn:#2E9E5B}
*{box-sizing:border-box;margin:0;padding:0}
[hidden]{display:none!important}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);min-height:100vh}
a{color:inherit;text-decoration:none}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px 40px}
.nav{background:linear-gradient(120deg,#0F1B2D,#1E2F52);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 4px 20px rgba(15,27,45,.25)}
.nav .wrap{display:flex;align-items:center;gap:14px;height:64px;padding-bottom:0}
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
.btn:disabled{background:#cbd0d8;cursor:not-allowed;transform:none;box-shadow:none}
.btn.ghost{background:rgba(255,255,255,.14);color:#fff}.btn.ghost:hover{box-shadow:none;background:rgba(255,255,255,.24)}
.btn.sm{padding:6px 10px;font-size:13px;border-radius:8px}.btn.grn{background:var(--grn)}.btn.red{background:var(--red)}.btn.line{background:#fff;color:var(--ink);border:1px solid var(--line)}
.hero{padding:28px 0 8px}.hero h1{font-size:30px}.hero p{color:var(--mut);margin-top:4px}
.grid{display:grid;gap:16px}.stats{grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin:18px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 2px 10px rgba(20,33,61,.05);animation:up .5s both;margin-bottom:16px}
@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.stat{display:flex;gap:14px;align-items:center;transition:transform .2s;margin-bottom:0}.stat:hover{transform:translateY(-4px)}
.stat .ic{width:52px;height:52px;border-radius:14px;display:grid;place-items:center;font-size:26px;background:#FFF1E6}
.stat b{font-size:26px;display:block;line-height:1.1}.stat small{color:var(--mut)}
.alert{border-radius:16px;padding:16px 18px;margin:8px 0;display:flex;gap:12px;align-items:flex-start;animation:up .5s both}
.alert.besok{background:#FFF4E0;border:1px solid #F6C26B}.alert.hari{background:#FDE8EA;border:1px solid #F3A5AD}
.alert .big{font-size:28px;animation:ring 2s ease-in-out infinite}
.alert ul{margin-top:6px;padding-left:18px}
label{font-size:13px;font-weight:700;color:var(--mut);display:block;margin:10px 0 4px}
input,select{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:10px;font-size:15px;background:#fff;color:var(--ink)}
input:focus,select:focus{outline:2px solid var(--or2);border-color:var(--or2)}
.fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 14px}
.tabs{display:flex;gap:8px;margin:12px 0 16px;flex-wrap:wrap}
.tab{border:1px solid var(--line);background:#fff;padding:10px 16px;border-radius:12px;font-weight:700;cursor:pointer;font-size:14px;color:var(--ink)}
.tab.active{background:var(--ink);color:#fff;border-color:var(--ink)}
.info{background:#E6F2F2;color:var(--teal);padding:10px 14px;border-radius:12px;font-size:14px;font-weight:600}
.cat h5{margin:16px 0 8px;font-size:12px;text-transform:uppercase;letter-spacing:.6px;color:var(--mut)}
.menu-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}
.opt{display:flex;align-items:center;gap:8px;padding:9px 12px;border:1px solid var(--line);border-radius:10px;cursor:pointer;font-size:14px;font-weight:500;color:var(--ink);margin:0;user-select:none;transition:.15s}
.opt input{width:auto;accent-color:var(--or)}
.opt:hover{border-color:var(--or2)}
.opt:has(input:checked){background:#FFF1E6;border-color:var(--or);font-weight:700}
.opt.off{opacity:.45;cursor:not-allowed}
.sum{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-top:16px;padding:12px 16px;background:#FFF8F0;border-radius:12px}
.sum b{font-size:20px}.cnt{font-weight:800}
.tools{display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap}.tools input{flex:1;min-width:160px}.tools select{width:auto}
.tbl{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;padding:10px;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.5px;border-bottom:2px solid var(--line)}
td{padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:middle}tr:hover td{background:#FFFBF5}
td small{color:var(--mut)}
.chip{padding:4px 10px;border-radius:99px;font-size:12px;font-weight:700;display:inline-block}
.chip.Baru{background:#E6F2F2;color:var(--teal)}.chip.Selesai{background:#E4F5EA;color:var(--grn)}
.chip.Paket{background:#FFF1E6;color:var(--or)}.chip.Dus{background:#EEF0F6;color:var(--ink)}
details summary{cursor:pointer;color:var(--teal);font-size:13px;margin-top:4px}
.mlist{margin:6px 0 0 18px;font-size:13px;color:var(--mut)}
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
.pk{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.pk label,.px label{margin:0;color:var(--ink);font-size:inherit}
.pk input,.px input[type=radio]{position:absolute;opacity:0;pointer-events:none;width:auto}
.pk .box{display:block;padding:16px;border:2px solid var(--line);border-radius:16px;cursor:pointer;background:#fff;transition:.15s}
.pk .box b{font-size:17px;display:block}.pk .box span{color:var(--mut);font-size:13px;font-weight:500}
.pk input:checked+.box{border-color:var(--or);background:#FFF1E6;box-shadow:0 6px 18px rgba(232,89,12,.18)}
.px{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px}
.px .box{display:block;text-align:center;padding:14px 8px;border:2px solid var(--line);border-radius:14px;cursor:pointer;background:#fff;transition:.15s}
.px .box b{font-size:22px;display:block;line-height:1.1}.px .box small{color:var(--mut);font-size:12px;font-weight:600}
.px .box:hover{border-color:var(--or2)}
.px input:checked+.box{border-color:var(--or);background:var(--or);color:#fff;box-shadow:0 6px 18px rgba(232,89,12,.3)}
.px input:checked+.box small{color:#ffe8d6}
.px input:focus-visible+.box,.pk input:focus-visible+.box{outline:3px solid var(--or2)}
.step{display:flex;align-items:center;gap:10px;margin:22px 0 10px;font-size:18px}
.step i{font-style:normal;width:30px;height:30px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:14px;font-weight:800}
.rinci{font-size:13px;color:var(--mut);margin-top:2px}
.sum{position:sticky;bottom:10px;box-shadow:0 8px 28px rgba(20,33,61,.18);border:1px solid #F3D9BF}
textarea{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:10px;font-size:15px;font-family:inherit;background:#fff;color:var(--ink);resize:vertical}
textarea:focus{outline:2px solid var(--or2);border-color:var(--or2)}
.hero.center{text-align:center;padding:36px 0 12px}
.ok-ic{font-size:56px;display:inline-block;animation:bob 2.4s ease-in-out infinite}
.kv{display:grid;grid-template-columns:150px 1fr;gap:8px 14px;font-size:15px;margin:14px 0}.kv dt{color:var(--mut);font-weight:600}
@media(max-width:560px){.kv{grid-template-columns:1fr}.kv dt{margin-top:6px}}
.login{min-height:100vh;display:grid;place-items:center;padding:20px;background:radial-gradient(circle at 20% 20%,#2a3f6d,#0F1B2D 60%)}
.login .box{width:min(400px,100%);background:#fff;border-radius:22px;padding:32px;box-shadow:0 30px 80px rgba(0,0,0,.4);animation:up .6s both}
.login h1{font-size:28px}.login .logo{font-size:46px;display:inline-block;animation:bob 2.4s ease-in-out infinite}
.login p{color:var(--mut);margin:4px 0 12px}
</style></head><body>
{% block body %}{% endblock %}
<div id="toasts"></div>
<script>
function toast(m,t){var d=document.createElement('div');d.className='toast '+(t||'');d.textContent=m;document.getElementById('toasts').appendChild(d);setTimeout(function(){d.style.opacity=0;d.style.transition='.4s';setTimeout(function(){d.remove()},400)},4500)}
function rp(n){return 'Rp'+Math.round(n).toLocaleString('id-ID')}
function initPaket(form){
 var tamb=+form.dataset.tambahan,defMax=+form.dataset.max;
 var boxes=form.querySelectorAll('input[name=menu]'),pax=form.querySelectorAll('input[name=pax_paket]'),
  paket=form.querySelectorAll('input[name=paket]'),extra=form.querySelector('[name=pax_tambahan]'),
  btn=form.querySelector('[data-submit]'),cnt=form.querySelector('.cnt'),tot=form.querySelector('.tot'),rin=form.querySelector('.rinci');
 function sel(list){for(var i=0;i<list.length;i++){if(list[i].checked)return list[i]}return null}
 function upd(){
  var pk=sel(paket),max=pk?+pk.dataset.menu:defMax,n=0;
  boxes.forEach(function(b){if(b.checked)n++});
  boxes.forEach(function(b){var off=(n>=max&&!b.checked);b.disabled=off;b.parentNode.classList.toggle('off',off)});
  cnt.textContent='Menu dipilih '+n+'/'+max;cnt.style.color=(n===max)?'var(--grn)':'var(--or)';
  var px=sel(pax),e=Math.max(0,parseInt(extra.value,10)||0),base=px?+px.dataset.harga:0;
  tot.textContent=rp(base+e*tamb);
  if(rin)rin.textContent=px?(px.value+' pax paket'+(e?' + '+e+' pax tambahan':'')+' = '+((+px.value)+e)+' pax'):'Pilih jumlah pax';
  btn.disabled=!(n===max&&px&&(!paket.length||pk))}
 boxes.forEach(function(b){b.addEventListener('change',upd)});
 pax.forEach(function(r){r.addEventListener('change',upd)});
 paket.forEach(function(r){r.addEventListener('change',upd)});
 extra.addEventListener('input',upd);upd()}
{% for c,m in get_flashed_messages(with_categories=true) %}toast({{ m|tojson }},{{ c|tojson }});{% endfor %}
</script>
{% block script %}{% endblock %}
</body></html>"""

MACROS = r"""{% macro pilih_pax(terpilih) %}
<div class="px">{% for p in PILIHAN_PAX %}<label><input type="radio" name="pax_paket" value="{{ p }}" data-harga="{{ HARGA_PILIHAN[p] }}" {% if terpilih==p %}checked{% endif %} required><span class="box"><b>{{ p }}</b><small>pax · {{ HARGA_PILIHAN[p]|rupiah }}</small></span></label>{% endfor %}</div>
{% endmacro %}
{% macro pilih_menu(menu, terpilih) %}
{% for kat, items in menu.items() %}<div class="cat"><h5>{{ kat }}</h5><div class="menu-grid">
{% for m in items %}<label class="opt"><input type="checkbox" name="menu" value="{{ m }}" {% if m in terpilih %}checked{% endif %}>{{ m }}</label>{% endfor %}
</div></div>{% endfor %}
{% endmacro %}"""

LOGIN = r"""{% extends "base.html" %}{% block title %}Masuk · CateringKu{% endblock %}
{% block body %}<div class="login"><form class="box" method="post">
<div class="logo">🍱</div><h1>CateringKu</h1><p>Masuk sebagai pemilik / admin catering</p>
<label>Username</label><input name="username" autofocus required>
<label>Password</label><input name="password" type="password" required>
<button class="btn" style="width:100%;margin-top:18px">Masuk</button>
</form></div>{% endblock %}"""

DASH = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu %}{% block title %}Dashboard · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div><div class="sp"></div>
<div class="clock" id="clock"></div><a class="btn ghost sm" href="/" target="_blank">Halaman pemesanan ↗</a>
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

<div class="card"><h3>➕ Tambah pesanan dus manual</h3>
<p style="color:var(--mut);font-size:14px;margin:4px 0 8px">Pesanan paket masuk otomatis dari halaman pemesanan pembeli. Form ini untuk pesanan dus yang dicatat sendiri.</p>
<form id="f-dus" method="post" action="/tambah_dus">
<div class="info">Pesanan lainnya (nasi dus / box): jumlah porsi dan harga bebas sesuai kesepakatan</div>
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" required></div>
<div><label>Menu dus</label><input name="menu" placeholder="mis. Nasi Dus Ayam Goreng" required></div>
<div><label>Jumlah porsi</label><input name="jumlah" id="d-jumlah" type="number" min="1" required></div>
<div><label>Harga per dus (Rp)</label><input name="harga" id="d-harga" type="number" min="1" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date"></div></div>
<div class="sum"><span>Total pesanan</span><span><b id="d-total">Rp0</b></span>
<button class="btn">Simpan pesanan dus</button></div></form>
</div>

<div class="card"><h3 style="margin-bottom:12px">📋 Daftar pesanan</h3>
<form class="tools" method="get"><input name="q" value="{{ q }}" placeholder="Cari pelanggan atau menu...">
<select name="status"><option value="">Semua status</option><option {% if st=='Baru' %}selected{% endif %}>Baru</option><option {% if st=='Selesai' %}selected{% endif %}>Selesai</option></select>
<button class="btn sm">Cari</button></form>
<div class="tbl"><table><tr><th>Pelanggan</th><th>Pesanan</th><th>Porsi/Pax</th><th>Total</th><th>Tanggal</th><th>Status</th><th>Aksi</th></tr>
{% for r in rows %}<tr>
<td><b>{{ r.pelanggan }}</b>{% if r.no_hp %}<br><small>📞 <a href="https://wa.me/{{ '62' + r.no_hp[1:] if r.no_hp.startswith('0') else r.no_hp }}" target="_blank">{{ r.no_hp }}</a></small>{% endif %}{% if r.alamat %}<br><small>📍 {{ r.alamat }}</small>{% endif %}{% if r.catatan %}<br><small>📝 {{ r.catatan }}</small>{% endif %}</td>
<td>{% if r.jenis=='Paket' %}<b>Paket Prasmanan</b> <span class="chip Paket">Paket</span>
<details><summary>Lihat {{ r.pilihan_menu|daftar|length }} menu</summary><ul class="mlist">{% for m in r.pilihan_menu|daftar %}<li>{{ m }}</li>{% endfor %}</ul></details>
{% else %}{{ r.menu }} <span class="chip Dus">Dus</span>{% endif %}</td>
<td>{{ r.jumlah }}{% if r.jenis=='Paket' and r.pax_tambahan %}<br><small>{{ r.pax_paket }} paket + {{ r.pax_tambahan }} tambahan</small>{% endif %}</td>
<td>{{ r.total|rupiah }}<br><small>{% if r.jenis=='Paket' %}{{ r.pax_paket }} pax paket{% if r.pax_tambahan %} + {{ r.pax_tambahan }} × {{ HARGA_TAMBAHAN|rupiah }}{% endif %}{% else %}{{ r.harga_satuan|rupiah }} / dus{% endif %}</small></td>
<td>{{ r.tanggal_acara|tgl }}{% if r.pengingat %}<span class="tag {{ r.pengingat }}">{{ 'BESOK' if r.pengingat=='besok' else 'HARI INI' }}</span>{% endif %}</td>
<td><span class="chip {{ r.status }}">{{ r.status }}</span></td>
<td><div class="act">
{% if r.status=='Baru' %}<form method="post" action="/status/{{ r.id }}"><button class="btn sm grn">Selesai</button></form>{% endif %}
<a class="btn sm line" href="/edit/{{ r.id }}">Edit</a>
<form method="post" action="/hapus/{{ r.id }}" onsubmit="return confirm('Hapus pesanan ini?')"><button class="btn sm red">Hapus</button></form></div></td>
</tr>{% else %}<tr><td colspan="7" class="empty">Belum ada pesanan. Pesanan dari pembeli akan muncul di sini 🍽️</td></tr>{% endfor %}
</table></div></div></div>
{% endblock %}
{% block script %}<script>
function dusTotal(){document.getElementById('d-total').textContent=rp((+document.getElementById('d-jumlah').value||0)*(+document.getElementById('d-harga').value||0))}
document.getElementById('d-jumlah').oninput=dusTotal;document.getElementById('d-harga').oninput=dusTotal;
document.querySelectorAll('.count').forEach(function(el){var n=+el.dataset.n,isrp=el.dataset.rp,t0=performance.now();
function f(v){return isrp?rp(v):Math.round(v)}
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

EDIT = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu, pilih_pax %}{% block title %}Edit pesanan · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div><div class="sp"></div><a class="btn ghost sm" href="/admin">← Kembali</a></div></div>
<div class="wrap" style="max-width:860px;padding-top:28px">
{% if p.jenis=='Paket' %}
<form class="card" id="f-edit" method="post" data-max="{{ JUMLAH_MENU }}" data-tambahan="{{ HARGA_TAMBAHAN }}">
<h3>✏️ Edit paket prasmanan #{{ p.id }}</h3>
<div class="fields">
<div><label>Nama pemesan</label><input name="pelanggan" value="{{ p.pelanggan }}" required></div>
<div><label>No. HP / WhatsApp</label><input name="no_hp" value="{{ p.no_hp or '' }}" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date" value="{{ p.tanggal_acara.isoformat() if p.tanggal_acara else '' }}"></div></div>
<label>Alamat pengiriman</label><textarea name="alamat" rows="2" required>{{ p.alamat or '' }}</textarea>
<label>Catatan</label><textarea name="catatan" rows="2">{{ p.catatan or '' }}</textarea>
<label>Jumlah pax paket</label>{{ pilih_pax(p.pax_paket) }}
<div class="fields"><div><label>Pax tambahan (+{{ HARGA_TAMBAHAN|rupiah }} / pax)</label><input name="pax_tambahan" type="number" min="0" value="{{ p.pax_tambahan or 0 }}"></div></div>
{{ pilih_menu(MENU_PAKET, p.pilihan_menu|daftar) }}
<div class="sum"><span><span class="cnt"></span><div class="rinci"></div></span><span>Total: <b class="tot">Rp0</b></span>
<span style="display:flex;gap:8px"><button class="btn" data-submit>Simpan perubahan</button><a class="btn line" href="/admin">Batal</a></span></div>
</form>
{% else %}
<form class="card" method="post"><h3>✏️ Edit pesanan dus #{{ p.id }}</h3>
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" value="{{ p.pelanggan }}" required></div>
<div><label>Menu dus</label><input name="menu" value="{{ p.menu }}" required></div>
<div><label>Jumlah porsi</label><input name="jumlah" type="number" min="1" value="{{ p.jumlah }}" required></div>
<div><label>Harga per dus (Rp)</label><input name="harga" type="number" min="1" value="{{ p.harga_satuan }}" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date" value="{{ p.tanggal_acara.isoformat() if p.tanggal_acara else '' }}"></div></div>
<div style="display:flex;gap:8px;margin-top:16px"><button class="btn" style="flex:1">Simpan perubahan</button><a class="btn line" href="/admin">Batal</a></div>
</form>
{% endif %}
</div>{% endblock %}
{% block script %}{% if p.jenis=='Paket' %}<script>initPaket(document.getElementById('f-edit'));</script>{% endif %}{% endblock %}"""


ORDER = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu, pilih_pax %}{% block title %}Pesan Catering · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div><div class="sp"></div><a class="btn ghost sm" href="/login">Admin</a></div></div>
<div class="wrap" style="max-width:860px">
<div class="hero center"><h1>Pesan Catering Prasmanan</h1><p>Pilih paket, tentukan jumlah pax, pilih menu, lalu isi data pemesan.</p></div>
<form id="f-order" method="post" action="/pesan" data-max="{{ JUMLAH_MENU }}" data-tambahan="{{ HARGA_TAMBAHAN }}">

<div class="card"><h3 class="step"><i>1</i>Pilih paket</h3>
<div class="pk">{% for k,p in PAKET.items() %}<label><input type="radio" name="paket" value="{{ k }}" data-menu="{{ p.jumlah_menu }}" {% if loop.first %}checked{% endif %} required><span class="box"><b>🍽️ {{ p.nama }}</b><span>{{ p.deskripsi }}</span></span></label>{% endfor %}</div></div>

<div class="card"><h3 class="step"><i>2</i>Jumlah pax</h3>
{{ pilih_pax(None) }}
<div class="fields" style="margin-top:6px"><div><label>Tambah pax (opsional) · {{ HARGA_TAMBAHAN|rupiah }} / pax</label>
<input name="pax_tambahan" type="number" min="0" step="1" value="0" inputmode="numeric"></div></div></div>

<div class="card"><h3 class="step"><i>3</i>Pilih menu</h3>
<div class="info">Pilih tepat {{ JUMLAH_MENU }} menu dari daftar di bawah</div>
{{ pilih_menu(MENU_PAKET, []) }}</div>

<div class="card"><h3 class="step"><i>4</i>Data pemesan</h3>
<div class="fields">
<div><label>Nama lengkap</label><input name="pelanggan" autocomplete="name" required></div>
<div><label>No. HP / WhatsApp</label><input name="no_hp" type="tel" inputmode="tel" autocomplete="tel" placeholder="08xxxxxxxxxx" required></div>
<div><label>Tanggal acara</label><input name="tanggal" id="tgl" type="date" required></div></div>
<label>Alamat pengiriman</label><textarea name="alamat" rows="2" autocomplete="street-address" required></textarea>
<label>Catatan (opsional)</label><textarea name="catatan" rows="2" placeholder="mis. jam antar, alergi, permintaan khusus"></textarea></div>

<div class="sum"><span><span class="cnt">Menu dipilih 0/{{ JUMLAH_MENU }}</span><div class="rinci">Pilih jumlah pax</div></span>
<span>Total: <b class="tot">Rp0</b></span><button class="btn" data-submit disabled>Pesan sekarang</button></div>
</form></div>{% endblock %}
{% block script %}<script>
initPaket(document.getElementById('f-order'));
var t=document.getElementById('tgl'),d=new Date();d.setMinutes(d.getMinutes()-d.getTimezoneOffset());t.min=d.toISOString().slice(0,10);
</script>{% endblock %}"""

THANKS = r"""{% extends "base.html" %}{% block title %}Pesanan diterima · CateringKu{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>🍱</span>CateringKu</div></div></div>
<div class="wrap" style="max-width:720px">
<div class="hero center"><div class="ok-ic">✅</div><h1>Pesanan diterima!</h1><p>Terima kasih, {{ p.pelanggan }}. Kami akan menghubungi Anda lewat WhatsApp untuk konfirmasi.</p></div>
<div class="card"><h3>Ringkasan pesanan #{{ p.id }}</h3>
<dl class="kv">
<dt>Paket</dt><dd>{{ p.menu }}</dd>
<dt>Jumlah pax</dt><dd>{{ p.jumlah }} pax ({{ p.pax_paket }} paket{% if p.pax_tambahan %} + {{ p.pax_tambahan }} tambahan{% endif %})</dd>
<dt>Tanggal acara</dt><dd>{{ p.tanggal_acara|tgl }}</dd>
<dt>No. HP</dt><dd>{{ p.no_hp }}</dd>
<dt>Alamat</dt><dd>{{ p.alamat }}</dd>
{% if p.catatan %}<dt>Catatan</dt><dd>{{ p.catatan }}</dd>{% endif %}
<dt>Menu dipilih</dt><dd><ul class="mlist" style="margin-top:0">{% for m in p.pilihan_menu|daftar %}<li>{{ m }}</li>{% endfor %}</ul></dd>
<dt>Total</dt><dd><b style="font-size:20px">{{ p.total|rupiah }}</b></dd>
</dl>
<a class="btn" href="/">Buat pesanan lagi</a></div></div>{% endblock %}"""

TEMPLATES = {"base.html": BASE, "macros.html": MACROS, "login.html": LOGIN, "dashboard.html": DASH, "edit.html": EDIT, "order.html": ORDER, "thanks.html": THANKS}