# ibdimport
MYSQL Restore Data from .FRM and .IBD Files


- frmdump
```
curl -s get.dbsake.net > dbsake
chmod u+x dbsake
for tbl in `ls -1 /path/to/frmfile/*.frm`; do ./dbsake frmdump $tbl | sed "s/timestamp DEFAULT NULL/timestamp NULL DEFAULT NULL/g" | sed "s/TIMESTAMP DEFAULT NULL/TIMESTAMP NULL DEFAULT NULL/g" | mysql -h 'host' -u 'yourusername' --password='' 'database'; echo $tbl; done;
```
- ibdimport
```
mkdir data_new
Config mysql_config.json
copy file from old ibd data to data_new
python3 ibdimport.py then chill with pain
```
