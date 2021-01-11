import os

class Search():
    """
    Searches all files at and below a given directory for a
    word.
    """

    def __init__(self, word, exts, start_dir, verbose=False):
        self.word = word.lower()
        self.exts = exts    # the files extensions that might contain the word.
        self.found = set()     # set of files where word is found.
        self.vfiles = 0     # numbers of visited files.
        self.start = start_dir
        self.verbose = verbose

    def folder_explorer(self):
        """
        Traverses through folders and calls file_traverser on
        files in the folder.
        """
        for (thisDir, subDir, filesHere) in os.walk(self.start):
            for file in filesHere:
                fpath = os.path.join(thisDir, file)
                self.file_traverser(fpath)

    def file_traverser(self, fpath):
        """
        Traverses a file with the aim of finding the user input.
        Skips files with extensions that are not in exts.

        fpath - file path.
        """
        self.vfiles += 1
        if self.verbose:
            print(self.vfiles, '-->', fpath)
        try:
            if os.path.splitext(fpath)[1] in self.exts:
                with open(fpath) as f:
                    doc = f.read().lower()
                if self.word in doc:
                    self.found.add(fpath)
            else:
                print(f'\nSkipping {fpath}\n')
        except:
            print(f'Error while traversing {fpath}.\nError_info: {sys.exc_info()}\n')

    def run(self):
        self.folder_explorer()
        print(f'Found in {len(self.found)} file(s).\nVisited {self.vfiles} file(s).\n')
        if self.found: print('File(s):\n', self.found)
        
if __name__ == "__main__":
    start_dir = input('Enter path to the starting directory: ')
    word = input('What word do you wish to find? ')
    extensions = input('Enter the file extensions of files you think might contain the word you wish to find: ').split()
    searcher = Search(word, extensions, start_dir, True)
    searcher.run()
