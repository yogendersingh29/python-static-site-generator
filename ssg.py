import typer
from ssg import Site

def main(source = "content", dest = "dist"):
    config = {"source": source, "dest": dest}
    obj_site = Site(**config)
    obj_site.build()

typer.run(main)
