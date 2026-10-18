# Проверки: предоставленные выводы CLI

Дата сбора: 18.10.2026. Ниже избранные строки из сообщений пользователя; это не полный терминальный лог. Все маршрутизаторы: процесс OSPF 1. Более поздние данные R13/R14 заменяют первоначальные значения.

## R19 — полностью тупиковая область

```text
R19#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Lo0          1     101             10.10.255.19/32    1     LOOP  0/0
Et0/0        1     101             10.10.200.77/30    10    P2P   1/1

R19#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
14.14.14.14       0   FULL/  -        00:00:36    10.10.200.78    Ethernet0/0
```

Единственная запись из show ip route ospf:

```text
O*IA  0.0.0.0/0 [110/11] via 10.10.200.78, 00:46:28, Ethernet0/0
```

## R14 — ABR

Из show ip ospf:

```text
It is an area border router
Area 10
    It is a stub area
    Generates stub default route with cost 1
Area 101
    It is a stub area, no summary LSA in this area
    Generates stub default route with cost 1
```

Из show ip ospf interface brief:

```text
Lo0          1     0               10.10.255.14/32    1     LOOP  0/0
Et1/0        1     0               10.10.200.89/30    10    P2P   1/1
Et0/1        1     10              10.10.200.86/30    10    P2P   1/1
Et0/0        1     10              10.10.200.66/30    10    P2P   1/1
Et0/3        1     101             10.10.200.78/30    10    P2P   1/1
```

Последний вывод после исправления default:

```text
R14(config)#do sh ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "static", distance 1, metric 0, candidate default path
  Routing Descriptor Blocks:
  * 172.20.20.2
      Route metric is 0, traffic share count is 1
```

## R15 — ABR и фильтрация

Из show ip ospf для area 102:

```text
Area-filter FILTER_IP_FROM_AREA101 in
```

Из show ip route ospf — запрещённые для R20 сети есть у самого R15:

```text
O IA     10.10.200.76/30 [110/20] via 10.10.200.89, 00:51:30, Ethernet1/0
O IA     10.10.255.19/32 [110/21] via 10.10.200.89, 00:51:30, Ethernet1/0
```

## R20 — результат фильтра

```text
R20#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Lo0          1     102             10.10.255.20/32    1     LOOP  0/0
Et0/0        1     102             10.10.200.73/30    10    P2P   1/1

R20#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
15.15.15.15       0   FULL/  -        00:00:36    10.10.200.74    Ethernet0/0
```

Из show ip route ospf (легенда опущена):

```text
Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 12 subnets, 2 masks
O IA     10.10.200.64/30 [110/30] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.200.68/30 [110/20] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.200.80/30 [110/20] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.200.84/30 [110/30] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.200.88/30 [110/20] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.255.12/32 [110/21] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.255.13/32 [110/21] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.255.14/32 [110/21] via 10.10.200.74, 00:52:31, Ethernet0/0
O IA     10.10.255.15/32 [110/11] via 10.10.200.74, 00:52:31, Ethernet0/0
```

## R12 — два default

```text
O*IA  0.0.0.0/0 [110/11] via 10.10.200.82, 00:55:07, Ethernet0/3
                [110/11] via 10.10.200.66, 00:55:07, Ethernet0/2
```

## R13 — исправление /32 и два default

```text
R13#sh ip ospf int br
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Lo0          1     10              10.10.255.13/32    1     LOOP  0/0
Et0/3        1     10              10.10.200.85/30    10    P2P   1/1
Et0/2        1     10              10.10.200.69/30    10    P2P   1/1
```

Из новой таблицы:

```text
O*IA  0.0.0.0/0 [110/11] via 10.10.200.86, 01:10:00, Ethernet0/3
                [110/11] via 10.10.200.70, 01:10:10, Ethernet0/2
C        10.10.255.13/32 is directly connected, Loopback0
```

## Проверки ping

Получены восемь успешных межроутерных тестов (5/5) и один ожидаемо неуспешный R20 → R19 (0/5). См. [результаты](ping-results.md).

## LSDB R20

Получен полный вывод summary для area 102: девять Type 3 от R15, без 10.10.200.76/30, 10.10.255.19/32 и default. Повторная таблица R20 согласуется с LSDB. См. [подробный вывод](r20-lsdb.md).

## Что не подтверждалось отдельным выводом

- Traceroute и ping к внешним назначениям.
- Детальное содержимое LSDB остальных областей и отдельные LSA default: для них получены сводные данные show ip ospf. Type 3 LSDB R20 проверена отдельно.
- Переключение при отказе линка, ABR или провайдера.
- IPv6 и работа нижней части Москвы через OSPF.

Отсутствующие проверки не обозначаются как успешные. Политика областей и фильтра проверены по конфигурациям и фактическому составу RIB.
