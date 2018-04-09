int foo(int a, int b);

int main(void) {
	return foo(5,900);
}

int foo(int a, int b) {
	int c=a+b;
	return c+3;
}
