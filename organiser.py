import os
import shutil

# Der Ordner der aufgeräumt werden soll
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Dateitypen und ihre Zielordner
ordner = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Dokumente": [".pdf", ".docx", ".txt", ".xlsx"],
    "Programme": [".exe", ".msi"],
    "Sonstiges": []
}

def organisiere():
    for datei in os.listdir(downloads):
        dateipfad = os.path.join(downloads, datei)
        
        if os.path.isfile(dateipfad):
            endung = os.path.splitext(datei)[1].lower()
            zielordner = "Sonstiges"
            
            for name, endungen in ordner.items():
                if endung in endungen:
                    zielordner = name
                    break
            
            ziel = os.path.join(downloads, zielordner)
            os.makedirs(ziel, exist_ok=True)
            shutil.move(dateipfad, os.path.join(ziel, datei))
            print(f"{datei} → {zielordner}")

organisiere()
print("Fertig!")