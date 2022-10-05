#!/bin/sh

echo "Waiting for postgres..."
while ! python3 -c "import socket;import sys; sys.exit(0) if 0 == socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(('postgres', 5432)) else sys.exit(1)"; do
  sleep 0.1
done
echo "PostgreSQL started"

flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app