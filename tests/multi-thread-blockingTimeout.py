from proxyMama import Manager
import threading
import time


def use_proxy(manager):
    # will block until a new proxy is ready or it takes longer than 2 seconds to get a proxy
    proxy = manager.random(blocking=True, timeout=2)
    if proxy is not None:
        print(f"using proxy: {proxy.address()}\n")
        time.sleep(2)

        proxy.release()
        print(f"released proxy\n")
    else:
        print("Proxy request timed out\n")


manager = Manager(single_use=True)
manager.load_file("proxies.txt")
# giving an example of what happens if all proxies are in use and blocking = True.
for i in range(8):
    threading.Thread(target=use_proxy, args=(manager,)).start()

# showing that proxies are now in use
print(manager.proxies)

