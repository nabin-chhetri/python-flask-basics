from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
def get_menuitems():
    menuitems = session.query(MenuItem).all()
    output = ""
    for item in menuitems:
        output += item.name
        output += "</br>"
        output += item.price
        output += "</br>"
        output += item.description
        output += "</br></br>"
    return output

# GET requests to retrieve all restaurants
@app.route('/restaurants')
def restaurants():
    restaurants = session.query(Restaurant).all()
    output = ""
    for restaurant in restaurants:
        output += restaurant.name
        output += "</br>"
    return output

@app.route('/menuitems')
def menuItems():
    menuItems = session.query(MenuItem).all()
    output = ""
    for menuItem in menuItems:
        output += "name : " + menuItem.name
        output += "</br>"
        output += "price : " + menuItem.price    
        output += "</br>"
        output += "description : " + menuItem.description
        output += "</br>"
        output += "course : " + menuItem.course
        output += "</br></br>"
    return output


# GET request to retrieve the menu items for a particular restaurant by id
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menuitems = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    output = ""
    for item in menuitems:
        output += item.name
        output += "</br>"
        output += item.price
        output += "</br>"
        output += item.description
        output += "</br>"
        output += item.course
        output += "</br></br>"
    return output
    


# Task 1: Create route for newMenuItem function here
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"


# Task 2: Create route for editMenuItem function here
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    pass