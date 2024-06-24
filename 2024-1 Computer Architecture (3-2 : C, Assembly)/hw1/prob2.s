# DO NOT MODIFY
.data
src:
    .word   1
    .word   2
    .word   3
    .word   4
    .word   0

.text
main:
# DO NOT MODIFY
    addi t0, x0, 0
    la t1, src
loop:
    slli t3, t0, 2
    add t4, t1, t3
    lw t5, 0(t4)
    beq t5, x0, exit
    addi t0, t0, 1
    jal x0, loop
exit:
    jal ra, print_lists
    addi a0, x0, 10
    add a1, x0, x0
    ecall # Terminate

print_lists:
    addi sp, sp, -4
    sw ra, 0(sp)

    la a0, src
    jal ra, print_list

    addi a1, x0, '\n'
    addi a0, x0, 11
    ecall

    lw ra, 0(sp)
    addi sp, sp, 4
    jr ra

print_list:
    # Stop recursing when the value at 0(a0) is 0
    lw t0, 0(a0)
    bne t0, x0, printChar
    jr ra

printChar:
    add t0, a0, x0         # a0 (현재 요소의 주소)를 t0에 복사
    lw a1, 0(t0)           # t0에서 원소 값을 a1에 로드
    andi t2, a1, 1         # a1의 값과 1을 AND 연산하여 홀수인지 체크 (결과를 t2에 저장)
    beqz t2, even          # t2가 0이면(짝수) even 레이블로 점프
odd:
    addi a0, x0, 1         # 홀수일 경우: 시스템 콜 준비 (정수 출력)
    ecall                  # 홀수 값 출력
    j nextChar             # 다음 문자 처리로 점프

even:
    mul a1, a1, a1         # 짝수일 경우: 원소 값을 제곱
    addi a0, x0, 1         # 시스템 콜 준비 (정수 출력)
    ecall                  # 제곱된 값 출력

nextChar:
    ## DO NOT MODIFY
    # Print a space
    addi a1, x0, ' '       
    addi a0, x0, 11        
    ecall                  

    addi a0, t0, 4         
    jal x0, print_list