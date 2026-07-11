# EU Music Gear Search

A tiny, hand-coded web page that searches used **musical instruments and audio gear**
across ~20 European classifieds and marketplaces at once. Type a make or model and it
lines up a deep link straight into the results on every site.

No server, no tracking, no accounts, no build step — it's a single `index.html` that
just builds the search URLs for you. It'll keep working long after the fancier tools
have rotted.

## Use it

Open `index.html` in any browser, type a query (e.g. `Roland Juno-60`), and click through
to the marketplaces you care about — or hit **Open all in tabs**. The query is saved in
the URL (`…/#roland+juno-60`), so results are bookmarkable and shareable.

## Host it on GitHub Pages

1. Push this repo to GitHub.
2. **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
3. Pick the `main` branch and the `/ (root)` folder, then **Save**.
4. Your search page goes live at `https://<you>.github.io/eu-classified-search/`.

## Sites covered

**Music specialists:** Reverb · eBay (Musical Instruments) · Audiofanzine (FR) ·
Mercatino Musicale (IT) · Sounds Market (ES)

**General marketplaces** (deep-linked to the music category where the site has one):
Leboncoin (FR) · Kleinanzeigen (DE) · Marktplaats (NL) · 2dehands (BE) · Subito (IT) ·
Wallapop (ES) · Milanuncios (ES) · Ricardo (CH) · Tutti (CH) · Willhaben (AT) ·
Blocket (SE) · Tori (FI) · Finn (NO) · DBA (DK) · OLX (PL) · Gumtree (UK) ·
DoneDeal (IE) · Bazoš (CZ)

## Add a marketplace

Everything lives in one `sites` list near the top of the `<script>` in `index.html`.
Add a line:

```js
{ type: "general", flag: "🇵🇹", name: "OLX Portugal", url: q => `https://www.olx.pt/ads/q-${dash(q)}/` },
```

- `type` is `"music"` (specialist / already gear) or `"general"` (classifieds).
- `url(q)` gets the raw query and returns the deep link. Use the `enc` / `dash` / `plus`
  helpers for the encoding a given site expects.
