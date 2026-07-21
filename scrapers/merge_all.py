"""
Tüm scraper çıktılarını ana tr.json ve eng.json dosyalarına birleştirir.

Kullanım:
  1. Önce her scraper'ı tek tek çalıştır:
     python scrapers/scrape_stackoverflow.py
     python scrapers/scrape_github_trending.py
     python scrapers/scrape_wikipedia_tech.py
     python scrapers/scrape_dev_to.py
     python scrapers/scrape_huggingface.py
     python scrapers/scrape_arxiv.py

  2. Sonra bu scripti çalıştır:
     python scrapers/merge_all.py
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
SCRAPERS_DIR = BASE_DIR

# Scraper output dosyaları
SCRAPER_FILES_EN = [
    "so_eng.json",
    "github_eng.json",
    "wiki_eng.json",
    "devto_eng.json",
    "hf_eng.json",
    "arxiv_eng.json",
    "bulk_en.json",
    "bulk_en2.json",
    "reddit_eng.json",
    "pwc_eng.json",
]

SCRAPER_FILES_TR = [
    "so_tr.json",
    "github_tr.json",
    "wiki_tr.json",
    "devto_tr.json",
    "hf_tr.json",
    "arxiv_tr.json",
    "bulk_tr.json",
    "bulk_tr2.json",
    "reddit_tr.json",
    "pwc_tr.json",
]

def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"train": []}

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # Ana dosyaları yükle
    eng_path = os.path.join(DATA_DIR, "eng.json")
    tr_path = os.path.join(DATA_DIR, "tr.json")

    eng_data = load_json(eng_path)
    tr_data = load_json(tr_path)

    original_en = len(eng_data["train"])
    original_tr = len(tr_data["train"])

    # EN scraper dosyalarını birleştir
    for fname in SCRAPER_FILES_EN:
        fpath = os.path.join(SCRAPERS_DIR, fname)
        scraped = load_json(fpath)
        eng_data["train"].extend(scraped.get("train", []))
        print(f"  EN: {fname} -> {len(scraped.get('train', []))} entries")

    # TR scraper dosyalarını birleştir
    for fname in SCRAPER_FILES_TR:
        fpath = os.path.join(SCRAPERS_DIR, fname)
        scraped = load_json(fpath)
        tr_data["train"].extend(scraped.get("train", []))
        print(f"  TR: {fname} -> {len(scraped.get('train', []))} entries")

    # Kaydet
    save_json(eng_data, eng_path)
    save_json(tr_data, tr_path)

    print(f"\neng.json: {original_en} -> {len(eng_data['train'])} entries")
    print(f"tr.json: {original_tr} -> {len(tr_data['train'])} entries")
    print("Done!")

if __name__ == "__main__":
    main()
