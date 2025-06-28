#!/bin/bash

# Enhanced auto-update script for keeping financial data fresh
# This script updates market data every 30 minutes and adds new content periodically

echo "🚀 Starting enhanced auto-update service for financial data..."

# Initial comprehensive update
echo "$(date): Running initial comprehensive update..."
python /app/comprehensive_update.py

# Counter for tracking update cycles
update_cycle=0

while true; do
    echo "$(date): Sleeping for 30 minutes..."
    sleep 1800  # 30 minutes
    
    update_cycle=$((update_cycle + 1))
    echo "$(date): Running update cycle #$update_cycle..."
    
    # Every cycle: basic price and data updates
    python /app/update_data.py
    
    # Every 4th cycle (2 hours): comprehensive update with potential new content
    if [ $((update_cycle % 4)) -eq 0 ]; then
        echo "$(date): Running comprehensive update (cycle $update_cycle)..."
        python /app/comprehensive_update.py
    fi
    
    # Every 12th cycle (6 hours): major refresh
    if [ $((update_cycle % 12)) -eq 0 ]; then
        echo "$(date): Running major refresh (cycle $update_cycle)..."
        # Could add additional refresh logic here
    fi
done