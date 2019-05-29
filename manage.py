from application import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.user import User

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
