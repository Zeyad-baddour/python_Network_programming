l1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
l2 = [80, 443, 20, 53]

d = {x : y for x,y in zip(l1, l2)}

print(d)