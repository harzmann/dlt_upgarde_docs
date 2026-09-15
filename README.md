# DLTNG Upgrade — Dokumentation / Documentation

## Deutsch

Öffentliche zweisprachige Dokumentation für DLTNG Upgrade, gebaut mit MkDocs Material und bereitgestellt über GitHub Pages.

- [Website Deutsch](https://harzmann.github.io/dlt_upgarde_docs/de/)
- [Website English](https://harzmann.github.io/dlt_upgarde_docs/en/)
- [Öffentlicher Download](https://github.com/harzmann/dlt_upgarde_docs/releases/tag/v0.2.0)

Das Repository heißt entsprechend der Vorgabe **`dlt_upgarde_docs`**. Es enthält Beschreibung, Anleitung, Downloadseite, Fehlerhilfe und getrennte Changelogs für Tool und Image. Der Programmquellcode liegt separat in `harzmann/dlt_upgrade`. EXE und Prüfsumme werden als öffentliche Release-Anlagen angeboten; große Binärdateien gehören nicht in die Git-Historie.

### Lokal bauen

```powershell
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe scripts/build.py
./.venv/Scripts/python.exe -m http.server 8000 --directory site
```

`release.json` enthält Version, echte EXE-Prüfsumme, Dateigröße und Downloadadressen. Der Build verweigert fehlende Prüfdaten, baut beide Sprachen mit strikter Prüfung und kontrolliert lokale Links. `assets/` enthält geteilte Illustrationen; sie werden beim Build in beide Sprachen kopiert. Die Sprachwahl verlinkt dieselbe Seite in der anderen Sprache.

Ein Push nach `main` baut und veröffentlicht die Website über `.github/workflows/pages.yml`. GitHub Pages muss dafür auf **GitHub Actions** eingestellt sein. Änderungen an Anleitung oder Changelogs immer in beiden Sprachen pflegen. Das Image-Changelog ist ein dokumentierter Stand des Image-Projekts; es ist keine automatische Hardwarefreigabe.

## English

Public bilingual documentation for DLTNG Upgrade, built with MkDocs Material and hosted on GitHub Pages.

- [German website](https://harzmann.github.io/dlt_upgarde_docs/de/)
- [English website](https://harzmann.github.io/dlt_upgarde_docs/en/)
- [Public download](https://github.com/harzmann/dlt_upgarde_docs/releases/tag/v0.2.0)

The repository is named **`dlt_upgarde_docs`** as requested. It contains the description, user guide, download page, troubleshooting and separate application/image changelogs. Application source is held separately in `harzmann/dlt_upgrade`. The EXE and checksum are public release assets; large binaries are not stored in Git history.

### Build locally

Use the commands above. `release.json` records the version, actual EXE checksum, size and download URLs. The build rejects missing verification data, builds both languages strictly and checks local links. Shared illustrations in `assets/` are copied into both language builds. The language selector links to the corresponding page in the other language.

A push to `main` builds and deploys the site through `.github/workflows/pages.yml`. GitHub Pages must use **GitHub Actions** as its source. Keep guide and changelog changes synchronized in both languages. The image changelog records a version of the image project; it does not grant hardware approval.
