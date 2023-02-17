from enum import auto
from strenum import StrEnum

class GEAR_STATS(StrEnum):
    ATTACK_STAB = auto()
    ATTACK_SLASH = auto()
    ATTACK_CRUSH = auto()
    ATTACK_MAGIC = auto()
    ATTACK_RANGED = auto()
    DEFENSE_STAB = auto()
    DEFENSE_SLASH = auto()
    DEFENSE_CRUSH = auto()
    DEFENSE_MAGIC = auto()
    DEFENSE_RANGED = auto()
    MELEE_STRENGTH = auto()
    RANGED_STRENGTH = auto()
    MAGIC_DAMAGE = auto()
    PRAYER_BONUS = auto()

class SKILL_TYPES(StrEnum):
    ATTACK = auto()
    DEFENSE = auto()
    STRENGTH = auto()
    HITPOINTS = auto()
    PRAYER = auto()
    MAGIC = auto()
    COOKING = auto()
    WOODCUTTING = auto()
    FLETCHING = auto()
    FISHING = auto()
    FIREMAKING = auto()
    CRAFTING = auto()
    SMITHING = auto()
    MINING = auto()
    HERBLORE = auto()
    AGILITY = auto()
    THIEVING = auto()
    SLAYER = auto()
    FARMING = auto()
    RUNECRAFTING = auto()
    HUNTER = auto()
    CONSTRUCTION = auto()
    
class ENEMY_STATS(StrEnum):
    ATTACK = auto()
    DEFENSE = auto()
    STRENGTH = auto()
    MAGIC = auto()
    RANGED = auto()
    DEFENSE_STAB = auto()
    DEFENSE_SLASH = auto()
    DEFENSE_CRUSH = auto()
    DEFENSE_MAGIC = auto()
    DEFENSE_RANGED = auto()
    MELEE_ACCURACY = auto()
    MELEE_STRENGTH = auto()
    RANGED_ACCURACY = auto()
    RANGED_STRENGTH = auto()
    MAGIC_DAMAGE = auto()
    MAGIC_ACCURACY = auto()
    ATTRIBUTES = auto()
    ATTACK_SPEED = auto()
    
class PLAYER_STATS(StrEnum):
    ATTACK = auto()
    DEFENSE = auto()
    STRENGTH = auto()
    RANGED = auto()
    MAGIC = auto()
    HITPOINTS = auto()

class GEAR_SLOTS(StrEnum):
    HEAD = auto()
    CAPE = auto()
    NECK = auto()
    AMMUNITION = auto()
    WEAPON = auto()
    SHIELD = auto()
    BODY = auto()
    LEGS = auto()
    HANDS = auto()
    FEET = auto()
    RING = auto()

class ATTACK_TYPES(StrEnum):
    STAB = auto()
    SLASH = auto()
    CRUSH = auto()
    MAGIC = auto()
    RANGED = auto()

class ATTACK_STYLES(StrEnum):
    # [MELEE OPTIONS]
    ACCURATE = auto()
    AGGRESSIVE = auto()
    DEFENSIVE = auto()
    CONTROLEED = auto()
    
    # [MAGE OPTIONS]
    STANDARD = auto()
    # DEFENSIVE = auto()    <-- Duplicate Key

    # [RANGE OPTIONS]
    # ACCURATE = auto()     <-- Duplicate Key
    RAPID = auto()
    LONGRANGE = auto()

ATTACK_TYPE_TO_BONUS_MAP = {
    ATTACK_TYPES.STAB.lower(): GEAR_STATS.ATTACK_STAB,
    ATTACK_TYPES.SLASH.lower(): GEAR_STATS.ATTACK_SLASH,
    ATTACK_TYPES.CRUSH.lower(): GEAR_STATS.ATTACK_CRUSH,
    ATTACK_TYPES.MAGIC.lower(): GEAR_STATS.ATTACK_MAGIC,
    ATTACK_TYPES.RANGED.lower(): GEAR_STATS.ATTACK_RANGED,
}

ATTACK_STYLE_TYPE_TO_ACCURACY_SKILL = {
    ATTACK_TYPES.STAB.lower(): PLAYER_STATS.ATTACK,
    ATTACK_TYPES.SLASH.lower(): PLAYER_STATS.ATTACK,
    ATTACK_TYPES.CRUSH.lower(): PLAYER_STATS.ATTACK,
    ATTACK_TYPES.MAGIC.lower(): PLAYER_STATS.MAGIC,
    ATTACK_TYPES.RANGED.lower(): PLAYER_STATS.RANGED,
}

ATTACK_STYLE_TYPE_TO_STRENGTH_SKILL = {
    ATTACK_TYPES.STAB.lower(): PLAYER_STATS.STRENGTH,
    ATTACK_TYPES.SLASH.lower(): PLAYER_STATS.STRENGTH,
    ATTACK_TYPES.CRUSH.lower(): PLAYER_STATS.STRENGTH,
    ATTACK_TYPES.MAGIC.lower(): PLAYER_STATS.MAGIC,
    ATTACK_TYPES.RANGED.lower(): PLAYER_STATS.RANGED,
}

ATTACK_STYLE_TYPE_TO_MONSTER_DEFENCE_TYPE = {
    ATTACK_TYPES.STAB.lower(): ENEMY_STATS.DEFENSE_STAB,
    ATTACK_TYPES.SLASH.lower(): ENEMY_STATS.DEFENSE_SLASH,
    ATTACK_TYPES.CRUSH.lower(): ENEMY_STATS.DEFENSE_CRUSH,
    ATTACK_TYPES.MAGIC.lower(): ENEMY_STATS.DEFENSE_MAGIC,
    ATTACK_TYPES.RANGED.lower(): ENEMY_STATS.DEFENSE_RANGED,
}

ATTACK_STYLE_TO_GEAR_STRENGTH = {
    ATTACK_TYPES.STAB: GEAR_STATS.MELEE_STRENGTH,
    ATTACK_TYPES.SLASH: GEAR_STATS.MELEE_STRENGTH,
    ATTACK_TYPES.CRUSH: GEAR_STATS.MELEE_STRENGTH,
    ATTACK_TYPES.MAGIC: GEAR_STATS.MAGIC_DAMAGE,
    ATTACK_TYPES.RANGED: GEAR_STATS.RANGED_STRENGTH,
}