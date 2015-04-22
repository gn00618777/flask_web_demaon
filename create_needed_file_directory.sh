#!/bin/bash

test -d /flask_web_demaon/static/download || mkdir -p /flask_web_demaon/static/download/client_configs

test -f /flask_web_demaon/tunnel_list || echo "list:" > tunnel_list

test -d /flask_web_demaon/ovpn_files || mkdir /flask_web_demaon/ovpn_files
