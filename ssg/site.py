from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        self.directory = self.dest / path.relative_to(self.source)
        self.directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        pathlist = self.source.glob('**/*.asm')
        for path in pathlist:
            if path.is_dir():
                self.create_dir(path)
