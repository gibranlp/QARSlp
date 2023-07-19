const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#171213", /* black   */
  [1] = "#2A5F66", /* red     */
  [2] = "#526261", /* green   */
  [3] = "#A17647", /* yellow  */
  [4] = "#3C926A", /* blue    */
  [5] = "#38708E", /* magenta */
  [6] = "#23BCB7", /* cyan    */
  [7] = "#a7c3c6", /* white   */

  /* 8 bright colors */
  [8]  = "#74888a",  /* black   */
  [9]  = "#2A5F66",  /* red     */
  [10] = "#526261", /* green   */
  [11] = "#A17647", /* yellow  */
  [12] = "#3C926A", /* blue    */
  [13] = "#38708E", /* magenta */
  [14] = "#23BCB7", /* cyan    */
  [15] = "#a7c3c6", /* white   */

  /* special colors */
  [256] = "#171213", /* background */
  [257] = "#a7c3c6", /* foreground */
  [258] = "#a7c3c6",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
