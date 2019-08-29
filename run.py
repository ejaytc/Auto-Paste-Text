#!/usr/bin/env python3
import os

path = r"/home/jay/Desktop/git\ Workspace/Auto-Paste-Text/Autopaste.pyw"

os.system('chmod +x Autopaste.pyw')
os.system('nohup ' + path + ' > output.log&')