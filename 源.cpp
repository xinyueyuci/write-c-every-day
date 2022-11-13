#include <stdio.h>
#include <string.h>
void ran()
{
	printf("%c\n",'\x34');
}
int ca()
{
	int input = 0;
	printf("加入比特\n");
	printf("你要好好学习吗？(1/0)>:");
	scanf("%d", &input);
	if (input == 1)
		printf("走上人生巅峰\n");
	else
		printf("买红黑树");




	return 0;
}
int main()
{
	ran();
	ca();

}
