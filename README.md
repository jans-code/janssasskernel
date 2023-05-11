# janssasskernel

![Logo](janssasskernel/logo-svg.svg)

A simple jupyter kernel implementation to play around with [Sass](https://sass-lang.com).
Defaults to sass indented input. You can use ```%%scss``` and ```%%sass``` cell magic
to choose your style of syntax.

## Dev Installation

- install Sass from npm.
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user janssasskernel`

## Uninstall

- `jupyter kernelspec uninstall janssasskernel`
- `pip uninstall janssasskernel`
