# nib: a set of tools for working within wordpress teams

## wat

This is set of tools written using [fabric](http://docs.fabfile.org/en/1.6/), a python-based tool for deployment + systems administration. The hope is that the annoying parts of setting up a new wordpress project will be marginalized by awesome productivity. If you'd like to contribute, fork it & change it & submit a pull request!

## Requirements

* Dropbox
* A MySQL database that contains your wp install
* OSX Mountain Lion w/up-to-date [OSX Xcode Command Line Tools](http://slashusr.wordpress.com/2012/07/27/os-x-mountain-lion-need-to-reinstall-xcode-command-line-tools/)
* [fabric](http://docs.fabfile.org/en/1.6/). (install with `sudo easy_install fabric==1.6`)

## installation

* clone this repository (into `~/Sandbox`, for example)
* Go to the Nib directory: `cd ~/Sandbox/nib`
* Make a copy of the sample fabricrc in your home directory with `cp sample.fabricrc ~/.fabricrc`
* Update the `.fabricrc` with your information (sublime it with `subl ~/.fabricrc`)
* Open your bash_profile
  `subl ~/.bash_profile`
* Add this line:
  `export PATH=${PATH}:/Applications/MAMP/Library/bin` to the bottom of your .bash_profile

## Usage

For the time being, **you have to run all of these commands from the `nib` directory**.

### Creating projects

Go to the `/Nib` folder in our shared `/Upstatement` folder on dropbox, and create a new project folder as you would normally.

### Listing projects

run `fab dip ls` from the command line.

### Listing local databases

run `fab dip lsdb`

### Dumping a local database to a project

If you had a project directory called `inkwell` which was using local database `wp_inkwell` you would run `fab dip dump:inkwell,db_name=wp_inkwell`

### Updating a local database with the latest project database

Let's say you're Jared, and you're working with Mike. 

Mike has just posted his local database for project `princeton` with a `fab dip dump` commmand, and you'd like to load that into a local database called `wp_prince`.

To load that, you'd run `fab dip load:princeton,wp_prince`

**note: This will only use the most recent file. At the moment you can't pull old SQL in using Nib**

## Changelog

* 2013-03-28: Removed the setup.py nonsense until I figure that out. Updated README for upstate-folk
* 2013-03-27: Created this thing.
