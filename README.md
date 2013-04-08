# ink: a set of tools for working within wordpress teams

## wat

This is set of tools written on top of [fabric](http://docs.fabfile.org/en/1.6/), a python-based tool for deployment + systems administration. The hope is that the annoying parts of setting up a new wordpress project will be marginalized by awesome productivity. If you'd like to contribute, fork it & change it & submit a pull request!

## Requirements

* Dropbox
* A MySQL database that contains your wp install
* OSX Mountain Lion w/up-to-date [OSX Xcode Command Line Tools](http://slashusr.wordpress.com/2012/07/27/os-x-mountain-lion-need-to-reinstall-xcode-command-line-tools/)
* [fabric](http://docs.fabfile.org/en/1.6/). (install with `sudo easy_install fabric==1.6`)

## installation

* Make a copy of the sample inkrc in your home directory with `cp sample.inkrc ~/.inkrc`
* Update the `.inkrc` with your information (sublime it with `subl ~/.inkrc`)
* Open your bash_profile `subl ~/.bash_profile`
* Add this line: `export PATH=${PATH}:/Applications/MAMP/Library/bin` to the bottom of your .bash_profile
* from the `ink` directory, run `sudo python setup.py install`

---

**MySQL**: You might need to download mySQL for osx. 

* Get the latest 64-bit MySQL **DMG** from here: [http://dev.mysql.com/downloads/mysql/](http://dev.mysql.com/downloads/mysql/)
* Install the two packages AND the prefpane
* Follow the MySQL instructions here: [http://akrabat.com/computing/setting-up-php-mysql-on-os-x-10-8-mountain-lion/](http://akrabat.com/computing/setting-up-php-mysql-on-os-x-10-8-mountain-lion/)
* After step 2 where you edit `~/.bash_profile`, dont forget to close your terminal window and open a new one. It won't work otherwise. Also, use `subl` if vim is confusing.
* Now you can start a MySQL server from your system preferences panel, and if you type `mysql` into terminal it will tell you which versin you're running. Ink needs this to live. I think. 


## Usage

### Creating projects

Go to the `/Ink` folder in our shared `/Upstatement` folder on dropbox, and create a new project folder as you would normally.

### Listing projects

run `ink.py list projects` from the command line.

### Listing local databases

run `ink.py list db`

### Dumping a local database to a project

If you had a project directory called `inkwell` which was using local database `wp_inkwell` you would run `ink.py save wp_inkwell to inkwell`

### Updating a local database with the latest project database

Let's say you're Jared, and you're working with Mike. 

Mike has just posted his local database for project `princeton` with a `ink.py save` commmand, and you'd like to load that into a local database called `wp_prince`.

As Jared, you'd run `ink.py update wp_prince from princeton` to pull in his changes.

**note: This will only use the most recent file. At the moment you can't pull old SQL in using Ink**