# Vulnerable service

Vulnerable web service for [rumeetup](https://rumeetup.ru/) CTF.

## Install

1. [OPTIONAL] Generate new keys
    ```bash
    pip install -r requirements-min.txt
    python generate_keys.py
    ```
2. [OPTIONAL] Copy .env.example & Update secrets in .env and .env.db
   ```bash
   mv .env.example .env
   ```
3. Run service
   ```bash
   docker-compose up
   ```
