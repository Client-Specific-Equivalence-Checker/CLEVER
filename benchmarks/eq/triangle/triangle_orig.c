int triangle(int n) {
  int r;
  r = g(n);
  return r;
}

int g(int n)
{
  int r;
  r = 0;

  if (n <= 0) {
    r = 0;
  } else {
    r = g(n - 1);
    r = n + r;
  }

  return r;
}

int main(void) {
	return triangle(5);
}