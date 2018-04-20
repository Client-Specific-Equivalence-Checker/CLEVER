/* Greatest common divisor */
unsigned int lib(unsigned int a, unsigned int b) {
  unsigned int r;

  if (a < b) {
    // swap(a,b)
    int temp = a;
    a = b;
    b = temp;
  }

  if (!b)
    return a;

  while ((r = a % b) != 0) {
    a = b;
    b = r;
  }

  return b;
}

#define CDCE925_PLL_FREQUENCY_MIN 80000
#define CDCE925_PLL_FREQUENCY_MAX 230000

// cdce925_pll_find_rate
int client(unsigned int rate, unsigned int parent_rate, int n, int m)
{
  unsigned int un;
  unsigned int um;
  unsigned int g;

  if (rate <= parent_rate) {
    /* Can always deliver parent_rate in bypass mode */
    rate = parent_rate;
    n = 0;
    m = 0;
    return 0;
  } else {
    /* In PLL mode, need to apply min/max range */
    if (rate < CDCE925_PLL_FREQUENCY_MIN)
      rate = CDCE925_PLL_FREQUENCY_MIN;
    else if (rate > CDCE925_PLL_FREQUENCY_MAX)
      rate = CDCE925_PLL_FREQUENCY_MAX;

    g = lib(rate, parent_rate);
    um = parent_rate / g;
    un = rate / g;
    /* When outside hw range, reduce to fit (rounding errors) */
    while ((un > 4095) || (um > 511)) {
    	un >>= 1;
    	um >>= 1;
    }
    if (un == 0)
    	un = 1;
    if (um == 0)
    	um = 1;
    
    n = un;
    m = um;
    return g;
  }
}
