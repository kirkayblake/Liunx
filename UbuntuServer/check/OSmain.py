import OScheck
import OSini
import OStime
import OSuser
import fail2ban
import ufw
import OSssh
if __name__ == '__main__':
    OScheck.main()
    print("Please press any key to continue……")
    input()
    OSini.main()
    OStime.main()
    OSuser.main()
    fail2ban.main()
    ufw.main()
    OSssh.main()

