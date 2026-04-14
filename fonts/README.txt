Umísti sem soubory písma pro "Momo Trust Display".

Požadované soubory (doporučené):
- MomoTrustDisplay.woff2
- MomoTrustDisplay.woff

Cesta: c:\Users\simon\Downloads\WEB PROJEKT\fonts\

Poznámky:
- @font-face v `style.css` nyní načítá tyto soubory. Pokud máš soubor s jiným názvem, uprav v `style.css` hodnotu `src: url('fonts/....')`.
- Pokud nemáš soubory písma, můžeš je buď stáhnout od dodavatele písma (ujisti se, že máš práva), nebo použít alternativní webfont (Google Fonts) a přidat link do `index.html`.

Jak to otestovat lokálně (PowerShell):
1) Spusť lokální server v kořenové složce projektu:
   Set-Location "C:\Users\simon\Downloads\WEB PROJEKT"
   py -3 -m http.server 8000
2) Otevři prohlížeč na http://localhost:8000/index.html a ověř, že titulek používá nový font.

Pokud chceš, můžu:
- Pomoci najít a stáhnout písmo (pokud máš odkaz), nebo
- Upravit CSS pro jiný font z Google Fonts (napiš název).