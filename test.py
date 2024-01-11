mininet.net import Mininet from mininet.node import Controller, RemoteController from mininet.cli import CLI from mininet.link import Link, TCLink, Intf from mininet.log import setLogLevel, info
def customNet():
"Create custom network." net = Mininet( controller=RemoteController)
info( "*** Creating nodes\n" ) h1 = net.addHost( ’h1’ ) h2 = net.addHost( ’h2’ ) h3 = net.addHost( ’h3’ ) h4 = net.addHost( ’h4’ ) h5 = net.addHost( ’h5’ )
s1 = net.addSwitch( ’s1’ ) s2 = net.addSwitch( ’s2’ ) s3 = net.addSwitch( ’s3’ )
info( "*** Creating controller\n" ) c0 = net.addController(’c0’, controller=RemoteController, ip=’0.0.0.0’, port=6633)
info( "*** Creating links\n" ) net.addLink( h1, s1 ) net.addLink( h2, s1 ) net.addLink( h3, s1 ) net.addLink( s1, s2 ) net.addLink( s2, s3 ) net.addLink( h4, s3 ) net.addLink( h5, s3 )
info( "*** Starting network\n") net.build() c0.start() s1.start( [c0] ) s2.start( [c0] )
s3.start( [c0] )
info( "*** Running CLI\n" ) CLI( net )
info( "*** Stopping network" ) net.stop()
if __name__ == ’__main__’: setLogLevel( ’info’ ) customNet()
