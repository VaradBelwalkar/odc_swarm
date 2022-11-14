#!/bin/sh

docker service update --publish-add target=22 $2

ssh-keygen -f "$1/id_rsa" -t rsa -q -N ""