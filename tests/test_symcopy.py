from unittest import TestCase
from tempfile import mkdtemp

from symcopy.symcopy import working_directory
import symcopy

import os, shutil, glob

class TestSymcopyTestCase(TestCase):
    def setUp(self):
        self.a = 'The widget'
        self.temp_dir = mkdtemp()
        self.working_directory = working_directory(self.temp_dir)
        self.working_directory.__enter__()

    def tearDown(self):
        self.working_directory.__exit__(None, None, None)
        shutil.rmtree(self.temp_dir)
        
class TestSymcopy(TestSymcopyTestCase):
    def test_symcopy(self):
        os.mkdir('new_folder')
        with open('a.bin', 'w'):pass
        with open('b.bin', 'w'):pass
        with open('c.bin', 'w'):pass
        
        assert 3 == len(list(glob.glob('*.bin')))
        assert 1 == len(list(glob.glob('new_folder')))
        assert 0 == len(list(glob.glob(os.path.join('new_folder','*'))))
        
        symcopy.symcopy('new_folder', self.temp_dir)
        
        assert 4 == len(list(glob.glob(os.path.join('new_folder','*'))))
        assert 3 == len(list(glob.glob(os.path.join('new_folder','*.bin'))))
        assert 1 == len(list(glob.glob(os.path.join('new_folder','new_folder'))))
        #A symlink to itself can be recursed forever
        assert 1 == len(list(glob.glob(os.path.join('new_folder','new_folder','new_folder'))))

class TestSymcopyFailure(TestSymcopyTestCase):
    def test_missing_directories_failure(self):
        FOLDER_NOT_FOUND = "ipuasbndg"
        #Sanity check:
        assert not os.path.exists(FOLDER_NOT_FOUND)
        
        try:
            symcopy.symcopy(FOLDER_NOT_FOUND, self.temp_dir)
            raise AssertionError("Expected ValueError")
        except ValueError: pass
        
        try:
            symcopy.symcopy(self.temp_dir, FOLDER_NOT_FOUND)
            raise AssertionError("Expected ValueError")
        except ValueError: pass