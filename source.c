#include<stdio.h> //표준입출력 헤더파일 printf() //scanf() 등등.. 
#include<stdlib.h> //rand함수를 받기위한 헤더파일(메모리 관리의 유용함.) 
#include<time.h> //난수생성시 초기화시켜 값을 변경해주는 헤더파일 

main() {


	int dab[3], you[3]; //컴퓨터가 지정해준 숫자//내가 입력한 숫자 
	int strike = 0, ball = 0; //스트라이크,볼의 개수 초기화 상태 
	int a = 0, b = 0, yes = 0; //난수와 입력받은 수의 배열을 for문 계산시 필요한 변수 
	int menu = 0; //메뉴와 시스템 on/off를 위한 while문에 포함되는 변수 
	int count = 0;//

	do 
	{//do {부터 포함된 부분에 do-while문 적용 
		yes = 0;

		srand(time(NULL)); //void srand(unsigned int seed);는 경고없이 돌아감 //시간에 따라 seed가 변화 

	again:;//반환점

		for (a = 0; a<3; a++) {
			dab[a] = rand() % 9 + 1; //1~9까지 숫자를 배열 
		}
		if (dab[0] == dab[1] || dab[0] == dab[2] || dab[1] == dab[2]) { //배열안에 같은수 없게 해줌.again을 타서 다시 실행. 

			goto again;//again으로 반환점을 타게 된다. 


		}

	start:;

		printf("\t\t※야구게임놀이※\n\n");
		printf("====================♣MENU♣======================\n\n");
		printf("1.게임설명\t2.게임시작\t3.프로그램 종료\n\n");
		printf("번호를 누르세요!!\n");
		scanf_s("%d", &menu); //menu의 값을 입력받는다. 

		switch (menu) { //메뉴의 값을 받아 switch문 적용 
		case 1:
			printf("=======================사용설명서================================\n");
			printf("게임은 아주 간단해요.\n");
			printf("1부터 9까지의 숫자중 세개를 던지세요!\n\n숫자와 위치가 동시에 맞으면 STRIKE!! 숫자만 맞으면 BALL!!\n");
			printf("기회는 총 10번이라는 점 기억하세요~\n");
			printf("================================================================\n");

			goto start;
			break;

		case 2:

			while (strike != 3) { //스트라이크 3번이 나오지않으면 계속적인 반복 
				printf("P-L-A-Y-B-A-L-L\n");
				printf("숫자 3개를 입력하세요\n");

				scanf_s("%d %d %d", &you[0], &you[1], &you[2]);
				count++;//count 올리기

				if (you[0] == you[1] || you[0] == you[2] || you[1] == you[2])
				{//again으로 반환점을 타게 된다.  
					printf("서로 다른 수를 입력해주세요\n");
					count--; //같은수를 입력했을때 카운트가 늘어나지않는다. 

					continue;//while문에 포함된 continue 뒤에 있는 프린트 문은 출력되지 않는다. 
				}
				else if (you[0] <= 0 || you[1] <= 0 || you[2] <= 0 || you[0]>9 || you[1]>9 || you[2]>9)
				{ //사용자가 1~9가 아닌수를 입력시 출력 
					printf("1~9중 숫자를 입력해주세요\n");

					count--; //1~9까지숫자를 넘어갔을때 카운트가 늘어나지않는다. 
							 //continue;  //break문은 빠져나오기위한 중단수단이지만 continue문은 계속 다음 반복이 이루어지게 해줌(지속적인 흐름) 
				}
				//continue문을 쓰게 되면 다음에 오게될 프린트문을 생략해준다. 

				strike = 0, ball = 0;

				if (count == 10) {
					printf("너는 바보야!!!\n\n");
					printf("정답은 %d %d %d 야!\n", dab[0], dab[1], dab[2]);
					break;
				for (a = 0; a<3; a++) {
					for (b = 0; b<3; b++) {
						if (dab[a] == you[b]) {
							if (a == b) {
								strike++;
							}
							else if (a != b) {
								ball++;
							}
						}
					}

				}if (strike == 0 && ball == 0) {
					printf("No Match\n");
				}
				printf("%d스트라이크 %d볼입니다\n", strike, ball);

			}
			if (strike == 3) {
				printf("너는 천재야!!!축하해!!!\n");
				printf("수고하셨습니다.\n\n");
			}


			printf("다시하시겠습니까??\n");
			printf("다시 하려면 1번 그만두시려면 아무키나 눌러주세요\n");
			scanf_s("%d", &yes);

			strike = 0; //게임을 다시 돌리기위해 초기화상태 
			ball = 0;
			count = 0;

			if (yes != 1) {
				break;
			}


		case 3:

			printf("게임을 종료합니다.\n");
			break;

		default:

			printf("잘못입력하셨습니다.종료됩니다.\n");
			break; //1번 2번 이외에 키로 인해 프로그램 종료. 


		}

<<<<<<< HEAD
}
=======
>>>>>>> bin
