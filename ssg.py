import typer
from ssg import site

def main(source = "content", dest = "dist"):
    config = {"source": source, "dest": dest}
    obj_site = site(**config)
    obj_site.build()

typer.run(main)
