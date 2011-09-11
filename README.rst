================
Apache2 Reloader
================

Reloads the apache2 server as if you wrote in a terminal ``/etc/init.d/apache2 reload``.

In your Python code simply write this::

	from apache2 import a2reload
	
	# now do the reloading
	a2relaod()


Requirements
============

This package works only in **Unix** Systems with **Apache2** server and **gcc** installed.


Installation
============

You have to have root privileges to install the reloader::

	sudo pip install apache2
	
