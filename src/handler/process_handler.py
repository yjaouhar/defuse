import psutil
from pathlib import Path
from handler import file_handler 

def kill_by_name(name):
    removed = []

    for proc in psutil.process_iter(['pid', 'name']):

        try:
            proc_name = proc.info['name']

            if proc_name and proc_name.lower() == name.lower():

                # CHILDREN FIRST
                children = proc.children(recursive=True)

                for child in children:

                    try:
                        child_name = child.name()
                        child_path = child.exe()

                        # kill child
                        if child.is_running():
                            child.kill()
                            child.wait(timeout=3)

                            # remove exe
                            file_handler.remove_exe(child_path)

                            removed.append(child_name)
                    except Exception as e:
                        print(f"Child error: {e}")

                # PARENT
                parent_path = proc.exe()
                current_dir = proc.cwd()
                if proc.is_running():
                    proc.kill()
                    proc.wait(timeout=3)

                    file_handler.remove_exe(parent_path)

                    removed.append(proc_name)

                file_handler.remove_exe(current_dir)
        except psutil.NoSuchProcess:
            pass

        except psutil.AccessDenied:
            print(f"Access denied PID {proc.pid}")

        except Exception as e:
            print(f"Error: {e}")

    return removed