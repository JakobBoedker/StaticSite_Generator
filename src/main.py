import os
from os.path import isfile
import shutil
import markdown


def copy_source_to_destination_dir(location, distdir, srcdir):
    srcpath = os.path.join(location, srcdir)
    if os.path.isfile(srcpath):
        print(srcpath)
        shutil.copy(srcpath, distdir)
    elif os.path.isdir(srcpath):
        splited = srcpath.split("/")[-1]
        if not splited == "static":
            distdir = location + distdir + "/" + splited
            os.mkdir(distdir)
        if os.path.exists(location + distdir):
            shutil.rmtree(location + distdir)
            os.mkdir(location + distdir)
        for fileOrDir in os.listdir(srcpath):
            copy_source_to_destination_dir(
                location, distdir, os.path.join(srcpath, fileOrDir)
            )


md = """
# test this is a test 

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """


def main():
    copy_source_to_destination_dir(
        "/home/jakob/workspace/github.com/jakobboedker/StaticSite_Generator/",
        "public",
        "static",
    )
    print(markdown.extract_title(md))


if __name__ == "__main__":
    main()
