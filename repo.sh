#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=SC1090,SC2128,SC2178

# setup a github repo and pypi project in the current folder

# it is assumed that the following are installed:
#   python3, git, hub, zsh

#? ------------------------------ Setup Initial Variables
    MAIN="[38;5;229m"
    ATTN="[38;5;178m"
    RESET="[0m"

    # debug_var = echo name and value of variable for debugging
    dv() { echo " ${ATTN}${1}${MAIN} = ${(P)1}${RESET}"; }

    BASH_SOURCE=$(realpath $0)
    # SCRIPT_NAME="${BASH_SOURCE##*/}"
    REPO_PATH="${BASH_SOURCE%/*}"
    REPO_NAME="${REPO_PATH##*/}"
    TEMPLATE_PATH="$HOME/Documents/coding/template"
    VERSION='0.0.1'
    HOMEPAGE='https://skeptycal.github.io/$REPO_NAME'


    dv BASH_SOURCE
    dv REPO_NAME
    dv REPO_PATH


    exit
#? ------------------------------ Get Repo Info
    vared -p "Name for python project repo: " -c REPO_NAME
    vared -p 'Enter Starting VERSION: ' -c VERSION


    echo "Setup for repo '$REPO_NAME' version ${VERSION}."

    HOMEPAGE='https://skeptycal.github.io/$REPO_NAME'
    DESCRIPTION='System utilities for Python on macOS.'

#? ------------------------------ Setup Repo
rm -rf $
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip wheel setuptools

git init
hub create -d $DESCRIPTION -h $HOMEPAGE $REPO_NAME
cp $HOME/
git add .
