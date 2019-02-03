# Udacity-FSND-PROJECT-IV
# Item Catalog Project

Udacity: Full Stack Web Development Nanodegree

## Project Overview

An application that is developed in order to provide a list of items within a variety of categories. This application also provides a user registration and authentication system, that allows registered users to have the ability to Create, Read, Update and Delete their own items.

## What you'll need (Pre-requisites):

1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Go to [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm) and clone or download it (contains all dependencies and libraries needed).
4. Add content of this [repository](https://github.com/AhmedEHaddad/Udacity-FSND-PROJECT-IV/tree/master/vagrant/catalog/catalogApp)

## How to run:

* clone this [repo](https://github.com/AhmedEHaddad/Udacity-FSND-PROJECT-IV/tree/master/vagrant/catalog/catalogApp) inside the `/vagrant/catalog` from this [Udacity's Repo](https://github.com/udacity/fullstack-nanodegree-vm)

* Launch the Virtual Machine using the command(from Udacity's repo vagrant folder):
```
    $ vagrant up
```
* Run the application inside the Virtual Machine:
```
    $ python /vagrant/catalog/catalogApp/app.py
```
* Access application by opening [http://localhost:5000](http://localhost:5000).

## API Endpoints
* JSON API Endpoint are available as follows:
  * all available categories info are available at `/category/JSON`
  * a certain category's items info are available `/category/<int:category_id>/items/JSON`
  * a certain item info is available at `/category/<int:category_id>/items/<int:item_id>/JSON`  

## License
MIT
## Resources

* [Intergrating Google Sign In](https://developers.google.com/identity/sign-in/web/sign-in)
* [Google Sign Out](https://developers.google.com/identity/sign-in/web/sign-in#sign_out_a_user)
* Udacity's Example Menu Application
* some GitHub repo's: [1](https://github.com/LeandriB/item_catalog).
