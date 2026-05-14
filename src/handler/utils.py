

def report_email(malware_name,proc_name,ip):
    print(f"""
To: security@organization.com
Subject: Malware Analysis Report: Mitigation of {malware_name}

Dear Security Team,

I am writing to report the successful analysis and mitigation of {malware_name} identified during an educational malware analysis exercise. Below are the details:

Summary:
The malware exhibited persistence mechanisms by adding to the Windows startup registry and communicating with a remote server. It was also running a process under the name {proc_name}.

Proof of Mitigation:
The malware process was successfully terminated, and its persistence mechanisms were removed. Additionally, its file was deleted from the system.

Attacker Information:
The malware communicated with the following IP address: {ip}

Please feel free to reach out for further clarification or additional details.

Best regards,
Yassine Jaouhary
""")
    
