#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.server.pid"
PORT=8000

echo "=== Stopping Science Calculator Services ==="

STOPPED=false

# 1. Stop via PID file if present
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        echo "Stopping service with PID $PID..."
        kill "$PID" 2>/dev/null || true
        for i in {1..5}; do
            if ! kill -0 "$PID" 2>/dev/null; then
                break
            fi
            sleep 1
        done
        if kill -0 "$PID" 2>/dev/null; then
            echo "Force terminating PID $PID..."
            kill -9 "$PID" 2>/dev/null || true
        fi
        STOPPED=true
    fi
    rm -f "$PID_FILE"
fi

# 2. Cleanup any lingering manage.py runserver instances for this project
EXTRA_PIDS=$(pgrep -f "$SCRIPT_DIR.*manage.py runserver" || pgrep -f "manage.py runserver" || true)
if [ -n "$EXTRA_PIDS" ]; then
    echo "Terminating lingering runserver process(es): $EXTRA_PIDS"
    for p in $EXTRA_PIDS; do
        kill "$p" 2>/dev/null || true
    done
    sleep 1
    for p in $EXTRA_PIDS; do
        if kill -0 "$p" 2>/dev/null; then
            kill -9 "$p" 2>/dev/null || true
        fi
    done
    STOPPED=true
fi

if [ "$STOPPED" = true ]; then
    echo "✓ All Science Calculator services have been stopped."
else
    echo "No running Science Calculator services detected on port $PORT."
fi
