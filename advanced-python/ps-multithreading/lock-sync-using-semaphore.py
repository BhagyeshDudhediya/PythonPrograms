import threading
from customsshclient import CustomSSHClient
import xml.etree.ElementTree as et
import logging

logging.basicConfig(format="%(threadName)s : %(message)s")
target_file = 'sshresponse.log'

class ThreadedSSHHandler(CustomSSHClient):
    """thread function"""

    def enroll(self, t_name):
        """add thread name into the pool"""
        self.pool.append(t_name)

    def remove(self, t_name):
        """Remove thread from the pool"""
        self.pool.remove(t_name)

    def __init__(self, host, port, username, pwd, job, sema, pool, lock):
        self.job = job
        self.semaphore = sema
        self.pool = pool
        self.lock = lock
        self.t_name = threading.current_thread().name
        super().__init__(host, port, username, pwd)
        self.__task_runner()

    def __task_runner(self):
        op = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        logging.warning(self.pool)
        # syncronise it by taking and releasing the lock after it's done
        with self.semaphore:
            self.enroll(self.t_name)
            logging.warning('enrolled:' + str(self.pool))
            with self.lock:
                """For multiple threads in semaphore"""
                with open(target_file, 'a') as fw:
                    """critical section"""
                    fw.write(caption.center(80, '-')+'\n')
                    fw.write(op)
                    fw.write('\n')

                logging.warning('Done with critical section')
            self.remove(self.t_name)
            logging.warning('removed:' + str(self.pool))

class ThreadedSSHClient:
    """mian thread"""
    def __init__(self, host_file):
        self.host_file = host_file
        self.sema = threading.Semaphore(2)        # sync using semaphore as only one thread in critical section
        self.sema_pool = list()
        self.lock = threading.Lock()
        self.__parse_host_file()

    def __parse_host_file(self):
        tree = et.parse(self.host_file)
        threads = list()

        for host_tag in tree.getiterator('host'):
            host_config = list()
            host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])
            for child_tag in host_tag:
                host_config.append(child_tag.text)
            # Class passed as target reference for thread
            host_config.extend([self.sema, self.sema_pool, self.lock])
            t = threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xml')