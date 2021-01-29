nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat=nat.replace('Fast', 'Gigabit')
print(nat)