import os
from PIL import Image, ImageDraw

def generate_icons():
    img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dvp-tex-kolkata\assets\images"
    os.makedirs(img_dir, exist_ok=True)

    # 1. logo.svg
    svg_logo = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 90" width="420" height="90">
  <defs>
    <linearGradient id="dvpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#3A86FF"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFD166"/>
      <stop offset="100%" stop-color="#F77F00"/>
    </linearGradient>
  </defs>
  <!-- Textile Loom / Diamond Weft Emblem -->
  <rect x="6" y="8" width="74" height="74" rx="16" fill="#0B132B" stroke="url(#dvpGrad)" stroke-width="2.5"/>
  <path d="M25 25 L61 25 L61 61 L25 61 Z" fill="none" stroke="url(#dvpGrad)" stroke-width="3" stroke-dasharray="6,4"/>
  <path d="M43 18 L68 43 L43 68 L18 43 Z" fill="none" stroke="url(#goldGrad)" stroke-width="4"/>
  <circle cx="43" cy="43" r="5" fill="#00E5FF"/>
  
  <!-- Text Brand -->
  <text x="96" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-weight="900" font-size="30" fill="#FFFFFF" letter-spacing="2">DVP TEX</text>
  <text x="96" y="68" font-family="'Inter', system-ui, sans-serif" font-weight="600" font-size="11.5" fill="#00E5FF" letter-spacing="3.5">TEXTILE EXPORTS &bull; KOLKATA</text>
</svg>"""

    with open(os.path.join(img_dir, "logo.svg"), "w", encoding="utf-8") as f:
        f.write(svg_logo)

    # 2. favicon.svg
    svg_favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="favGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#3A86FF"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFD166"/>
      <stop offset="100%" stop-color="#F77F00"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="24" fill="#0B132B"/>
  <rect x="6" y="6" width="88" height="88" rx="20" fill="none" stroke="url(#favGrad)" stroke-width="3"/>
  <path d="M50 20 L80 50 L50 80 L20 50 Z" fill="none" stroke="url(#goldGrad)" stroke-width="6"/>
  <circle cx="50" cy="50" r="8" fill="#00E5FF"/>
</svg>"""

    with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_favicon)

    # 512x512 image
    size = (512, 512)
    img = Image.new("RGBA", size, (11, 19, 43, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([(16, 16), (496, 496)], radius=96, outline=(0, 229, 255, 255), width=16)
    
    # Diamond weave
    pts = [(256, 110), (402, 256), (256, 402), (110, 256)]
    draw.polygon(pts, outline=(255, 209, 102, 255), width=24)
    draw.ellipse([(226, 226), (286, 286)], fill=(0, 229, 255, 255))

    img.save(os.path.join(img_dir, "logo-512.png"), "PNG")

    apple = img.resize((180, 180), Image.Resampling.LANCZOS)
    apple.save(os.path.join(img_dir, "apple-touch-icon.png"), "PNG")

    fav32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    fav32.save(os.path.join(img_dir, "favicon-32x32.png"), "PNG")
    fav32.save(os.path.join(img_dir, "favicon.ico"), format="ICO", sizes=[(32, 32)])

    print("DVP Tex favicon suite generated successfully!")

if __name__ == "__main__":
    generate_icons()
