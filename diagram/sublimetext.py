from .base import BaseViewer
import sys
from subprocess import check_call, Popen as run_command


class SublimeViewer(BaseViewer):
    def load(self):
        if sys.platform not in ('darwin',):
            raise Exception("Currently only supported on MacOS")
        if not check_call("which subl > /dev/null", shell=True) == 0:
            raise Exception("Can't find subl. Have you exported path?\nFor Example, exec \"ln -s \"/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl\"")

    def view(self, diagram_files):
        displaycmd = ['subl']
        displaycmd.extend(diagram_file.name for diagram_file in diagram_files)
        run_command(displaycmd).wait()
