import glob
import tarfile

for file in glob.glob("VS_*.tar.gz"):
    print("Reading files", file)
    tar_content = tarfile.open(file)
    # ...