
addr = "127.0.0.1"

def gen_hosts():
    with open("hosts", "w") as f:
        for i in range(1500):
            host = "www.%d.com" % (i)
            f.write("%s\t%s\n" % (addr, host))


if __name__ == "__main__":
    gen_hosts()

