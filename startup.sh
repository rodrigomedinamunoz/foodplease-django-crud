#!/bin/bash
# Ensure virtualenv installed packages are used, then start gunicorn
gunicorn foodplease.wsgi:application --bind=0.0.0.0:$PORT --workers 4
