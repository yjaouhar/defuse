from handler import process_handler as p 
from handler import network_handler as n 
# from handler import registry_handler as r
from  handler import file_handler as f
from handler import utils


target=""
while True:
    target = input("[Process Name]: ")
    if target.strip():
        break
# regstry = r.remove_from_registry(target)
ips= n.get_remote_ips(target)
files_path = p.kill_by_name(target)
f.remove_files(files_path)
utils.report_email(target,"proc.exe" , "127.0.0.0")
# print(kill)