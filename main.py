
import os

ENTRY = "The climax was my performance review and I failed it on purpose — one blinking light, zero applause, and a family that only notices me when I stop."

os.makedirs("/output", exist_ok=True)

fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
os.write(fd, ENTRY.encode("utf-8"))
os.close(fd)
