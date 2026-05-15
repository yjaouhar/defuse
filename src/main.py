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
ip= n.get_remote_ips(target)
# regstry = r.remove_from_registry(target)
kill = p.kill_by_name(target)
print(f"""
killed : {kill} 
Attacker ip : {ip}
""")


