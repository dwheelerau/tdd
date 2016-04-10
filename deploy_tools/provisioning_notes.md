Provisioning a new site
=======================
deploy_tools/provisioning_notes.md.
## Required packages:
* nginx
* python3
* Git
* pip3
* virtualenv

e.g.,, on Ubuntu:
sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv

## Nginx Virtual Host config
* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart Job
* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username
/home/username
└── sites
    └── SITENAME
          ├── database
          ├── source
          ├── static
          └── virtualenv
