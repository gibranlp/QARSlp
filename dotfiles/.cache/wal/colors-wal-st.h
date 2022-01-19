const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#051828", /* black   */
  [1] = "#24605A", /* red     */
  [2] = "#28675C", /* green   */
  [3] = "#2E7162", /* yellow  */
  [4] = "#59906B", /* blue    */
  [5] = "#678F8E", /* magenta */
  [6] = "#98B4B4", /* cyan    */
  [7] = "#d2dddc", /* white   */

  /* 8 bright colors */
  [8]  = "#939a9a",  /* black   */
  [9]  = "#24605A",  /* red     */
  [10] = "#28675C", /* green   */
  [11] = "#2E7162", /* yellow  */
  [12] = "#59906B", /* blue    */
  [13] = "#678F8E", /* magenta */
  [14] = "#98B4B4", /* cyan    */
  [15] = "#d2dddc", /* white   */

  /* special colors */
  [256] = "#051828", /* background */
  [257] = "#d2dddc", /* foreground */
  [258] = "#d2dddc",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
