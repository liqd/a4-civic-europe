#!/bin/sh

set -e -v

if [ -n ${TRAVIS_SSH_SECRET} ]; then
    SSH_ID_ARG="-i ${HOME}/id_rsa"
    cat <<EOF | openssl enc -d -aes-256-cbc -pbkdf2 -pass env:TRAVIS_SSH_SECRET -a -out ~/id_rsa
U2FsdGVkX1+DKl+w4oPFMBjan1a5isrUQwSTwvrUKsReRhSBu9x1PDBDjE0bbuot
zyBGFRF1Gi96YNzPp9Df85E1zD1Y0sdFN4fft0j1R1FY5YXVudDxoDjUUZfFZ9QV
oYAyDtztixs8YWfEZ2/d3txIHU+YJva8g6n2OvsfkWb7xbtXIuIFZxfjbcz6Vo/H
liBk/JVX3McDHz0nm4g1ozRcQzcD+OumaaKl+THFRJuu74dxuYO1QOwLwidQXjDF
00/aYPPdmP8ypVS9OmY9M3k9spZkPXwLl74srRP6+pePMJfvGtohT2ZeJDlMR51N
00cph6lUeVo80Bz3zbhN4DclHlHFpGFOsXYLvAYA0LirC8vVdngejGjUTs8WJ7aN
QcfsG/FlP5QDiEKNCPSo16QV4L033KUetcasyGke15LOLjbk8tB53Z9ecmYSo1LQ
PfXWnGVOxuHUPT7koJzjCTQhL8M77pt9rR330Xz9BsInkRfJrESOzd9jb3i+j1Vv
f1ZMXjz4ottNNUzwLdK5xPsM+GeKeNnpDANrp5kHx0wH8bZWciLmcvUJIMJIAK3Y
6ds5hCTBvHOGVIEecKORxw==
EOF
    chmod 600 ~/id_rsa
fi

ssh ${SSH_ID_ARG} -oStrictHostKeyChecking=no build@build.liqd.net deploy civic_europe master
