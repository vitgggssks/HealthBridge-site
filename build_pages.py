import base64, os

SITE = '/home/user/healthbridge_site'
os.makedirs(SITE, exist_ok=True)
hero_b64 = base64.b64encode(open(f'{SITE}/hero.jpg', 'rb').read()).decode()

CSS = """
:root{--p:#1E8E8A;--pd:#14726F;--pl:#EAF5F4;--bd:#DCEAE8;--tx:#1F2A29;--mu:#6B7A78;--g:#E9B824}
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
body{background:#F3F8F7;color:var(--tx)}
a{text-decoration:none;color:inherit}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.hdr{background:#fff;border-bottom:1px solid var(--bd);position:sticky;top:0;z-index:50}
.hdr-in{display:flex;align-items:center;gap:28px;height:64px}
.logo{display:flex;align-items:center;gap:8px;font-size:20px;font-weight:800;color:var(--p)}
.logo-ic{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,#2BB3AE,#1E8E8A);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px}
.logo small{display:block;font-size:9px;font-weight:500;color:var(--mu);letter-spacing:.2px;margin-top:1px}
.nav{display:flex;gap:4px;flex:1}
.nav a{padding:8px 14px;border-radius:9px;font-size:14px;font-weight:600;color:#33413F}
.nav a:hover{background:var(--pl)}
.nav a.act{color:var(--p);border-bottom:3px solid var(--p);border-radius:0;padding:8px 14px 5px}
.badge-n{background:#E24545;color:#fff;border-radius:50%;font-size:10px;padding:1px 5px;margin-left:4px;vertical-align:top}
.hdr-r{display:flex;align-items:center;gap:14px}
.lang{border:1px solid var(--bd);border-radius:9px;padding:5px 10px;font-size:13px;font-weight:600;cursor:pointer;background:#fff}
.prof{display:flex;align-items:center;gap:8px;cursor:pointer}
.avt{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#8FD4D0,#1E8E8A);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.hero{position:relative;color:#fff;background:linear-gradient(120deg,rgba(14,90,88,.55),rgba(20,110,105,.25)),url('HEROURI') center/cover no-repeat;min-height:520px;display:flex;align-items:center}
.hero-in{padding:56px 0;width:100%}
.kick{font-size:15px;font-weight:600;opacity:.95;margin-bottom:10px}
.hero h1{font-size:46px;line-height:1.12;font-weight:800;max-width:560px}
.hero h1 .hl{color:#7FE0D8}
.hero p.sub{margin-top:14px;font-size:16px;max-width:470px;opacity:.96;line-height:1.45}
.script{position:absolute;right:6%;top:34%;font-family:'Segoe Script','Brush Script MT',cursive;font-size:26px;color:#fff;opacity:.95;text-align:center;transform:rotate(-6deg)}
.search-bar{background:#fff;border-radius:16px;padding:8px;display:flex;gap:8px;margin-top:28px;max-width:980px;box-shadow:0 10px 30px rgba(0,60,58,.16)}
.sf{flex:1;display:flex;align-items:center;gap:10px;padding:8px 14px;border-radius:12px}
.sf+.sf{border-left:1px solid var(--bd);border-radius:0}
.sf .i{color:var(--p);font-size:17px}
.sf b{display:block;font-size:13px;color:var(--tx)}
.sf span{display:block;font-size:12px;color:var(--mu)}
.btn{background:var(--p);color:#fff;border:none;border-radius:12px;padding:14px 26px;font-size:15px;font-weight:700;cursor:pointer;white-space:nowrap}
.btn:hover{background:var(--pd)}
.btn-o{background:#fff;color:var(--tx);border:1px solid var(--bd)}
.trust{display:flex;gap:10px;margin-top:26px;flex-wrap:wrap}
.tb{background:rgba(255,255,255,.14);backdrop-filter:blur(4px);border:1px solid rgba(255,255,255,.35);border-radius:12px;padding:10px 14px;display:flex;gap:10px;align-items:center;font-size:12.5px}
.tb .ic{width:30px;height:30px;border-radius:50%;background:#fff;color:var(--p);display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700}
.tb b{display:block;font-size:12.5px}
.tb span{font-size:11px;opacity:.9}
.sec{padding:44px 0}
.sec-t{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:20px}
.sec h2{font-size:26px;font-weight:800}
.more{color:var(--p);font-size:14px;font-weight:700}
.cats{display:flex;gap:14px;overflow-x:auto;padding-bottom:8px}
.cat{min-width:158px;background:#fff;border:1px solid var(--bd);border-radius:14px;padding:12px;position:relative;cursor:pointer;transition:.2s}
.cat:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(20,114,111,.12)}
.cat-img{height:86px;border-radius:10px;background:linear-gradient(135deg,var(--pl),#CFE9E6);display:flex;align-items:flex-end;justify-content:center;margin-bottom:10px}
.cat-ic{width:52px;height:52px;border-radius:50%;background:#fff;box-shadow:0 4px 10px rgba(0,60,58,.15);display:flex;align-items:center;justify-content:center;font-size:24px;color:var(--p)}
.cta{background:linear-gradient(90deg,#E4F3F1,#F0F9F7);border:1px solid var(--bd);border-radius:18px;display:flex;align-items:center;gap:22px;padding:26px 30px;margin:10px 0 46px}
.cta .ic{width:52px;height:52px;border-radius:14px;background:var(--pl);color:var(--p);font-size:26px;display:flex;align-items:center;justify-content:center}
.cta b{font-size:18px}
.cta p{font-size:13.5px;color:var(--mu);margin-top:3px}
.cta .btn{margin-left:auto}
.ftr{background:#0F3B39;color:#CFE4E2;margin-top:30px}
.ftr-in{display:flex;gap:40px;padding:36px 0 26px;flex-wrap:wrap}
.fcol{min-width:170px}
.fcol h4{color:#fff;font-size:14px;margin-bottom:12px}
.fcol a{display:block;font-size:13px;margin:7px 0;opacity:.85}
.fcol a:hover{opacity:1;color:#fff}
.copy{border-top:1px solid rgba(255,255,255,.12);padding:16px 0;font-size:12px;display:flex;justify-content:space-between;opacity:.8}
.card{background:#fff;border:1px solid var(--bd);border-radius:16px;padding:22px}
.grid2{display:grid;grid-template-columns:300px 1fr;gap:22px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.check{display:flex;gap:8px;align-items:center;font-size:13px;color:#3A4A48;margin:6px 0}
.check::before{content:'✓';color:var(--p);font-weight:800}
.inp{width:100%;border:1px solid var(--bd);border-radius:11px;padding:12px 14px;font-size:14px;outline:none}
.inp:focus{border-color:var(--p)}
.lbl{font-size:12.5px;font-weight:700;color:#3A4A48;margin:14px 0 6px;display:block}
.doc{border:2px dashed var(--bd);border-radius:14px;padding:26px;text-align:center;color:var(--mu);font-size:13px;cursor:pointer;background:#FBFDFD}
.doc:hover{border-color:var(--p);color:var(--p)}
.tag{display:inline-block;background:var(--pl);color:var(--pd);border-radius:8px;padding:3px 9px;font-size:11.5px;font-weight:700;margin:2px 4px 2px 0}
.star{color:var(--g);letter-spacing:2px}
.ok{color:#16A34A;font-weight:700}
.chip-ok{background:#E4F5E9;color:#16A34A;border-radius:8px;padding:3px 10px;font-size:11.5px;font-weight:700}
.chip-w{background:#FFF4D6;color:#A97E00;border-radius:8px;padding:3px 10px;font-size:11.5px;font-weight:700}
"""

HEADER = """
<header class="hdr"><div class="wrap hdr-in">
<a class="logo" href="index.html"><span class="logo-ic">🌿</span><span>HealthBridge<small>Здоров'я. Інтеграція. Підтримка.</small></span></a>
<nav class="nav">
<a href="index.html" class="{A_H}">🏠 Головна</a>
<a href="search.html" class="{A_S}">🔍 Пошук</a>
<a href="favorites.html" class="{A_F}">🤍 Обране</a>
<a href="appointments.html" class="{A_A}">📋 Мої записи</a>
<a href="messages.html" class="{A_M}">🔔 Повідомлення<span class="badge-n">3</span></a>
</nav>
<div class="hdr-r"><button class="lang">🇺🇦 UA ▾</button>
<a class="prof" href="cabinet.html"><span class="avt">М</span><span style="font-size:13px;font-weight:700">Марія<br><span style="font-size:11px;color:var(--mu);font-weight:500">Профіль</span></span></a></div>
</div></header>
"""

FOOTER = """
<footer class="ftr"><div class="wrap">
<div class="ftr-in">
<div class="fcol"><a class="logo" href="index.html" style="color:#fff"><span class="logo-ic">🌿</span>HealthBridge</a><p style="font-size:12.5px;opacity:.8;margin-top:12px;max-width:220px">Міжнародна платформа перевірених лікарів і спеціалістів інтегративної медицини.</p></div>
<div class="fcol"><h4>Платформа</h4><a href="search.html">Знайти спеціаліста</a><a href="index.html#cats">Категорії</a><a href="booking.html">Запис на прийом</a><a href="login.html">Вхід</a></div>
<div class="fcol"><h4>Професіоналам</h4><a href="cabinet.html">Кабінет професіонала</a><a href="verification.html">Верифікація</a><a href="verification.html#docs">Документи</a></div>
<div class="fcol"><h4>Про допомогу</h4><a href="#">✉ support@healthbridge.care</a><a href="#">📲 Контакти</a><a href="#">Умови та приватність</a></div>
</div>
<div class="copy"><span>© 2026 HealthBridge. Усі професіонали мають диплом про вищу медичну освіту.</span><span>UA · ₴ UAH · +3h EET</span></div>
</div></footer>
"""


def doc(title, body, active):
    h = (HEADER.replace('{A_H}', 'act' if active == 'h' else '')
               .replace('{A_S}', 'act' if active == 's' else '')
               .replace('{A_F}', 'act' if active == 'f' else '')
               .replace('{A_A}', 'act' if active == 'a' else '')
               .replace('{A_M}', 'act' if active == 'm' else ''))
    css = CSS.replace('HEROURI', f'data:image/jpeg;base64,{hero_b64}')
    return (f'<!DOCTYPE html>\n<html lang="uk"><head><meta charset="UTF-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'\n<title>{title} — HealthBridge</title><style>{css}</style></head>\n'
            f'<body>{h}\n{body}\n{FOOTER}\n</body></html>')


def write(name, title, body, active):
    open(f'{SITE}/{name}', 'w', encoding='utf-8').write(doc(title, body, active))
    print('page:', name)


DOCS_DATA = [
    ('Олена', 'Кравченко', 'Сімейний лікар, невролог', 'Київ, Україна', '22 роки', '4.9', '612', '850 ₴'),
    ('Марко', 'Штайнер', 'Остеопат, фізіотерапевт', 'Варшава, Польща', '15 років', '4.8', '344', '1 200 ₴'),
    ('Анна', 'Соколова', 'Психолог, терапевт', 'Львів, Україна', '11 років', '4.9', '498', '700 ₴'),
    ('Георг', 'Мюллер', 'Акупунктурист', 'Берлін, Німеччина', '18 років', '4.7', '230', '1 500 ₴')]

DOC_CARDS = ''.join(f"""
<div class="card" style="display:flex;gap:18px;margin-bottom:14px">
 <div class="avt" style="width:74px;height:74px;font-size:26px;border-radius:16px">{n[0]}</div>
 <div style="flex:1">
  <div style="display:flex;gap:10px;align-items:center"><b style="font-size:17px">{n} {s}</b><span class="chip-ok">✔ Диплом перевірено</span></div>
  <div style="font-size:13.5px;color:var(--mu);margin:4px 0">{spec} · {loc}</div>
  <div class="star">★★★★★ <b style="color:var(--tx)">{rt}</b> <span style="color:var(--mu);font-size:12px">({rv} відгуків)</span></div>
  <div style="margin-top:6px"><span class="tag">{exp} досвіду</span><span class="tag">🎥 Онлайн</span><span class="tag">🏥 Особисто</span></div>
 </div>
 <div style="text-align:right"><div style="font-size:13px;color:var(--mu)">Від</div><b style="font-size:19px;color:var(--p)">{pr}</b><br><a class="btn" style="margin-top:10px;display:inline-block;padding:10px 18px" href="doctor.html">Записатись</a></div>
</div>""" for n, s, spec, loc, exp, rt, rv, pr in DOCS_DATA)

# ══════════ 1. ГОЛОВНА ══════════
CATS = [('🩺', 'Лікарі', '1 250+ спеціалістів'), ('👨‍⚕️', 'Спеціалісти', '850+ спеціалістів'), ('📍', 'Акупунктура', '320+ спеціалістів'),
        ('🤲', 'Фізіотерапія', '280+ спеціалістів'), ('🏃', 'Реабілітація', '210+ спеціалістів'), ('🦴', 'Остеопатія', '190+ спеціалістів'),
        ('🌱', 'Інтегративна медицина', '160+ спеціалістів'), ('🧘', 'Wellness', '140+ спеціалістів')]
cats_html = ''.join(
    f'''<a class="cat" href="search.html"><div style="position:absolute;left:50%;top:38px;transform:translateX(-50%);z-index:2"><span class="cat-ic">{ic}</span></div><div class="cat-img"></div><b style="display:block;font-size:13.5px;margin:4px 0 2px">{n}</b><span style="font-size:11px;color:var(--mu)">{c}</span><span class="arr" style="position:absolute;right:10px;bottom:12px;color:var(--p);font-weight:800">›</span></a>'''
    for ic, n, c in CATS)
BADGES = [('🛡', 'Вища медична освіта', "Обов'язкова вимога"), ('✔', 'Перевірені спеціалісти', 'Лікарі та спеціалісти'), ('🔖', 'Онлайн-запис', 'У зручний час'),
          ('🌍', 'Міжнародна платформа', 'Доступ у будь-якій країні'), ('🌿', 'Інтегративний підхід', 'Сучасні та комплементарні методи'), ('💚', 'Піклування про вас', 'На кожному етапі')]
badges_html = ''.join(f'<div class="tb"><span class="ic">{i}</span><span><b>{t}</b><span>{s}</span></span></div>' for i, t, s in BADGES)
write('index.html', 'Головна', f"""
<section class="hero"><div class="wrap hero-in">
<div class="script">Ваше здоров'я<br>у надійних руках ✍💚</div>
<div class="kick">Міжнародна платформа</div>
<h1>Пошук, перевірка та запис<br>до <span class="hl">лікарів і спеціалістів</span></h1>
<p class="sub">З вищою медичною освітою, сучасними методами та інтегративним підходом до здоров'я.</p>
<form class="search-bar" action="search.html">
 <div class="sf"><span class="i">🔍</span><span><b>Кого ви шукаєте?</b><span>Лікар, спеціаліст, метод, послуга…</span></span></div>
 <div class="sf"><span class="i">📍</span><span><b>Місто або країна</b><span>Виберіть локацію</span></span></div>
 <div class="sf"><span class="i">⚕</span><span><b>Спеціальність, метод або послуга</b><span>Наприклад: неврологія, акупунктура…</span></span></div>
 <button class="btn">🔍 Знайти</button>
</form>
<div class="trust">{badges_html}</div>
</div></section>
<section class="sec wrap" id="cats">
<div class="sec-t"><h2>Популярні категорії</h2><a class="more" href="search.html">Усі категорії →</a></div>
<div class="cats">{cats_html}</div>
<div class="cta"><span class="ic">🌿🤲</span><div><b>Пошукайте свого спеціаліста вже сьогодні</b><p>Знайдіть найкращих лікарів і спеціалістів поруч або онлайн. Ваше здоров'я — наш пріоритет.</p></div><a class="btn" href="search.html">Перейти до пошуку →</a></div>
</section>""", 'h')

# ══════════ 2. ПОШУК ══════════
write('search.html', 'Пошук', f"""
<section class="sec wrap"><div class="grid2">
<div class="card" style="height:max-content">
 <b style="font-size:16px">Фільтри пошуку</b>
 <label class="lbl">Що шукаємо</label><input class="inp" placeholder="Лікар, спеціаліст, метод…">
 <label class="lbl">Країна / місто</label><input class="inp" value="Україна · Київ">
 <label class="lbl">Пошук в радіусі</label><input type="range" style="width:100%;accent-color:var(--p)">
 <div style="font-size:12px;color:var(--mu)">25 км · 📍 моя локація</div>
 <label class="lbl">Формат</label>
 <div class="check">Онлайн-консультація</div><div class="check">Особистий прийом</div>
 <label class="lbl">Стаж від</label><input class="inp" placeholder="5 років">
 <button class="btn" style="width:100%;margin-top:18px">Застосувати фільтри</button>
</div>
<div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px"><h2>112 спеціалістів · Київ</h2><span style="font-size:13px;color:var(--mu)">Сортування: рекомендовані ▾</span></div>
{DOC_CARDS}
</div>
</div></section>""", 's')

# ══════════ 3. ЛІКАР ══════════
SLOTS = ''.join(f'<div style="border:1px solid var(--bd);border-radius:10px;padding:10px 6px;text-align:center;font-size:12.5px;font-weight:600;cursor:pointer">{d}<br><span style="color:var(--p)">{t}</span></div>'
                for d, t in [('Сьогодні', '16:30'), ('Сьогодні', '18:00'), ('Завтра', '10:00'), ('Завтра', '11:30'), ('Завтра', '15:00'), ('27 вер', '09:30'), ('27 вер', '12:00'), ('27 вер', '17:00')])
write('doctor.html', 'Профіль лікаря', f"""
<section class="sec wrap">
<div class="card" style="display:flex;gap:24px;margin-bottom:18px">
 <div class="avt" style="width:120px;height:120px;font-size:44px;border-radius:24px">О</div>
 <div style="flex:1">
  <div style="display:flex;gap:10px;align-items:center"><h2>Олена Кравченко</h2><span class="chip-ok">✔ Диплом вищої медичної освіти</span><span class="chip-ok">✔ Відеоверифікація обличчя</span></div>
  <p style="color:var(--mu);margin:6px 0">Сімейний лікар · Невролог · Інтегративний підхід · Київ, Україна</p>
  <div class="star" style="margin:6px 0">★★★★★ <b style="color:var(--tx)">4.9</b> <span style="color:var(--mu);font-size:13px">612 відгуків · 22 роки досвіду · 🇺🇦 🇬🇧</span></div>
  <div><span class="tag">Первинний прийом — 850 ₴</span><span class="tag">Онлайн — 700 ₴</span><span class="tag">Наступний вільний час: сьогодні 16:30</span></div>
 </div>
 <a class="btn" style="align-self:center;padding:14px 30px" href="booking.html">Записатись →</a>
</div>
<div class="grid2"><div>
<div class="card"><h3 style="margin-bottom:12px">Про спеціаліста</h3><p style="font-size:14px;line-height:1.6;color:#3A4A48">22 роки клінічного досвіду в неврології та сімейній медицині. Інтегрує сучасну доказову медицину з комплементарними методами — для підтримки не лише симптомів, а й цілісного здоров'я.</p>
<label class="lbl">Освіта</label><div class="check">Національний медичний університет ім. О. О. Богомольця</div><div class="check">Сертифікація з інтегративної неврології (2022)</div>
<label class="lbl">Методи роботи</label><span class="tag">Неврологія</span><span class="tag">Сімейна терапія</span><span class="tag">Wellness-програми</span></div>
<div class="card" style="margin-top:18px"><h3 style="margin-bottom:12px">Останні відгуки</h3>
<p style="font-size:13px;margin-bottom:14px">⭐⭐⭐⭐⭐ «Уважна та професійна, все пояснила зрозуміло». — Марина <span style="float:right;color:var(--mu);font-size:11px">цього тижня</span></p>
<p style="font-size:13px">⭐⭐⭐⭐⭐ «Допомогла поставити діагноз після року безуспішних обстежень». — Ігор <span style="float:right;color:var(--mu);font-size:11px">2 тижні тому</span></p>
</div>
</div>
<div>
<div class="card"><h3 style="margin-bottom:12px">Найближчі вікна запису</h3>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">{SLOTS}</div>
 <a class="btn" style="width:100%;margin-top:16px;display:block;text-align:center" href="booking.html">Обрати час та записатись</a>
</div>
<div class="card" style="margin-top:18px"><h3>📍 Локація</h3><p style="font-size:13px;color:var(--mu);margin-top:6px">Київ, вул. Медична 12 · клініка «HealthBridge Center» · також консультації онлайн 🎥</p></div>
</div>
</div></section>""", 's')

# ══════════ 4. ЗАПИС ══════════
CAL_HTML = ''.join('<tr>' + ''.join(
    f'<td style="padding:4px"><div style="height:34px;display:flex;align-items:center;justify-content:center;border-radius:8px;font-size:13px;'
    f'{"background:var(--p);color:#fff;font-weight:700" if str(d) == "26" else "background:#fff;border:1px solid var(--bd)"}">{d}</div></td>'
    for d in w) + '</tr>'
    for w in [[30, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, '', '', '']])
TIMES = ''.join(f'<div style="border:1px solid var(--bd);border-radius:10px;padding:10px;text-align:center;font-size:13px;font-weight:600;cursor:pointer;{"background:var(--p);color:#fff;border-color:var(--p)" if t == "16:30" else ""}">{t}</div>'
                for t in ['09:30', '10:00', '11:30', '14:00', '15:30', '16:30', '17:30', '18:00'])
write('booking.html', 'Запис на прийом', f"""
<section class="sec wrap"><h2 style="margin-bottom:18px">Запис: Олена Кравченко · Первинний прийом</h2>
<div class="grid2"><div class="card">
<b>📅 Вересень 2026</b>
<table style="width:100%;margin-top:10px;border-collapse:separate;border-spacing:2px">
<tr style="font-size:11px;color:var(--mu);text-align:center"><td>Пн</td><td>Вт</td><td>Ср</td><td>Чт</td><td>Пт</td><td>Сб</td><td>Нд</td></tr>
{CAL_HTML}
</table>
</div>
<div class="card">
<b>🕓 Обрано: 26 вересня, 16:30 · Особистий прийом · 850 ₴</b>
<label class="lbl">Ваше ім'я</label><input class="inp" value="Марія Савчук">
<label class="lbl">Телефон</label><input class="inp" value="+380 50 123 45 67">
<label class="lbl">Коментар (необов'язково)</label><textarea class="inp" rows="2" placeholder="Коротко опишіть, що турбує…"></textarea>
<div style="margin-top:14px;font-size:12.5px;color:var(--mu)">✓ Сповіщення коштами SMS та email · ✓ Скасування безкоштовно до 24 год</div>
<button class="btn" style="width:100%;margin-top:16px;padding:16px">Підтвердити запис ✅</button>
</div></div>
<div class="card" style="margin-top:18px"><b>Інші вільні години сьогодні:</b><div style="display:grid;grid-template-columns:repeat(8,1fr);gap:8px;margin-top:10px">{TIMES}</div></div>
</section>""", 'a')

# ══════════ 5. КАБІНЕТ ══════════
MENU = ''.join(
    f'<a href="{u}" style="display:flex;gap:9px;padding:9px;border-radius:9px;font-size:13.5px;font-weight:600;'
    f'background:{"var(--pl)" if u == "cabinet.html" else "transparent"};color:{"var(--pd)" if u == "cabinet.html" else "#33413F"}">{i} {t}</a>'
    for i, t, u in [('📊', 'Огляд', 'cabinet.html'), ('📋', 'Записи', 'appointments.html'), ('📅', 'Графік', '#'), ('✔', 'Верифікація', 'verification.html'), ('💳', 'Виплати', '#'), ('⚙', 'Налаштування', '#')])
STATS = ''.join(f'<div class="card" style="text-align:center;padding:16px"><div style="font-size:26px;font-weight:800;color:var(--p)">{v}</div><div style="font-size:12px;color:var(--mu)">{k}</div></div>'
                for v, k in [(12, 'Записів цього тижня'), ('4.9 ★', 'Рейтинг'), (98, 'Відгуків')])
write('cabinet.html', 'Кабінет професіонала', f"""
<section class="sec wrap"><div class="grid2" style="grid-template-columns:250px 1fr">
<div class="card" style="height:max-content;padding:16px">
 <div style="text-align:center;padding:8px 0"><div class="avt" style="width:66px;height:66px;margin:0 auto;font-size:24px;border-radius:20px">А</div><b style="display:block;margin-top:8px">Анна Соколова</b><span class="chip-ok" style="display:inline-block;margin-top:6px">✔ Верифіковано</span></div>
 <hr style="border:none;border-top:1px solid var(--bd);margin:10px 0 6px">
 {MENU}
</div>
<div>
<div class="card" style="margin-bottom:16px"><b style="font-size:16px">📬 Підтвердження контактів</b>
 <div style="display:flex;align-items:center;gap:10px;margin-top:12px;font-size:13.5px">@ <span style="flex:1">anna.sokolova@healthbridge.care ✏</span><span class="chip-ok">Підтверджено ✔</span></div>
 <div style="display:flex;align-items:center;gap:10px;margin-top:10px;font-size:13.5px">📱 <span style="flex:1">+380 44 555 35 35 ✏</span><button class="btn" style="padding:6px 14px;font-size:12px">Підтвердити</button></div>
</div>
<div class="card" style="margin-bottom:16px"><b style="font-size:16px">🔄 Синхронізація календаря</b><p style="font-size:12.5px;color:var(--mu);margin-top:6px">Google Calendar • Apple Calendar • Outlook</p><div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px"><span style="font-size:13px;font-weight:600">Синхронізація активна</span><input type="checkbox" checked style="accent-color:var(--p);width:18px;height:18px"></div></div>
<div class="grid3">{STATS}</div>
</div></div></section>""", 'a')

# ══════════ 6. ВЕРИФІКАЦІЯ ══════════
DTYPES = ''.join(f'<span class="tag" style="{"background:var(--p);color:#fff" if i == 0 else ""}">{d}</span>'
                 for i, d in enumerate(['Паспорт', 'ID-картка', 'Водійське посвідчення']))
write('verification.html', 'Верифікація професіонала', f"""
<section class="sec wrap" style="max-width:760px;margin:0 auto">
<h2 style="margin-bottom:8px">Верифікація</h2>
<p style="color:var(--mu);font-size:14px;margin-bottom:18px">Кроки: Документи → жива відеоверифікація обличчя → Passkey-вхід</p>
<div class="card" id="docs">
<div style="display:flex;gap:8px;margin-bottom:14px">{DTYPES}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
<div class="doc">🖼<br><b style="color:var(--tx)">Паспорт *</b><br>Додати документ із галереї або сфотографувати його</div>
<div class="doc">🎓<br><b style="color:var(--tx)">Диплом *</b><br>Додати фото диплома з галереї або зробити знімок</div>
</div>
<button class="btn" style="width:100%;margin-top:16px">Перевірити документи</button>
</div>
<div class="card" style="margin-top:16px;text-align:center">
<b style="font-size:16px">Крок 2 · Жива відеоверифікація</b>
<div style="width:210px;height:250px;margin:14px auto;border:4px solid var(--p);border-radius:110px;background:linear-gradient(180deg,#CDEDE9,#EAF5F4);display:flex;align-items:center;justify-content:center;font-size:84px">🙂</div>
<p style="font-size:13px;color:var(--mu)">Тримайте обличчя в центрі рамки — автоматичне розпізнавання з передньою камерою браузера</p>
<button class="btn" style="margin-top:14px">🎥 Почати відеоверифікацію</button>
</div>
<p style="text-align:center;font-size:12px;color:var(--mu);margin-top:14px">Після успіху — увімкнення Passkey-входу за відбитком (WebAuthn), щоб наступні входи не потребували повторних верифікацій.</p>
</section>""", 'a')

# ══════════ 7. ВХІД ══════════
write('login.html', 'Вхід', f"""
<section class="sec wrap" style="max-width:420px;margin:40px auto">
<div class="card" style="padding:30px">
<div style="text-align:center;margin-bottom:16px"><div class="logo-ic" style="margin:0 auto;width:52px;height:52px;font-size:26px;border-radius:14px">🌿</div><h2 style="margin-top:10px">Вхід до акаунту</h2></div>
<label class="lbl">Email</label><input class="inp" value="maria.savchuk@gmail.com">
<label class="lbl">Пароль</label><input class="inp" type="password" value="demo-password">
<a class="btn" style="width:100%;margin-top:18px;display:block;text-align:center;padding:14px" href="index.html">Увійти</a>
<div style="text-align:center;font-size:13px;color:var(--mu);margin:16px 0 10px">— або увійти через —</div>
<div style="display:flex;gap:10px">
<button class="btn btn-o" style="flex:1">🅖 Google</button>
<button class="btn btn-o" style="flex:1">🍎 Apple</button>
</div>
<p style="font-size:11.5px;color:var(--mu);text-align:center;margin-top:16px">Після першого входу зможете увімкнути швидкий вхід за відбитком (Passkey) 🫆</p>
</div></section>""", '')

# ══════════ 8. ОБРАНЕ ══════════
write('favorites.html', 'Обране', f"""
<section class="sec wrap"><h2 style="margin-bottom:6px">🤍 Обрані спеціалісти</h2>
<p style="color:var(--mu);font-size:13.5px;margin-bottom:18px">4 спеціалісти у вашій колекції</p>
{DOC_CARDS}
</section>""", 'f')

# ══════════ 9. МОЇ ЗАПИСИ ══════════
APPTS = [('Пт, 26 вересня · 16:30', 'Олена Кравченко · Сімейний лікар', '🏥 Особисто · Київ', 'chip-w', '⏳ Очікує'),
         ('Сб, 4 жовтня · 11:00', 'Анна Соколова · Психолог', '🎥 Онлайн', 'chip-ok', '✔ Підтверджено'),
         ('12 вересня, минув', 'Марко Штайнер · Остеопат', '🏥 Варшава', 'chip-ok', '✅ Завершено')]
APPT_ROWS = ''.join(f"""
<div class="card" style="display:flex;gap:16px;align-items:center;margin-bottom:12px">
<div style="width:46px;height:46px;border-radius:12px;background:var(--pl);display:flex;align-items:center;justify-content:center;font-size:20px">📋</div>
<div style="flex:1"><b>{d}</b><div style="font-size:13px;color:var(--mu)">{w} · {h}</div></div>
<span class="{c}">{s}</span>
<button class="btn" style="padding:9px 16px;font-size:12.5px">Деталі</button>
</div>""" for d, w, h, c, s in APPTS)
write('appointments.html', 'Мої записи', f"""
<section class="sec wrap" style="max-width:820px">
<h2 style="margin-bottom:16px">📋 Мої записи</h2>
{APPT_ROWS}
<div class="cta" style="margin-top:20px"><span class="ic">🌿</span><div><b>Знайдіть нового спеціаліста</b><p>Додайте наступний прийом за хвилину</p></div><a class="btn" href="search.html">До пошуку →</a></div>
</section>""", 'a')

# ══════════ 10. ПОВІДОМЛЕННЯ ══════════
CHATS = [('Олена Кравченко', 'Нагадування про прийом сьогодні о 16:30 📋', '14:02', '1'),
         ('HealthBridge', 'Ваша верифікація контактів пройшла успішно ✔', '09:00', '2'),
         ('Анна Соколова', 'Надіслала рекомендації після сесії', 'вч.', '')]
CHAT_ROWS = ''.join(f"""
<div style="display:flex;gap:12px;padding:12px;border-bottom:1px solid var(--bd);cursor:pointer;{'background:var(--pl)' if n == 'Олена Кравченко' else ''}">
<div class="avt">{n[0]}</div>
<div style="flex:1"><b style="font-size:13.5px">{n}</b><div style="font-size:12px;color:var(--mu)">{m}</div></div>
<div style="font-size:11px;color:var(--mu)">{t}{f'<div class="badge-n" style="margin-top:4px">{u}</div>' if u else ''}</div>
</div>""" for n, m, t, u in CHATS)
write('messages.html', 'Повідомлення', f"""
<section class="sec wrap"><h2 style="margin-bottom:16px">🔔 Повідомлення</h2>
<div class="grid2" style="grid-template-columns:340px 1fr">
<div class="card" style="padding:0;height:max-content">{CHAT_ROWS}</div>
<div class="card" style="min-height:380px;display:flex;flex-direction:column">
<div style="border-bottom:1px solid var(--bd);padding-bottom:10px;margin-bottom:12px"><b>Олена Кравченко</b> <span style="font-size:11px;color:#16A34A">● онлайн</span></div>
<div style="font-size:13px;display:flex;flex-direction:column;gap:8px;flex:1">
<div style="background:var(--pl);border-radius:12px 12px 12px 2px;padding:10px 14px;max-width:70%">Добрий день! Нагадую про прийом сьогодні о 16:30 — вул. Медична 12, кабінет 4 📋</div>
<div style="background:var(--p);color:#fff;border-radius:12px 12px 2px 12px;padding:10px 14px;max-width:70%;align-self:flex-end">Дякую! Буду вчасно 🙌</div>
<div style="background:var(--pl);border-radius:12px 12px 12px 2px;padding:10px 14px;max-width:70%">Чудово. Якщо бажаєте прийти раніше — у зоні очікування затишна кімната з чаєм 🌿</div>
</div>
<div style="display:flex;gap:8px;margin-top:14px"><input class="inp" placeholder="Написати повідомлення…"><button class="btn" style="padding:12px 18px">➤</button></div>
</div>
</div></section>""", 'm')

open(f'{SITE}/README.md', 'w', encoding='utf-8').write("""# HealthBridge Desktop Web (HTML)

Повний набір статичних сторінок десктопного сайту у фірмовому стилі платформи.

## Сторінки
| Файл | Розділ |
|---|---|
| index.html | Головна (хіро-фото, пошукова панель, категорії, довіра) |
| search.html | Пошук спеціалістів з фільтрами |
| doctor.html | Профіль лікаря |
| booking.html | Запис на прийом (календар + форма) |
| cabinet.html | Кабінет професіонала |
| verification.html | Верифікація (документи + відео) |
| login.html | Вхід (email / Google / Apple) |
| favorites.html | Обране |
| appointments.html | Мої записи |
| messages.html | Повідомлення |

Відкрито — `index.html`. Самодостатні файли (стилі вбудовані), фото головна вбудоване.
""")
print('ALL 10 PAGES + README written')
