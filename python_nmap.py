import nmap

tgHost='220.181.57.217'
tgPorts='3389,21,22,80,8080'

def nmapScan(host,port):
    nmScan=nmap.PortScanner()
    nmScan.scan(host,port)
    state=nmScan[host]['tcp'][int(port)]['state']
    print "[*] " +host+" tcp/"+port+" "+state

if __name__=='__main__':
    Ports=tgPorts.split(',')
    for Port in Ports:
      nmapScan(tgHost,Port)