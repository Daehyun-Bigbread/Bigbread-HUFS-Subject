#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
// 제약조건
// 1. input 으로 주어지는 파일의 한줄은 100자를 넘지 않음.
// 2. input 으로 주어지는 파일의 길이는 100000줄을 넘지 않음. 즉, address trace 길이는 100000줄을 넘지 않음.
#define MAX_ROW     100000
#define MAX_COL     2
#define MAX_INPUT   100

// instruction cache
struct instruction_cache{
    int tag;
    int valid;
    int time; // LRU 이용하기 위한 변수
};
// data cache
struct data_cache{
    int tag;
    int valid;
    int time;
    int dirty;
};

// 전역변수
// 문제를 풀기 위한 힌트로써 제공된 것이며, 마음대로 변환 가능합니다.
enum COLS {
    MODE,
    ADDR
};

int i_total, i_miss;            /* instructino cache 총 접근 횟수, miss 횟수*/
int d_total, d_miss, d_write;   /* data cache 접근 횟수 및 miss 횟수, memory write 횟수 */
int trace[MAX_ROW][MAX_COL] = {{0,0},};
int trace_length = 0;
int time_count;

struct instruction_cache *ip;
struct data_cache *dp;

// 구현해야하는 함수
void solution(int cache_size, int block_size, int assoc, char replacement_policy);
void read_op(int addr, int cache_size, int block_size, int assoc, char replacement_policy);
void write_op(int addr, int cache_size, int block_size, int assoc, char replacement_policy);
void fetch_inst(int addr, int cache_size, int block_size, int assoc, char replacement_policy);
int lru(int set, int assoc, char mode);
int random_replacement(int set, int assoc, char mode);



int main(){
    // DO NOT MODIFY -- START --  //
    // cache size
    int cache[5] = {1024, 2048, 4096, 8192, 16384};
    // block size
    int block[2] = {16, 64};
    // associatvity e.g., 1-way, 2-way, ... , 8-way
    int associative[4] = {1, 2, 4, 8};
    int i=0,j=0,k=0;

    /* 입력 받아오기 */
    char input[MAX_INPUT];

    while (fgets(input, sizeof(input), stdin)) {
        if(sscanf(input, "%d %x\n", &trace[trace_length][MODE], &trace[trace_length][ADDR]) != 2) {
            fprintf(stderr, "error!\n");
        }
        trace_length++;
    }

    /* 캐시 시뮬레이션 */
    printf("cache size || block size || associative || d-miss rate || i-miss rate || mem write\n");
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 2; j++) {
            for (k = 0; k < 4; k++) {
                solution(cache[i], block[j], associative[k], 'L');
                solution(cache[i], block[j], associative[k], 'R');
            }
        }
    }
    // DO NOT MODIFY -- END --  //
    return 0;
}

void solution(int cache_size, int block_size, int assoc, char replacement_policy) {
    i_total = i_miss = 0;
    d_total = d_miss = d_write = 0;
    time_count = 0;

    int num = cache_size / block_size;
//    ip = (struct instruction_cache*)malloc(sizeof(struct instruction_cache) * num);
//    dp = (struct data_cache*)malloc(sizeof(struct data_cache) * num);
     ip = (struct instruction_cache*)calloc(num, sizeof(struct instruction_cache));
     dp = (struct data_cache*)calloc(num, sizeof(struct data_cache));

    // DO NOT MODIFY -- START --  //
    int mode, addr;
    double i_miss_rate, d_miss_rate;    /* miss rate을 저장하는 변수 */

    int index = 0;
    while(index != trace_length) {
        mode = trace[index][MODE];
        addr = trace[index][ADDR];

        switch(mode) {
            case 0 :
                read_op(addr, cache_size, block_size, assoc, replacement_policy);
                d_total++;
                break;
            case 1 :
                write_op(addr, cache_size, block_size, assoc, replacement_policy);
                d_total++;
                break;
            case 2 :
                fetch_inst(addr, cache_size, block_size, assoc, replacement_policy);
                i_total++;
                break;
        }
        index++;
    }
    // DO NOT MODIFY -- END --  //

    // hint. data cache miss rate 와 intruction cache miss rate를 계산하시오.
    // ? 에는 알맞는 변수를 넣으면 됩니다.
    free(ip);
    free(dp);
//    memset(ip, 0, sizeof(struct instruction_cache) * num);
//    memset(dp, 0, sizeof(struct data_cache) * num);

    i_miss_rate = (double)i_miss / (double)i_total;
    d_miss_rate = (double)d_miss / (double)d_total;

    // LRU 또는 Random 출력
    if (replacement_policy == 'L') {
        printf("LRU ");
    } else {
        printf("Random ");
    }

    // DO NOT MODIFY -- START --  //
    printf("%8d\t%8d\t%8d\t%.4lf\t%.4lf\t%8d\n", cache_size, block_size, assoc, d_miss_rate, i_miss_rate, d_write);
    // DO NOT MODIFY -- END --  //

}

// 아래 함수를 직접 구현하시오, 차례로 읽기, 쓰기, 그리고 인스트럭션 fetch 동작입니다.
void read_op(int addr, int cache_size, int block_size, int assoc, char replacement_policy){
    int num_of_sets = cache_size / (block_size * assoc); // LRU로 교체할 엔트리 주소찾기
    int set = (addr / block_size) % num_of_sets; // 세트 인덱스 계산
    int tag = addr / (block_size * num_of_sets); // 태그 계산

    int i, found = 0;

    for (i = 0; i < assoc; i++) { // 연관성에 따른 반복문
        if (dp[set * assoc + i].valid == 1 && dp[set * assoc + i].tag == tag) { // 캐시 엔트리가 유효하고 태그가 일치하는지 확인
            found = 1; // Cache Hit
            dp[set * assoc + i].time = time_count++; // 시간 값 갱신
            break;
        }
    }

    if (!found) { // Cache Miss
        d_miss++; // 데이터 캐시 미스 +1
        int offset;
        if (replacement_policy == 'L') {
            offset = lru(set, assoc, 'D');
        } else {
            offset = random_replacement(set, assoc, 'D');  // LRU 알고리즘을 사용해 교체할 캐시를 찾음
        }
        if (dp[set * assoc + offset].dirty == 1){ // 교체할 캐시가 dirty 인 경우 (캐시와 메모리가 서로 다를 때)
            d_write++; // 메모리 +1
        }

        dp[set * assoc + offset].tag = tag; // 새로운 태그
        dp[set * assoc + offset].valid = 1; // valid 1
        dp[set * assoc + offset].time = time_count++; // 시간 값 갱신
        dp[set * assoc + offset].dirty = 0; // dirty 상태 초기화
    }
}
void write_op(int addr, int cache_size, int block_size, int assoc, char replacement_policy) {
    int num_of_sets = cache_size / (block_size * assoc); // 데이터 캐시의 세트 수 계산
    int set = (addr / block_size) % num_of_sets; // 세트 인덱스 계산
    int tag = addr / (block_size * num_of_sets); // 태그 계산

    int i, found = 0;

    for (i = 0; i < assoc; i++) { // 연관성에 따른 반복문
        if (dp[set * assoc + i].valid == 1 && dp[set * assoc + i].tag == tag) { // 캐시 엔트리가 유효하고 태그가 일치하는지 확인
            found = 1; // Cache Hit
            dp[set * assoc + i].time = time_count++; // 시간 값 갱신
            dp[set * assoc + i].dirty = 1;
            break;
        }
    }

    if (!found) {
        d_miss++; // 데이터 캐시 미스 +1
        int offset;
        if (replacement_policy == 'L') {
            offset = lru(set, assoc, 'D');
        } else {
            offset = random_replacement(set, assoc, 'D');
        }

        if (dp[set * assoc + offset].dirty == 1){
            d_write++;
        }

        dp[set * assoc + offset].tag = tag; // 새로운 태그
        dp[set * assoc + offset].valid = 1; // valid 1
        dp[set * assoc + offset].time = time_count++; // 시간 값을 현재 값으로 갱신
        dp[set * assoc + offset].dirty = 1; // dirty bit를 1로 -> 데이터가 변경되었음을 표시
    }
}


void fetch_inst(int addr, int cache_size, int block_size, int assoc, char replacement_policy){
    int num_of_sets = cache_size / (block_size * assoc); // 데이터 캐시의 세트 수 계산
    int set = (addr / block_size) % num_of_sets; // 세트 인덱스 계산
    int tag = addr / (block_size * num_of_sets); // 태그 계산

    int i, j, found = 0;

    for (i = 0; i < assoc; i++) { // 연관성에 따른 반복문
        if (ip[set * assoc + i].valid == 1 && ip[set * assoc + i].tag == tag) { // 인스트럭션 캐시 엔트리 확인
            found = 1; // Cache Hit
            ip[set * assoc + i].time = time_count++; // 시간 값을 현재 값으로 갱신
            break;
        }
    }

    if (!found) { // Cache Miss
        i_miss++; // 인스트럭션 미스 + 1
        int offset;
        if(replacement_policy == 'L') {
            offset = lru(set, assoc, 'I');
        } else {
            offset = random_replacement(set, assoc, 'I');
        }
        ip[set * assoc + offset].tag = tag; // 새로운 태그
        ip[set * assoc + offset].valid = 1; // valid 1
        ip[set * assoc + offset].time = time_count++; // 시간 값을 현재 값으로 갱신
    }
}
// hint. LRU 알고리즘 교체 정책을 구현하기 위한 함수도 작성하셔서 적용하면 됩니다.
int lru(int set, int assoc, char mode) {
    int min = time_count;
    int min_index = 0;

    for (int i = 0; i < assoc; i++) {
        if (mode == 'D') {
            if (dp[set * assoc + i].valid == 0) {
                return i;
            }
            if (dp[set * assoc + i].time < min) {
                min = dp[set * assoc + i].time;
                min_index = i;
            }
        } else if (mode == 'I') {
            if (ip[set * assoc + i].valid == 0) {
                return i;
            }
            if (ip[set * assoc + i].time < min) {
                min = ip[set * assoc + i].time;
                min_index = i;
            }
        }
    }

    return min_index;
}

int random_replacement(int set, int assoc, char mode) {
    srand(time(NULL));
    return rand() % assoc;
}
