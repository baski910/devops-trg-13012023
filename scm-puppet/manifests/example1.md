node "hostname of agent" {
   user { 'bob':
     ensure => present,
     managehome => true
     }
}
