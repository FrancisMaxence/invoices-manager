import os
import shutil
import time

# Custom modules for tests
import paths
import utils

class File_manager:
    def __init__(self, main, scan_ho, main_files=False):
        self.main = main
        self.scan_ho = scan_ho
        self.waiting = paths.waiting
        
        # A supprimer lorsque duplicate_file aura été corrigé
        # Prévoir des test unitaires pour s'assurer du bon fonctionnement de ce code
        self.main_files = os.listdir(self.main)
        self.files_length = len(self.main_files)
        

    """ 
    Getters
    """
    def get_main(self):
        return self.main
    
    def get_scan_ho(self):
        return self.scan_ho
    
    def get_main_files(self):
        return self.main_files
    
    def get_waiting(self):
        return self.waiting
    

    """
    Methods
    """
    def duplicate_file(self):
        # Revoir le code, il n'est pas possible de calculer 
        # la taille du dossier main tant qu'aucune facture n'a été scannée.
        main_length = len(self.main_files)
        
        for i in range(main_length):
            shutil.copy(f'{self.main}/{self.main_files[i-1]}', f'{self.scan_ho}')
            shutil.move(f'{self.main}/{self.main_files[i-1]}', f'{self.waiting}')
    
    
    def archive_files(self):
        waiting_list = os.listdir(self.waiting)
        scan_ho_list = os.listdir(self.scan_ho)
        waiting_length = len(waiting_list)

        if waiting_list != scan_ho_list:
            for i in range(waiting_length):
                shutil.move(f'{self.waiting}/{waiting_list[i-1]}', f'{paths.archives}')

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)

        for i in range(self.files_length):
            shutil.move(f'{self.waiting}/{self.main_files[i-1]}', f'{self.main}')
            os.remove(f'{self.scan_ho}/{self.main_files[i-1]}')




if __name__ == '__main__':
    a = File_manager(paths.src, paths.scan_ho, utils.test_files)
    a.testing_file_move()
