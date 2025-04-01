import subprocess
import sys
import urllib.parse

def search_ads(query):
    encoded_query = urllib.parse.quote(query)
    urls = [
        f"https://www.leboncoin.fr/recherche?text={encoded_query}&kst=k",
        f"https://www.marktplaats.nl/q/{query.replace(' ', '+')}/",
        f"https://www.kleinanzeigen.de/s-{query.replace(' ', '-')}/k0",
        f"https://fr.audiofanzine.com/recherche/{encoded_query}.html",
        f"https://www.subito.it/annunci-italia/vendita/usato/?q={encoded_query}",
        f"https://www.ricardo.ch/de/s/{query.replace(' ', '%20')}/",
        f"https://www.mercatinomusicale.com/ann/search.asp?ns=1&rp=&ct=&ch=&__rpct=&kw={query.replace(' ', '+')}",
        f"https://reverb.com/marketplace?query={encoded_query}",
        f"https://soundsmarket.com/servicios/compraventa?clave={encoded_query}",
    ]
    
    for url in urls:
        subprocess.run(["open", url])  # Uses macOS's built-in open command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_ads.py \"search term\"")
    else:
        search_query = " ".join(sys.argv[1:])
        search_ads(search_query)