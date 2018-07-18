int foo(int a, int b) {
	int c=0;
	if (a<0) {
		for (int i=1;i<=a;++i)
			c += b;
	}
	return c;

int main(int x, char*argv[]) {                
	if (x>=63 && x<87)                
		return foo(x,75);                
	return 0;
