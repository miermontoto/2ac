.code

main:
	ori 	r4, r0, 1
	daddi	r3, r2, 4
	xor		r1, r3, r5
	ld		r9, 12(r5)
	dmul 	r8, r5, r4
	and		r5, r8, r4
	xor		r6, r2, r4
	xor		r3, r3, r3
	daddi	r3, r2, 3
	dmul	r8, r9, r4
