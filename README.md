# ibdimport
MYSQL Restore Data from .FRM and .IBD Files


- frmdump
```
curl -s get.dbsake.net > dbsake
chmod u+x dbsake
for tbl in `ls -1 /path/to/frmfile/*.frm`; do ./dbsake frmdump $tbl | mysql -h 'host' -u 'yourusername' --password='' 'database'; echo $tbl; done;
```
- ibdimport
```
mkdir oldibd
Config mysql-config.json
copy file old.ibd data to oldibd folder
python3 ibdimport.py then chill with pain
```
