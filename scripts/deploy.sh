#!/bin/sh

set -e -v

if [ -n ${TRAVIS_SSH_SECRET} ]; then
    SSH_ID_ARG="-i ${HOME}/id_rsa"
    cat <<EOF | openssl enc -d -pass env:TRAVIS_SSH_SECRET -aes256 -a -out ~/id_rsa
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
KMnKASpAO5TKo43YmEhXUQ==
EOF
    chmod 600 ~/id_rsa
fi

ssh -p 22036 ${SSH_ID_ARG} -oStrictHostKeyChecking=no build@benhabib.liqd.net deploy advocate_europe master
