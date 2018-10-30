from abc import ABC, abstractmethod
from zipfile import ZipFile
from glob import glob
from tarfile import TarFile

class ArchiveManager:
    """abstract class"""
    def save(self):
        """abstract method"""
        pass

class ZipArchive(ArchiveManager):
    """concrete class"""
    def __init__(self, name):
        self.archive_name = name

    def save(self, *args):
        with ZipFile(self.archive_name, mode='w') as zf:
            for file in args:
                zf.write(file)
                print ('added:', file)

class TARArchive(ArchiveManager):
    def __init__(self, name):
        self.archive_name = name

    def save(self, *args):
        pass

def make_archive(archive_name, archive_type='zip'):
    """factory method"""
    archive = None
    if (archive_type == 'zip'):
        archive = ZipArchive(archive_name)
    elif (archive_type == 'tar'):
        archive = TARArchive(archive_name)

    return archive

if __name__ == '__main__':
    # glob returns list of file with py extension. * converts list into elements
    make_archive('src.zip').save(*glob('*.py'))