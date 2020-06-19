#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=SC1090,SC2128,SC2178

# setup a github repo and pypi project in the current folder

# it is assumed that the following are installed:
#   python3, git, hub, zsh

#? ------------------------------ Setup Initial Variables
    BASH_SOURCE=$(realpath $0)
    # SCRIPT_NAME="${BASH_SOURCE##*/}"
    SCRIPT_PATH="${BASH_SOURCE%/*}"
    REPO_NAME="${SCRIPT_PATH##*/}"
    VERSION='0.0.1'
    HOMEPAGE='https://skeptycal.github.io/$REPO_NAME'

#? ------------------------------ Get Repo Info
    vared -p "Name for python project repo: " -c REPO_NAME
    vared -p 'Enter Starting VERSION: ' -c VERSION


    echo "Setup for repo '$REPO_NAME' version ${VERSION}."

    HOMEPAGE='https://skeptycal.github.io/$REPO_NAME'
    DESCRIPTION='System utilities for Python on macOS.'

#? ------------------------------ Setup Repo
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip wheel setuptools

git init
hub create -d $DESCRIPTION -h $HOMEPAGE $REPO_NAME
cp $HOME/
git add .
