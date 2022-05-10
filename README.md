# Personal Blog


# Development Guide

Create virtual environment

 `python3 -m venv ./venv `

Activate virtual environment
`source venv/bin/activate`

Install requirements

`pip install -r requirements.txt` 

## Site generation

### Locally serving site

`pelican --listen`

### Publish site

Regenerate site content

`pelican content -s publishconf.py`