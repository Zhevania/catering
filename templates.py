BASE = r"""<!doctype html>
<html lang="id"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{% block title %}QueenCatering{% endblock %}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#1E1429;--bg:#F6F3F8;--card:#fff;--line:#E6DFEC;--or:#E8590C;--or2:#F4A261;--plum:#34103F;--plum2:#4B1B5B;--gold:#E0A526;--teal:#1C7C7D;--mut:#6B6577;--red:#D62839;--grn:#2E9E5B}
*{box-sizing:border-box;margin:0;padding:0}
[hidden]{display:none!important}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);min-height:100vh}
a{color:inherit;text-decoration:none}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px 40px}
.nav{background:linear-gradient(120deg,#2A0D34,#4B1B5B);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 4px 20px rgba(42,13,52,.3)}
.nav .wrap{display:flex;align-items:center;gap:14px;height:64px;padding-bottom:0}
.brand{font-weight:800;font-size:22px;letter-spacing:.3px;display:flex;align-items:center;gap:8px}
.brand span{display:inline-block;animation:bob 2.4s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-4deg)}50%{transform:translateY(-4px) rotate(4deg)}}
.sp{flex:1}.clock{font-size:14px;color:#e4d6ec;font-variant-numeric:tabular-nums}
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
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 2px 10px rgba(52,16,63,.05);animation:up .5s both;margin-bottom:16px}
@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.stat{display:flex;gap:14px;align-items:center;transition:transform .2s;margin-bottom:0}.stat:hover{transform:translateY(-4px)}
.stat .ic{width:52px;height:52px;border-radius:14px;display:grid;place-items:center;font-size:26px;background:#F3EAF7}
.stat b{font-size:26px;display:block;line-height:1.1}.stat small{color:var(--mut)}
.alert{border-radius:16px;padding:16px 18px;margin:8px 0;display:flex;gap:12px;align-items:flex-start;animation:up .5s both}
.alert.besok{background:#FFF4E0;border:1px solid #F6C26B}.alert.hari{background:#FDE8EA;border:1px solid #F3A5AD}
.alert .big{font-size:28px;animation:ring 2s ease-in-out infinite}
.alert ul{margin-top:6px;padding-left:18px}
label{font-size:13px;font-weight:700;color:var(--mut);display:block;margin:10px 0 4px}
input,select,textarea{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:10px;font-size:15px;background:#fff;color:var(--ink);font-family:inherit}
textarea{resize:vertical}
input:focus,select:focus,textarea:focus{outline:2px solid var(--or2);border-color:var(--or2)}
.fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 14px}
.full{grid-column:1/-1}
.tabs{display:flex;gap:8px;margin:12px 0 16px;flex-wrap:wrap}
.tab{border:1px solid var(--line);background:#fff;padding:10px 16px;border-radius:12px;font-weight:700;cursor:pointer;font-size:14px;color:var(--ink)}
.tab.active{background:var(--plum);color:#fff;border-color:var(--plum)}
.info{background:#F3EAF7;color:var(--plum);padding:10px 14px;border-radius:12px;font-size:14px;font-weight:600}
.sum{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-top:16px;padding:12px 16px;background:#FBF6EC;border-radius:12px}
.sum b{font-size:20px}.cnt{font-weight:800;color:var(--or)}.cnt.ok{color:var(--grn)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips.pick{margin:8px 0 4px}
.pill{background:#EFE9F4;color:var(--plum);padding:8px 14px;border-radius:99px;font-size:14px}
.chip-opt{position:relative;margin:0;cursor:pointer}
.chip-opt input{position:absolute;opacity:0;width:1px;height:1px}
.chip-opt span{display:inline-block;background:#EFE9F4;color:var(--plum);padding:9px 16px;border-radius:99px;font-size:14px;font-weight:600;border:2px solid transparent;transition:.15s;user-select:none}
.chip-opt:hover span{border-color:var(--gold)}
.chip-opt input:checked + span{background:var(--plum);color:#fff}
.chip-opt input:focus-visible + span{outline:2px solid var(--gold)}
.chip-opt.off{opacity:.4;cursor:not-allowed}
.tools{display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap}.tools input{flex:1;min-width:160px}.tools select{width:auto}
.tbl{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;padding:10px;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.5px;border-bottom:2px solid var(--line)}
td{padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:middle}tr:hover td{background:#FCFAFD}
td small{color:var(--mut)}
.chip{padding:4px 10px;border-radius:99px;font-size:12px;font-weight:700;display:inline-block}
.chip.Baru{background:#E6F2F2;color:var(--teal)}.chip.Selesai{background:#E4F5EA;color:var(--grn)}
.chip.Paket{background:#F3EAF7;color:var(--plum)}.chip.Dus{background:#EEF0F6;color:var(--ink)}
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
.toast{background:var(--plum);color:#fff;padding:12px 16px;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.3);animation:up .3s both;max-width:320px;font-size:14px}
.toast.ok{background:var(--grn)}.toast.error{background:var(--red)}.toast.warn{background:var(--or)}
.login{min-height:100vh;display:grid;place-items:center;padding:20px;background:radial-gradient(circle at 20% 20%,#6a2c80,#34103F 60%)}
.login .box{width:min(400px,100%);background:#fff;border-radius:22px;padding:32px;box-shadow:0 30px 80px rgba(0,0,0,.4);animation:up .6s both}
.login h1{font-size:28px}.login .logo{font-size:46px;display:inline-block;animation:bob 2.4s ease-in-out infinite}
.login p{color:var(--mut);margin:4px 0 12px}
.bar{position:sticky;bottom:12px;z-index:15;background:var(--plum);color:#fff;border-radius:16px;padding:14px 18px;display:flex;gap:14px;align-items:center;justify-content:space-between;flex-wrap:wrap;box-shadow:0 14px 40px rgba(42,13,52,.4);margin-top:24px}
.bar .tot{font-size:24px;font-weight:800}.bar .cnt{color:#F4C95D}.bar .cnt.ok{color:#7ee2a8}
.kode{display:inline-block;margin:10px 0;padding:10px 22px;border:2px dashed var(--gold);border-radius:14px;font-size:28px;font-weight:800;letter-spacing:2px;color:var(--plum)}
.kv td:first-child{color:var(--mut);width:34%}
/* ===== Tampilan pembeli ===== */
.q{font-family:"DM Sans",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.q input:focus,.q textarea:focus,.q select:focus{outline:2px solid var(--gold);border-color:var(--gold)}
.qwrap{max-width:1000px;margin:0 auto;padding:0 20px}
.qhead{background:var(--plum);color:#fff}
.qtop{display:flex;align-items:center;justify-content:space-between;padding:22px 0 6px}
.q .qbrand,.q .qh1,.q .qpax,.q .qcard h3,.q .qsec h2{font-family:"Playfair Display",Georgia,serif}
.qbrand{font-size:34px;font-weight:700;color:#fff;letter-spacing:.2px}.qbrand span{color:var(--gold)}
.qbtn{display:inline-flex;align-items:center;justify-content:center;background:var(--gold);color:#2A0E33;border:0;border-radius:10px;padding:12px 20px;font-weight:700;font-size:16px;cursor:pointer;transition:.15s;font-family:inherit}
.qbtn:hover{transform:translateY(-2px);box-shadow:0 8px 18px rgba(224,165,38,.35)}
.qbtn:disabled{background:#cfc8d6;color:#7b7385;cursor:not-allowed;transform:none;box-shadow:none}
.qtabs{display:flex;gap:6px}
.qtabs a{padding:12px 20px 14px;color:#e4d6ec;font-weight:700;border-bottom:3px solid transparent}
.qtabs a.on{color:#fff;border-bottom-color:var(--gold)}
.qh1{font-size:38px;margin:44px 0 10px;line-height:1.15}
.qsub{color:var(--mut);margin-bottom:26px}
.qerr{background:#FDE8EA;border:1px solid #F3A5AD;border-radius:14px;padding:14px 18px;margin-bottom:18px;font-weight:700}
.qcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:20px;align-items:stretch}
.qcard{position:relative;display:block;margin:0;cursor:pointer;color:var(--ink);font-size:16px;font-weight:400}
.qcard>input{position:absolute;opacity:0;pointer-events:none;width:1px;height:1px}
.qcard-in{height:100%;background:#fff;border:2px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;transition:.2s}
.qcard:hover .qcard-in{transform:translateY(-4px);box-shadow:0 14px 30px rgba(52,16,63,.12)}
.qcard>input:checked + .qcard-in{border-color:var(--plum);box-shadow:0 14px 34px rgba(52,16,63,.2)}
.qpax{font-size:52px;font-weight:700;color:var(--plum);line-height:1}.qpax small{font-size:18px;color:var(--mut);font-weight:600}
.qcard h3{font-size:22px}
.qprice b{font-size:20px;color:var(--ink)}.qprice span{color:var(--mut)}
.qdesc{color:var(--mut);min-height:44px}
.qcard h4{margin-top:6px;font-size:16px}
.qpick{margin-top:auto;text-align:center;padding:12px;border-radius:12px;font-weight:700}
.qpick.off{border:2px solid var(--plum);color:var(--plum)}
.qpick.on{display:none;background:var(--plum);color:#fff}
.qcard>input:checked + .qcard-in .qpick.off{display:none}
.qcard>input:checked + .qcard-in .qpick.on{display:block}
.qsec{margin-top:40px}.qsec h2{font-size:26px;margin-bottom:6px}
.qsec .hint{color:var(--mut);margin-bottom:12px}
.cek{display:flex;gap:8px;max-width:520px}.cek input{flex:1}
@media print{.nav,.qhead,.noprint{display:none!important}}
</style></head><body class="{% block bodyclass %}{% endblock %}">
{% block body %}{% endblock %}
<div id="toasts"></div>
<script>
function toast(m,t){var d=document.createElement('div');d.className='toast '+(t||'');d.textContent=m;document.getElementById('toasts').appendChild(d);setTimeout(function(){d.style.opacity=0;d.style.transition='.4s';setTimeout(function(){d.remove()},400)},4500)}
function rp(n){return 'Rp '+Math.round(n).toLocaleString('id-ID')}
function initPaketForm(form){
 var sets=form.querySelectorAll('.menu-set'),btn=form.querySelector('[data-submit]'),cnt=form.querySelector('.cnt'),tot=form.querySelector('.tot'),label=form.querySelector('.paket-txt'),judul=form.querySelector('.menu-judul');
 function pilih(){var r=form.querySelector('input[name=paket]:checked');if(r)return r;var s=form.querySelector('select[name=paket]');return(s&&s.value)?s.options[s.selectedIndex]:null}
 function upd(){
  var p=pilih(),key=p?p.value:'',max=p?+p.dataset.jumlah:0,n=0;
  sets.forEach(function(s){var on=(s.dataset.paket===key);s.hidden=!on;s.querySelectorAll('input').forEach(function(i){i.disabled=!on;if(!on)i.checked=false})});
  var act=form.querySelectorAll('.menu-set:not([hidden]) input[name=menu]');
  act.forEach(function(b){if(b.checked)n++});
  act.forEach(function(b){var off=(n>=max&&!b.checked);b.disabled=off;b.closest('.chip-opt').classList.toggle('off',off)});
  if(cnt){cnt.textContent=p?('Menu dipilih '+n+'/'+max):'Pilih paket dulu';cnt.classList.toggle('ok',!!p&&n===max)}
  if(tot)tot.textContent=p?rp(+p.dataset.pax*+p.dataset.harga):'Rp 0';
  if(label)label.textContent=p?(p.dataset.nama+' · '+p.dataset.pax+' pax'):'Pilih paket';
  if(judul)judul.textContent=p?('Pilih '+max+' menu untuk '+p.dataset.nama):'Pilih paket terlebih dahulu';
  if(btn)btn.disabled=!(p&&n===max)}
 form.addEventListener('change',upd);upd()}
{% for c,m in get_flashed_messages(with_categories=true) %}toast({{ m|tojson }},{{ c|tojson }});{% endfor %}
</script>
{% block script %}{% endblock %}
</body></html>"""

MACROS = r"""{% macro pilih_menu(paket, terpilih, aktif) %}
{% for kode, p in paket.items() %}<div class="menu-set" data-paket="{{ kode }}"{% if kode != aktif %} hidden{% endif %}>
<div class="chips pick">{% for m in p.menu %}<label class="chip-opt"><input type="checkbox" name="menu" value="{{ m }}"{% if kode == aktif and m in terpilih %} checked{% endif %}{% if kode != aktif %} disabled{% endif %}><span>{{ m }}</span></label>{% endfor %}</div>
</div>{% endfor %}
{% endmacro %}"""

LOGIN = r"""{% extends "base.html" %}{% block title %}Login Admin · QueenCatering{% endblock %}
{% block body %}<div class="login"><form class="box" method="post">
<div class="logo">👑</div><h1>QueenCatering</h1><p>Login pemilik / admin catering</p>
<label>Username</label><input name="username" autofocus required>
<label>Password</label><input name="password" type="password" required>
<button class="btn" style="width:100%;margin-top:18px">Masuk</button>
<p style="text-align:center;margin-top:14px"><a href="/" style="color:var(--plum);font-weight:700">← Kembali ke halaman pembeli</a></p>
</form></div>{% endblock %}"""

DASH = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu %}{% block title %}Dashboard · QueenCatering{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>👑</span>QueenCatering</div><div class="sp"></div>
<div class="clock" id="clock"></div>
<button class="bell {% if notif %}ring{% endif %}" id="bell" title="Pemberitahuan">🔔<span class="badge" id="badge"></span></button>
<a class="btn ghost sm" href="/">Halaman pembeli</a><a class="btn ghost sm" href="/logout">Keluar ({{ user }})</a></div></div>
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

<div class="card"><h3>➕ Pesanan baru</h3>
<div class="tabs"><button type="button" class="tab active" data-t="paket">🍽️ Paket Catering</button><button type="button" class="tab" data-t="dus">📦 Pesanan Lainnya (Dus)</button></div>

<form id="f-paket" method="post" action="/tambah_paket">
<div class="info">Pilih paket, lalu pilih menu sesuai jumlah yang ditentukan paket</div>
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" required></div>
<div><label>Paket</label><select name="paket" required><option value="" selected disabled>Pilih paket</option>
{% for kode, p in PAKET.items() %}<option value="{{ kode }}" data-pax="{{ p.pax }}" data-harga="{{ p.harga }}" data-jumlah="{{ p.jumlah_menu }}" data-nama="{{ p.nama }}">{{ p.nama }} · {{ p.pax }} pax · {{ (p.pax*p.harga)|rupiah }}</option>{% endfor %}</select></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date"></div></div>
<h4 class="menu-judul" style="margin:16px 0 4px"></h4>
{{ pilih_menu(PAKET, [], '') }}
<div class="sum"><span class="cnt">Pilih paket dulu</span><span>Total: <b class="tot">Rp 0</b></span>
<button class="btn" data-submit disabled>Simpan pesanan paket</button></div></form>

<form id="f-dus" method="post" action="/tambah_dus" hidden>
<div class="info">Pesanan lainnya (nasi dus / box): jumlah porsi dan harga bebas sesuai kesepakatan</div>
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" required></div>
<div><label>Menu dus</label><input name="menu" placeholder="mis. Nasi Dus Ayam Goreng" required></div>
<div><label>Jumlah porsi</label><input name="jumlah" id="d-jumlah" type="number" min="1" required></div>
<div><label>Harga per dus (Rp)</label><input name="harga" id="d-harga" type="number" min="1" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date"></div></div>
<div class="sum"><span>Total pesanan</span><span><b id="d-total">Rp 0</b></span>
<button class="btn">Simpan pesanan dus</button></div></form>
</div>

<div class="card"><h3 style="margin-bottom:12px">📋 Daftar pesanan</h3>
<form class="tools" method="get"><input name="q" value="{{ q }}" placeholder="Cari nama, menu, kode, atau nomor...">
<select name="status"><option value="">Semua status</option><option {% if st=='Baru' %}selected{% endif %}>Baru</option><option {% if st=='Selesai' %}selected{% endif %}>Selesai</option></select>
<button class="btn sm">Cari</button></form>
<div class="tbl"><table><tr><th>Pelanggan</th><th>Pesanan</th><th>Porsi/Pax</th><th>Total</th><th>Tanggal</th><th>Status</th><th>Aksi</th></tr>
{% for r in rows %}<tr>
<td><b>{{ r.pelanggan }}</b>{% if r.sumber=='Online' %} <span class="chip Paket">Online</span>{% endif %}
{% if r.telepon %}<br><small><a href="https://wa.me/{{ r.telepon }}" target="_blank" rel="noopener">📱 {{ r.telepon }}</a></small>{% endif %}
{% if r.alamat %}<br><small>📍 {{ r.alamat }}</small>{% endif %}{% if r.jam_acara %}<br><small>🕒 {{ r.jam_acara }}</small>{% endif %}
{% if r.catatan %}<br><small>📝 {{ r.catatan }}</small>{% endif %}{% if r.kode %}<br><small>{{ r.kode }}</small>{% endif %}</td>
<td>{% if r.jenis=='Paket' %}<b>{{ r.menu }}</b> <span class="chip Paket">Paket</span>
<details><summary>Lihat {{ r.pilihan_menu|daftar|length }} menu</summary><ul class="mlist">{% for m in r.pilihan_menu|daftar %}<li>{{ m }}</li>{% endfor %}</ul></details>
{% else %}{{ r.menu }} <span class="chip Dus">Dus</span>{% endif %}</td>
<td>{{ r.jumlah }}</td>
<td>{{ r.total|rupiah }}<br><small>{{ r.harga_satuan|rupiah }} / {{ 'pax' if r.jenis=='Paket' else 'dus' }}</small></td>
<td>{{ r.tanggal_acara|tgl }}{% if r.pengingat %}<span class="tag {{ r.pengingat }}">{{ 'BESOK' if r.pengingat=='besok' else 'HARI INI' }}</span>{% endif %}</td>
<td><span class="chip {{ r.status }}">{{ r.status }}</span></td>
<td><div class="act">
{% if r.status=='Baru' %}<form method="post" action="/status/{{ r.id }}"><button class="btn sm grn">Selesai</button></form>{% endif %}
<a class="btn sm line" href="/edit/{{ r.id }}">Edit</a>
<form method="post" action="/hapus/{{ r.id }}" onsubmit="return confirm('Hapus pesanan ini?')"><button class="btn sm red">Hapus</button></form></div></td>
</tr>{% else %}<tr><td colspan="7" class="empty">Belum ada pesanan. Tambahkan lewat form di atas 🍽️</td></tr>{% endfor %}
</table></div></div></div>
{% endblock %}
{% block script %}<script>
initPaketForm(document.getElementById('f-paket'));
document.querySelectorAll('.tab').forEach(function(t){t.onclick=function(){
 document.querySelectorAll('.tab').forEach(function(x){x.classList.toggle('active',x===t)});
 document.getElementById('f-paket').hidden=(t.dataset.t!=='paket');
 document.getElementById('f-dus').hidden=(t.dataset.t!=='dus')}});
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
if('Notification' in window&&Notification.permission==='granted')new Notification('QueenCatering',{body:d.jumlah+' pesanan perlu disiapkan hari ini / besok'})}
last=d.jumlah}).catch(function(){})}
cek();setInterval(cek,30000);
</script>{% endblock %}"""

EDIT = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu %}{% block title %}Edit pesanan · QueenCatering{% endblock %}
{% block body %}
<div class="nav"><div class="wrap"><div class="brand"><span>👑</span>QueenCatering</div><div class="sp"></div><a class="btn ghost sm" href="/admin">← Kembali</a></div></div>
<div class="wrap" style="max-width:860px;padding-top:28px">
{% if p.jenis=='Paket' %}
<form class="card" id="f-edit" method="post">
<h3>✏️ Edit pesanan paket #{{ p.id }}</h3>
{% if not paket_key %}<div class="alert besok" style="margin-top:10px"><div><b>Pesanan ini memakai paket lama.</b> Pilih paket dan menu baru agar bisa disimpan.</div></div>{% endif %}
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" value="{{ p.pelanggan }}" required></div>
<div><label>Paket</label><select name="paket" required>{% if not paket_key %}<option value="" selected disabled>Pilih paket</option>{% endif %}
{% for kode, k in PAKET.items() %}<option value="{{ kode }}" data-pax="{{ k.pax }}" data-harga="{{ k.harga }}" data-jumlah="{{ k.jumlah_menu }}" data-nama="{{ k.nama }}"{% if kode==paket_key %} selected{% endif %}>{{ k.nama }} · {{ k.pax }} pax · {{ (k.pax*k.harga)|rupiah }}</option>{% endfor %}</select></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date" value="{{ p.tanggal_acara.isoformat() if p.tanggal_acara else '' }}"></div>
<div><label>Nomor WhatsApp pembeli</label><input name="telepon" value="{{ p.telepon or '' }}" placeholder="0812xxxxxxx"></div>
<div><label>Jam acara</label><input name="jam" type="time" value="{{ p.jam_acara or '' }}"></div>
<div class="full"><label>Alamat / lokasi acara</label><input name="alamat" value="{{ p.alamat or '' }}"></div>
<div class="full"><label>Catatan</label><input name="catatan" value="{{ p.catatan or '' }}"></div></div>
<h4 class="menu-judul" style="margin:16px 0 4px"></h4>
{{ pilih_menu(PAKET, p.pilihan_menu|daftar, paket_key) }}
<div class="sum"><span class="cnt"></span><span>Total: <b class="tot">Rp 0</b></span>
<span style="display:flex;gap:8px"><button class="btn" data-submit>Simpan perubahan</button><a class="btn line" href="/admin">Batal</a></span></div>
</form>
{% else %}
<form class="card" method="post"><h3>✏️ Edit pesanan dus #{{ p.id }}</h3>
<div class="fields">
<div><label>Nama pelanggan</label><input name="pelanggan" value="{{ p.pelanggan }}" required></div>
<div><label>Menu dus</label><input name="menu" value="{{ p.menu }}" required></div>
<div><label>Jumlah porsi</label><input name="jumlah" type="number" min="1" value="{{ p.jumlah }}" required></div>
<div><label>Harga per dus (Rp)</label><input name="harga" type="number" min="1" value="{{ p.harga_satuan }}" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date" value="{{ p.tanggal_acara.isoformat() if p.tanggal_acara else '' }}"></div>
<div><label>Nomor WhatsApp pembeli</label><input name="telepon" value="{{ p.telepon or '' }}" placeholder="0812xxxxxxx"></div>
<div><label>Jam acara</label><input name="jam" type="time" value="{{ p.jam_acara or '' }}"></div>
<div class="full"><label>Alamat / lokasi acara</label><input name="alamat" value="{{ p.alamat or '' }}"></div>
<div class="full"><label>Catatan</label><input name="catatan" value="{{ p.catatan or '' }}"></div></div>
<div style="display:flex;gap:8px;margin-top:16px"><button class="btn" style="flex:1">Simpan perubahan</button><a class="btn line" href="/admin">Batal</a></div>
</form>
{% endif %}
</div>{% endblock %}
{% block script %}{% if p.jenis=='Paket' %}<script>initPaketForm(document.getElementById('f-edit'));</script>{% endif %}{% endblock %}"""

BERANDA = r"""{% extends "base.html" %}{% from "macros.html" import pilih_menu %}{% block title %}QueenCatering · Paket Catering{% endblock %}
{% block bodyclass %}q{% endblock %}
{% block body %}
<header class="qhead"><div class="qwrap">
<div class="qtop"><a class="qbrand" href="/">Queen<span>Catering</span></a><a class="qbtn" href="/login">Login Admin</a></div>
<nav class="qtabs"><a class="on" href="#paket">Paket catering</a><a href="#cek">Cek pesanan</a></nav>
</div></header>

<main class="qwrap" id="paket" style="padding-bottom:40px">
<h1 class="qh1">Pilih paket sesuai jumlah tamu</h1>
<p class="qsub">Pilih paket berdasarkan jumlah pax, tentukan menu favoritmu, lalu isi tanggal acara. Pemesanan minimal {{ MIN_HARI }} hari sebelum acara.</p>

<form id="f-pesan" method="post" action="/pesan">
{% if error %}<div class="qerr">⚠️ {{ error }}</div>{% endif %}
<div class="qcards">
{% for kode, p in PAKET.items() %}<label class="qcard">
<input type="radio" name="paket" value="{{ kode }}" data-pax="{{ p.pax }}" data-harga="{{ p.harga }}" data-jumlah="{{ p.jumlah_menu }}" data-nama="{{ p.nama }}"{% if f.get('paket')==kode %} checked{% endif %} required>
<div class="qcard-in">
<div class="qpax">{{ p.pax }} <small>pax</small></div>
<h3>{{ p.nama }}</h3>
<div class="qprice"><b>{{ (p.pax*p.harga)|rupiah }}</b> <span>({{ p.harga|rupiah }}/pax)</span></div>
<p class="qdesc">{{ p.deskripsi }}</p>
<h4>Pilih {{ p.jumlah_menu }} menu dari:</h4>
<div class="chips">{% for m in p.menu %}<span class="pill">{{ m }}</span>{% endfor %}</div>
<span class="qpick off">Pilih paket ini</span><span class="qpick on">✓ Paket dipilih</span>
</div></label>{% endfor %}
</div>

<section class="qsec"><h2 class="menu-judul">Pilih paket terlebih dahulu</h2>
<p class="hint">Ketuk menu untuk memilih. Jumlah menu mengikuti paket yang kamu pilih.</p>
{{ pilih_menu(PAKET, terpilih, f.get('paket','')) }}</section>

<section class="qsec"><h2>Data pemesan</h2>
<div class="card" style="margin-top:12px"><div class="fields">
<div><label>Nama lengkap</label><input name="pelanggan" value="{{ f.get('pelanggan','') }}" required></div>
<div><label>Nomor WhatsApp</label><input name="telepon" type="tel" value="{{ f.get('telepon','') }}" placeholder="0812xxxxxxx" required></div>
<div><label>Tanggal acara</label><input name="tanggal" type="date" min="{{ min_tgl }}" value="{{ f.get('tanggal','') }}" required></div>
<div><label>Jam acara (opsional)</label><input name="jam" type="time" value="{{ f.get('jam','') }}"></div>
<div class="full"><label>Alamat / lokasi acara</label><textarea name="alamat" rows="2" required>{{ f.get('alamat','') }}</textarea></div>
<div class="full"><label>Catatan (opsional)</label><textarea name="catatan" rows="2" placeholder="mis. tanpa pedas, antar sebelum jam 10">{{ f.get('catatan','') }}</textarea></div>
</div>
<input name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true"></div></section>

<div class="bar"><div><div class="paket-txt" style="font-weight:800">Pilih paket</div><small class="cnt">Pilih paket dulu</small></div>
<div class="tot">Rp 0</div><button class="qbtn" data-submit disabled>Pesan sekarang</button></div>
</form>

<section class="qsec" id="cek"><h2>Cek pesanan</h2>
<p class="hint">Sudah memesan? Masukkan kode pesanan kamu (contoh: QC-7F3K9Q).</p>
<form class="cek" action="/cek" method="get"><input name="kode" placeholder="QC-XXXXXX" required><button class="qbtn">Cek</button></form></section>
<p style="text-align:center;color:var(--mut);margin-top:40px;font-size:13px">© QueenCatering</p>
</main>
{% endblock %}
{% block script %}<script>initPaketForm(document.getElementById('f-pesan'));</script>{% endblock %}"""

PESANAN = r"""{% extends "base.html" %}{% block title %}Pesanan {{ p.kode }} · QueenCatering{% endblock %}
{% block bodyclass %}q{% endblock %}
{% block body %}
<header class="qhead"><div class="qwrap"><div class="qtop"><a class="qbrand" href="/">Queen<span>Catering</span></a><a class="qbtn" href="/">← Pesan lagi</a></div><nav class="qtabs"><a class="on" href="#">Pesanan kamu</a></nav></div></header>
<div class="qwrap" style="max-width:760px;padding-top:28px;padding-bottom:40px">
<div class="card" style="text-align:center">
{% if p.status=='Baru' %}<div style="font-size:44px">✅</div><h2>Pesanan diterima</h2>{% else %}<div style="font-size:44px">🎉</div><h2>Pesanan selesai</h2>{% endif %}
<p style="color:var(--mut);margin-top:4px">Simpan kode ini untuk mengecek pesanan kamu:</p>
<div class="kode">{{ p.kode }}</div><br><span class="chip {{ p.status }}">Status: {{ p.status }}</span></div>

<div class="card"><h3 style="margin-bottom:10px">Ringkasan pesanan</h3>
<table class="kv">
<tr><td>Nama</td><td><b>{{ p.pelanggan }}</b></td></tr>
<tr><td>WhatsApp</td><td>{{ p.telepon }}</td></tr>
<tr><td>Tanggal acara</td><td>{{ p.tanggal_acara|tgl }}{% if p.jam_acara %} · {{ p.jam_acara }}{% endif %}</td></tr>
<tr><td>Alamat</td><td>{{ p.alamat }}</td></tr>
{% if p.catatan %}<tr><td>Catatan</td><td>{{ p.catatan }}</td></tr>{% endif %}
<tr><td>Paket</td><td>{{ p.menu }} · {{ p.jumlah }} pax × {{ p.harga_satuan|rupiah }}</td></tr>
<tr><td>Total</td><td><b style="font-size:20px;color:var(--plum)">{{ p.total|rupiah }}</b></td></tr>
</table></div>

<div class="card"><h3>Menu pilihan ({{ p.pilihan_menu|daftar|length }} menu)</h3>
<div class="chips" style="margin-top:12px">{% for m in p.pilihan_menu|daftar %}<span class="pill">{{ m }}</span>{% endfor %}</div></div>

<div class="card noprint"><h3>Langkah berikutnya</h3>
<p style="color:var(--mut);margin:8px 0 14px">Admin akan menghubungi kamu lewat WhatsApp di nomor {{ p.telepon }} untuk konfirmasi pesanan dan pembayaran.</p>
<div class="act"><button class="btn line" onclick="window.print()">🖨️ Cetak</button></div></div>
</div>{% endblock %}"""

TEMPLATES = {"base.html": BASE, "macros.html": MACROS, "login.html": LOGIN, "dashboard.html": DASH,
             "edit.html": EDIT, "beranda.html": BERANDA, "pesanan.html": PESANAN}