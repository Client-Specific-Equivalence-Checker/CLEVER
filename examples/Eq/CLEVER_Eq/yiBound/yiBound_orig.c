int lib(int x) {
  if (x > 10)
    return 11;
  else
    return x;
}

int client(int x) {
  if (x < -100 || x > 100) {
    return x;
  }
  if (x > lib(x))
    return x;
  else
    return lib(x);
}

int main() {
  int x;
  return client(x);
}
