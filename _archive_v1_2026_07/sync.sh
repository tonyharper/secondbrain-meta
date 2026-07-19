#!/bin/bash
set -e

cd "$(dirname "$0")"

# Sync to Google Drive
GDRIVE="$HOME/Library/CloudStorage/GoogleDrive-tonyharper@meta.com/My Drive/cal"
echo "Syncing to Google Drive..."
rsync -av --delete --exclude='.git/' "$(dirname "$0")/" "$GDRIVE/"
echo "Synced to Google Drive."
