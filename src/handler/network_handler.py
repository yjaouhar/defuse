import psutil

def get_remote_ips(p_name)->list:
    ips = set()

    for conn in psutil.net_connections():
        if conn.raddr:
            p = psutil.Process(conn.pid)
            if p.name() == p_name:
                print("______  " , conn)
                ip = conn.raddr.ip
                ips.add(ip)

    return list(ips)

