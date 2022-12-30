.data
	var: dword 12
	res: dword 0

.code
main:
	daddi 	r10, r0, 5		; r10 <- 5
	daddi	r3, r0, 4		; r3 <- 4
	daddi	r4, r6, 7 		; r4 <- 7
	xor		r3, r3, r3
	ld    	r5, var(r0) 	; load var in r5
loop:
	xor		r6, r6, r6		; r6 <- 0
	ori		r2, r2, 2		; r2 <- 0
	daddi  	r5, r5, -3 		; r5 <- r5 - 3
	beqz	r5, end			; checks if r5 is equals 0, and if so jumps to end label
	j		loop
end:
	sd 		r5, res(r0)		; store r5
