#include <stdio.h>
#include <string.h>
void ran()
{
	printf("%c\n",'\x34');
}
int ca()
{
	int input = 0;
	printf("�������\n");
	printf("��Ҫ�ú�ѧϰ��(1/0)>:");
	scanf("%d", &input);
	if (input == 1)
		printf("���������۷�\n");
	else
		printf("������");




	return 0;
}
int main()
{
	ran();
	ca();

}
