from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from app.models import User,Role,Pitch,Comment,Upvote,Downvote


# creating app instance
# app = create_app('production')
app = create_app('development')


migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)


@manager.command

def test():

    """
    Run the unit tests.

    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role,Pitch = Pitch,Comment = Comment,Upvote = Upvote,Downvote = Downvote) #,Pitch=Pitch, Comment=Comment     ,Pitches=Pitches, Coding = Coding,Business = Business,Forex=Forex,Religion = Religion

if __name__ == '__main__':
    manager.run()
