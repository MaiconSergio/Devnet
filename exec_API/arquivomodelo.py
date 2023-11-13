Value INTF (\S+)
Value IPADDR (\d+\.\d+\.\d+\.\d+)
Value STATUS (\w+)
Value PROTOCOL (\w+)

Start
  ^${INTF}\s+${IPADDR}\s+\w+\s+\w+\s+${STATUS}\s+${PROTOCOL} -> Record
