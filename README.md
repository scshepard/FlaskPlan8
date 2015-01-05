microblog
=========

A decently featured microblogging web application written in Python and Flask that I am developing in my Flask Mega-Tutorial series that begins [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Installation
------------

The tutorial referenced above explains how to setup a virtual environment with all the required modules.

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

Setup
# python db_create.py
# python db_migrate.py

Test/Debug
Currently the file (root directory) run.py has the attribute host set; be sure to delete the entire host='1999' etc string.
I am bypassing the openid feature (since I cannot get it to work). It presumes that the user to sign on is scs (see below for manually adding it)
# python tests.py

python
>>>
from app.models import User, Post
from app import db,models
import datetime

u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()

u = User.query.get(1)
p = Post(body='my first post',timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()

To delete all posts:
from app.models import Post
from app import db
for post in Post.query.all():
 db.session.delete(post)

db.session.commit()

