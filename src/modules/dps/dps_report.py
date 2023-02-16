import os
from ...vault import Vault
from .dps_calc import DamageCalculator

if __name__ == "__main__":
    vault = Vault(f"{os.getcwd()}/src/data")
    
    player = vault.getPlayerTemplate("maxed_combats")
    bowfa = vault.getItemByName("Bow of Faerdhinen")
    print(bowfa)