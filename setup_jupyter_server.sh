#!/bin/bash

apt-get update

apt-get install python-pip -y 

apt-get install build-essential python3-dev python-dev -y

pip install jupyter

jupyter notebook --generate-config

cat > ~/.jupyter/jupyter_notebook_config.py <<EOF
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha1:e87a5e965b49:d25800fd63a764769a06cc116c92f26d3c$
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 8888
EOF






