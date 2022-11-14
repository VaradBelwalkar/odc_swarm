#!/bin/sh
ssh -i $1/.ssh/keyForRemoteServer -o "StrictHostKeyChecking no" -p "$2" user@127.0.0.1