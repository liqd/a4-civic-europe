#!/bin/sh

set -e -v

if [ -n ${TRAVIS_SSH_SECRET} ]; then
    SSH_ID_ARG="-i ${HOME}/id_rsa"
    cat <<EOF | openssl enc -d -aes-256-cbc -pbkdf2 -pass env:TRAVIS_SSH_SECRET -a -out ~/id_rsa
U2FsdGVkX1+/BL7aPLwnE7RyGgR1slqsocmNwPw+LXsUauHpU5bSbmJn//dQfEEL
uc51C6dKEA0/rv+8aPnehn8qx44iOOvnW9vfdur6tdtgkvioAsXonjTy1llzSlm4
6rQMXjTv08FtkGlvB3rTuNArTD/V5vy5mzywOc8F+UGvW2d9NDB7140ss9oLl9HQ
I5zqU24w02ZK565w3KBnThSRcWxhRnIxnN/mFlr+VOGNK7zRHlTHTVAJVCsXMUeP
1vVG/PMMFLHhRoElpnXkLXyQAA9izVR9QKSoShXRJodVMJO+tBpvuKx4KkX1ypBB
JjaMQ3DH6V8x96bcAx8T6QBeHDpxrKfbM4fO1mm/dCHa4Iu+0h9HL4mzMQBlFoZ4
11UXHZUY37qzbM6cFTxVemcEKdMJsAzDiExa3ZKtY8SDtN+s5xYVmxdW6CvZx+ri
L67FJhq6QDPLzyy5E/0xdD1PYerHy99i7BGVMXPYHJHOU2BuY6kivvfNddqinVBu
yqDl1uVWdbqm8WdEb4wjbtxcsZuYclrsxC23+Rar3W8xYXHTpPrMJ4yZlbS1m7+W
LK2tA2wn8/WMMvqFzcMMXw==
EOF
    chmod 600 ~/id_rsa
fi

ssh ${SSH_ID_ARG} -oStrictHostKeyChecking=no build@conway.liqd.net deploy civic_europe master
