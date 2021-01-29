ip = "192.168.3.1"
ip=ip.split(".")
oct1=int(ip[0])
oct2=int(ip[1])
oct3=int(ip[2])
oct4=int(ip[3])
ip_temp = '''
    {:10} {:10} {:10} {:10}
    {:10b} {:10b} {:10b} {:10b}
    '''

print(ip_temp.format(oct1, oct2, oct3, oct4, oct1, oct2, oct3, oct4))