#!/usr/bin/bash
log_cleaner()
{
echo "Cleaning logs ..."
sudo find  /var/log -type f \( -name "*.log" -o -name "btmp" -o -name "lastlog" -o -name "wtmp" \) -exec truncate -s 0 {} \;
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s

echo "log content erased!"

}


log_cleaner






