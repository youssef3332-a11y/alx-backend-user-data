#!/usr/bin/env python3
"""
Main file
"""
from user import User
from db import DB

db = DB()
user = db.add_user("youssef", "hashedpassword")
print(user.id)
print(user.email)
print(user.hashed_password)
print(user.session_id)