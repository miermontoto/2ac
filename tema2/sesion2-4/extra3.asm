daddi r1, r1, 16
daddi r2, r2, 1
nop
a:
  dsub r1, r1, r2
  bnez r1, a
  ori r1, r0, 4
