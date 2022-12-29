"""
Create table for users
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
CREATE TABLE users (
user_id serial,
username text,
is_deleted bool
);
""")
]
