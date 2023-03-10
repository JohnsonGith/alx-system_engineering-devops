# Executes a bash command
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep -f killmenow',
}
