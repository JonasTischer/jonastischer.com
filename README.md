# Personal Blog

My personal blog generated with [Pelican](https://docs.getpelican.com/en/latest/index.html)

Deployed using Cloudflare (https://dash.cloudflare.com/login)

Inspired by [Duarte Carmo](https://github.com/duarteocarmo/duarteocarmo.com)

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