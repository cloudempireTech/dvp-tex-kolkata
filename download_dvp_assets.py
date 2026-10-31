import os
import urllib.request
from PIL import Image

def download_and_optimize():
    img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dvp-tex-kolkata\assets\images"
    os.makedirs(img_dir, exist_ok=True)

    images = [
        # 1. Cotton canvas tote bags
        ("cotton-canvas-totes.jpg", "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=1200&q=80"),
        # 2. Industrial weaving loom / textile manufacturing
        ("industrial-weaving-loom.jpg", "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1200&q=80"),
        # 3. Luxury bed linen made-ups
        ("luxury-bed-linens.jpg", "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=1200&q=80"),
        # 4. Fabric rolls in workshop
        ("organic-fabric-rolls.jpg", "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=1200&q=80"),
        # 5. Kitchen / table linen made-ups
        ("table-linen-madeups.jpg", "https://images.unsplash.com/photo-1574634534894-89d7576c8259?auto=format&fit=crop&w=1200&q=80"),
        # 6. Yarn spools & colorful textile thread
        ("yarn-spinning-spools.jpg", "https://images.unsplash.com/photo-1584992236310-6edddc08acff?auto=format&fit=crop&w=1200&q=80"),
        # 7. Global export shipping containers
        ("export-container-cargo.jpg", "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&q=80"),
        # 8. Fabric quality inspection
        ("quality-inspection-fabric.jpg", "https://images.unsplash.com/photo-1513094735237-8f2714d57c13?auto=format&fit=crop&w=1200&q=80"),
        # 9. Eco drawstring bags / pouches
        ("eco-drawstring-pouches.jpg", "https://images.unsplash.com/photo-1598532163257-ae3c6b2524b6?auto=format&fit=crop&w=1200&q=80"),
        # 10. Fine textile texture and weave
        ("textile-craftsmanship-detail.jpg", "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=1200&q=80")
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for name, url in images:
        out_path = os.path.join(img_dir, name)
        temp_path = os.path.join(img_dir, "temp_" + name)
        print(f"Downloading {name}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp, open(temp_path, 'wb') as out_file:
                out_file.write(resp.read())

            with Image.open(temp_path) as im:
                im = im.convert("RGB")
                im = im.resize((1200, 800), Image.Resampling.LANCZOS)
                im.save(out_path, "JPEG", quality=82, optimize=True)

            if os.path.exists(temp_path):
                os.remove(temp_path)

            file_size_kb = os.path.getsize(out_path) / 1024
            print(f"  Saved {name} ({file_size_kb:.1f} KB)")
        except Exception as e:
            print(f"  Error downloading {name}: {e}")

if __name__ == "__main__":
    download_and_optimize()
