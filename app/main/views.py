from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm, UpdateProfile
from ..models import Review,User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  



# Views

@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data

    '''    
        
    return render_template('index.html')


    







