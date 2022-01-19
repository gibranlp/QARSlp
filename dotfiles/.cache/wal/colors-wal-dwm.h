static const char norm_fg[] = "#d2dddc";
static const char norm_bg[] = "#051828";
static const char norm_border[] = "#939a9a";

static const char sel_fg[] = "#d2dddc";
static const char sel_bg[] = "#28675C";
static const char sel_border[] = "#d2dddc";

static const char urg_fg[] = "#d2dddc";
static const char urg_bg[] = "#24605A";
static const char urg_border[] = "#24605A";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
