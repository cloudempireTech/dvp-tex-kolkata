import os
import subprocess

src_video = r"C:\Users\dasan\.gemini\antigravity\scratch\tishoo-manufacturing-contai\assets\videos\hero.mp4"
dest_video = r"C:\Users\dasan\.gemini\antigravity\scratch\dvp-tex-kolkata\assets\videos\hero.mp4"
poster_img = r"C:\Users\dasan\.gemini\antigravity\scratch\dvp-tex-kolkata\assets\images\hero-poster.jpg"

print("Copying & optimizing 16:9 hero video with +faststart...")
cmd_video = [
    "ffmpeg", "-y", "-i", src_video,
    "-c:v", "copy", "-c:a", "copy",
    "-movflags", "+faststart",
    dest_video
]
subprocess.run(cmd_video, check=True)

print("Extracting high-definition hero poster at 1.5s...")
cmd_poster = [
    "ffmpeg", "-y", "-ss", "00:00:01.500", "-i", dest_video,
    "-vframes", "1", "-q:v", "2",
    poster_img
]
subprocess.run(cmd_poster, check=True)

v_size = os.path.getsize(dest_video) / (1024 * 1024)
p_size = os.path.getsize(poster_img) / 1024
print(f"Hero video ready: {v_size:.2f} MB")
print(f"Hero poster ready: {p_size:.1f} KB")
