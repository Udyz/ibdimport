import glob
import os, sys, time
import json
import mysql.connector

class mysql_client:
	with open('mysql-config.json', 'r') as file:
		data = json.load(file)
		host = data['host']
		user = data['user']
		port = data['port']
		password = data['password']
		database = data['database']
		dataoldibd_path = data['dataoldibd_path']
		datanewibd_path = data['datanewibd_path']

def cursor(query):
	conn = mysql.connector.connect(
		host=mysql_client.host,
		user=mysql_client.user,
		password=str(mysql_client.password),	
		port=mysql_client.port,
		database=mysql_client.database
		)
	
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except mysql.connector.errors.DatabaseError as f:
		print(f)
	conn.commit()
	cursor.close()
	conn.close()
def main():
	file = glob.glob(f"{mysql_client.dataoldibd_path}\\*.ibd")
	for fibd in file:
		get_table = fibd.split(mysql_client.dataoldibd_path)[1].split('\\')[1].split('.ibd')[0]
		print(f'+ TABLE {get_table} DISCARD')
		cursor(f'ALTER TABLE `{get_table}` DISCARD TABLESPACE')
		print(f'+ TABLE {get_table} IMPORT')
		cmd = f'copy "{mysql_client.dataoldibd_path}\\{get_table}.ibd" "{mysql_client.datanewibd_path}"'
		os.system(cmd if os.name == "nt" else cmd.replace('copy', 'cp'))
		cursor(f'ALTER TABLE `{get_table}` IMPORT TABLESPACE;')
		os.system(f'move "{mysql_client.dataoldibd_path}\\{get_table}.ibd" "{mysql_client.dataoldibd_path}\\{get_table}.ibd_bak"' if os.name=="nt" else f'mv "{mysql_client.dataoldibd_path}\\{get_table}.ibd" "{mysql_client.dataoldibd_path}\\{get_table}.ibd_bak"')
if __name__ == '__main__':
	main()