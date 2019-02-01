# Udacity-FSND-ProjectII: building a web App
# anlaysing the data from the news database
#created by: ahmed.e.haddad2.0@gmail.com

#########################################
#Imports
#########################################
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import datetime
#from flask_bootstrap import Bootstrap


app = Flask(__name__)
#bootstrap = Bootstrap(app)

APPLICATION_NAME = "Electro Portal Web Application"


####################################################
# Connect to Database and create database session
####################################################
engine = create_engine('sqlite:///electroportal.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




#########################################
#CRUD functionality
#########################################
# Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(desc(Item.date)).limit(5)
    '''if 'username' not in login_session:
        return render_template('publicCategories.html', categories=categories)
    else:
        return render_template('allCategories.html', categories=categories)'''
    #return "A webpage to show all categories"
    return render_template('home.html', categories=categories, items=items)

# Create a new Category


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    '''if 'username' not in login_session:
        return redirect('/login')'''
    if request.method == 'POST':
        #newCategory = Category(
            #name=request.form['name'], user_id=login_session['user_id'])
        newCategory = Category(
            name=request.form['name'], user_id=2) #remove later
        session.add(newCategory)
        session.commit()
        flash('New Category "%s" Successfully Created' % newCategory.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')
    #return "A webpage to create a new category"

# Edit a category


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    '''if 'username' not in login_session:
        return redirect('/login')
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this Category. Please create your own Category in order to edit.');}</script><body onload='myFunction()'>"'''
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)
    #return "A webpage to edit a certain category"


# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    '''if 'username' not in login_session:
        return redirect('/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this category. Please create your own category in order to delete.');}</script><body onload='myFunction()'>"'''
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('"%s" Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)
    #return "A webpage to delete a certain category"

# Show a category's items


@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    #creator = getUserInfo(category.user_id)
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    '''if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicItems.html', items=items, category=category, creator=creator)
    else:
        return render_template('menu.html', items=items, category=category, creator=creator)'''
    #return "A webpage that shows a category's list of items"
    return render_template('categoryItems.html', category=category, items=items)


# Show an item's description
@app.route('/category/<int:category_id>/items/<int:item_id>')
def showItem(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('anItem.html', item=item, category_id= category_id)

# Create a new category's item
@app.route('/category/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newItem(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    '''if 'username' not in login_session:
        return redirect('/login')

    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add items to this category. Please create your own category in order to add items.');}</script><body onload='myFunction()'>"'''
    if request.method == 'POST':
            newItem = Item(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            model=request.form['model'],
            manufacturer=request.form['manufacturer'],
            type=request.form['type'],
            date=datetime.datetime.now(),
            category_id=category_id,
            user_id=category.user_id)
            session.add(newItem)
            session.commit()
            flash('New Item "%s" Item Successfully Created' % (newItem.name))
            return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('newItem.html', category_id=category_id)
    #return " A webpage to create a new item in a certain category"

# Edit a menu item


@app.route('/category/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    '''if 'username' not in login_session:
        return redirect('/login')

    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit menu items to this category. Please create your own category in order to edit items.');}</script><body onload='myFunction()'>"'''
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            editedItem.date=datetime.datetime.now()
        if request.form['description']:
            editedItem.description = request.form['description']
            editedItem.date=datetime.datetime.now()
        if request.form['price']:
            editedItem.price = request.form['price']
            editedItem.date=datetime.datetime.now()
        if request.form['type']:
            editedItem.type = request.form['type']
            editedItem.date=datetime.datetime.now()
        if request.form['model']:
            editedItem.model = request.form['model']
            editedItem.date=datetime.datetime.now()
        if request.form['manufacturer']:
            editedItem.manufacturer = request.form['manufacturer']
            editedItem.date=datetime.datetime.now()
        session.add(editedItem)
        session.commit()
        flash('Item Successfully Edited')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editItem.html', category_id=category_id, item_id=item_id, item=editedItem)
    #return " A webpage to edit an item in a certain category"


# Delete an item
@app.route('/category/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    '''if 'username' not in login_session:
        return redirect('/login')

    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete menu items to this category. Please create your own category in order to delete items.');}</script><body onload='myFunction()'>"'''
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item Successfully Deleted')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)
    #return " A webpage to delete an item in a certain category"

#########################################
#########################################
#Authenication & Authorization
#########################################



#########################################
#########################################
#JSON API Endpoints
#########################################



#########################################
#########################################
#Imports
#########################################




#########################################
#Imports
#########################################







###############################################
#Running the server #always at the end of file
###############################################
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


######################End Of Code#####################################
