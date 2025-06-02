#!/bin/bash

# Auto-update script for keeping financial data fresh
# This script updates market data every 30 minutes to simulate real-time changes

echo "🚀 Starting auto-update service for financial data..."

while true; do
    echo "$(date): Updating market data..."
    python /app/update_data.py
    
    echo "$(date): Sleeping for 30 minutes..."
    sleep 1800  # 30 minutes
done