from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manger


migrate = Migrate(app,db)

manger = Manger(app)
manger.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manger.run()
