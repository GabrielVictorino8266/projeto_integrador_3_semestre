from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.create_collection('vehicles')


    def downgrade(self):
        self.db.vehicles.drop()
