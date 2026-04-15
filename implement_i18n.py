#!/usr/bin/env python3
"""
i18n implementation script for portfolio website.
Processes all HTML files, adds data-i18n attributes, and generates translation keys.
"""
from bs4 import BeautifulSoup, NavigableString, Tag
import os, re, json

BASE = '/home/runner/work/My-website-project/My-website-project/htmls/'

PAGE_MAP = {
    'index.html': 'index',
    'about.html': 'about',
    'projects.html': 'projects',
    'the-universe.html': 'univ',
    'universe-origin.html': 'origin',
    'universe-stars.html': 'ustars',
    'universe-galaxies.html': 'ugal',
    'universe-planets.html': 'uplanets',
    'universe-blackholes.html': 'ubh',
    'universe-neutron.html': 'uneutron',
    'universe-dark.html': 'udark',
    'universe-systems.html': 'usys',
    'shape-universe.html': 'shape',
    'star-main-sequence.html': 'star-ms',
    'star-red-dwarf.html': 'star-rd',
    'star-red-giant.html': 'star-rg',
    'star-white-dwarf.html': 'star-wd',
    'star-brown-dwarf.html': 'star-bd',
    'star-supergiant.html': 'star-sg',
    'star-variable.html': 'star-var',
    'galaxy-spiral.html': 'gal-spiral',
    'galaxy-elliptical.html': 'gal-ellip',
    'galaxy-lenticular.html': 'gal-lent',
    'galaxy-irregular.html': 'gal-irr',
    'galaxy-dwarf.html': 'gal-dwarf',
    'galaxy-blazars.html': 'gal-blazar',
    'galaxy-quasars.html': 'gal-quasar',
    'systems-single.html': 'sys-single',
    'systems-binary.html': 'sys-binary',
    'systems-multiple.html': 'sys-multi',
    'systems-compact.html': 'sys-compact',
    'systems-debris.html': 'sys-debris',
}

en_translations = {}
counters = {}

def next_key(page, kind):
    k = f"{page}.{kind}"
    counters[k] = counters.get(k, 0) + 1
    return f"{page}.{kind}{counters[k]}"

def has_tag_children(el):
    for child in el.children:
        if isinstance(child, Tag):
            return True
    return False

def inner_html(el):
    return el.decode_contents().strip()

def plain_text(el):
    return el.get_text(' ', strip=True)

def tag_i18n(el, key):
    if has_tag_children(el):
        el['data-i18n-html'] = key
        en_translations[key] = inner_html(el)
    else:
        el['data-i18n'] = key
        en_translations[key] = plain_text(el)

NAV_TEXT_MAP = {
    'Home': 'nav.home',
    'About': 'nav.about',
    'My Projects': 'nav.projects',
    'THE UNIVERSE': 'nav.universe',
    'STARS': 'nav.stars',
    'PLANETARY SYSTEMS': 'nav.planetary-systems',
}
# Pre-seed these keys
en_translations['nav.home'] = 'Home'
en_translations['nav.about'] = 'About'
en_translations['nav.projects'] = 'My Projects'
en_translations['nav.universe'] = 'THE UNIVERSE'
en_translations['nav.stars'] = 'STARS'
en_translations['nav.planetary-systems'] = 'PLANETARY SYSTEMS'

LANG_BTN_HTML = '<button class="lang-btn" id="lang-btn" aria-label="Switch language">🇬🇧</button>'

def process_file(filename):
    page = PAGE_MAP.get(filename, filename.replace('.html',''))
    filepath = os.path.join(BASE, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Add data-i18n-title to <html> element
    html_el = soup.find('html')
    title_tag = soup.find('title')
    if html_el and title_tag:
        title_key = f'title.{page}'
        html_el['data-i18n-title'] = title_key
        en_translations[title_key] = title_tag.get_text().strip()
    
    # 2. Process nav links
    for a in soup.select('a.nav-link'):
        text = a.get_text().strip()
        key = NAV_TEXT_MAP.get(text)
        if key:
            a['data-i18n'] = key
    
    # 3. Add lang button to nav-right (before the instagram icon)
    nav_right = soup.find(class_='nav-right')
    if nav_right:
        ig = nav_right.find(class_='instagram-icon')
        lang_btn = BeautifulSoup(LANG_BTN_HTML, 'html.parser')
        if ig:
            ig.insert_before(lang_btn)
        else:
            nav_right.append(lang_btn)
    
    # 4. Process page-specific content
    if filename == 'index.html':
        process_index(soup, page)
    elif filename == 'about.html':
        process_about(soup, page)
    elif filename == 'projects.html':
        process_projects(soup, page)
    elif filename == 'the-universe.html':
        process_universe_hub(soup, page)
    else:
        process_generic(soup, page)
    
    # 5. Add i18n.js script before </body>
    body = soup.find('body')
    if body:
        i18n_script = soup.new_tag('script', src='../scripts/i18n.js')
        # Find module script (for index.html) and insert before it
        module_script = body.find('script', type='module')
        if module_script:
            module_script.insert_before(i18n_script)
        else:
            # Insert before last script tag, or at end of body
            scripts = body.find_all('script')
            if scripts:
                scripts[0].insert_before(i18n_script)
            else:
                body.append(i18n_script)
    
    # Write modified HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Processed {filename}")


def process_index(soup, page):
    h1 = soup.find('h1', class_='hero-title')
    if h1:
        key = f'{page}.h1'
        h1['data-i18n'] = key
        en_translations[key] = h1.get_text().strip()
    
    hero_btn = soup.find('a', class_='hero-button')
    if hero_btn:
        key = f'{page}.btn'
        hero_btn['data-i18n'] = key
        en_translations[key] = hero_btn.get_text().strip()


def process_about(soup, page):
    # About Me section title
    for h2 in soup.find_all('h2', class_='about-section-title'):
        text = h2.get_text().strip()
        key = f'about.section.{text.lower().replace(" ", "-")}'
        h2['data-i18n'] = key
        en_translations[key] = text
    
    # About me paragraphs
    about_text = soup.find(class_='about-me-text')
    if about_text:
        for i, p in enumerate(about_text.find_all('p'), 1):
            key = f'about.intro.p{i}'
            tag_i18n(p, key)
    
    # Avatar alt
    avatar = soup.find('img', class_='avatar-img')
    if avatar:
        key = 'about.avatar.alt'
        avatar['data-i18n-alt'] = key
        en_translations[key] = avatar.get('alt', 'Avatar')
    
    # Skill cards
    for i, card in enumerate(soup.find_all('div', class_='skill-card'), 1):
        title = card.find(class_='skill-card-title')
        if title:
            key = f'about.skill.card{i}.title'
            title['data-i18n'] = key
            en_translations[key] = title.get_text().strip()
        for j, li in enumerate(card.find_all('li'), 1):
            key = f'about.skill.card{i}.li{j}'
            tag_i18n(li, key)
    
    # Timeline items
    for i, item in enumerate(soup.find_all('div', class_='timeline-item'), 1):
        year = item.find(class_='timeline-year')
        title = item.find(class_='timeline-title')
        desc = item.find(class_='timeline-desc')
        if year:
            key = f'about.tl{i}.year'
            year['data-i18n'] = key
            en_translations[key] = year.get_text().strip()
        if title:
            key = f'about.tl{i}.title'
            title['data-i18n'] = key
            en_translations[key] = title.get_text().strip()
        if desc:
            key = f'about.tl{i}.desc'
            tag_i18n(desc, key)
    
    # Timeline footer paragraph
    tf = soup.find(class_='timeline-footer')
    if tf:
        p = tf.find('p')
        if p:
            key = 'about.tl.footer'
            tag_i18n(p, key)
    
    # Certificates
    for i, cert in enumerate(soup.find_all('div', class_='cert-card'), 1):
        for cls in ['cert-info-title', 'cert-info-issuer', 'cert-info-year']:
            el = cert.find(class_=cls)
            if el:
                key = f'about.cert{i}.{cls.replace("cert-info-","")}'
                tag_i18n(el, key)
    
    # Contact labels
    for i, link in enumerate(soup.find_all('a', class_='contact-link'), 1):
        label = link.find(class_='contact-label')
        if label:
            key = f'about.contact{i}.label'
            label['data-i18n'] = key
            en_translations[key] = label.get_text().strip()
    
    # Gaming paragraph
    gaming_p = soup.find('p', class_='about-paragraph-gaming')
    if gaming_p:
        key = 'about.gaming.p'
        tag_i18n(gaming_p, key)


def process_projects(soup, page):
    h1 = soup.find('h1', class_='projects-title')
    if h1:
        key = f'{page}.h1'
        h1['data-i18n'] = key
        en_translations[key] = h1.get_text().strip()
    
    intro = soup.find('p', class_='projects-intro')
    if intro:
        key = f'{page}.intro'
        tag_i18n(intro, key)
    
    for i, card in enumerate(soup.find_all('article', class_='project-card'), 1):
        h2 = card.find('h2', class_='project-card-title')
        if h2:
            key = f'{page}.card{i}.title'
            h2['data-i18n'] = key
            en_translations[key] = h2.get_text().strip()
        desc = card.find('p', class_='project-card-desc')
        if desc:
            key = f'{page}.card{i}.desc'
            tag_i18n(desc, key)
        # Footer links
        for j, a in enumerate(card.select('.project-card-footer a'), 1):
            key = f'{page}.card{i}.link{j}'
            a['data-i18n'] = key
            en_translations[key] = a.get_text().strip()


def process_universe_hub(soup, page):
    h1 = soup.find('h1', class_='universe-title')
    if h1:
        key = f'{page}.h1'
        h1['data-i18n'] = key
        en_translations[key] = h1.get_text().strip()
    
    for i, card_title in enumerate(soup.find_all('h2', class_='universe-card-title'), 1):
        key = f'{page}.card{i}'
        card_title['data-i18n'] = key
        en_translations[key] = card_title.get_text().strip()


def process_generic(soup, page):
    """Process universe/* and star-*, galaxy-*, systems-* pages."""
    # H1
    h1 = soup.find('h1', class_='universe-title')
    if h1:
        key = f'{page}.h1'
        h1['data-i18n'] = key
        en_translations[key] = h1.get_text().strip()
    
    # Special intro paragraph (origin/neutron/stars pages have .origin-intro)
    intro = soup.find('p', class_='origin-intro')
    if intro:
        key = f'{page}.intro'
        tag_i18n(intro, key)
    
    # Special intro for shape page
    shape_intro = soup.find(class_='shape-page')
    
    # Question/section title h2s in origin-hero
    hero_q = soup.find(class_='origin-question')
    if hero_q:
        key = f'{page}.hero.q'
        tag_i18n(hero_q, key)
    
    # "What was before" title
    what_before = soup.find(class_='what-before-title')
    if what_before:
        key = f'{page}.whatbefore.title'
        tag_i18n(what_before, key)
    
    # Short/longer answer labels
    for cls in ['short-answer', 'longer-answer']:
        el = soup.find(class_=cls)
        if el:
            key = f'{page}.{cls.replace("-","")}'
            tag_i18n(el, key)
    
    # Process all origin-text divs
    c = {'h2': 0, 'h3': 0, 'p': 0, 'li': 0}
    for text_div in soup.find_all(class_='origin-text'):
        for child in text_div.children:
            if not isinstance(child, Tag):
                continue
            tag_name = child.name
            
            if tag_name in ('h2', 'h3'):
                c[tag_name] += 1
                key = f'{page}.{tag_name}{c[tag_name]}'
                tag_i18n(child, key)
            elif tag_name == 'p':
                # Skip already-tagged elements
                if child.get('data-i18n') or child.get('data-i18n-html'):
                    continue
                # Skip empty or whitespace-only
                text = child.get_text().strip()
                if not text:
                    continue
                c['p'] += 1
                key = f'{page}.p{c["p"]}'
                tag_i18n(child, key)
            elif tag_name == 'ul':
                for li in child.find_all('li', recursive=False):
                    c['li'] += 1
                    key = f'{page}.li{c["li"]}'
                    tag_i18n(li, key)
    
    # Also handle figure captions
    for i, cap in enumerate(soup.find_all(class_='figure-caption'), 1):
        key = f'{page}.cap{i}'
        cap['data-i18n'] = key
        en_translations[key] = cap.get_text().strip()
    
    # Conclusion text
    concl = soup.find(class_='conclusion-text')
    if concl:
        key = f'{page}.conclusion'
        tag_i18n(concl, key)


# Process all files
for filename in PAGE_MAP:
    try:
        process_file(filename)
    except Exception as e:
        print(f"ERROR processing {filename}: {e}")
        import traceback
        traceback.print_exc()

# Output collected keys
print(f"\nTotal EN keys: {len(en_translations)}")
# Save to file for inspection
with open('/home/runner/work/My-website-project/My-website-project/en_keys.json', 'w', encoding='utf-8') as f:
    json.dump(en_translations, f, ensure_ascii=False, indent=2)
print("Keys saved to en_keys.json")
