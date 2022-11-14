#!/bin/sh
addr="${SWARMHOSTADDR}"
scp -i $1/masterKeyForContainerSSH -q -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P $2 $1/id_rsa.pub user@$addr:~/
ssh -i $1/masterKeyForContainerSSH -o "StrictHostKeyChecking no" -p $2 user@$addr << EOF
rm -f ~/.ssh/authorized_keys
mv ~/id_rsa.pub ~/.ssh/authorized_keys
exit
EOF
