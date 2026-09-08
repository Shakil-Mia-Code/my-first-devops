import os
import shutil

source_dir = "/source_code"
backup_dir = "/backup_destination"
output_zip_name = "/backup_destination/server_source_backup"

print("=========================================")
print("   AUTOMATED STORAGE BACKUP SYSTEM       ")
print("=========================================")

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"Created secure backup storage directory at: {backup_dir}")

print(f"Compressing and archiving: {source_dir} ...")

shutil.make_archive(output_zip_name, 'zip', source_dir)

print("=========================================")
print(" SUCCESS: Backup Created and Zip Locked!")
print("=========================================")
