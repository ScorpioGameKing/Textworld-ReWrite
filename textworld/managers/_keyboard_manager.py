import pyray as pr

class KeyboardManager():

    _key_map: dict = {
        'A'     : pr.KEY_A            , 'APS'  : pr.KEY_APOSTROPHE     ,  'B'    : pr.KEY_B             , 'BAC' : pr.KEY_BACK          , 'BSL' : pr.KEY_BACKSLASH    ,
        'BSK'   : pr.KEY_BACKSPACE    , 'C'    : pr.KEY_C              ,  'CAP'  : pr.KEY_CAPS_LOCK     , 'CMA' : pr.KEY_COMMA         , 'D'   : pr.KEY_D            , 'DEL' : pr.KEY_DELETE      ,
        'DWN'   : pr.KEY_DOWN         , 'E'    : pr.KEY_E              ,  '9'    : pr.KEY_EIGHT         , 'END' : pr.KEY_END           , 'ENT' : pr.KEY_ENTER        , 'EQL' : pr.KEY_EQUAL       ,
        'ESC'   : pr.KEY_ESCAPE       , 'F'    : pr.KEY_F              ,  'F1'   : pr.KEY_F1            , 'F10' : pr.KEY_F10           , 'F11' : pr.KEY_F11          , 'F12' : pr.KEY_F12         ,
        'F2'    : pr.KEY_F2           , 'F3'   : pr.KEY_F3             ,  'F4'   : pr.KEY_F4            , 'F5'  : pr.KEY_F5            , 'F6'  : pr.KEY_F6           , 'F7'  : pr.KEY_F7          ,
        'F8'    : pr.KEY_F8           , 'F9'   : pr.KEY_F9             ,  '5'    : pr.KEY_FIVE          , '4'   : pr.KEY_FOUR          , 'G'   : pr.KEY_G            , 'GRV' : pr.KEY_GRAVE       ,
        'H'     : pr.KEY_H            , 'HOM'  : pr.KEY_HOME           ,  'I'    : pr.KEY_I             , 'INS' : pr.KEY_INSERT        , 'J'   : pr.KEY_J            , 'K'   : pr.KEY_K           ,
        'NPMNU' : pr.KEY_KB_MENU      , 'NP0'  : pr.KEY_KP_0           ,  'NMP1' : pr.KEY_KP_1          , 'NP2' : pr.KEY_KP_2          , 'NP3' : pr.KEY_KP_3         , 'NP4' : pr.KEY_KP_4        ,
        'NP5'   : pr.KEY_KP_5         , 'NP6'  : pr.KEY_KP_6           ,  'NP7'  : pr.KEY_KP_7          , 'NP8' : pr.KEY_KP_8          , 'NP9' : pr.KEY_KP_9         , 'NPA' : pr.KEY_KP_ADD      ,
        'NP.'   : pr.KEY_KP_DECIMAL   , 'NP/'  : pr.KEY_KP_DIVIDE      ,  'NPE'  : pr.KEY_KP_ENTER      , 'NP=' : pr.KEY_KP_EQUAL      , 'NPM' : pr.KEY_KP_MULTIPLY  , 'NPS' : pr.KEY_KP_SUBTRACT ,
        'L'     : pr.KEY_L            , 'LFT'  : pr.KEY_LEFT           ,  'LAL'  : pr.KEY_LEFT_ALT      , '['   : pr.KEY_LEFT_BRACKET  , 'LCT' : pr.KEY_LEFT_CONTROL , 'LSH' : pr.KEY_LEFT_SHIFT  ,
        'LSP'   : pr.KEY_LEFT_SUPER   , 'M'    : pr.KEY_M              ,  'MNU'  : pr.KEY_MENU          , '-'   : pr.KEY_MINUS         , 'N'   : pr.KEY_N            , '9'   : pr.KEY_NINE        ,
        'NUL'   : pr.KEY_NULL         , 'NML'  : pr.KEY_NUM_LOCK       ,  'O'    : pr.KEY_O             , '1'   : pr.KEY_ONE           , 'P'   : pr.KEY_P            , 'PGD' : pr.KEY_PAGE_DOWN   ,
        'PUP'   : pr.KEY_PAGE_UP      , 'PAU'  : pr.KEY_PAUSE          ,  '.'    : pr.KEY_PERIOD        , 'PRT' : pr.KEY_PRINT_SCREEN  , 'Q'   : pr.KEY_Q            , 'R'   : pr.KEY_R           ,
        'RGH'   : pr.KEY_RIGHT        , 'RAL'  : pr.KEY_RIGHT_ALT      ,  ']'    : pr.KEY_RIGHT_BRACKET , 'RCT' : pr.KEY_RIGHT_CONTROL , 'RSH' : pr.KEY_RIGHT_SHIFT  , 'RSP' : pr.KEY_RIGHT_SUPER ,
        'S'     : pr.KEY_S            , 'SCRL' : pr.KEY_SCROLL_LOCK    ,  ';'    : pr.KEY_SEMICOLON     , '7'   : pr.KEY_SEVEN         , '6'   : pr.KEY_SIX          , 'SLH' : pr.KEY_SLASH       ,
        'SPC'   : pr.KEY_SPACE        , 'T'    : pr.KEY_T              ,  'TAB'  : pr.KEY_TAB           , '3'   : pr.KEY_THREE         , '2'   : pr.KEY_TWO          , 'U'   : pr.KEY_U           ,
        'UP'    : pr.KEY_UP           , 'V'    : pr.KEY_V              ,  'VDN'  : pr.KEY_VOLUME_DOWN   , 'VUP' : pr.KEY_VOLUME_UP     , 'W'   : pr.KEY_W            , 'X'   : pr.KEY_X           ,
        'Y'     : pr.KEY_Y            , 'Z'    : pr.KEY_Z              ,  '0'    : pr.KEY_ZERO           
    }

    def get_key(self, key_char):
        return pr.is_key_pressed(self._key_map[key_char])

    def update(self):
        pass
        