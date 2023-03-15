#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janssasskernel
IPKernelApp.launch_instance(kernel_class=janssasskernel)