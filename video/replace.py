from pathlib import Path
import gzip

script_dir = Path(__file__).resolve().parent

input_file = script_dir / "original_frames.bin.gz"
output_file = script_dir / "frames.bin.gz"

with gzip.open(input_file, "rb") as f:
    data = f.read()

data = data.replace(b"\x01", b"\x00")

with gzip.open(output_file, "wb") as f:
    f.write(data)