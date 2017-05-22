# coding: utf-8
# Copyright 2015 Moses Palmér
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

KEYSYMS = {
    '\u0020': 'space',
    '\u0021': 'exclam',
    '\u0022': 'quotedbl',
    '\u0023': 'numbersign',
    '\u0024': 'dollar',
    '\u0025': 'percent',
    '\u0026': 'ampersand',
    '\u0027': 'apostrophe',
    '\u0027': 'quoteright',
    '\u0028': 'parenleft',
    '\u0029': 'parenright',
    '\u002a': 'asterisk',
    '\u002b': 'plus',
    '\u002c': 'comma',
    '\u002d': 'minus',
    '\u002e': 'period',
    '\u002f': 'slash',
    '\u0030': '0',
    '\u0031': '1',
    '\u0032': '2',
    '\u0033': '3',
    '\u0034': '4',
    '\u0035': '5',
    '\u0036': '6',
    '\u0037': '7',
    '\u0038': '8',
    '\u0039': '9',
    '\u003a': 'colon',
    '\u003b': 'semicolon',
    '\u003c': 'less',
    '\u003d': 'equal',
    '\u003e': 'greater',
    '\u003f': 'question',
    '\u0040': 'at',
    '\u0041': 'A',
    '\u0042': 'B',
    '\u0043': 'C',
    '\u0044': 'D',
    '\u0045': 'E',
    '\u0046': 'F',
    '\u0047': 'G',
    '\u0048': 'H',
    '\u0049': 'I',
    '\u004a': 'J',
    '\u004b': 'K',
    '\u004c': 'L',
    '\u004d': 'M',
    '\u004e': 'N',
    '\u004f': 'O',
    '\u0050': 'P',
    '\u0051': 'Q',
    '\u0052': 'R',
    '\u0053': 'S',
    '\u0054': 'T',
    '\u0055': 'U',
    '\u0056': 'V',
    '\u0057': 'W',
    '\u0058': 'X',
    '\u0059': 'Y',
    '\u005a': 'Z',
    '\u005b': 'bracketleft',
    '\u005c': 'backslash',
    '\u005d': 'bracketright',
    '\u005e': 'asciicircum',
    '\u005f': 'underscore',
    '\u0060': 'grave',
    '\u0060': 'quoteleft',
    '\u0061': 'a',
    '\u0062': 'b',
    '\u0063': 'c',
    '\u0064': 'd',
    '\u0065': 'e',
    '\u0066': 'f',
    '\u0067': 'g',
    '\u0068': 'h',
    '\u0069': 'i',
    '\u006a': 'j',
    '\u006b': 'k',
    '\u006c': 'l',
    '\u006d': 'm',
    '\u006e': 'n',
    '\u006f': 'o',
    '\u0070': 'p',
    '\u0071': 'q',
    '\u0072': 'r',
    '\u0073': 's',
    '\u0074': 't',
    '\u0075': 'u',
    '\u0076': 'v',
    '\u0077': 'w',
    '\u0078': 'x',
    '\u0079': 'y',
    '\u007a': 'z',
    '\u007b': 'braceleft',
    '\u007c': 'bar',
    '\u007d': 'braceright',
    '\u007e': 'asciitilde',
    '\u00a0': 'nobreakspace',
    '\u00a1': 'exclamdown',
    '\u00a2': 'cent',
    '\u00a3': 'sterling',
    '\u00a4': 'currency',
    '\u00a5': 'yen',
    '\u00a6': 'brokenbar',
    '\u00a7': 'section',
    '\u00a8': 'diaeresis',
    '\u00a9': 'copyright',
    '\u00aa': 'ordfeminine',
    '\u00ab': 'guillemotleft',
    '\u00ac': 'notsign',
    '\u00ad': 'hyphen',
    '\u00ae': 'registered',
    '\u00af': 'macron',
    '\u00b0': 'degree',
    '\u00b1': 'plusminus',
    '\u00b2': 'twosuperior',
    '\u00b3': 'threesuperior',
    '\u00b4': 'acute',
    '\u00b5': 'mu',
    '\u00b6': 'paragraph',
    '\u00b7': 'periodcentered',
    '\u00b8': 'cedilla',
    '\u00b9': 'onesuperior',
    '\u00ba': 'masculine',
    '\u00bb': 'guillemotright',
    '\u00bc': 'onequarter',
    '\u00bd': 'onehalf',
    '\u00be': 'threequarters',
    '\u00bf': 'questiondown',
    '\u00c0': 'Agrave',
    '\u00c1': 'Aacute',
    '\u00c2': 'Acircumflex',
    '\u00c3': 'Atilde',
    '\u00c4': 'Adiaeresis',
    '\u00c5': 'Aring',
    '\u00c6': 'AE',
    '\u00c7': 'Ccedilla',
    '\u00c8': 'Egrave',
    '\u00c9': 'Eacute',
    '\u00ca': 'Ecircumflex',
    '\u00cb': 'Ediaeresis',
    '\u00cc': 'Igrave',
    '\u00cd': 'Iacute',
    '\u00ce': 'Icircumflex',
    '\u00cf': 'Idiaeresis',
    '\u00d0': 'ETH',
    '\u00d0': 'Eth',
    '\u00d1': 'Ntilde',
    '\u00d2': 'Ograve',
    '\u00d3': 'Oacute',
    '\u00d4': 'Ocircumflex',
    '\u00d5': 'Otilde',
    '\u00d6': 'Odiaeresis',
    '\u00d7': 'multiply',
    '\u00d8': 'Ooblique',
    '\u00d9': 'Ugrave',
    '\u00da': 'Uacute',
    '\u00db': 'Ucircumflex',
    '\u00dc': 'Udiaeresis',
    '\u00dd': 'Yacute',
    '\u00de': 'THORN',
    '\u00de': 'Thorn',
    '\u00df': 'ssharp',
    '\u00e0': 'agrave',
    '\u00e1': 'aacute',
    '\u00e2': 'acircumflex',
    '\u00e3': 'atilde',
    '\u00e4': 'adiaeresis',
    '\u00e5': 'aring',
    '\u00e6': 'ae',
    '\u00e7': 'ccedilla',
    '\u00e8': 'egrave',
    '\u00e9': 'eacute',
    '\u00ea': 'ecircumflex',
    '\u00eb': 'ediaeresis',
    '\u00ec': 'igrave',
    '\u00ed': 'iacute',
    '\u00ee': 'icircumflex',
    '\u00ef': 'idiaeresis',
    '\u00f0': 'eth',
    '\u00f1': 'ntilde',
    '\u00f2': 'ograve',
    '\u00f3': 'oacute',
    '\u00f4': 'ocircumflex',
    '\u00f5': 'otilde',
    '\u00f6': 'odiaeresis',
    '\u00f7': 'division',
    '\u00f8': 'oslash',
    '\u00f9': 'ugrave',
    '\u00fa': 'uacute',
    '\u00fb': 'ucircumflex',
    '\u00fc': 'udiaeresis',
    '\u00fd': 'yacute',
    '\u00fe': 'thorn',
    '\u00ff': 'ydiaeresis',
    '\u0104': 'Aogonek',
    '\u02d8': 'breve',
    '\u0141': 'Lstroke',
    '\u013d': 'Lcaron',
    '\u015a': 'Sacute',
    '\u0160': 'Scaron',
    '\u015e': 'Scedilla',
    '\u0164': 'Tcaron',
    '\u0179': 'Zacute',
    '\u017d': 'Zcaron',
    '\u017b': 'Zabovedot',
    '\u0105': 'aogonek',
    '\u02db': 'ogonek',
    '\u0142': 'lstroke',
    '\u013e': 'lcaron',
    '\u015b': 'sacute',
    '\u02c7': 'caron',
    '\u0161': 'scaron',
    '\u015f': 'scedilla',
    '\u0165': 'tcaron',
    '\u017a': 'zacute',
    '\u02dd': 'doubleacute',
    '\u017e': 'zcaron',
    '\u017c': 'zabovedot',
    '\u0154': 'Racute',
    '\u0102': 'Abreve',
    '\u0139': 'Lacute',
    '\u0106': 'Cacute',
    '\u010c': 'Ccaron',
    '\u0118': 'Eogonek',
    '\u011a': 'Ecaron',
    '\u010e': 'Dcaron',
    '\u0110': 'Dstroke',
    '\u0143': 'Nacute',
    '\u0147': 'Ncaron',
    '\u0150': 'Odoubleacute',
    '\u0158': 'Rcaron',
    '\u016e': 'Uring',
    '\u0170': 'Udoubleacute',
    '\u0162': 'Tcedilla',
    '\u0155': 'racute',
    '\u0103': 'abreve',
    '\u013a': 'lacute',
    '\u0107': 'cacute',
    '\u010d': 'ccaron',
    '\u0119': 'eogonek',
    '\u011b': 'ecaron',
    '\u010f': 'dcaron',
    '\u0111': 'dstroke',
    '\u0144': 'nacute',
    '\u0148': 'ncaron',
    '\u0151': 'odoubleacute',
    '\u0159': 'rcaron',
    '\u016f': 'uring',
    '\u0171': 'udoubleacute',
    '\u0163': 'tcedilla',
    '\u02d9': 'abovedot',
    '\u0126': 'Hstroke',
    '\u0124': 'Hcircumflex',
    '\u0130': 'Iabovedot',
    '\u011e': 'Gbreve',
    '\u0134': 'Jcircumflex',
    '\u0127': 'hstroke',
    '\u0125': 'hcircumflex',
    '\u0131': 'idotless',
    '\u011f': 'gbreve',
    '\u0135': 'jcircumflex',
    '\u010a': 'Cabovedot',
    '\u0108': 'Ccircumflex',
    '\u0120': 'Gabovedot',
    '\u011c': 'Gcircumflex',
    '\u016c': 'Ubreve',
    '\u015c': 'Scircumflex',
    '\u010b': 'cabovedot',
    '\u0109': 'ccircumflex',
    '\u0121': 'gabovedot',
    '\u011d': 'gcircumflex',
    '\u016d': 'ubreve',
    '\u015d': 'scircumflex',
    '\u0138': 'kra',
    '\u0156': 'Rcedilla',
    '\u0128': 'Itilde',
    '\u013b': 'Lcedilla',
    '\u0112': 'Emacron',
    '\u0122': 'Gcedilla',
    '\u0166': 'Tslash',
    '\u0157': 'rcedilla',
    '\u0129': 'itilde',
    '\u013c': 'lcedilla',
    '\u0113': 'emacron',
    '\u0123': 'gcedilla',
    '\u0167': 'tslash',
    '\u014a': 'ENG',
    '\u014b': 'eng',
    '\u0100': 'Amacron',
    '\u012e': 'Iogonek',
    '\u0116': 'Eabovedot',
    '\u012a': 'Imacron',
    '\u0145': 'Ncedilla',
    '\u014c': 'Omacron',
    '\u0136': 'Kcedilla',
    '\u0172': 'Uogonek',
    '\u0168': 'Utilde',
    '\u016a': 'Umacron',
    '\u0101': 'amacron',
    '\u012f': 'iogonek',
    '\u0117': 'eabovedot',
    '\u012b': 'imacron',
    '\u0146': 'ncedilla',
    '\u014d': 'omacron',
    '\u0137': 'kcedilla',
    '\u0173': 'uogonek',
    '\u0169': 'utilde',
    '\u016b': 'umacron',
    '\u203e': 'overline',
    '\u3002': 'kana_fullstop',
    '\u300c': 'kana_openingbracket',
    '\u300d': 'kana_closingbracket',
    '\u3001': 'kana_comma',
    '\u30fb': 'kana_conjunctive',
    '\u30f2': 'kana_WO',
    '\u30a1': 'kana_a',
    '\u30a3': 'kana_i',
    '\u30a5': 'kana_u',
    '\u30a7': 'kana_e',
    '\u30a9': 'kana_o',
    '\u30e3': 'kana_ya',
    '\u30e5': 'kana_yu',
    '\u30e7': 'kana_yo',
    '\u30c3': 'kana_tsu',
    '\u30fc': 'prolongedsound',
    '\u30a2': 'kana_A',
    '\u30a4': 'kana_I',
    '\u30a6': 'kana_U',
    '\u30a8': 'kana_E',
    '\u30aa': 'kana_O',
    '\u30ab': 'kana_KA',
    '\u30ad': 'kana_KI',
    '\u30af': 'kana_KU',
    '\u30b1': 'kana_KE',
    '\u30b3': 'kana_KO',
    '\u30b5': 'kana_SA',
    '\u30b7': 'kana_SHI',
    '\u30b9': 'kana_SU',
    '\u30bb': 'kana_SE',
    '\u30bd': 'kana_SO',
    '\u30bf': 'kana_TA',
    '\u30c1': 'kana_CHI',
    '\u30c4': 'kana_TSU',
    '\u30c6': 'kana_TE',
    '\u30c8': 'kana_TO',
    '\u30ca': 'kana_NA',
    '\u30cb': 'kana_NI',
    '\u30cc': 'kana_NU',
    '\u30cd': 'kana_NE',
    '\u30ce': 'kana_NO',
    '\u30cf': 'kana_HA',
    '\u30d2': 'kana_HI',
    '\u30d5': 'kana_FU',
    '\u30d8': 'kana_HE',
    '\u30db': 'kana_HO',
    '\u30de': 'kana_MA',
    '\u30df': 'kana_MI',
    '\u30e0': 'kana_MU',
    '\u30e1': 'kana_ME',
    '\u30e2': 'kana_MO',
    '\u30e4': 'kana_YA',
    '\u30e6': 'kana_YU',
    '\u30e8': 'kana_YO',
    '\u30e9': 'kana_RA',
    '\u30ea': 'kana_RI',
    '\u30eb': 'kana_RU',
    '\u30ec': 'kana_RE',
    '\u30ed': 'kana_RO',
    '\u30ef': 'kana_WA',
    '\u30f3': 'kana_N',
    '\u309b': 'voicedsound',
    '\u309c': 'semivoicedsound',
    '\u060c': 'Arabic_comma',
    '\u061b': 'Arabic_semicolon',
    '\u061f': 'Arabic_question_mark',
    '\u0621': 'Arabic_hamza',
    '\u0622': 'Arabic_maddaonalef',
    '\u0623': 'Arabic_hamzaonalef',
    '\u0624': 'Arabic_hamzaonwaw',
    '\u0625': 'Arabic_hamzaunderalef',
    '\u0626': 'Arabic_hamzaonyeh',
    '\u0627': 'Arabic_alef',
    '\u0628': 'Arabic_beh',
    '\u0629': 'Arabic_tehmarbuta',
    '\u062a': 'Arabic_teh',
    '\u062b': 'Arabic_theh',
    '\u062c': 'Arabic_jeem',
    '\u062d': 'Arabic_hah',
    '\u062e': 'Arabic_khah',
    '\u062f': 'Arabic_dal',
    '\u0630': 'Arabic_thal',
    '\u0631': 'Arabic_ra',
    '\u0632': 'Arabic_zain',
    '\u0633': 'Arabic_seen',
    '\u0634': 'Arabic_sheen',
    '\u0635': 'Arabic_sad',
    '\u0636': 'Arabic_dad',
    '\u0637': 'Arabic_tah',
    '\u0638': 'Arabic_zah',
    '\u0639': 'Arabic_ain',
    '\u063a': 'Arabic_ghain',
    '\u0640': 'Arabic_tatweel',
    '\u0641': 'Arabic_feh',
    '\u0642': 'Arabic_qaf',
    '\u0643': 'Arabic_kaf',
    '\u0644': 'Arabic_lam',
    '\u0645': 'Arabic_meem',
    '\u0646': 'Arabic_noon',
    '\u0647': 'Arabic_ha',
    '\u0648': 'Arabic_waw',
    '\u0649': 'Arabic_alefmaksura',
    '\u064a': 'Arabic_yeh',
    '\u064b': 'Arabic_fathatan',
    '\u064c': 'Arabic_dammatan',
    '\u064d': 'Arabic_kasratan',
    '\u064e': 'Arabic_fatha',
    '\u064f': 'Arabic_damma',
    '\u0650': 'Arabic_kasra',
    '\u0651': 'Arabic_shadda',
    '\u0652': 'Arabic_sukun',
    '\u0452': 'Serbian_dje',
    '\u0453': 'Macedonia_gje',
    '\u0451': 'Cyrillic_io',
    '\u0454': 'Ukrainian_ie',
    '\u0455': 'Macedonia_dse',
    '\u0456': 'Ukrainian_i',
    '\u0457': 'Ukrainian_yi',
    '\u0458': 'Cyrillic_je',
    '\u0459': 'Cyrillic_lje',
    '\u045a': 'Cyrillic_nje',
    '\u045b': 'Serbian_tshe',
    '\u045c': 'Macedonia_kje',
    '\u045e': 'Byelorussian_shortu',
    '\u045f': 'Cyrillic_dzhe',
    '\u2116': 'numerosign',
    '\u0402': 'Serbian_DJE',
    '\u0403': 'Macedonia_GJE',
    '\u0401': 'Cyrillic_IO',
    '\u0404': 'Ukrainian_IE',
    '\u0405': 'Macedonia_DSE',
    '\u0406': 'Ukrainian_I',
    '\u0407': 'Ukrainian_YI',
    '\u0408': 'Cyrillic_JE',
    '\u0409': 'Cyrillic_LJE',
    '\u040a': 'Cyrillic_NJE',
    '\u040b': 'Serbian_TSHE',
    '\u040c': 'Macedonia_KJE',
    '\u040e': 'Byelorussian_SHORTU',
    '\u040f': 'Cyrillic_DZHE',
    '\u044e': 'Cyrillic_yu',
    '\u0430': 'Cyrillic_a',
    '\u0431': 'Cyrillic_be',
    '\u0446': 'Cyrillic_tse',
    '\u0434': 'Cyrillic_de',
    '\u0435': 'Cyrillic_ie',
    '\u0444': 'Cyrillic_ef',
    '\u0433': 'Cyrillic_ghe',
    '\u0445': 'Cyrillic_ha',
    '\u0438': 'Cyrillic_i',
    '\u0439': 'Cyrillic_shorti',
    '\u043a': 'Cyrillic_ka',
    '\u043b': 'Cyrillic_el',
    '\u043c': 'Cyrillic_em',
    '\u043d': 'Cyrillic_en',
    '\u043e': 'Cyrillic_o',
    '\u043f': 'Cyrillic_pe',
    '\u044f': 'Cyrillic_ya',
    '\u0440': 'Cyrillic_er',
    '\u0441': 'Cyrillic_es',
    '\u0442': 'Cyrillic_te',
    '\u0443': 'Cyrillic_u',
    '\u0436': 'Cyrillic_zhe',
    '\u0432': 'Cyrillic_ve',
    '\u044c': 'Cyrillic_softsign',
    '\u044b': 'Cyrillic_yeru',
    '\u0437': 'Cyrillic_ze',
    '\u0448': 'Cyrillic_sha',
    '\u044d': 'Cyrillic_e',
    '\u0449': 'Cyrillic_shcha',
    '\u0447': 'Cyrillic_che',
    '\u044a': 'Cyrillic_hardsign',
    '\u042e': 'Cyrillic_YU',
    '\u0410': 'Cyrillic_A',
    '\u0411': 'Cyrillic_BE',
    '\u0426': 'Cyrillic_TSE',
    '\u0414': 'Cyrillic_DE',
    '\u0415': 'Cyrillic_IE',
    '\u0424': 'Cyrillic_EF',
    '\u0413': 'Cyrillic_GHE',
    '\u0425': 'Cyrillic_HA',
    '\u0418': 'Cyrillic_I',
    '\u0419': 'Cyrillic_SHORTI',
    '\u041a': 'Cyrillic_KA',
    '\u041b': 'Cyrillic_EL',
    '\u041c': 'Cyrillic_EM',
    '\u041d': 'Cyrillic_EN',
    '\u041e': 'Cyrillic_O',
    '\u041f': 'Cyrillic_PE',
    '\u042f': 'Cyrillic_YA',
    '\u0420': 'Cyrillic_ER',
    '\u0421': 'Cyrillic_ES',
    '\u0422': 'Cyrillic_TE',
    '\u0423': 'Cyrillic_U',
    '\u0416': 'Cyrillic_ZHE',
    '\u0412': 'Cyrillic_VE',
    '\u042c': 'Cyrillic_SOFTSIGN',
    '\u042b': 'Cyrillic_YERU',
    '\u0417': 'Cyrillic_ZE',
    '\u0428': 'Cyrillic_SHA',
    '\u042d': 'Cyrillic_E',
    '\u0429': 'Cyrillic_SHCHA',
    '\u0427': 'Cyrillic_CHE',
    '\u042a': 'Cyrillic_HARDSIGN',
    '\u0386': 'Greek_ALPHAaccent',
    '\u0388': 'Greek_EPSILONaccent',
    '\u0389': 'Greek_ETAaccent',
    '\u038a': 'Greek_IOTAaccent',
    '\u03aa': 'Greek_IOTAdiaeresis',
    '\u038c': 'Greek_OMICRONaccent',
    '\u038e': 'Greek_UPSILONaccent',
    '\u03ab': 'Greek_UPSILONdieresis',
    '\u038f': 'Greek_OMEGAaccent',
    '\u0385': 'Greek_accentdieresis',
    '\u2015': 'Greek_horizbar',
    '\u03ac': 'Greek_alphaaccent',
    '\u03ad': 'Greek_epsilonaccent',
    '\u03ae': 'Greek_etaaccent',
    '\u03af': 'Greek_iotaaccent',
    '\u03ca': 'Greek_iotadieresis',
    '\u0390': 'Greek_iotaaccentdieresis',
    '\u03cc': 'Greek_omicronaccent',
    '\u03cd': 'Greek_upsilonaccent',
    '\u03cb': 'Greek_upsilondieresis',
    '\u03b0': 'Greek_upsilonaccentdieresis',
    '\u03ce': 'Greek_omegaaccent',
    '\u0391': 'Greek_ALPHA',
    '\u0392': 'Greek_BETA',
    '\u0393': 'Greek_GAMMA',
    '\u0394': 'Greek_DELTA',
    '\u0395': 'Greek_EPSILON',
    '\u0396': 'Greek_ZETA',
    '\u0397': 'Greek_ETA',
    '\u0398': 'Greek_THETA',
    '\u0399': 'Greek_IOTA',
    '\u039a': 'Greek_KAPPA',
    '\u039b': 'Greek_LAMBDA',
    '\u039b': 'Greek_LAMDA',
    '\u039c': 'Greek_MU',
    '\u039d': 'Greek_NU',
    '\u039e': 'Greek_XI',
    '\u039f': 'Greek_OMICRON',
    '\u03a0': 'Greek_PI',
    '\u03a1': 'Greek_RHO',
    '\u03a3': 'Greek_SIGMA',
    '\u03a4': 'Greek_TAU',
    '\u03a5': 'Greek_UPSILON',
    '\u03a6': 'Greek_PHI',
    '\u03a7': 'Greek_CHI',
    '\u03a8': 'Greek_PSI',
    '\u03a9': 'Greek_OMEGA',
    '\u03b1': 'Greek_alpha',
    '\u03b2': 'Greek_beta',
    '\u03b3': 'Greek_gamma',
    '\u03b4': 'Greek_delta',
    '\u03b5': 'Greek_epsilon',
    '\u03b6': 'Greek_zeta',
    '\u03b7': 'Greek_eta',
    '\u03b8': 'Greek_theta',
    '\u03b9': 'Greek_iota',
    '\u03ba': 'Greek_kappa',
    '\u03bb': 'Greek_lambda',
    '\u03bc': 'Greek_mu',
    '\u03bd': 'Greek_nu',
    '\u03be': 'Greek_xi',
    '\u03bf': 'Greek_omicron',
    '\u03c0': 'Greek_pi',
    '\u03c1': 'Greek_rho',
    '\u03c3': 'Greek_sigma',
    '\u03c2': 'Greek_finalsmallsigma',
    '\u03c4': 'Greek_tau',
    '\u03c5': 'Greek_upsilon',
    '\u03c6': 'Greek_phi',
    '\u03c7': 'Greek_chi',
    '\u03c8': 'Greek_psi',
    '\u03c9': 'Greek_omega',
    '\u23b7': 'leftradical',
    '\u2320': 'topintegral',
    '\u2321': 'botintegral',
    '\u23a1': 'topleftsqbracket',
    '\u23a3': 'botleftsqbracket',
    '\u23a4': 'toprightsqbracket',
    '\u23a6': 'botrightsqbracket',
    '\u239b': 'topleftparens',
    '\u239d': 'botleftparens',
    '\u239e': 'toprightparens',
    '\u23a0': 'botrightparens',
    '\u23a8': 'leftmiddlecurlybrace',
    '\u23ac': 'rightmiddlecurlybrace',
    '\u2264': 'lessthanequal',
    '\u2260': 'notequal',
    '\u2265': 'greaterthanequal',
    '\u222b': 'integral',
    '\u2234': 'therefore',
    '\u221d': 'variation',
    '\u221e': 'infinity',
    '\u2207': 'nabla',
    '\u223c': 'approximate',
    '\u2243': 'similarequal',
    '\u21d4': 'ifonlyif',
    '\u21d2': 'implies',
    '\u2261': 'identical',
    '\u221a': 'radical',
    '\u2282': 'includedin',
    '\u2283': 'includes',
    '\u2229': 'intersection',
    '\u222a': 'union',
    '\u2227': 'logicaland',
    '\u2228': 'logicalor',
    '\u2202': 'partialderivative',
    '\u0192': 'function',
    '\u2190': 'leftarrow',
    '\u2191': 'uparrow',
    '\u2192': 'rightarrow',
    '\u2193': 'downarrow',
    '\u25c6': 'soliddiamond',
    '\u2592': 'checkerboard',
    '\u2409': 'ht',
    '\u240c': 'ff',
    '\u240d': 'cr',
    '\u240a': 'lf',
    '\u2424': 'nl',
    '\u240b': 'vt',
    '\u2518': 'lowrightcorner',
    '\u2510': 'uprightcorner',
    '\u250c': 'upleftcorner',
    '\u2514': 'lowleftcorner',
    '\u253c': 'crossinglines',
    '\u23ba': 'horizlinescan1',
    '\u23bb': 'horizlinescan3',
    '\u2500': 'horizlinescan5',
    '\u23bc': 'horizlinescan7',
    '\u23bd': 'horizlinescan9',
    '\u251c': 'leftt',
    '\u2524': 'rightt',
    '\u2534': 'bott',
    '\u252c': 'topt',
    '\u2502': 'vertbar',
    '\u2003': 'emspace',
    '\u2002': 'enspace',
    '\u2004': 'em3space',
    '\u2005': 'em4space',
    '\u2007': 'digitspace',
    '\u2008': 'punctspace',
    '\u2009': 'thinspace',
    '\u200a': 'hairspace',
    '\u2014': 'emdash',
    '\u2013': 'endash',
    '\u2026': 'ellipsis',
    '\u2025': 'doubbaselinedot',
    '\u2153': 'onethird',
    '\u2154': 'twothirds',
    '\u2155': 'onefifth',
    '\u2156': 'twofifths',
    '\u2157': 'threefifths',
    '\u2158': 'fourfifths',
    '\u2159': 'onesixth',
    '\u215a': 'fivesixths',
    '\u2105': 'careof',
    '\u2012': 'figdash',
    '\u215b': 'oneeighth',
    '\u215c': 'threeeighths',
    '\u215d': 'fiveeighths',
    '\u215e': 'seveneighths',
    '\u2122': 'trademark',
    '\u2018': 'leftsinglequotemark',
    '\u2019': 'rightsinglequotemark',
    '\u201c': 'leftdoublequotemark',
    '\u201d': 'rightdoublequotemark',
    '\u211e': 'prescription',
    '\u2032': 'minutes',
    '\u2033': 'seconds',
    '\u271d': 'latincross',
    '\u2663': 'club',
    '\u2666': 'diamond',
    '\u2665': 'heart',
    '\u2720': 'maltesecross',
    '\u2020': 'dagger',
    '\u2021': 'doubledagger',
    '\u2713': 'checkmark',
    '\u2717': 'ballotcross',
    '\u266f': 'musicalsharp',
    '\u266d': 'musicalflat',
    '\u2642': 'malesymbol',
    '\u2640': 'femalesymbol',
    '\u260e': 'telephone',
    '\u2315': 'telephonerecorder',
    '\u2117': 'phonographcopyright',
    '\u2038': 'caret',
    '\u201a': 'singlelowquotemark',
    '\u201e': 'doublelowquotemark',
    '\u22a5': 'downtack',
    '\u230a': 'downstile',
    '\u2218': 'jot',
    '\u2395': 'quad',
    '\u22a4': 'uptack',
    '\u25cb': 'circle',
    '\u2308': 'upstile',
    '\u22a2': 'lefttack',
    '\u22a3': 'righttack',
    '\u2017': 'hebrew_doublelowline',
    '\u05d0': 'hebrew_aleph',
    '\u05d1': 'hebrew_bet',
    '\u05d1': 'hebrew_beth',
    '\u05d2': 'hebrew_gimel',
    '\u05d2': 'hebrew_gimmel',
    '\u05d3': 'hebrew_dalet',
    '\u05d3': 'hebrew_daleth',
    '\u05d4': 'hebrew_he',
    '\u05d5': 'hebrew_waw',
    '\u05d6': 'hebrew_zain',
    '\u05d6': 'hebrew_zayin',
    '\u05d7': 'hebrew_chet',
    '\u05d7': 'hebrew_het',
    '\u05d8': 'hebrew_tet',
    '\u05d8': 'hebrew_teth',
    '\u05d9': 'hebrew_yod',
    '\u05da': 'hebrew_finalkaph',
    '\u05db': 'hebrew_kaph',
    '\u05dc': 'hebrew_lamed',
    '\u05dd': 'hebrew_finalmem',
    '\u05de': 'hebrew_mem',
    '\u05df': 'hebrew_finalnun',
    '\u05e0': 'hebrew_nun',
    '\u05e1': 'hebrew_samech',
    '\u05e1': 'hebrew_samekh',
    '\u05e2': 'hebrew_ayin',
    '\u05e3': 'hebrew_finalpe',
    '\u05e4': 'hebrew_pe',
    '\u05e5': 'hebrew_finalzade',
    '\u05e5': 'hebrew_finalzadi',
    '\u05e6': 'hebrew_zade',
    '\u05e6': 'hebrew_zadi',
    '\u05e7': 'hebrew_kuf',
    '\u05e7': 'hebrew_qoph',
    '\u05e8': 'hebrew_resh',
    '\u05e9': 'hebrew_shin',
    '\u05ea': 'hebrew_taf',
    '\u05ea': 'hebrew_taw',
    '\u0e01': 'Thai_kokai',
    '\u0e02': 'Thai_khokhai',
    '\u0e03': 'Thai_khokhuat',
    '\u0e04': 'Thai_khokhwai',
    '\u0e05': 'Thai_khokhon',
    '\u0e06': 'Thai_khorakhang',
    '\u0e07': 'Thai_ngongu',
    '\u0e08': 'Thai_chochan',
    '\u0e09': 'Thai_choching',
    '\u0e0a': 'Thai_chochang',
    '\u0e0b': 'Thai_soso',
    '\u0e0c': 'Thai_chochoe',
    '\u0e0d': 'Thai_yoying',
    '\u0e0e': 'Thai_dochada',
    '\u0e0f': 'Thai_topatak',
    '\u0e10': 'Thai_thothan',
    '\u0e11': 'Thai_thonangmontho',
    '\u0e12': 'Thai_thophuthao',
    '\u0e13': 'Thai_nonen',
    '\u0e14': 'Thai_dodek',
    '\u0e15': 'Thai_totao',
    '\u0e16': 'Thai_thothung',
    '\u0e17': 'Thai_thothahan',
    '\u0e18': 'Thai_thothong',
    '\u0e19': 'Thai_nonu',
    '\u0e1a': 'Thai_bobaimai',
    '\u0e1b': 'Thai_popla',
    '\u0e1c': 'Thai_phophung',
    '\u0e1d': 'Thai_fofa',
    '\u0e1e': 'Thai_phophan',
    '\u0e1f': 'Thai_fofan',
    '\u0e20': 'Thai_phosamphao',
    '\u0e21': 'Thai_moma',
    '\u0e22': 'Thai_yoyak',
    '\u0e23': 'Thai_rorua',
    '\u0e24': 'Thai_ru',
    '\u0e25': 'Thai_loling',
    '\u0e26': 'Thai_lu',
    '\u0e27': 'Thai_wowaen',
    '\u0e28': 'Thai_sosala',
    '\u0e29': 'Thai_sorusi',
    '\u0e2a': 'Thai_sosua',
    '\u0e2b': 'Thai_hohip',
    '\u0e2c': 'Thai_lochula',
    '\u0e2d': 'Thai_oang',
    '\u0e2e': 'Thai_honokhuk',
    '\u0e2f': 'Thai_paiyannoi',
    '\u0e30': 'Thai_saraa',
    '\u0e31': 'Thai_maihanakat',
    '\u0e32': 'Thai_saraaa',
    '\u0e33': 'Thai_saraam',
    '\u0e34': 'Thai_sarai',
    '\u0e35': 'Thai_saraii',
    '\u0e36': 'Thai_saraue',
    '\u0e37': 'Thai_sarauee',
    '\u0e38': 'Thai_sarau',
    '\u0e39': 'Thai_sarauu',
    '\u0e3a': 'Thai_phinthu',
    '\u0e3f': 'Thai_baht',
    '\u0e40': 'Thai_sarae',
    '\u0e41': 'Thai_saraae',
    '\u0e42': 'Thai_sarao',
    '\u0e43': 'Thai_saraaimaimuan',
    '\u0e44': 'Thai_saraaimaimalai',
    '\u0e45': 'Thai_lakkhangyao',
    '\u0e46': 'Thai_maiyamok',
    '\u0e47': 'Thai_maitaikhu',
    '\u0e48': 'Thai_maiek',
    '\u0e49': 'Thai_maitho',
    '\u0e4a': 'Thai_maitri',
    '\u0e4b': 'Thai_maichattawa',
    '\u0e4c': 'Thai_thanthakhat',
    '\u0e4d': 'Thai_nikhahit',
    '\u0e50': 'Thai_leksun',
    '\u0e51': 'Thai_leknung',
    '\u0e52': 'Thai_leksong',
    '\u0e53': 'Thai_leksam',
    '\u0e54': 'Thai_leksi',
    '\u0e55': 'Thai_lekha',
    '\u0e56': 'Thai_lekhok',
    '\u0e57': 'Thai_lekchet',
    '\u0e58': 'Thai_lekpaet',
    '\u0e59': 'Thai_lekkao',
    '\u0152': 'OE',
    '\u0153': 'oe',
    '\u0178': 'Ydiaeresis',
    '\u20ac': 'EuroSign',
    '\u0491': 'Ukrainian_ghe_with_upturn',
    '\u0490': 'Ukrainian_GHE_WITH_UPTURN'}
