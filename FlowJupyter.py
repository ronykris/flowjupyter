from ipykernel.kernelbase import Kernel
import os
import subprocess

class FlowJupyter(Kernel):
    implementation = 'FlowJupyter'
    implementation_version = '0.1'
    language = 'flow command line'
    language_version = '0.1'    
    banner = "Flow kernel - flow jupyter! "

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            process = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if process.returncode != 0:
                error_message = error.decode()
                self.send_response(self.iopub_socket, 'stream', {'name': 'stderr', 'text': error_message})
                return {'status': 'error', 'execution_count': self.execution_count, 'ename': '', 'evalue': '', 'traceback': []}
            
            output_message = output.decode()
            self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text': output_message})

        return {'status': 'ok', 'execution_count': self.execution_count}
            
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=FlowJupyter)