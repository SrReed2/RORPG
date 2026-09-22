# RORPG

RORPG is a text-based RPG created as a practice project for Object-Oriented Programming (OOP).

## Features

- Attack and deal damage.
- Receive damage.
- Dodge attacks.
- Heal.
- Equip items.
- Fight enemies.

## Requirements

- python 3.10+
- git

## Structure

├── entities/
|   ├── behavior/
|   |   ├── __init__.py
|   |   └── behavior.py
|   ├── items/
|   |   ├── __init__.py
|   |   ├── heal_object.py
|   |   ├── item.py
|   |   └── weapon.py
|   ├── __init__.py
|   ├── character.py
|   ├── enemy,py
|   └── player.py
├── world/
|   ├── generation.py
|   └── room.py
├── main.py
└── README.md

