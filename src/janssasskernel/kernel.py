#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import os, shutil

class janssasskernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'sass'
    language_version = '1.58.1'
    language_info = {
        'name': 'Sass',
        'mimetype': 'text/css',
        'file_extension': '.scss',
    }
    banner = "Syntactically Awesome Stylesheets"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            workingdir = "/tmp/sasskernel/"
            os.mkdir(workingdir)
            with open(workingdir + "sassfile.scss", "w") as f:
                    f.write(code)
            os.system('sass --no-source-map ' + workingdir + 'sassfile.scss '  + workingdir + 'cssfile.css')
            with open(workingdir + "cssfile.css") as f:
                    solution = f.read()
            shutil.rmtree(workingdir)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }