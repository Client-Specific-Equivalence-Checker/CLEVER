int foo(int a, int b);


int main(void) {
	return foo(5,900);
}

int foo(int a, int b) {
	const int d=3;
	int c=b+a;
	return c+d;
}
