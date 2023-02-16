import os
from ...vault import Vault
from .dps_calc import DamageCalculator
from ...vault import GearSet, GEAR_SLOTS

if __name__ == "__main__":
    vault = Vault(f"{os.getcwd()}/src/data")
    
    player = vault.getPlayerByTemplate("maxed_combats")

    kbd = vault.getMonsterByName("King Black Dragon")
    bowfa = vault.getItemByName("Bow of Faerdhinen")
    
    gearset = GearSet()
    gearset.setItemInSlot(GEAR_SLOTS.WEAPON, bowfa)
    
    calc = DamageCalculator(player, [kbd], [gearset])