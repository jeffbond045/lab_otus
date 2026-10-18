# Результаты ping

Источник: сообщение пользователя от 18.10.2026. Нормализованные выдержки: команда, source, строка ответов и итог. Служебные приглашения и Telnet-вход опущены. Команды не запускались моделью.

## R12 → R13

```text
R12#ping 10.10.255.13 source Loopback0
Packet sent with a source address of 10.10.255.12
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R12 → R19

```text
R12#ping 10.10.255.19 source Loopback0
Packet sent with a source address of 10.10.255.12
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R20 → R12

```text
R20#ping 10.10.255.12 source Loopback0
Packet sent with a source address of 10.10.255.20
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R20 → R19

```text
R20#ping 10.10.255.19 source Loopback0
Packet sent with a source address of 10.10.255.20
.....
Success rate is 0 percent (0/5)
```

## R14 → R15

```text
R14#ping 10.10.255.15 source Loopback0
Packet sent with a source address of 10.10.255.14
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R14 → R20

```text
R14#ping 10.10.255.20 source Loopback0
Packet sent with a source address of 10.10.255.14
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms
```

## R15 → R14

```text
R15#ping 10.10.255.14 source Loopback0
Packet sent with a source address of 10.10.255.15
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R15 → R19

```text
R15#ping 10.10.255.19 source Loopback0
Packet sent with a source address of 10.10.255.15
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

## R12 → R20 — полный результат

```text
R12#ping 10.10.255.20 source loopback 0
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.255.20, timeout is 2 seconds:
Packet sent with a source address of 10.10.255.12
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

Получен отдельным сообщением после первоначально обрезанного вывода.

## Локальный тест R15

```text
R15#ping 10.10.255.15 source Loopback0
Packet sent with a source address of 10.10.255.15
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

Назначение принадлежит самому R15. Этот тест не доказывает прохождение пакетов через сеть и не включён в таблицу межроутерных проверок.
