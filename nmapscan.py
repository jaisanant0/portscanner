import nmap
import optparse
from socket import*

def nmapscan(trghost,trgport) :
      trgip = gethostbyname(trghost)
      
      nscan = nmap.PortScanner()
      nscan.scan(trghost,trgport)
      nstate = nscan[trgip]['tcp'][int(trgport)]['state']
      print("[+] " + trgip + " "  +  "%d/tcp" %int(trgport) + " " + nstate)


def main() :
      parser=optparse.OptionParser(" %prog " + " -H <target host> -P <tarhet port(s)> ")
      parser.add_option("-H" , dest = "trghost" ,  type ="string" , help ="Specify target host")
      parser.add_option("-P" , dest = "trgport" ,  type ="string" ,help ="Specify target port(s) seperated by comma")
      (options,args) = parser.parse_args()
      trghost = options.trghost
      trgports = str(options.trgport).split(',')

      if (trghost == 0) | (trgports[0] == 0) :
           print ("Specify target host and target port(s)")
           exit(0)
      print("[+]  Scanning " + trghost + " - " + (str(gethostbyname(trghost))))
      for trgport in trgports :
             
            nmapscan(trghost,trgport)
            


      
if __name__ == '__main__' :
      main()
