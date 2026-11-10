# Streams telemetry upstream via MQTT/HTTP.
# A intercepted connection failure transparently drops back into a transactional SQLite buffer, checking the uplink status continuosly

import os
import time
import json
import sqlite3
import random
import requests

# Config via environment variables for k8s compliance
DB_PATH = os.getenv("DB_PATH","/app/data/telemetry_buffer.db")
HQ_ENDPOINT = os.getenv("HQ_ENDPOINT","http://hq-ingest-service:8080")
NODE_ID = os.getenv("NODE_ID","tactical-edge-node-01")

def int_db():
    """Initializes the localized SQLite failure buffer"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry_queue(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL
            payload TEXT    
        )
    ''')
    conn.commit()
    conn.close()

def buffer_locally(timestamp, payload):
    """Safely dumps data onto a persistent disk during network blackout"""