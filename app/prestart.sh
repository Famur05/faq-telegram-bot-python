#!/usr/bin/env bash
set -e

python3 -m app.faq_db

exec python3 -m app.main