#!/usr/bin/env python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager
json ="""{"argv":["python","-m","janssasskernel", "-f", "{connection_file}"],
 "display_name":"Sass"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Generator: Adobe Illustrator 17.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->

<svg
   version="1.1"
   id="Layer_1"
   x="0px"
   y="0px"
   viewBox="0 0 300.00001 300"
   enable-background="new 0 0 547.8 410.6"
   xml:space="preserve"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"><defs
   id="defs35" />
<path
   fill="#cd6799"
   d="m 258.34691,166.8456 c -10.46808,0.0548 -19.56599,2.57592 -27.18412,6.30277 -2.79514,-5.53548 -5.59028,-10.46808 -6.08354,-14.08532 -0.54807,-4.22012 -1.20575,-6.79603 -0.54807,-11.83825 0.65768,-5.04221 3.61724,-12.22189 3.56244,-12.76995 -0.0548,-0.54807 -0.65768,-3.12398 -6.68642,-3.17879 -6.02874,-0.0548 -11.23537,1.15094 -11.83825,2.74033 -0.60287,1.5894 -1.75381,5.20664 -2.52111,8.93349 -1.04132,5.48067 -12.05747,25.04666 -18.36024,35.29551 -2.02785,-4.00089 -3.78166,-7.50851 -4.16531,-10.30366 -0.54806,-4.22011 -1.20574,-6.79603 -0.54806,-11.83824 0.65768,-5.04222 3.61724,-12.22189 3.56243,-12.76996 -0.0548,-0.54807 -0.65768,-3.12398 -6.68642,-3.17879 -6.02873,-0.0548 -11.23537,1.15094 -11.83824,2.74033 -0.60288,1.5894 -1.26056,5.31625 -2.52111,8.9335 -1.26055,3.61724 -15.89394,36.28203 -19.73041,44.72226 -1.97304,4.32973 -3.67205,7.78255 -4.8778,10.13924 0,0 0,0 0,0 0,0 -0.0548,0.16442 -0.21922,0.43845 -1.04133,2.02785 -1.6442,3.12398 -1.6442,3.12398 0,0 0,0 0,0.0548 -0.8221,1.47978 -1.69901,2.84995 -2.13746,2.84995 -0.32884,0 -0.93172,-3.94608 0.10961,-9.31714 2.19227,-11.34499 7.3989,-28.99274 7.3441,-29.59562 0,-0.32884 0.98652,-3.39801 -3.39802,-4.98741 -4.27492,-1.58939 -5.80951,1.04133 -6.19316,1.04133 -0.38364,0 -0.65768,0.93172 -0.65768,0.93172 0,0 4.76819,-19.84003 -9.09791,-19.84003 -8.65946,0 -20.60731,9.48156 -26.526438,18.03141 -3.726855,2.02784 -11.673826,6.35757 -20.168863,11.01614 -3.233595,1.80862 -6.576804,3.61724 -9.700785,5.31625 -0.219227,-0.21922 -0.438454,-0.49325 -0.657681,-0.71248 -16.770849,-17.92179 -47.791438,-30.58213 -46.476077,-54.64227 0.49326,-8.76907 3.507628,-31.787882 59.574877,-59.739297 46.147237,-22.744778 82.867727,-16.442008 89.225297,-2.466301 9.09791,19.949637 -19.6756,56.998968 -67.35743,62.370018 -18.195818,2.02785 -27.732183,-4.98741 -30.143678,-7.61813 -2.521108,-2.74033 -2.904755,-2.90475 -3.836468,-2.35669 -1.534588,0.8221 -0.548067,3.2884 0,4.71338 1.424974,3.72685 7.28929,10.30366 17.209302,13.53725 8.769071,2.84995 30.088874,4.43934 55.902834,-5.53547 C 171.91675,122.12334 194.49711,91.047944 187.8655,65.014764 181.23389,38.597937 137.38854,29.883672 95.899867,44.626673 71.236854,53.395744 44.491187,67.207032 25.254037,85.183628 2.3996452,106.55824 -1.2175967,125.13771 0.26218412,132.92026 5.5784335,160.54283 43.669087,178.51943 58.905348,191.83745 c -0.767294,0.43846 -1.479781,0.8221 -2.082654,1.15094 -7.618131,3.78167 -36.66568,18.96312 -43.900163,35.02148 -8.2210046,18.19582 1.31536,31.23982 7.61813,32.99363 19.565991,5.42587 39.680048,-4.32973 50.476967,-20.44289 10.796919,-16.11317 9.481558,-37.04933 4.494149,-46.6405 -0.05481,-0.10962 -0.109614,-0.21923 -0.219227,-0.32884 1.973041,-1.15094 4.000889,-2.35669 5.97393,-3.50763 3.891275,-2.30188 7.727744,-4.43934 11.016145,-6.19316 -1.863427,5.09703 -3.233595,11.18057 -3.891275,19.94964 -0.8221,10.30366 3.398015,23.67649 8.933491,28.93793 2.466302,2.30189 5.371059,2.35669 7.234489,2.35669 6.46719,0 9.37194,-5.37105 12.60553,-11.72863 3.94609,-7.78255 7.50852,-16.82566 7.50852,-16.82566 0,0 -4.43934,24.44379 7.61813,24.44379 4.38454,0 8.82388,-5.6999 10.79692,-8.60465 0,0.0548 0,0.0548 0,0.0548 0,0 0.10962,-0.16442 0.32884,-0.54807 0.43846,-0.71249 0.71249,-1.15094 0.71249,-1.15094 0,0 0,-0.0548 0,-0.10961 1.75381,-3.06918 5.6999,-10.02963 11.56421,-21.59384 7.56333,-14.90742 14.85262,-33.5417 14.85262,-33.5417 0,0 0.65768,4.54896 2.90475,12.11228 1.31536,4.43934 4.0557,9.31714 6.24796,14.03051 -1.75381,2.4663 -2.84994,3.83647 -2.84994,3.83647 0,0 0,0 0.0548,0.0548 -1.42497,1.86343 -2.95956,3.89127 -4.65857,5.86432 -5.97393,7.12487 -13.0988,15.29106 -14.08532,17.64775 -1.15094,2.79514 -0.8769,4.82299 1.31536,6.46719 1.5894,1.20575 4.43935,1.37017 7.3441,1.20575 5.37106,-0.38365 9.15272,-1.69901 11.01615,-2.52111 2.90475,-1.04133 6.30277,-2.63072 9.48155,-4.98741 5.86432,-4.32973 9.42676,-10.52288 9.09792,-18.68908 -0.16442,-4.49415 -1.6442,-8.9883 -3.45283,-13.20842 0.54807,-0.76729 1.04133,-1.53458 1.5894,-2.30188 9.26233,-13.53725 16.44201,-28.38986 16.44201,-28.38986 0,0 0.65768,4.54895 2.90475,12.11227 1.09614,3.83647 3.34321,8.00178 5.31625,12.05748 -8.71426,7.07006 -14.08532,15.29107 -16.00355,20.66212 -3.45283,9.97482 -0.7673,14.46897 4.32973,15.5103 2.30188,0.49326 5.59028,-0.60288 8.00177,-1.6442 3.06918,-0.98652 6.68642,-2.68553 10.13924,-5.20664 5.86432,-4.32973 11.50941,-10.35847 11.18057,-18.52466 -0.16442,-3.72686 -1.15094,-7.39891 -2.52111,-10.96134 7.3989,-3.06918 16.93527,-4.76818 29.10235,-3.34321 26.08799,3.06917 31.23982,19.34676 30.2533,26.1976 -0.98652,6.85084 -6.46719,10.57769 -8.27581,11.72863 -1.80862,1.15094 -2.4115,1.53459 -2.24708,2.35669 0.21923,1.20575 1.09614,1.15094 2.63073,0.93171 2.13746,-0.38364 13.70167,-5.53547 14.19493,-18.14101 0.8221,-16.11317 -14.52377,-33.70612 -41.65309,-33.5417 z M 57.096727,234.69629 c -8.659458,9.42675 -20.716931,12.98919 -25.923567,9.97482 -5.590283,-3.2336 -3.398015,-17.1545 7.234484,-27.12932 6.46719,-6.08354 14.797808,-11.72863 20.333284,-15.18145 1.260554,-0.76729 3.123981,-1.86343 5.371056,-3.2336 0.383647,-0.21922 0.602874,-0.32884 0.602874,-0.32884 v 0 c 0.438453,-0.27403 0.876907,-0.54806 1.31536,-0.8221 3.891276,14.24974 0.16442,26.80048 -8.933491,36.72049 z m 63.027703,-42.85884 c -3.01437,7.3441 -9.31714,26.1428 -13.15361,25.10147 -3.2884,-0.87691 -5.31625,-15.12665 -0.65768,-29.21197 2.35669,-7.07006 7.3441,-15.51029 10.24885,-18.7987 4.71338,-5.26144 9.92001,-7.01525 11.18057,-4.87779 1.58939,2.79514 -5.75471,23.18323 -7.61813,27.78699 z m 52.01155,24.88224 c -1.26055,0.65768 -2.4663,1.09614 -3.01437,0.7673 -0.38364,-0.21923 0.54807,-1.09614 0.54807,-1.09614 0,0 6.522,-7.01525 9.09791,-10.19404 1.47978,-1.86343 3.2336,-4.0557 5.09702,-6.522 0,0.21923 0,0.49326 0,0.71249 0,8.38542 -8.11139,14.03051 -11.72863,16.33239 z m 40.1185,-9.15272 c -0.93171,-0.65768 -0.76729,-2.84994 2.35669,-9.70078 1.20575,-2.68553 4.05569,-7.17968 8.93349,-11.50941 0.54807,1.75382 0.93171,3.45283 0.87691,5.04222 -0.0548,10.57769 -7.61813,14.52377 -12.16709,16.16797 z"
   id="path18"
   style="stroke-width:0.548067" />
<g
   id="g20">
</g>
<g
   id="g22">
</g>
<g
   id="g24">
</g>
<g
   id="g26">
</g>
<g
   id="g28">
</g>
<g
   id="g30">
</g>
</svg>"""

def install_kernelspec():
    kerneldir = "/tmp/janssasskernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janssasskernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janssasskernel')