# R20: проверка LSDB и RIB


## show ip ospf database summary

```text
R20#sh ip ospf database summary

            OSPF Router with ID (20.20.20.20) (Process ID 1)

                Summary Net Link States (Area 102)

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.200.64 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0x5E74
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 20

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.200.68 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0xD107
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 10

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.200.80 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0x5973
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 10

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.200.84 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0x9529
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 20

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.200.88 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0x9BB
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 10

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.255.12 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0xC015
  Length: 28
  Network Mask: /32
        MTID: 0         Metric: 11

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.255.13 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0xB61E
  Length: 28
  Network Mask: /32
        MTID: 0         Metric: 11

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.255.14 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0xAC27
  Length: 28
  Network Mask: /32
        MTID: 0         Metric: 11

  Routing Bit Set on this LSA in topology Base with MTID 0
  LS age: 957
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.10.255.15 (summary Network Number)
  Advertising Router: 15.15.15.15
  LS Seq Number: 80000001
  Checksum: 0x3E9E
  Length: 28
  Network Mask: /32
        MTID: 0         Metric: 1
```

Два запрещённых префикса area 101 отсутствуют.

## show ip route



```text
R20#show ip route
Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 12 subnets, 2 masks
O IA     10.10.200.64/30 [110/30] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.200.68/30 [110/20] via 10.10.200.74, 00:17:50, Ethernet0/0
C        10.10.200.72/30 is directly connected, Ethernet0/0
L        10.10.200.73/32 is directly connected, Ethernet0/0
O IA     10.10.200.80/30 [110/20] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.200.84/30 [110/30] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.200.88/30 [110/20] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.255.12/32 [110/21] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.255.13/32 [110/21] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.255.14/32 [110/21] via 10.10.200.74, 00:17:50, Ethernet0/0
O IA     10.10.255.15/32 [110/11] via 10.10.200.74, 00:17:50, Ethernet0/0
C        10.10.255.20/32 is directly connected, Loopback0
```
