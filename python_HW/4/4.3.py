config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config=config.split()
config=config[-1].split(',')
print(config)