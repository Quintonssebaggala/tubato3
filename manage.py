from app import app
from app.data.models import db, Experience, Image, Flyer, Advert, ShoppingCart, Date_available, Imageexp, Rating, Shop, Slideshow, Story, User, Role 
from flask_migrate import Migrate

migrate = Migrate(app, db)

with app.app_context():
    # db.drop_all()
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, 
    			db=db, 
    			Experience=Experience, 
    			Image=Image, 
    			Flyer=Flyer, 
    			Advert=Advert, 
    			ShoppingCart=ShoppingCart, 
    			Date_available=Date_available, 
    			Imageexp=Imageexp, 
    			Rating=Rating,  
    			Shop=Shop, 
    			Slideshow=Slideshow, 
    			Story=Story,
                User=User,
                Role=Role)
