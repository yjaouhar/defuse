import psutil
import sys

def kill_by_name(name)->str:
    killed = []

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == name.lower():
            try:
                children = proc.children(recursive=True)

                # Kill child
                for child in children:
                    # child.kill()
                    killed.append((child.pid, child.name()))

                # Kill parent
                # proc.kill()
                print("==========++> " , proc)
                killed.append((proc.pid, proc.name()))

            except psutil.NoSuchProcess:
                pass
            except psutil.AccessDenied:
                print(f"Permission refusée: PID {proc.pid}")

    return "proc_name"

