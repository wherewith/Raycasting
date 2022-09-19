import zipfile
import pathlib
import os

file_dir = pathlib.Path("./build/web")

with zipfile.ZipFile("web-release.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=1) as archive:
    for file_path in file_dir.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(file_dir))
os.replace("./web-release.zip", "./build/web-release.zip")
