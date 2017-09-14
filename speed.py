import speedtest

class Speed:
    def __init__(self):
        self.stest = speedtest.Speedtest()

    @property
    def results(self):
        servers = [2065, 2206, 1781]
        self.stest.get_servers(servers)
        self.stest.get_best_server()
        self.stest.download()
        self.stest.upload()
        return self.stest.results.dict()
