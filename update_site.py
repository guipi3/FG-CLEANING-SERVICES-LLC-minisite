#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

# Get directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Update manifest.json
manifest = {
    "name": "TFG Cleaning Services LLC",
    "short_name": "TFG Cleaning",
    "description": "Professional residential and commercial cleaning services in Sanford, FL",
    "start_url": "/bio.html",
    "display": "standalone",
    "orientation": "portrait-primary",
    "background_color": "#ffffff",
    "theme_color": "#003D7A",
    "icons": [
        {"src": "logo-hojetech-16.png", "sizes": "16x16", "type": "image/png", "purpose": "any"},
        {"src": "logo-hojetech-32.png", "sizes": "32x32", "type": "image/png", "purpose": "any"},
        {"src": "logo-hojetech-64.png", "sizes": "64x64", "type": "image/png", "purpose": "any"},
        {"src": "logo-hojetech-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "logo-hojetech-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}
    ]
}

manifest_path = os.path.join(script_dir, "manifest.json")
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
print("✓ manifest.json updated")

# Update vcard.vcf
vcard_content = """BEGIN:VCARD
VERSION:3.0
PRODID:-//TFG Cleaning Services LLC//EN
FN:TFG Cleaning Services LLC
ORG:TFG Cleaning Services LLC
TEL;TYPE=WORK,VOICE:+1-407-335-6387
EMAIL;TYPE=WORK:tfgcleaningsvcs@gmail.com
ADR;TYPE=WORK:;;Sanford;FL;;USA
URL:https://www.tfgcleaningservices.com
NOTE:Professional residential and commercial cleaning services
END:VCARD"""

vcard_path = os.path.join(script_dir, "vcard.vcf")
with open(vcard_path, 'w', encoding='utf-8') as f:
    f.write(vcard_content)
print("✓ vcard.vcf updated")

# Replace content in bio.html
bio_path = os.path.join(script_dir, "bio.html")
with open(bio_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Color replacements
replacements = [
    # Colors
    ("background: #f87f0d", "background: linear-gradient(135deg, #003D7A 0%, #0066CC 100%)"),
    ("#2649cf", "#00A8CC"),
    ("border: 2px solid #00A8CC", "border: 3px solid #00A8CC"),
    ("border-color: #2649cf", "border-color: #00A8CC"),
    ("background: #274bcf", "background: rgba(255, 255, 255, 0.2)"),
    ("border: 1px solid #9a9a9a", "border: 1px solid rgba(255, 255, 255, 0.3)"),
    ("color: #1d2a3a;", "color: #ffffff;"),
    ("#e9d7c3", "#00A8CC"),
    ("border-top: 3px solid #25d366", "border-top: 3px solid #00A8CC"),
    ("color: #000000;", "color: #ffffff;"),
    ("opacity: 1;", "opacity: 0.95;"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Text replacements
text_replacements = [
    ("Doutor Tech Informática", "TFG Cleaning Services LLC"),
    ("Conserto de PC e notebook", "Professional House Cleaning"),
    ("Ilhéus Bahia", "Sanford, FL"),
    ("Doutor Tech oferece serviços", "TFG Cleaning Services LLC offers professional"),
    ("imagemdigitalbr@gmail.com", "tfgcleaningsvcs@gmail.com"),
    ("5573988779970", "14073356387"),
    ("https://instagram.com/doutor_tech_informatica", "https://instagram.com/tfgcleaning"),
    ("logotipo-doutor-tech-ilhes-bahia-2.png", "logo.png"),
]

for old, new in text_replacements:
    content = content.replace(old, new)

# Save bio.html
with open(bio_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ bio.html updated")

print("\n✅ All files updated successfully!")
print("   - Color scheme changed to blue (#003D7A, #00A8CC)")
print("   - Company name: TFG Cleaning Services LLC")
print("   - Location: Sanford, FL")
print("   - Contact: (407) 335-6387")
