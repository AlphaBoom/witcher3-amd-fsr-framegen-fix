from pathlib import Path
import hashlib,json,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
NAME='witcher3-amd-fsr-framegen-fix-v1.0.0.zip'
MOD='mods/modFSRStartupReinit'

def main():
    info=json.loads((ROOT/'build-info.json').read_text(encoding='utf-8'))
    entries={p.relative_to(ROOT).as_posix():p.read_bytes() for p in (ROOT/MOD).rglob('*') if p.is_file()}
    for path,expected in info['mod_script_sha256'].items():
        if path not in entries or hashlib.sha256(entries[path]).hexdigest()!=expected:
            raise SystemExit('Tested script hash mismatch: '+path)
    entries={name:(data if name.endswith('.ws') else data.replace(b'\r\n',b'\n')) for name,data in entries.items()}
    entries[MOD+'/NOTICE.md']=(ROOT/'NOTICE.md').read_bytes().replace(b'\r\n',b'\n')
    entries[MOD+'/LICENSE-MOD']=(ROOT/'LICENSE-MOD').read_bytes().replace(b'\r\n',b'\n')
    expected=set(info['mod_script_sha256'])|{MOD+'/README.txt',MOD+'/NOTICE.md',MOD+'/LICENSE-MOD'}
    if set(entries)!=expected:
        raise SystemExit('Unexpected distribution files: '+repr(set(entries)^expected))
    out=ROOT/'dist'; out.mkdir(exist_ok=True)
    archive=out/NAME
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(entries.items()):
            item=zipfile.ZipInfo(name,(2026,10,29,0,0,0))
            item.compress_type=zipfile.ZIP_DEFLATED
            item.external_attr=0o100644 << 16
            z.writestr(item,data)
    with zipfile.ZipFile(archive) as z, tempfile.TemporaryDirectory(prefix='fsr-zip-verify-',dir=out) as temp:
        assert Path(temp).resolve().is_relative_to(out.resolve())
        if z.testzip() is not None: raise SystemExit('ZIP integrity failure')
        for name in z.namelist():
            if not name.startswith(MOD+'/') or '\\' in name or '..' in Path(name).parts:
                raise SystemExit('Invalid install path: '+name)
        z.extractall(temp)
        extracted={p.relative_to(temp).as_posix():p.read_bytes() for p in Path(temp).rglob('*') if p.is_file()}
        if extracted!=entries: raise SystemExit('Extraction byte comparison failed')
    checksum=hashlib.sha256(archive.read_bytes()).hexdigest()
    (out/'SHA256SUMS.txt').write_text(checksum+'  '+NAME+'\n',encoding='ascii')
    print('Verified ZIP: '+str(archive))
    print('Entries: '+str(len(entries)))
    print('Extracted script bytes match both tested files.')
    print('SHA256: '+checksum)

if __name__=='__main__': main()
