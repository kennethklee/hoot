hoot
====

People discovery in events

install requirements
===
* Python 2.7
* PIP
* virtualenv
* virtualenvwrapper (optional, used in install instructions)

install
===
* clone the repo `git clone git@github.com:kennethklee/hoot.git`
* go into the project `cd hoot`
* create virtual env `mkvirtualenv hoot`
* run `pip install -r requirements.txt`
* make a copy of the dev settings `mv settings/example_development.py settings/development.py`

When you're done working on it, `deactivate`

When you're working on it again, `workon hoot`

run the server
===
`./manage.py runserver`

deploy
===
Requirements:
* fabric

# To deploy to staging: `fab staging deploy`
# To deploy to production: `fab production deploy`


