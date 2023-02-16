from enum import auto
from strenum import StrEnum

class GEAR_STATS(StrEnum):
    ATTACK_STAB = auto()
    ATTACK_SLASH = auto()
    ATTACK_CRUSH = auto()
    ATTACK_MAGIC = auto()
    ATTACK_RANGE = auto()
    DEFENSE_STAB = auto()
    DEFENSE_SLASH = auto()
    DEFENSE_CRUSH = auto()
    DEFENSE_MAGIC = auto()
    DEFENSE_RANGE = auto()
    MELEE_STRENGTH = auto()
    RANGE_STRENGTH = auto()
    MAGIC_DAMAGE = auto()
    PRAYER_BONUS = auto()

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
    ATTACK_TYPES.RANGED.lower(): GEAR_STATS.ATTACK_RANGE,
}
