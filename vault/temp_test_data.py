from item import Item

###########################################
#                  ITEMS                  #
###########################################

BOW_OF_FAERDHINEN = Item({
    "name": "Bow of Faerdhinen",
    "slot": "two-handed",
    "range": 10,
    "attack_speed": 5,
    "bonuses": {
        "attack_stab": 0,
        "attack_slash": 0,
        "attack_crush": 0,
        "attack_magic": 0,
        "attack_range": 128,
        "defense_stab": 0,
        "defense_slash": 0,
        "defense_crush": 0,
        "defense_magic": 0,
        "defense_range": 0,
        "melee_strength": 0,
        "range_strength": 106,
        "magic_damage": 0,
        "prayer_bonus": 0,
    },
    "attack_styles": {
        "accurate": {
            "style_type": "ranged",
            "weapon_style": "accurate",
            "boosts": {
                "attack_ranged": 3,
            }
        },
        "rapid": {
            "style_type": "ranged",
            "weapon_style": "rapid",
            "boosts": {
                "attack_speed": 1
            }
        },
        "longrange": {
            "style_type": "ranged",
            "weapon_style": "longranged",
            "boosts": {
                "defense": 3,
                "range": 0,
            }
        }
    }
})