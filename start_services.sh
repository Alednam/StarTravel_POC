#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.server.pid"
LOG_FILE="$SCRIPT_DIR/server.log"
PORT=8000

echo "=== Starting Science Calculator Services ==="

# 1. Check Python virtual environment
if [ -d "$SCRIPT_DIR/venv" ]; then
    PYTHON_BIN="$SCRIPT_DIR/venv/bin/python"
else
    echo "Error: Virtual environment not found at $SCRIPT_DIR/venv."
    echo "Please create one using: python3 -m venv venv && ./venv/bin/pip install -r requirements.txt"
    exit 1
fi

# 2. Check for .env file
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    if [ -f "$SCRIPT_DIR/.env.example" ]; then
        echo "Warning: .env not found. Copying .env.example to .env..."
        cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    else
        echo "Warning: No .env or .env.example file found."
    fi
fi

# 3. Check if server is already running
if [ -f "$PID_FILE" ]; then
    EXISTING_PID=$(cat "$PID_FILE")
    if kill -0 "$EXISTING_PID" 2>/dev/null; then
        echo "Service is already running with PID $EXISTING_PID (port $PORT)."
        echo "URL: http://127.0.0.1:$PORT/"
        exit 0
    else
        rm -f "$PID_FILE"
    fi
fi

# Also verify port availability
if command -v ss >/dev/null 2>&1; then
    if ss -tulpn | grep -q ":$PORT "; then
        echo "Notice: Port $PORT is already in use by an active process."
        echo "If this is another runserver instance, stop it or run ./stop_services.sh first."
        exit 1
    fi
fi

# 4. Run database migrations and populate knowledge base if empty
echo "Checking database migrations..."
"$PYTHON_BIN" "$SCRIPT_DIR/manage.py" migrate --noinput

if [ -f "$SCRIPT_DIR/science_engine/fixtures/knowledge_base.json" ]; then
    TOPIC_COUNT=$("$PYTHON_BIN" -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scicalc.settings')
django.setup()
from science_engine.models import Topic
print(Topic.objects.count())
" 2>/dev/null || echo "0")
    if [ "$TOPIC_COUNT" -eq 0 ]; then
        echo "Database is empty. Auto-loading knowledge base fixture (416 topics, 1,330 equations)..."
        "$PYTHON_BIN" "$SCRIPT_DIR/manage.py" loaddata knowledge_base
    fi
fi

# 5. Start Django development server in background
echo "Starting Django server on port $PORT..."
PYTHONUNBUFFERED=1 nohup "$PYTHON_BIN" "$SCRIPT_DIR/manage.py" runserver "0.0.0.0:$PORT" </dev/null > "$LOG_FILE" 2>&1 &
SERVER_PID=$!
echo "$SERVER_PID" > "$PID_FILE"

# 6. Verify startup
sleep 2
if kill -0 "$SERVER_PID" 2>/dev/null; then
    echo "✓ Science Calculator service started successfully!"
    echo "  PID: $SERVER_PID"
    echo "  Log: $LOG_FILE"
    echo "  URL: http://127.0.0.1:$PORT/ (or http://localhost:$PORT/)"
else
    echo "✗ Server failed to start. Last log entries:"
    tail -n 20 "$LOG_FILE"
    rm -f "$PID_FILE"
    exit 1
fi
