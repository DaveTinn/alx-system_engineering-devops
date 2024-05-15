# Changing the OS configuration to login with the 'holberton' user and open a file without any error message

exec {'Configuring the OS':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path	  => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
