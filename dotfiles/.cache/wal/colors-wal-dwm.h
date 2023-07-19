static const char norm_fg[] = "#a7c3c6";
static const char norm_bg[] = "#171213";
static const char norm_border[] = "#74888a";

static const char sel_fg[] = "#a7c3c6";
static const char sel_bg[] = "#526261";
static const char sel_border[] = "#a7c3c6";

static const char urg_fg[] = "#a7c3c6";
static const char urg_bg[] = "#2A5F66";
static const char urg_border[] = "#2A5F66";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
