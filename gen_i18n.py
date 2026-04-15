#!/usr/bin/env python3
"""Generate scripts/i18n.js with full EN and CS translations."""
import json, os

with open('/home/runner/work/My-website-project/My-website-project/en_keys.json') as f:
    en = json.load(f)

# ── Czech translations ─────────────────────────────────────────────────────────
cs = {
  # ── Shared nav ──────────────────────────────────────────────────────────────
  'nav.home': 'Domů',
  'nav.about': 'O mně',
  'nav.projects': 'Moje projekty',
  'nav.universe': 'VESMÍR',
  'nav.stars': 'HVĚZDY',
  'nav.planetary-systems': 'PLANETÁRNÍ SOUSTAVY',

  # ── Page titles ─────────────────────────────────────────────────────────────
  'title.index':    'Simon Sykora – 3D Vesmír',
  'title.about':    'O mně – Moje portfolio',
  'title.projects': 'Moje projekty – Portfolio',
  'title.univ':     'Vesmír',
  'title.origin':   'Velký třesk',
  'title.ustars':   'Hvězdy',
  'title.ugal':     'Galaxie',
  'title.uplanets': 'Planety',
  'title.ubh':      'Černé díry',
  'title.uneutron': 'Neutronové hvězdy',
  'title.udark':    'Temná hmota a energie',
  'title.usys':     'Planetární soustavy',
  'title.shape':    'Tvar vesmíru',
  'title.star-ms':  'Hvězdy hlavní posloupnosti',
  'title.star-rd':  'Červení trpaslíci',
  'title.star-rg':  'Červení obři',
  'title.star-wd':  'Bílí trpaslíci',
  'title.star-bd':  'Hnědí trpaslíci',
  'title.star-sg':  'Nadobři',
  'title.star-var': 'Proměnné hvězdy',
  'title.gal-spiral':  'Spirální galaxie',
  'title.gal-ellip':   'Eliptické galaxie',
  'title.gal-lent':    'Čočkové galaxie',
  'title.gal-irr':     'Nepravidelné galaxie',
  'title.gal-dwarf':   'Trpasličí galaxie',
  'title.gal-blazar':  'Blazary',
  'title.gal-quasar':  'Kvazary',
  'title.sys-single':  'Jednoduché planetární soustavy',
  'title.sys-binary':  'Binární planetární soustavy',
  'title.sys-multi':   'Vícehvězdné planetární soustavy',
  'title.sys-compact': 'Kompaktní víceplanetové soustavy',
  'title.sys-debris':  'Soustavy s troskovými disky',

  # ── Index ──────────────────────────────────────────────────────────────────
  'index.h1':  'VÍTEJTE NA MÉM WEBU',
  'index.btn': 'Vstoupit do VESMÍRU',

  # ── About ──────────────────────────────────────────────────────────────────
  'about.section.about-me':     'O mně',
  'about.section.skills':       'Dovednosti',
  'about.section.timeline':     'Časová osa',
  'about.section.certificates': 'Certifikáty',
  'about.section.contact':      'Kontakt',

  'about.intro.p1': 'Ahoj, jsem <strong>Simon Sykora</strong> — vývojář a nadšenec do technologií, který miluje budování věcí na pomezí softwaru, hardwaru a designu.',
  'about.intro.p2': 'Momentálně studuji na <strong>Střední průmyslové škole IT v Žďáru nad Sázavou</strong> a rád prozkoumávám vše od elektroniky a vestavěných systémů po webový a aplikační vývoj.',
  'about.intro.p3': 'Když nekóduji, rád pozoruji noční oblohu, fotografuji a sleduji nejnovější vesmírné mise — a to je asi důvod, proč má celé toto portfolio vesmírný motiv. 🌌',
  'about.avatar.alt': 'Avatar',

  'about.skill.card1.title': 'Jazyky',
  'about.skill.card1.li1': 'Dart (Flutter)',
  'about.skill.card1.li2': 'JavaScript',
  'about.skill.card1.li3': 'HTML / CSS',
  'about.skill.card1.li4': 'C / C++',

  'about.skill.card2.title': 'Frameworky a nástroje',
  'about.skill.card2.li1': 'Flutter',
  'about.skill.card2.li2': 'Three.js',
  'about.skill.card2.li3': 'Git a GitHub',
  'about.skill.card2.li4': 'Arduino / ESP32',
  'about.skill.card2.li5': 'VS Code',
  'about.skill.card2.li6': 'Android Studio',

  'about.skill.card3.title': 'Ostatní',
  'about.skill.card3.li1': 'Hobby robotika',
  'about.skill.card3.li2': '3D tisk',
  'about.skill.card3.li3': 'Elektronika',
  'about.skill.card3.li4': 'UI design',
  'about.skill.card3.li5': 'Fotografie',
  'about.skill.card3.li6': 'Střih videa a fotografií',
  'about.skill.card3.li7': 'Webdesign',

  'about.tl1.year':  '2022',
  'about.tl1.title': 'Začal jsem kódovat',
  'about.tl1.desc':  'Napsal jsem první řádky kódu v C ve škole a propadl jsem programování. Začal jsem se učit základy webu — HTML, CSS a vanilla JavaScript.',
  'about.tl2.year':  '2023',
  'about.tl2.title': 'První hardwarový projekt',
  'about.tl2.desc':  'Ponořil jsem se do Arduina a postavil první automatizační projekty. Objevil jsem robotiku a rozhodl se spojit software s hardwarem.',
  'about.tl3.year':  '2024',
  'about.tl3.title': 'Robotické rameno + Flutter App',
  'about.tl3.desc':  'Navrhl a sestavil jsem 3D tištěné robotické rameno ovládané bezdrátově přes vlastní Flutter mobilní aplikaci. První komplexní hardware/software projekt od základů.',
  'about.tl4.year':  '2025',
  'about.tl4.title': 'Toto portfoliové webové stránky',
  'about.tl4.desc':  'Začal jsem pracovat na tomto vesmírně laděném portfoliu s Three.js pozadím, animovanými hvězdnými poli a rostoucí znalostní základnou o vesmíru.',
  'about.tl5.year':  'Budoucnost',
  'about.tl5.title': 'Co dál…',
  'about.tl5.desc':  'Více vylepšení, AI experimenty a projekty překračující hranice. Sledujte dál — tato časová osa se stále píše. ✨',
  'about.tl.footer': 'Všechny moje projekty najdete v sekci <a class="inline-link" href="projects.html">Moje projekty</a>.',

  'about.cert1.title':  'Cambridge Certificate English Advanced (CAE C1)',
  'about.cert1.issuer': 'Cambridge English',
  'about.cert1.year':   '31. LEDNA 2026',

  'about.contact1.label': 'Instagram',
  'about.contact2.label': 'GitHub',
  'about.contact3.label': 'E-mail',
  'about.contact4.label': 'Discord',

  'about.gaming.p': 'Jsem také vášnivý hráč. Pokud vás to zajímá, moji herní kolekci najdete na <a href="https://backloggd.com/u/Goatedgamerboi/" target="_blank" rel="noopener noreferrer" class="inline-link">Backloggd</a>.',

  # ── Projects ──────────────────────────────────────────────────────────────
  'projects.h1':    'Moje projekty',
  'projects.intro': 'Sbírka věcí, které jsem postavil — od robotiky po webové zážitky. Další projekty jsou na cestě, takže se vracejte. 🚀',

  'projects.card1.title': 'Robotické rameno',
  'projects.card1.desc':  'Plně 3D tištěné robotické rameno s 5 stupni volnosti, ovládané bezdrátově přes vlastní Flutter mobilní aplikaci. Aplikace streamuje příkazy pro serva přes Bluetooth, což umožňuje plynulý a přesný pohyb. Navrženo od základů — od mechanické struktury po firmware a mobilní UI.',
  'projects.card1.link1': '↗ GitHub',
  'projects.card1.link2': 'Detaily (již brzy)',

  'projects.card2.title': 'Toto portfoliové webové stránky',
  'projects.card2.desc':  'Vesmírně laděné osobní portfolio postavené na vanilla HTML, CSS a JavaScriptu. Obsahuje Three.js 3D hvězdné pole na domovské stránce s animovanými planetami, 2D canvas hvězdné pole se střelkami na vnitřních stránkách, animace při rolování a neustále rostoucí znalostní základnu o vesmíru. Je navrženo jako vizuálně poutavé a některé věci mohou být skryté — musíte průzkoumat nebo rolovat dolů, abyste je našli.',
  'projects.card2.link1': '↗ GitHub',
  'projects.card2.link2': 'Zobrazit živě',

  # ── Universe hub (the-universe.html) ─────────────────────────────────────
  'univ.h1':    'VŠE CO POTŘEBUJETE VĚDĚT',
  'univ.card1': 'POČÁTEK VESMÍRU',
  'univ.card2': 'TVAR VESMÍRU',
  'univ.card3': 'GALAXIE',
  'univ.card4': 'PLANETÁRNÍ SOUSTAVY',
  'univ.card5': 'HVĚZDY',
  'univ.card6': 'PLANETY',
  'univ.card7': 'ČERNÉ DÍRY',
  'univ.card8': 'NEUTRONOVÉ HVĚZDY',
  'univ.card9': 'TEMNÁ HMOTA A ENERGIE',

  # ── Origin of the Universe ───────────────────────────────────────────────
  'origin.h1':    'VELKÝ TŘESK',
  'origin.intro': '„Původ, vývoj a podstata vesmíru lidstvo fascinovaly a mátly po staletí. Nové myšlenky a velké objevy učiněné v průběhu 20. století přeměnily kosmologii — způsob, jakým pojímáme a studujeme vesmír — i když mnoho zůstává neznámé." <span class="origin-attrib">NASA</span>',
  'origin.hero.q': 'Lámete si nad tím hlavu?',
  'origin.whatbefore.title': 'Co bylo před Velkým třeskem?',
  'origin.shortanswer': '<strong>Krátká odpověď:</strong><br/>❗ Podle moderní fyziky vůbec nic — ani čas, ani prostor. Velký třesk byl začátkem samotného času.',
  'origin.longeranswer': '<strong>Delší odpověď:</strong><br/>Existují hypotézy o tom, co mohlo existovat „před", ale v současnosti nemáme experimenty, které by je potvrdily nebo vyvrátily.',

  'origin.p1': 'Přibližně před 13,8 miliardami let prošel vesmír extrémně rychlou expanzí nazývanou kosmická inflace, při níž se prostor sám rozpínal rychleji než rychlost světla. Vědci stále nevědí, co existovalo před inflací nebo co ji pohánělo, ale energie pohánějící tento proces mohla být součástí samotné struktury prostoročasu. Inflace pomáhá vysvětlit základní rysy dnešního vesmíru — jeho velkoplošnou plochost, stejnorodost a způsob, jakým se drobné kvantové fluktuace roztáhly do počátečních hustotních variací, z nichž později vznikly galaxie.',
  'origin.p2': 'Když inflace skončila, její energie se přeměnila na hmotu a záření — tím začal samotný Velký třesk. Přibližně jednu sekundu po této události byl vesmír neuvěřitelně horký, asi 10 miliard °C, a tvořil hustou „prvotní polévku" částic a světla. V následujících minutách, v období zvaném nukleosyntéza, se protony a neutrony srážely a vytvářely první prvky: vodík, hélium a stopy lithia a berylia.',
  'origin.p3': 'Teorie Velkého třesku popisuje, jak se vesmír rozšíří z počátečního stavu extrémně vysoké hustoty a teploty. Kosmologické modely na základě této teorie úspěšně vysvětlují jevy jako hojnost lehkých prvků, záření kosmického mikrovlnného pozadí (CMB) a velkoplošnou strukturu vesmíru. Přesná měření rychlosti expanze vesmíru stanovují jeho stáří na 13,787 ± 0,02 miliardy let.',
  'origin.p4': 'Jak se vesmír rozšiřoval, chladl, což umožnilo vznik subatomárních částic — a nakonec atomů. Tyto prvotní prvky, většinou vodík s trochou hélia a lithia, se později za pomoci gravitace a temné hmoty shlukly a vytvořily první hvězdy a galaxie. Pozorování vzdálených supernov ukazují, že expanze vesmíru se zrychluje — tento jev je přisuzován temné energii.',
  'origin.p5': 'Myšlenku expandujícího vesmíru zavedl v roce 1922 Alexander Friedmann, který odvodil rovnice popisující kosmickou expanzi. Nezávisle na něm Edwin Hubble pozoroval v roce 1929, že galaxie se od nás vzdalují rychlostí úměrnou jejich vzdálenosti. V roce 1931 Georges Lemaître navrhl, že vesmír pocházel z „prvotního atomu" — tak se zrodila moderní idea Velkého třesku.',
  'origin.p6': 'Navzdory svému úspěchu čelí model Velkého třesku stále otevřeným otázkám — asymetrie hmoty a antihmoty, skutečná povaha temné hmoty a původ temné energie.',
  'origin.p7': 'Vědci využili devět let dat ze sondy NASA Wilkinson Microwave Anisotropy Probe k vytvoření tohoto podrobného celooblohového snímku kosmického mikrovlnného pozadí. Snímek odhaluje 13,8 miliardy let staré teplotní fluktuace (zobrazené různými barvami) — zárodky, z nichž vyrostly dnešní galaxie.',

  'origin.h21': 'Lámete si nad tím hlavu?',
  'origin.h31': '💥Proběhl Velký třesk, i když čas ještě neexistoval?',
  'origin.p8':  '<strong>Ano — čas vznikl spolu s prostorem.</strong>',
  'origin.li1': 'Velký třesk není explozí v čase.',
  'origin.li2': 'Je to nulový moment — zrození samotného času.',
  'origin.li3': 'Neexistuje žádné „předtím", protože čas ještě nezačal plynout.',
  'origin.li4': 'Jinými slovy: „Čas začal prvním tichotem hodin vesmíru." Předtím nebylo nic, co by mohlo čas měřit — protože čas sám neexistoval.',

  'origin.h32': '🌀 „Expandoval prostor náhle po nepatrném zlomku sekundy?"',
  'origin.p9':  '<strong>Ano — to je inflační fáze.</strong>',
  'origin.li5': 'Přibližně 10<sup>-35</sup> sekund po vzniku prostoru začala kosmická inflace.',
  'origin.li6': 'V neuvěřitelně krátkém okamžiku se prostor rozšířil daleko více než za celý zbytek kosmické historie.',
  'origin.li7': 'Nebyla to exploze jako dynamit — byl to samotný prostor, který se expandoval všude najednou.',
  'origin.li8': 'Představte si to jako „super-nafukování" vesmíru, nikoli částice explodující do prázdného prostoru.',

  'origin.h33': '⚛️ „A částice se vytvořily teprve potom?"',
  'origin.p10': '<strong>Správně — hmota se objevila po inflaci.</strong>',
  'origin.li9':  'Když inflace skončila (kolem 10<sup>-32</sup> sekund), prostor se začal zahřívat — toto období se nazývá přehřívání (reheating).',
  'origin.li10': 'Energie prostoru se přeměnila na částice: kvarky, gluony, elektrony…',
  'origin.li11': 'Tyto částice tvořily první prvotní polévku — kvark-gluonové plazma.',

  'origin.h34': '🌌 „A jakmile se částice vytvořily, expandovaly spolu s prostorem?"',
  'origin.p11': '<strong>Přesně tak.</strong>',
  'origin.li12': 'Částice nevystřelovaly ven — existovaly uvnitř expandujícího prostoru a roztahovaly se s ním.',
  'origin.li13': 'Hmota se vytvořila uvnitř vesmíru, který se již rychle rozrůstal.',
  'origin.li14': 'Postupem času se vytvořily atomy, hvězdy a galaxie — vše „plave" v prostoru, který se stále zvětšuje.',

  'origin.h35': '🧠 Závěr',
  'origin.p12': '"V jednom okamžiku vznikl prostor a čas. Okamžitě poté (ve zlomku sekundy) prošel vesmír inflací — fází, kdy se prostor sám extrémně rychle expandoval. Poté se energie přeměnila na hmotu — a tato hmota expanduje spolu s prostorem dodnes."',

  'origin.h22': 'Co bylo před Velkým třeskem?',
  'origin.h36': '🧪 Standardní kosmologie — čas začíná Velkým třeskem',
  'origin.li15': 'Podle Einsteina je čas součástí prostoru — sjednoceného prostoročasu.',
  'origin.li16': 'Pokud prostor vznikl při Velkém třesku, čas vznikl s ním.',
  'origin.li17': 'Ptát se na „předtím" proto nemá fyzikální smysl.',
  'origin.li18': 'Je to jako ptát se, co leží severně od severního pólu.',

  'origin.h37': '🌀 Cyklický vesmír / teorie Velkého odrazu',
  'origin.li19': 'Vesmír se může opakovaně rozšiřovat a smršťovat.',
  'origin.li20': 'Před naším Velkým třeskem se mohl zhroutit předchozí vesmír.',
  'origin.li21': 'Po tomto „velkém krachu" nastal nový Velký třesk.',
  'origin.li22': 'Některé verze říkají, že tento cyklus může pokračovat donekonečna.',
  'origin.li23': '🔁 Třesk → expanze → kolaps → třesk → ...',

  'origin.h38': '🌌 Multivesmír / Kvantová fluktuace / Vakuové modely',
  'origin.li24': 'V některých modelech náš vesmír vznikl z kvantové fluktuace v „vakuovém stavu".',
  'origin.li25': 'Mohlo by existovat nekonečně mnoho vesmírů, každý s odlišnými fyzikálními zákony.',
  'origin.li26': 'Náš vesmír je jen jednou bublinou mezi nesčetnými dalšími.',

  'origin.h39': '🧊 Věčná inflace',
  'origin.li27': 'Inflace (rychlá expanze prostoru) může probíhat donekonečna.',
  'origin.li28': 'V různých oblastech se zastavuje v různých časech a vytváří nové vesmíry.',
  'origin.li29': 'Nové vesmíry se neustále rodí — jako bubliny v nekonečné pěně.',
  'origin.li30': 'Náš vesmír je jen jednou bublinou.',

  'origin.p13':       'Koncept cyklického vesmíru',
  'origin.cap1':      'Koncept cyklického vesmíru',
  'origin.conclusion': '"V jednom okamžiku vznikl prostor a čas. Okamžitě poté (ve zlomku sekundy) prošel vesmír inflací — fází, kdy se prostor sám extrémně rychle expandoval. Poté se energie přeměnila na hmotu — a tato hmota expanduje spolu s prostorem dodnes."',

  # ── Shape of the Universe ───────────────────────────────────────────────
  'shape.h1': 'TVAR VESMÍRU',
  'shape.p1': 'Skutečný tvar vesmíru je jednou z nejhlubších otevřených otázek moderní kosmologie. Vědci popisují tvar kosmu dvěma základními způsoby: geometrickým zakřivením (které určuje, jak se prostor lokálně ohýbá) a topologií (která popisuje, jak je prostor propojen v největších měřítkách). Tyto dva koncepty společně určují, zda je vesmír nekonečný nebo konečný, plochý nebo zakřivený.',
  'shape.p2': 'Zásadním mezníkem byla mise Planck. Jedním z jejích hlavních cílů bylo zjistit, zda je vesmír dokonale plochý nebo má mírné zakřivení. Analýzou drobných teplotních variací kosmického mikrovlnného záření pozadí Planck zjistil, že vesmír se jeví jako ohromně plochý — s jakýmkoli možným zakřivením omezeným na chybu přibližně 1 část z 500.',
  'shape.p3': 'Pochopení zakřivení je jen polovina příběhu. Druhá polovina spočívá v topologii — studiu toho, jak je prostor globálně propojen. Dokonce i dokonale plochý vesmír může mít bohatou a překvapivou topologii. Jednou populární možností je, že vesmír by mohl mít tvar 3D toru (vyšší analogie prostoru podobného donutu). V takovém vesmíru by cestování dostatečně daleko jedním směrem mohlo vás přivést zpět z opačné strany.',
  'shape.p4': 'Tato myšlenka vede k fascinujícím scénářům. V dostatečně malém toroidálním vesmíru bychom teoreticky mohli vidět umírající galaxii v jednom směru a zároveň její mnohem mladší verzi z jiného směru, protože světlo by si razilo různé obtočné cesty. Nicméně tato možnost se stává prakticky nemožnou ve vesmíru, který se rozrůstá tak rychle jako ten náš.',
  'shape.p5': 'Kromě toroidálních možností kosmologové zkoumají mnoho dalších potenciálních topologií. Pozitivně zakřivený vesmír by mohl mít tvar 3-sféry (vyšší analogie povrchu zeměkoule). Slavný Poincarého dvanáctistěnový prostor si představuje vesmír vyplněný opakujícími se dvanáctistěny, jejichž protilehlé stěny se propojují s rotací. Hyperbolické topologie vyvstávají z negativně zakřiveného prostoru.',
  'shape.p6': 'Navzdory tomuto množství možností současná pozorování neodhalují žádné opakující se vzory v rozdělení galaxií nebo v kosmickém mikrovlnném záření pozadí, které by naznačovaly malý nebo těsně zavinutý vesmír. V kombinaci s extrémně přesným měřením plochosti z mise Planck důkazy naznačují jeden ze dvou hlavních scénářů: buď je vesmír skutečně nekonečný, nebo je konečný, ale neobyčejně velký.',
  'shape.p7': 'To, co dnes vidíme, je kosmos, který se chová téměř dokonale plochý, následující známá pravidla Euklidovské geometrie na desítky miliard světelných let. Přímé čáry zůstávají rovnoběžné, trojúhelníky mají součet úhlů 180 stupňů a světlo se chová, jako by se pohybovalo dokonale plochým prostorem (kromě míst, kde hmota lokálně zakřivuje prostoročas).',
  'shape.p8': 'Nakonec tvar vesmíru zůstává hlubokou vědeckou záhadou. Moderní měření přísně omezují to, čím může být, ale zároveň odhalují, jak mnoho leží za naším dosahem. Ať již nekonečný nebo konečný, zakřivený nebo plochý, jednoduchý nebo vícenásobně propojený — vesmír stále vyzývá naši fantazii.',
  'shape.cap1': 'Mise Planck: teplotní anizotropie kosmického mikrovlnného záření pozadí',

  # ── Stars hub (universe-stars.html) ─────────────────────────────────────
  'ustars.h1':    'HVĚZDY',
  'ustars.intro': 'Hvězda je <strong>obrovská svítící koule horkého plazmatu</strong> udržovaná pohromadě vlastní gravitací. Ve středu hvězdy přeměňuje jaderná fúze lehké prvky na těžší a uvolňuje přitom obrovské množství energie.',

  'ustars.h21': 'Z čeho jsou hvězdy složeny',
  'ustars.p1': 'Většina hvězd se skládá hlavně z <strong>vodíku</strong> a <strong>hélia</strong>, s malým množstvím těžších prvků (astronomové je nazývají „kovy"). Protože jsou hvězdy tak horké, hmota uvnitř nich existuje jako plazma: atomy jsou rozděleny na jádra a volné elektrony.',
  'ustars.p2': 'Gravitace se snaží hvězdu stlačit dovnitř, zatímco tlak horkého plynu a energie z fúze tlačí ven. Stabilní hvězda je rovnováhou mezi těmito dvěma silami (hydrostatická rovnováha).',

  'ustars.h31': 'Proč mají hvězdy různé barvy',
  'ustars.p3': 'Barva hvězdy je hlavně vodítkem k její <strong>povrchové teplotě</strong>. Horké hvězdy vypadají modrobíle, zatímco chladnější hvězdy vypadají oranžově nebo červeně. To souvisí s tím, jak horký objekt vyzařuje světlo (přibližně jako „absolutně černé těleso").',
  'ustars.p4': 'Barva sama o sobě vám ale neřekne vše. Dvě hvězdy mohou mít podobné barvy, ale velmi odlišné velikosti a jasnosti. Proto astronomové používají diagramy jako <strong>Hertzsprungův–Russellův (H-R) diagram</strong> pro porovnání teploty a svítivosti.',

  'ustars.h32': 'Světlo, spektra a prvky',
  'ustars.p5': 'Když rozložíme světlo hvězdy do duhy (<strong>spektrum</strong>), vidíme tmavé absorpční čáry. Tyto čáry fungují jako otisky prvků v atmosféře hvězdy — vodíku, hélia, sodíku, vápníku a mnoha dalších. Spektra mohou také odhalit teplotu hvězdy, povrchovou gravitaci, rotaci a zda se pohybuje směrem k nám nebo od nás (Dopplerův jev).',

  'ustars.h33': 'Kolik hvězd existuje?',
  'ustars.p6': 'Přesné číslo neznáme. Běžný odhad řádu velikosti pro pozorovatelný vesmír je <strong>~10<sup>22</sup> až 10<sup>24</sup> hvězd</strong> (přibližně <strong>10–1000 sextiliard</strong>), protože může existovat stovky miliard galaxií, každá s miliardami až biliony hvězd.',
  'ustars.p7': 'Jen v naší vlastní Mléčné dráze se odhady obvykle pohybují v řádu <strong>~100–400 miliard</strong> hvězd. Dokonce i v naší galaxii je většina hvězd příliš slabá na to, abychom je viděli bez dalekohledů.',

  'ustars.h22': 'Zrození, život a smrt',
  'ustars.p8': '<strong>Zrození:</strong> hvězdy se tvoří uvnitř studených molekulárních mraků. Když se husté místo zhroutí, zahřeje se a stane se protohvězdou. Jakmile se jádro stane dostatečně horkým a hustým, začne fúze vodíku a hvězda vstoupí do dlouhé stabilní fáze.',
  'ustars.p9': '<strong>Život:</strong> většinu svého života stráví hvězda na <strong>hlavní posloupnosti</strong>, fúzí vodíku na hélium. Jaderné reakce v jádru závisí na hmotnosti hvězdy. <strong>Hmotnost</strong> hvězdy ovládá téměř vše: teplotu, jasnost a životnost. Masivní hvězdy spalují palivo rychle a žijí krátce; malé hvězdy spalují pomalu a mohou existovat extrémně dlouhou dobu.',
  'ustars.p10': '<strong>Smrt:</strong> když jádro dojde palivo, hvězda změní strukturu. Hvězdy podobné Slunci se expandují do <strong>červených obrů</strong>, pak odhodí vnější vrstvy a zanechají <strong>bílého trpaslíka</strong>. Velmi masivní hvězdy se stanou <strong>nadobry</strong> a mohou skončit mocnými výbuchy supernov.',

  'ustars.h34': 'Proč je hmotnost „hlavním ovladačem"',
  'ustars.p11': 'Hmotnost nastavuje tlak a teplotu v jádru. Vyšší teplota jádra fúzi výrazně urychluje, takže velké hvězdy jsou jasnější, ale kratší životnosti. Malé hvězdy jsou slabé, ale stabilní po dlouhou dobu. Proto vesmír obsahuje mnoho dlouho žijících červených trpaslíků.',

  'ustars.h35': 'Co se stane s materiálem?',
  'ustars.p12': 'Když hvězdy ztrácejí hmotu — hvězdným větrem, expandujícími obálkami nebo výbuchy — obohacují okolní prostor těžšími prvky. Pozdější generace hvězd (a planet) se tvoří z tohoto „recyklovaného" materiálu. V tom smyslu mnohé atomy v Zemi a v našich tělech byly kdysi uvnitř hvězd.',

  'ustars.h36': 'Planetární mlhoviny a hvězdné mlhoviny',
  'ustars.p13': 'Planetární mlhoviny jsou svítící obálky plynu vyvržené umírajícími hvězdami malé hmotnosti, představující konec hvězdného života, zatímco hvězdné mlhoviny (nebo hvězdné líhně/emisní mlhoviny) jsou obrovské mraky prachu a plynu, kde se rodí nové hvězdy. Planetární mlhoviny jsou krátkodobé hrobky, zatímco hvězdné mlhoviny jsou živá, dlouhotrvající místa zrodu.',

  'ustars.h23': 'Jasnost, vzdálenost a proč hvězdy blikají',
  'ustars.p14': 'Hvězda může vypadat jasně ze dvou různých důvodů: může být skutečně svítivá, nebo může být blízko k nám. Astronomové tyto pojmy oddělují: <strong>svítivost</strong> (skutečný výkon) a <strong>zdánlivá jasnost</strong> (jak jasná vypadá ze Země).',
  'ustars.p15': 'Hvězdy <strong>blikají</strong>, protože zemská atmosféra je turbulentní. Jak světlo hvězdy prochází pohyblivými vrstvami vzduchu, ohýbá se různými způsoby, což způsobuje zdánlivé chvění. Planety obvykle blikají méně, protože se jeví jako malé kotouče, nikoli jako bodové zdroje.',

  'ustars.h24': 'Hlavní typy hvězd',
  'ustars.p16': 'Tyto kategorie se překrývají: například červený trpaslík je také hvězdou hlavní posloupnosti, zatímco červený obr je pozdější evoluční fází. Hlavní myšlenka je, že hmotnost a stáří určují, jak hvězda vypadá a jak se chová.',

  'ustars.h25': 'VY Canis Majoris',
  'ustars.p17': '<strong>VY Canis Majoris (VY CMa)</strong> je velmi svítivá, vyvinutá masivní hvězda v souhvězdí Canis Major. Je klasifikována jako <strong>červený hyperobr</strong>: vzácná fáze, kdy masivní hvězda expandovala do obrovské velikosti a ztrácí hmotu prostřednictvím silných větrů.',
  'ustars.p18': '<strong>Poznámka:</strong> snímek zde je ilustrací hvězdy typu červeného nadobra/hyperobrů (ne nutně VY CMa samotné), použité k ladění s tématem stránky.',

  'ustars.h37': 'Jak velká je? „Kolik Sluncí se vejde dovnitř?"',
  'ustars.p19': 'Protože atmosféra hvězdy je rozšířená a prašná, přesný poloměr je nejistý. Ale klíčová myšlenka je měřítko: pokud je poloměr hvězdy přibližně <strong>1000× poloměr Slunce</strong>, její objem je přibližně 1000<sup>3</sup> = 10<sup>9</sup>× větší.',
  'ustars.p20': 'Takže ve smyslu „objemu" by se v takové hvězdě vešly přibližně <strong>miliarda Sluncí</strong> (jako hrubé, snadno zapamatovatelné srovnání). Toto je ilustrace, ne přesné měření.',

  'ustars.h38': 'Co se stane dále (supernova)',
  'ustars.p21': 'Hvězdy tak masivní, jako je VY CMa, mají skončit svůj život v <strong>supernově kolapsu jádra</strong>. Před tím mohou ztratit hodně hmoty a vytvořit složité obálky plynu a prachu kolem sebe. Výbuch obohacuje prostor těžkými prvky a může zanechat kompaktní pozůstatek (často <strong>neutronová hvězda</strong> nebo <strong>černá díra</strong>).',

  'ustars.h39': 'Ohrozilo by nás to?',
  'ustars.p22': 'Ze Země by takový jev byl neuvěřitelnou podívanou na obloze, ale hlavní nebezpečí od supernovy pochází z <strong>velmi blízkého</strong> zdroje (přibližně do několika desítek světelných let). VY CMa je od nás dostatečně daleko, takže není považována za přímou hrozbu pro Zemi.',
  'ustars.p23': 'I když není nebezpečná, výbuchy masivních hvězd mají pro vesmír velký význam: pomáhají vytvářet a šířit prvky, z nichž se později stávají nové hvězdy, planety a život.',

  # ── Galaxies hub (universe-galaxies.html) ───────────────────────────────
  'ugal.h1':    'GALAXIE',
  'ugal.intro': '<strong>Galaxie</strong> je obrovský gravitační systém složený z miliard až bilionů hvězd, plynu, prachu a temné hmoty. Galaxie jsou základní stavební kameny vesmíru na největších měřítkách.',
  'ugal.p1': 'Na nejjednodušší úrovni je galaxie obrovská sbírka hmoty udržovaná pohromadě gravitací. Obsahuje hvězdy (od nově narozených hvězdokup po starověké populace), mezihvězdný plyn a prach (surový materiál pro nové hvězdy) a mnohem větší neviditelnou složku zvanou temná hmota. Galaxie se pohybují od malých trpasličích galaxií s pouhými několika miliony hvězd po obrovské eliptické s biliony hvězd.',

  'ugal.h21': 'Hlavní typy galaxií',
  'ugal.p2':  '<strong>Galaxie se běžně seskupují podle tvaru a struktury.</strong>',
  'ugal.li1': '<a class="type-link" href="galaxy-spiral.html"><strong>Spirální galaxie</strong></a>',
  'ugal.li2': '<a class="type-link" href="galaxy-elliptical.html"><strong>Eliptické galaxie</strong></a>',
  'ugal.li3': '<a class="type-link" href="galaxy-irregular.html"><strong>Nepravidelné galaxie</strong></a>',
  'ugal.li4': '<a class="type-link" href="galaxy-dwarf.html"><strong>Trpasličí galaxie</strong></a>',
  'ugal.li5': '<a class="type-link" href="galaxy-lenticular.html"><strong>Čočkové galaxie</strong></a>',
  'ugal.li6': '<a class="type-link" href="galaxy-blazars.html"><strong>Blazary</strong></a>',
  'ugal.li7': '<a class="type-link" href="galaxy-quasars.html"><strong>Kvazary</strong></a>',
  'ugal.li8': '<strong>Aktivní galaxie</strong> — Přibližně 10 % známých galaxií je aktivních, což znamená, že jejich jádro vyzařuje výjimečně velké množství energie z důvodu akrece do centrální supermassivní černé díry.',
  'ugal.li9': '<strong>Seyfertovy galaxie</strong> — Jsou nejčastějším typem aktivních galaxií a také nejběžnějším typem aktivních galaktických jader (AGN).',
  'ugal.p3': 'Tyto kategorie jsou užitečným výchozím bodem, ale skutečné galaxie mohou být nepořádné. Mnoho vykazuje tyče, prstence, zkroucení nebo přílivové chvosty a jejich vzhled se může v průběhu kosmického času měnit.',

  'ugal.h22': 'Evoluce galaxií',
  'ugal.p4': 'Galaxie nejsou statické objekty. Během miliard let rostou, transformují se a někdy zastavují svou hvězdotvorbu. V moderní kosmologii (tzv. „hierarchický" obraz) se nejprve tvoří malé struktury, které se pak prostřednictvím kontinuální akumulace plynu a opakovaných splynutí budují do větších.',
  'ugal.p5': '<strong>Časová osa (přibližně):</strong> první hvězdy se vytvořily v průběhu prvních několika set milionů let po Velkém třesku a první malé galaxie se mají objevit do <strong>první miliardy let</strong>. Během dalších miliard let se galaxie shromáždily do větších systémů a kosmická míra hvězdotvorby dosáhla vrcholu přibližně <strong>před ~10 miliardami let</strong>.',
  'ugal.p6': 'Zpětná vazba od supernov a od supermasivních černých děr (aktivní galaktická jádra) může zahřívat nebo vypuzovat plyn, regulující rychlost tvorby nových hvězd. To pomáhá vysvětlit, proč se mnoho masivních galaxií stane „uhašenými" (tvořícími málo nových hvězd) v pozdních dobách.',

  'ugal.h31': 'Srážky, interakce a splynutí',
  'ugal.p7': 'Srážky galaxií jsou běžné, protože galaxie žijí ve skupinách a shlucích. Většinou se hvězdy vzájemně přímo nesrazí (prostor mezi hvězdami je obrovský), ale gravitace silně přetváří galaxie. Přílivové síly mohou vytáhnout dlouhé chvosty, vyvolat hvězdné výbuchy, nakrmit centrální černé díry a narušit disky.',

  'ugal.li10': '<strong>Interakce:</strong> blízký průchod může deformovat tvary a zapálit novou hvězdotvorbu.',
  'ugal.li11': '<strong>Vedlejší splynutí:</strong> velká galaxie absorbuje menší a postupně ji roztrhá.',
  'ugal.li12': '<strong>Hlavní splynutí:</strong> dvě galaxie podobné hmotnosti se slijí; disky mohou být zničeny a vytvoří se více sféroidní systém.',
  'ugal.li13': '<strong>Mléčná dráha × Andromeda:</strong> očekává se, že se tyto dvě galaxie přiblíží a nakonec slijí za přibližně 4–5 miliard let.',
  'ugal.p8': 'Protože splynutí byla častější v raném vesmíru, mnoho galaxií, které dnes vidíme, nese „fosilní" důkazy minulých srážek v jejich hvězdných tocích, bulge struktuře a pohybech hvězd a plynu.',

  'ugal.h23': 'Mléčná dráha',
  'ugal.p9': 'Mléčná dráha je <strong>tyčová spirální galaxie</strong>, která obsahuje naši Sluneční soustavu. Má rotující disk se spirálními rameny, centrální bulge/tyč a rozšířené halo dominované temnou hmotou. Z naší polohy uvnitř disku ji vidíme jako jasný pruh přes noční oblohu.',
  'ugal.li14': '<strong>Velikost:</strong> přibližně <strong>~100 000</strong> světelných let napříč (odhad řádu velikosti).',
  'ugal.li15': '<strong>Hvězdy:</strong> přibližně <strong>stovky miliard</strong> hvězd.',
  'ugal.li16': '<strong>Centrální černá díra:</strong> Sagittarius A*, přibližně <strong>~4 miliony</strong> slunečních hmotností.',
  'ugal.li17': '<strong>Poloha Slunce:</strong> přibližně <strong>~26 000</strong> světelných let od středu.',
  'ugal.li18': '<strong>Čas:</strong> nejstarší hvězdy jsou &gt; <strong>13 miliard</strong> let staré.',
  'ugal.p10': 'Mléčná dráha rostla prostřednictvím dlouhé historie akumulace a vedlejších splynutí. Proudy hvězd kolem galaxie jsou důkazem menších galaxií, které byly časem roztrhány a absorbovány.',

  'ugal.h24': 'Andromeda (M31)',
  'ugal.p11': 'Andromeda (Messier 31) je nejbližší velká spirální galaxie k Mléčné dráze a největší člen Místní skupiny. Je viditelná pouhým okem z tmavých míst a dlouho byla klíčovým cílem pro pochopení vývoje spirálních galaxií.',
  'ugal.li19': '<strong>Vzdálenost:</strong> přibližně <strong>~2,5 milionu</strong> světelných let.',
  'ugal.li20': '<strong>Velikost:</strong> větší než Mléčná dráha (přibližně <strong>~200 000+</strong> světelných let napříč).',
  'ugal.li21': '<strong>Pohyb:</strong> přibližuje se k Mléčné dráze rychlostí přibližně <strong>~100 km/s</strong>.',
  'ugal.li22': '<strong>Budoucnost:</strong> pravděpodobné blízké setkání/splynutí s Mléčnou dráhou za přibližně <strong>~4–5 miliard</strong> let.',
  'ugal.p12': 'Stejně jako Mléčná dráha, Andromeda vykazuje důkazy minulých splynutí a interakcí. Studium jejích hvězd, plynu a satelitních galaxií pomáhá rekonstruovat historii sestavení naší místní kosmické sousedství.',

  'ugal.h25': 'Pozorovatelný vesmír a jeho kosmická síť',
  'ugal.p13': 'Galaxie nejsou rozmístěny rovnoměrně. Na největších měřítkách je gravitace uspořádává do kosmické sítě: filamentů, stěn a shluků oddělených obrovskými prázdnotami. Skupiny a shluky galaxií jsou udržovány pohromadě sdíleným haleem temné hmoty.',
  'ugal.p14': 'Kosmická síť je největší známá struktura ve vesmíru — obrovská síť vzájemně propojených filamentů složených z galaxií, galaktických shluků a temné hmoty, táhnoucí se přes miliardy světelných let. Tato síťovitá struktura vznikla z drobných fluktuací v raném vesmíru, postupně formovaných gravitací po miliardy let.',
  'ugal.cap1': 'Spirální galaxie Messier 74 — fotografovaná Vesmírným dalekohledem Hubble',
  'ugal.cap2': 'Dvě slévající se galaxie: IC 2163 a NGC 2207',
  'ugal.cap3': 'Mapa Mléčné dráhy — naše domovská galaxie',
  'ugal.cap4': 'Andromeda (M31) — nejbližší velká spirální galaxie k Mléčné dráze (ilustrace)',
  'ugal.cap5': 'Panoramatický pohled na celou blízkou infračervenou oblohu odhalující Mléčnou dráhu',

  # ── Planets hub (universe-planets.html) ─────────────────────────────────
  'uplanets.h1': 'PLANETY',
}

# I'll continue building cs dict in the generator below
# For now, just write what we have and fill in from en for missing keys

output_path = '/home/runner/work/My-website-project/My-website-project/scripts/i18n.js'

# Identify all keys that still need CS translation  
missing_cs = [k for k in en if k not in cs]
print(f"Keys with CS translation: {len(cs)}")
print(f"Keys missing CS translation: {len(missing_cs)}")
print("Missing keys:")
for k in missing_cs[:20]:
    print(f"  {k}")
