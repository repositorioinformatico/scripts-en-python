import zipfile
with zipfile.ZipFile('/tmp/root.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/')
