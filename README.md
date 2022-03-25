#  Platform for the idea challenge Civic Europe

Civic Europe is a platform for an idea challenge. It is
based on [adhocracy 4](https://github.com/liqd/adhocracy4).

![Build Status](https://github.com/liqd/a4-civic-europe/actions/workflows/django.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/liqd/a4-civic-europe/badge.svg?branch=main)](https://coveralls.io/github/liqd/a4-civic-europe?branch=main)

## Requirements

*   nodejs (+ npm)
*   python 3.x (+ venv + pip)
*   libmagic
*   libjpeg
*   libpq (only if postgres should be used)

## Installation

    git clone https://github.com/liqd/a4-civic-europe.git
    cd a4-civic-europe
    make install
    make fixtures
    make watch

