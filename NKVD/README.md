# Vulnerable service

Vulnerable web service for [rumeetup](https://rumeetup.ru/) CTF.

## Install

1. Generate new keys
    ```bash
    pip install -r requirements-min.txt
    python generate_keys.py
    ```
2. Copy .env.example
   ```bash
   mv .env.example .env
   ```
3. Update secrets in .env and .env.db
4. Run service
   ```bash
   docker-compose up
   ```
