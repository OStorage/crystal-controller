from abstract_metric import Metric

class Slowdown(Metric):
    _sync = {}
    _async = ['get_value', 'attach', 'detach', 'notify', 'start_consuming','stop_consuming', 'init_consum', 'stop_actor']
    _ref = ['attach', 'detach']
    _parallel = []

    def __init__(self, queue, host):
        Metric.__init__(self)

        self.host = host
        self.queue = queue
        self.name = "slowdown"
        # Consumer("localhost", 25672, queue, self)
        # thread1 = Consumer("localhost", 25672, queue, self)
        # Start new Threads
        # thread1.start()
        print 'Slowdown initialized'
    def notify(self, body):
        """
        PUT VAL swift_mdw/groupingtail-swift_metrics*4f0279da74ef4584a29dc72c835fe2c9*get_ops/counter interval=5.000 1448964179.433:198
        """
        print body


    def get_value(self):
        return self.value

    # def callback(self, ch, method, properties, body):
    #     print 'body', body
    #     self.notify(body)
