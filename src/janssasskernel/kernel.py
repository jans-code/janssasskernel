#!/usr/bin/env python
import os
import shutil
from ipykernel.kernelbase import Kernel

workingdir = "/tmp/sasskernel/"

class janssasskernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'sass'
    language_version = '1.58.1'
    language_info = {
        'name': 'SCSS',
        'mimetype': 'text/plain',
        'file_extension': '.scss',
    }
    banner = "Syntactically Awesome Stylesheets"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            code = code.strip()
            if code[:6].lower() == '%%scss':
                code = code[6:]
                with open(workingdir + "sassfile.scss", "w") as f:
                    f.write(code)
                os.system('sass --no-source-map ' + workingdir + 'sassfile.scss '  + workingdir + 'cssfile.css')
                with open(workingdir + "cssfile.css", 'r', encoding='utf-8') as f:
                    solution = f.read()
            else:
                if code[:6].lower() == '%%sass':
                    code = code[6:]
                with open(workingdir + "scssfile.sass", "w") as f:
                    f.write(code)
                os.system('sass --no-source-map ' + workingdir + 'scssfile.sass '  + workingdir + 'cssfile.css')
                with open(workingdir + "cssfile.css", 'r', encoding='utf-8') as f:
                    solution = f.read()
                
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        if os.path.exists(workingdir):
            shutil.rmtree(workingdir)