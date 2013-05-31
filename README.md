# ink: tools for wordpress teams that work

## wat

This is set of tools written on top of [fabric](http://docs.fabfile.org/en/1.6/), a python-based tool for deployment + systems administration. The hope is that the annoying parts of setting up a new wordpress project will be marginalized by awesome productivity. If you'd like to contribute, fork it & change it & submit a pull request!

## Requirements

* Dropbox
* A MySQL database that contains your wp install (If this is a mystery, download [Sequel Pro](http://www.sequelpro.com/), and talk to Jared or Pete)
* OSX Mountain Lion w/up-to-date [OSX Xcode Command Line Tools](http://slashusr.wordpress.com/2012/07/27/os-x-mountain-lion-need-to-reinstall-xcode-command-line-tools/)
* [fabric](http://docs.fabfile.org/en/1.6/). (install with `sudo easy_install fabric==1.6`)

## installation

* Clone this repo and cd into the `ink` dir
* Make a copy of the sample inkrc in your home directory with `cp sample.inkrc ~/.inkrc`
* Update the `.inkrc` with your information (sublime it with `subl ~/.inkrc`)
* from the `ink` directory, run `sudo python setup.py install`

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
