# Pyghthouse 

[![Build](https://github.com/ProjectLighthouseCAU/pyghthouse/actions/workflows/build.yml/badge.svg)](https://github.com/ProjectLighthouseCAU/pyghthouse/actions/workflows/build.yml)

A Python Lighthouse Adapter

(README WIP; please consult pyghthouse/ph.py or examples/README.md for usage information.)

Example scripts can be found [here](examples)

## Troubleshooting

If you are experiencing errors regarding SSL certificates,
instantiate Pyghthouse using the `ignore_ssl_cert=True`
keyword argument.

## Required packages
- websocket-client
- msgpack

##### Optional packages used in examples
- numpy
- Pillow

## Guide to install packages
To install packages in python, you can use `pip install <package name>` in a command line. For example `pip install numpy`.
If you have problems with installing, we recommend to use this guide: https://packaging.python.org/en/latest/tutorials/installing-packages/

In Thonny, you can use a Package Manager. You can find it in `Tools > Manage packages...`
