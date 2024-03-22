# Install flask from pip3, using Puppet
package { 'flask':
    provider => 'pip3',
    ensure   => '2.1.0',
}
