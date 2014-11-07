from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
contact = Table('contact', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=30)),
    Column('lastname', String(length=30)),
    Column('phone', String(length=15)),
    Column('mobile', String(length=15)),
    Column('address', String(length=100)),
    Column('city', String(length=50)),
    Column('country', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['contact'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['contact'].drop()
