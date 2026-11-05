"""Read MSI tables without executing installer actions; reconstruct local file layout."""
from pathlib import Path
import ctypes as C, shutil, json
api=C.WinDLL('msi.dll');U=C.c_uint;P=C.POINTER(U)
api.MsiOpenDatabaseW.argtypes=[C.c_wchar_p,C.c_void_p,P]
api.MsiDatabaseOpenViewW.argtypes=[U,C.c_wchar_p,P]
api.MsiViewExecute.argtypes=[U,U];api.MsiViewFetch.argtypes=[U,P]
api.MsiRecordGetStringW.argtypes=[U,U,C.c_wchar_p,P]
api.MsiCloseHandle.argtypes=[U]
db=U();rc=api.MsiOpenDatabaseW(str(Path('work/LibreOffice_26.8.2_Win_x86-64.msi').resolve()),None,C.byref(db))
assert rc==0,('MsiOpenDatabase',rc)
def query(sql,n):
    view=U();assert api.MsiDatabaseOpenViewW(db,sql,C.byref(view))==0
    assert api.MsiViewExecute(view,0)==0
    result=[]
    while True:
        rec=U();rc=api.MsiViewFetch(view,C.byref(rec))
        if rc==259:break
        assert rc==0,rc
        vals=[]
        for i in range(1,n+1):
            buf=C.create_unicode_buffer(8192);size=U(len(buf))
            assert api.MsiRecordGetStringW(rec,i,buf,C.byref(size))==0
            vals.append(buf.value)
        result.append(vals);api.MsiCloseHandle(rec)
    api.MsiCloseHandle(view);return result
dirs={row[0]:row[1:] for row in query('SELECT `Directory`,`Directory_Parent`,`DefaultDir` FROM `Directory`',3)}
components=dict(query('SELECT `Component`,`Directory_` FROM `Component`',2))
files=query('SELECT `File`,`Component_`,`FileName` FROM `File`',3)
api.MsiCloseHandle(db)
base=Path('work/libreoffice').resolve();flat=Path('work/lo-flat').resolve();workspace=Path('work').resolve()
assert base.is_relative_to(workspace) and flat.is_relative_to(workspace)
def directory(key):
    if not key or key=='TARGETDIR':return Path()
    parent,name=dirs[key];name=name.split(':')[0].split('|')[-1]
    if name in ['.','SourceDir']:name=''
    return directory(parent)/name
copied=0;missing=[]
for key,comp,name in files:
    source=flat/key
    if not source.exists():missing.append(key);continue
    dest=base/directory(components[comp])/name.split('|')[-1]
    assert dest.resolve().is_relative_to(base)
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest);copied+=1
print(json.dumps({'copied':copied,'missing':len(missing),'missing_sample':missing[:8],'soffice_paths':[str(p) for p in base.rglob('soffice.exe')]},indent=2))
