import pytest

from bondhon import bijoy_classic


def test_swap_kar_location():
    assert bijoy_classic.swap_kar_location('আমি') == 'আিম'


@pytest.mark.parametrize('given,expected', [
    ('১', '1'),
    ('২', '2'),
    ('৩', '3'),
    ('৪', '4'),
    ('৫', '5'),
    ('৬', '6'),
    ('৭', '7'),
    ('৮', '8'),
    ('৯', '9'),
    ('০', '0'),
])
def test_numbers(given, expected):
    assert bijoy_classic.from_unicode(given) == expected


@pytest.mark.parametrize('given,expected', [
    ('ং', 's'),
    ('ঃ', 't'),
    ('অ', 'A'),
    ('আ', 'Av'),
    ('ই', 'B'),
    ('ঈ', 'C'),
    ('উ', 'D'),
    ('ঊ', 'E'),
    ('ঋ', 'F'),
    ('এ', 'G'),
    ('ঐ', 'H'),
    ('ও', 'I'),
    ('ঔ', 'J'),
    ('ক', 'K'),
    ('খ', 'L'),
    ('গ', 'M'),
    ('ঘ', 'N'),
    ('ঙ', 'O'),
    ('চ', 'P'),
    ('ছ', 'Q'),
    ('জ', 'R'),
    ('ঝ', 'S'),
    ('ঞ', 'T'),
    ('ট', 'U'),
    ('ঠ', 'V'),
    ('ড', 'W'),
    ('ঢ', 'X'),
    ('ণ', 'Y'),
    ('ত', 'Z'),
    ('থ', '_'),
    ('দ', '`'),
    ('ধ', 'a'),
    ('ন', 'b'),
    ('প', 'c'),
    ('ফ', 'd'),
    ('ব', 'e'),
    ('ভ', 'f'),
    ('ম', 'g'),
    ('য', 'h'),
    ('র', 'i'),
    ('ল', 'j'),
    ('শ', 'k'),
    ('ষ', 'l'),
    ('স', 'm'),
    ('হ', 'n'),
    ('া', 'v'),
    ('ি', 'w'),
    ('ী', 'x')
])
def test_individual_chars(given, expected):
    assert bijoy_classic.from_unicode(given) == expected


@pytest.mark.parametrize('given,expected', [
    ('ক্ক', '°'),
    ('ক্ট', '±'),
    ('ক্ট্র', '±ª'),
    ('ক্ত', '³'),
    ('ক্ত্র', '³«'),
    ('ক্ব', 'K¡'),
    ('ক্ম', '´'),
    ('ক্য', 'K¨'),
    ('ক্র', 'µ'),
    ('ক্ল', 'K¬'),
    ('ক্ষ', '¶'),
    ('ক্ষ্ণ', '¶è'),
    ('ক্ষ্ব', '¶¡'),
    ('ক্ষ্ম', '²'),
    ('ক্ষ্ম্য', '²¨'),
    ('ক্ষ্য', '¶¨'),
    ('ক্স', '·'),
    ('খ্য', 'L¨'),
    ('খ্র', 'Lª'),
    ('গ্‌ণ', 'M&Y'),
    ('গ্ধ', '»'),
    ('গ্ধ্য', '»¨'),
    ('গ্ধ্র', '»ª'),
    ('গ্ন', 'Mœ'),
    ('গ্ন্য', 'Mœ¨'),
    ('গ্ব', 'M¦'),
    ('গ্ম', 'M¥'),
    ('গ্য', 'M¨'),
    ('গ্র', 'MÖ'),
    ('গ্র্য', 'M¨©'),
    ('গ্ল', 'M­'),
    ('ঘ্ন', 'Nœ'),
    ('ঘ্য', 'N¨'),
    ('ঘ্র', 'Nª'),
    ('ঙ্ক', '¼'),
    ('ঙ্‌ক্ত', 'O&³'),
    ('ঙ্ক্য', '¼¨'),
    ('ঙ্ক্ষ', '•¶'),
    ('ঙ্খ', '•L'),
    ('ঙ্গ', '½'),
    ('ঙ্গ্য', '½¨'),
    ('ঙ্ঘ', '•N'),
    ('ঙ্ঘ্য', '•N¨'),
    ('ঙ্ঘ্র', '•Nª'),
    ('ঙ্ম', '•g'),
    ('চ্চ', '”P'),
    ('চ্ছ', '”Q'),
    ('চ্ছ্ব', '”Q¡'),
    ('চ্ছ্র', '”Qª'),
    ('চ্ঞ', '”T'),
    ('চ্ব', '”¡'),
    ('চ্য', 'P¨'),
    ('জ্জ', '¾'),
    ('জ্জ্ব', '¾¡'),
    ('জ্ঝ', 'À'),
    ('জ্ঞ', 'Á'),
    ('জ্ব', 'R¡'),
    ('জ্য', 'R¨'),
    ('জ্র', 'Rª'),
    ('ঞ্চ', 'Â'),
    ('ঞ্ছ', 'Ã'),
    ('ঞ্জ', 'Ä'),
    ('ঞ্ঝ', 'Å'),
    ('ট্ট', 'Æ'),
    ('ট্ব', 'U¡'),
    ('ট্ম', 'U¥'),
    ('ট্য', 'U¨'),
    ('ট্র', 'Uª'),
    ('ড্ড', 'Ç'),
    ('ড্ব', 'W¡'),
    ('ড্য', 'W¨'),
    ('ড্র', 'Wª'),
    ('ড়্গ', 'ÿ'),
    ('ঢ্য', 'X¨'),
    ('ঢ্র', 'Xª'),
    ('ণ্ট', 'È'),
    ('ণ্ঠ', 'É'),
    ('ণ্ঠ্য', 'É¨'),
    ('ণ্ড', 'Ê'),
    ('ণ্ড্য', 'Ê¨'),
    ('ণ্ড্র', 'Êª'),
    ('ণ্ঢ', 'YX'),
    ('ণ্ণ', 'Yè'),
    ('ণ্ব', 'Y¡'),
    ('ণ্ম', 'Y¥'),
    ('ণ্য', 'Y¨'),
    ('ত্ত', 'Ë'),
    ('ত্ত্র', 'Ë«'),
    ('ত্ত্ব', 'Ë¡'),
    ('ত্ত্য', 'Ë¨'),
    ('ত্থ', 'Ì'),
    ('ত্ন', 'Zœ'),
    ('ত্ব', 'Z¡'),
    ('ত্ম', 'Í'),
    ('ত্ম্য', 'Í¨'),
    ('ত্য', 'Z¨'),
    ('ত্র', 'Î'),
    ('ত্র্য', 'Z¨©'),
    ('ৎল', 'rj'),
    ('ৎস', 'rm'),
    ('থ্ব', '_¡'),
    ('থ্য', '_¨'),
    ('থ্র', '_ª'),
    ('দ্গ', '˜M'),
    ('দ্ঘ', '™N'),
    ('দ্দ', 'Ï'),
    ('দ্দ্ব', 'Ï¡'),
    ('দ্ধ', '×'),
    ('দ্ব', 'Ø'),
    ('দ্ভ', '™¢'),
    ('দ্ভ্র', '™£'),
    ('দ্ম', 'Ù'),
    ('দ্য', '`¨'),
    ('দ্র', '`ª'),
    ('দ্র্য', '`¨©'),
    ('ধ্ন', 'aœ'),
    ('ধ্ব', 'aŸ'),
    ('ধ্ম', 'a¥'),
    ('ধ্য', 'a¨'),
    ('ধ্র', 'aª'),
    ('ন্ট', '›U'),
    ('ন্ট্র', '›Uª'),
    ('ন্ঠ', 'Ú'),
    ('ন্ড', 'Û'),
    ('ন্ড্র', 'Ûª'),
    ('ন্ত', 'š—'),
    ('ন্ত্ব', 'š—¡'),
    ('ন্ত্য', 'š—¨'),
    ('ন্ত্র', 'š¿'),
    ('ন্ত্র্য', 'š—¨©'),
    ('ন্থ', 'š’'),
    ('ন্থ্র', 'š’ª'),
    ('ন্দ', '›`'),
    ('ন্দ্য', '›`¨'),
    ('ন্দ্ব', '›Ø'),
    ('ন্দ্র', '›`ª'),
    ('ন্ধ', 'Ü'),
    ('ন্ধ্য', 'Ü¨'),
    ('ন্ধ্র', 'Üª'),
    ('ন্ন', 'bœ'),
    ('ন্ব', 'š^'),
    ('ন্ম', 'b¥'),
    ('ন্য', 'b¨'),
    ('প্ট', 'Þ'),
    ('প্ত', 'ß'),
    ('প্ন', 'cœ'),
    ('প্প', 'à'),
    ('প্য', 'c¨'),
    ('প্র', 'cÖ'),
    ('প্র্য', 'c¨©'),
    ('প্ল', 'c­'),
    ('প্স', 'á'),
    ('ফ্র', 'd«'),
    ('ফ্ল', 'd¬'),
    ('ব্জ', 'â'),
    ('ব্দ', 'ã'),
    ('ব্ধ', 'ä'),
    ('ব্ব', 'eŸ'),
    ('ব্য', 'e¨'),
    ('ব্র', 'eª'),
    ('ব্ল', 'e­'),
    ('ভ্ব', 'f¡'),
    ('ভ্য', 'f¨'),
    ('ভ্র', 'å'),
    ('ম্ন', 'æ'),
    ('ম্প', '¤c'),
    ('ম্প্র', '¤cÖ'),
    ('ম্ফ', 'ç'),
    ('ম্ব', '¤^'),
    ('ম্ব্র', '¤^ª'),
    ('ম্ভ', '¤¢'),
    ('ম্ভ্র', '¤£'),
    ('ম্ম', '¤§'),
    ('ম্য', 'g¨'),
    ('ম্র', 'gª'),
    ('ম্ল', '¤¬'),
    ('য্য', 'h¨'),
    ('র্ক', 'K©'),
    ('র্ক্য', 'K¨©'),
    ('র্গ্য', 'M¨©'),
    ('র্ঘ্য', 'N¨©'),
    ('র্চ্য', 'P¨©'),
    ('র্জ্য', 'R¨©'),
    ('র্ণ্য', 'Y¨©'),
    ('র্ত্য', 'Z¨©'),
    ('র্থ্য', '_¨©'),
    ('র্ব্য', 'e¨©'),
    ('র্ম্য', 'g¨©'),
    ('র্শ্য', 'k¨©'),
    ('র্ষ্য', 'l¨©'),
    ('র্হ্য', 'n¨©'),
    ('র্খ', 'L©'),
    ('র্গ', 'M©'),
    ('র্গ্র', 'MÖ©'),
    ('র্ঘ', 'N©'),
    ('র্চ', 'P©'),
    ('র্ছ', 'Q©'),
    ('র্জ', 'R©'),
    ('র্ঝ', 'S©'),
    ('র্ট', 'U©'),
    ('র্ড', 'W©'),
    ('র্ণ', 'Y©'),
    ('র্ত', 'Z©'),
    ('র্ত্র', 'Î©'),
    ('র্থ', '_©'),
    ('র্দ', '`©'),
    ('র্দ্ব', 'Ø©'),
    ('র্দ্র', '`ª©'),
    ('র্ধ', 'a©'),
    ('র্ধ্ব', 'aŸ©'),
    ('র্ন', 'b©'),
    ('র্প', 'c©'),
    ('র্ফ', 'd©'),
    ('র্ভ', 'f©'),
    ('র্ম', 'g©'),
    ('র্য', 'h©'),
    ('র্ল', 'j©'),
    ('র্শ', 'k©'),
    ('র্শ্ব', 'k¦©'),
    ('র্ষ', 'l©'),
    ('র্স', 'm©'),
    ('র্হ', 'n©'),
    ('র্ঢ্য', 'X¨©'),
    ('ল্ক', 'é'),
    ('ল্ক্য', 'é¨'),
    ('ল্গ', 'ê'),
    ('ল্ট', 'ë'),
    ('ল্ড', 'ì'),
    ('ল্প', 'í'),
    ('ল্‌ফ', 'j&d'),
    ('ল্ব', 'j¡'),
    ('ল্‌ভ', 'j&f'),
    ('ল্ম', 'j¥'),
    ('ল্য', 'j¨'),
    ('ল্ল', 'j­'),
    ('শ্চ', 'ð'),
    ('শ্ছ', 'ñ'),
    ('শ্ন', 'kœ'),
    ('শ্ব', 'k¦'),
    ('শ্ম', 'k¥'),
    ('শ্য', 'k¨'),
    ('শ্র', 'kª'),
    ('শ্ল', 'k­'),
    ('ষ্ক', '®‹'),
    ('ষ্ক্র', '®Œ'),
    ('ষ্ট', 'ó'),
    ('ষ্ট্য', 'ó¨'),
    ('ষ্ট্র', 'óª'),
    ('ষ্ঠ', 'ô'),
    ('ষ্ঠ্য', 'ô¨'),
    ('ষ্ণ', 'ò'),
    ('ষ্প', '®c'),
    ('ষ্প্র', '®cÖ'),
    ('ষ্ফ', 'õ'),
    ('ষ্ব', '®^'),
    ('ষ্ম', '®§'),
    ('ষ্য', 'l¨'),
    ('স্ক', '¯‹'),
    ('স্ক্র', '¯Œ'),
    ('স্খ', 'ö'),
    ('স্ট', '÷'),
    ('স্ট্র', '÷ª'),
    ('স্ত', '¯—'),
    ('স্ত্ব', '¯—¡'),
    ('স্ত্য', '¯—¨'),
    ('স্ত্র', '¯¿'),
    ('স্থ', '¯’'),
    ('স্থ্য', '¯’¨'),
    ('স্ন', 'ø'),
    ('স্প', '¯c'),
    ('স্প্র', '¯cÖ'),
    ('স্প্‌ল', '¯c&j'),
    ('স্ফ', 'ù'),
    ('স্ব', '¯^'),
    ('স্ম', '¯§'),
    ('স্য', 'm¨'),
    ('স্র', 'mª'),
    ('স্ল', '¯¬'),
    ('হ্ণ', 'nœ'),
    ('হ্ন', 'ý'),
    ('হ্ব', 'nŸ'),
    ('হ্ম', 'þ'),
    ('হ্য', 'n¨'),
    ('হ্র', 'nª'),
    ('হ্ল', 'n­'),
])
def test_conjugated(given, expected):
    assert bijoy_classic.from_unicode(given) == expected


@pytest.mark.parametrize('given,expected', [
    ('কোন', '†Kvb'),
    ('মৌনতা', '†gŠbZv'),
])
def test_surrounding_kars(given, expected):
    assert bijoy_classic.from_unicode(given) == expected


@pytest.mark.parametrize('given,bijoy', [
    ('কুরুক্ষেত্র', 'Kzi“‡¶Î'),
    ('কিংকর্তব্যবিমূঢ়', 'wKsKZ©e¨weg‚‚p'),
    ('অনিরুদ্ধ', 'Awbi“×'),
    ('বাংলাদেশ', 'evsjv‡`k'),
])
def test_words(given, bijoy):
    assert bijoy_classic.from_unicode(given) == bijoy


@pytest.mark.parametrize('given,bijoy', [
    ('নাকের নাসারন্ধ্র দিয়ে শ্বাসক্রিয়ার বায়ু প্রবেশ ও প্রস্থান করে।',
     'bv‡Ki bvmviÜª w`‡q k¦vmwµqvi evqz cÖ‡ek I cÖ¯’vb K‡i|'),

    ('আমাদের দেশে যে একবার বিবাহ করিয়াছে বিবাহ সম্বন্ধে তাহার মনে আর কোন উদ্বেগ থাকে না।',  # noqa: E501
     'Avgv‡`i †`‡k †h GKevi weevn Kwiqv‡Q weevn m¤^‡Ü Zvnvi g‡b Avi †Kvb D‡ØM _v‡K bv|'),  # noqa: E501
])
def test_sentences(given, bijoy):
    assert bijoy_classic.from_unicode(given) == bijoy
