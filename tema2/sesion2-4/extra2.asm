.code
  daddi r2, r2, 1
  nop
  daddi r1, r2, 2
a:
  dmul r3, r3, r3
  dmul r5, r5, r5
  dsub r2, r2, r1
  beqz r1, a
  j b
b:
  ori r1, r0, 4
