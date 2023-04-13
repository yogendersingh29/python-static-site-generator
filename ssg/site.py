from pathlib import Path

class site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        self.directory = Path(self.dest).relative_to(self.source)
        Path(self.directory).mkdir(parents=True, exist_ok=True)

    def build(self):
        Path(self.dest).mkdir(parents=True, exist_ok=True)
        pathlist = Path(self.source).glob('**/*.asm')
        for path in pathlist:
            if Path.is_dir(path):
                site.create_dir(self, path)
