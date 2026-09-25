"""Verify downloaded research archives against this release's checksums and members."""
from pathlib import Path
import argparse, hashlib, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
def digest(stream):
    h=hashlib.sha256()
    for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory',type=Path)
    p.add_argument('--members',action='store_true',help='Also decompress and verify every member hash.')
    args=p.parse_args()
    manifest=json.loads((ROOT/'provenance/release-manifest.json').read_text())
    for asset in manifest['assets']:
        path=args.directory/asset['name']
        assert path.stat().st_size==asset['bytes'],path.name
        with path.open('rb') as f:assert digest(f)==asset['sha256'],path.name
        checked=0
        if args.members:
            with zipfile.ZipFile(path) as z:
                internal=json.loads(z.read('MANIFEST.json'))
                members=internal['files'];assert len(members)==asset['members']
                assert set(z.namelist())=={'MANIFEST.json'}|{x['path'] for x in members}
                for item in members:
                    assert not item['path'].startswith('/') and '..' not in Path(item['path']).parts
                    assert z.getinfo(item['path']).file_size==item['bytes']
                    with z.open(item['path']) as f:assert digest(f)==item['sha256'],item['path']
                    checked+=1
        print(json.dumps({'archive':path.name,'sha256':'passed','members_checked':checked}),flush=True)
if __name__=='__main__':main()
