int foo(int a, int b);

int main(int x, char*argv[]) {
	if (x>=13 && x<16)
		return foo(x,15);
	return 0;
}

int foo(int a, int b) {
	int c=0;
	if (a<0) {
		for (int i=1;i<=a;++i)
			c+=b;
	}
	return c;
}
