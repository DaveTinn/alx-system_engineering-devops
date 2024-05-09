# Debugging why Apache returns 500, fixt it and then automate using Puppet

exec { 'fix and automate':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
