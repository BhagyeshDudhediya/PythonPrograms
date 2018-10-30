import threading
from customsshclient import CustomSSHClient
import xml.etree.ElementTree as et
import logging

logging.basicConfig(format="%(threadName)s : %(message)s")
target_file = 'sshresponse.log'

class ThreadedSSHHandler(CustomSSHClient):
    """thread function"""
    def __init__(self, host, port, username, pwd, job, lock):
        self.job = job
        self.lock_obj = lock
        self.t_name = threading.current_thread().name
        super().__init__(host, port, username, pwd)
        self.__task_runner()

    def __task_runner(self):
        op = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        logging.warning('Check for the lock')
        # syncronise it by taking and releasing the lock after it's done
        with self.lock_obj:
            logging.warning('Acquired the lock')
            with open(target_file, 'a') as fw:
                """critical section"""
                fw.write(caption.center(80, '-')+'\n')
                fw.write(op)
                fw.write('\n')
            logging.warning('Releasing the lock')

class ThreadedSSHClient:
    """mian thread"""
    def __init__(self, host_file):
        self.host_file = host_file
        self.lock_obj = threading.Lock()        # sync using lock
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
            host_config.append(self.lock_obj)
            t = threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xml')