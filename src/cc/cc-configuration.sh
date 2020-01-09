#
# Modified configuration for CC Base / MLS mode compliance
#
# su alias, added for EAL4+ configuration
alias su="echo \"Always use '/bin/su -' (see 'Evaluated Configuration Guide')\"; echo >/dev/null"

# ssh / ssh-keygen use of /dev/random as seed source
# You MUST enable the following lines to be compliant with the
# requirements of the evaluated configuration. For a description of this
# configuration and its implication, see /etc/sysconfig/sshd. Use the
# 'readonly' setting to ensure that all users are required to use this
# variable.
export SSH_USE_STRONG_RNG=12
readonly SSH_USE_STRONG_RNG

#
# The following environment variable disables the use of the AES-NI
# Intel processor instruction set. This is required by BSI as the AES-NI
# instruction set was not subject to evaluation
export OPENSSL_DISABLE_AES_NI=1
readonly OPENSSL_DISABLE_AES_NI

# Setting the umask value to a DISA STIG compliant value for normal users
# This setting overrides the setting in /etc/profile
umask 027
