import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
player_HP = 100
player_AC = 14
pl_ability_mods = {'str':5, 'dex':3, 'con':3, 'int':-1, 'wis':0, 'cha':1}
pl_prof_bonus = 4

enemy_HP = 100
enemy_AC = 15
en_ability_mods = {'str':2, 'dex':5, 'con':3, 'int':0, 'wis':3, 'cha':0}
en_prof_bonus = 3

player = []
enemy = []
combat_round = []
player_roll = []
enemy_roll = []
player_dmg = []
enemy_dmg = []
player_current_HP = [player_HP]
enemy_current_HP = [enemy_HP]

for x in range(10) :
    pl_die = np.random.randint(1,20)
    player_attack = pl_die + pl_ability_mods['str'] + pl_prof_bonus
    pl_dmg_die = (np.random.randint(1,8))
    pl_dmg_roll = pl_dmg_die + pl_ability_mods['str']
    pl_crit = (pl_dmg_die * 2) + pl_ability_mods['str']
    en_die = np.random.randint(1,20)
    enemy_attack = en_die + en_ability_mods['dex'] + en_prof_bonus
    en_dmg_die = (np.random.randint(1, 6))
    en_dmg_roll = en_dmg_die + en_ability_mods['dex']
    en_crit = (en_dmg_die * 2) + en_ability_mods['dex']
    if player_attack >= enemy_AC:
        if pl_die == 20:
            pl_dmg_roll.replace(pl_crit)
        player.append('player_hit')
        combat_round.append(x + 1)
        player_roll.append(player_attack)
        player_dmg.append(pl_dmg_roll)
        enemy_current_HP.append(enemy_current_HP[x] - pl_dmg_roll)
    elif player_attack < enemy_AC:
        player.append('player_miss')
        player_roll.append(player_attack)
        player_dmg.append(0)
        enemy_current_HP.append(enemy_current_HP[x] - 0)
    if enemy_attack >= player_AC:
        if en_die == 20:
            en_dmg_roll.replace(en_crit)
        enemy.append('enemy_hit')
        enemy_roll.append(enemy_attack)
        enemy_dmg.append(en_dmg_roll)
        player_current_HP.append(player_current_HP[x] - en_dmg_roll)
    elif enemy_attack < player_AC:
        enemy.append('enemy_miss')
        enemy_roll.append(enemy_attack)
        enemy_dmg.append(0)
        player_current_HP.append(player_current_HP[x] - 0)

encounter = {'player':player, 'pl_roll': player_roll, 'pl_dmg':player_dmg, 'enemy_HP': enemy_current_HP, 'enemy':enemy, 'en_roll':enemy_roll, 'en_dmg':enemy_dmg, 'player_HP':player_current_HP}
combat = pd.DataFrame.from_dict(encounter, orient='index')
combat = combat.transpose()
combat = combat.fillna(0)
print(combat.to_string())