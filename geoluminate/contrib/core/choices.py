from django.db import models
from django.utils.translation import gettext_lazy as _


class DateTimeChoices(models.TextChoices):
    """A class for storing choices for DateTimeField models. To use with fuzzy dates."""

    YEAR = "%Y", _("Year")
    MONTH = "%M", _("Month")
    DAY = "%d", _("Day")
    HOUR = "%h", _("Hour")
    MINUTE = "%m", _("Minute")
    SECOND = "%s", _("Second")


class ProjectStatus(models.IntegerChoices):
    CONCEPT = 0, _("Concept")
    PLANNING = 1, _("Planning")
    # SEARCHING_FOR_FUNDING = 3, _("Searching for funding")
    # SEARCHING_FOR_COLLABORATORS = 4, _("Searching for collaborators")
    IN_PROGRESS = 2, _("In progress")
    COMPLETE = 3, _("Complete")


class ProjectTags(models.TextChoices):
    """A class for storing choices for tags on the Project model."""

    COLLABORATORS_WANTED = "Collaborators wanted", _("Looking for collaborators")
    FUNDING_REQUIRED = "Funding required", _("Looking for funding")
    HAS_FUNDING = "Has funding", _("Has funding")
    POSITIONS_OPEN = "Positions open", _("Positions open")
    EQUIPMENT_REQUIRED = "Equipment required", _("Looking for tools")


class DataCiteDescriptionTypes(models.TextChoices):
    """A class for storing choices for DescriptionType on the Description model. Based on the
    Datacite DescriptionType vocabulary."""

    ABSTRACT = "Abstract", _("Abstract")
    METHODS = "Methods", _("Methods")
    SERIES_INFORMATION = "SeriesInformation", _("Series Information")
    TABLE_OF_CONTENTS = "TableOfContents", _("Table of Contents")
    TECHNICAL_INFO = "TechnicalInfo", _("Technical Information")
    OTHER = "Other", _("Other")


DiscoveryTags = [
    (
        _("Looking for"),
        [
            ("collaborators_wanted", _("Collaborators")),
            ("funding_wanted", _("Funding")),
            ("equipment_wanted", _("Equipment")),
        ],
    ),
    (
        _("Has"),
        [
            ("has_funding", _("Funding")),
            ("has_open_positions", _("Open Positions")),
            ("has_equipment", _("Equipment")),
        ],
    ),
]


iso_639_1_languages = [
    (
        "Common",
        [
            ("en", _("English")),
            ("es", _("Spanish")),
            ("fr", _("French")),
            ("de", _("German")),
            ("it", _("Italian")),
            ("pt", _("Portuguese")),
            ("ru", _("Russian")),
            ("zh", _("Chinese")),
            ("ja", _("Japanese")),
            ("ar", _("Arabic")),
        ],
    ),
    (
        "Other",
        [
            ("aa", _("Afar")),
            ("ab", _("Abkhazian")),
            ("ae", _("Avestan")),
            ("af", _("Afrikaans")),
            ("ak", _("Akan")),
            ("am", _("Amharic")),
            ("an", _("Aragonese")),
            # ("ar", _("Arabic")),
            ("as", _("Assamese")),
            ("av", _("Avaric")),
            ("ay", _("Aymara")),
            ("az", _("Azerbaijani")),
            ("ba", _("Bashkir")),
            ("be", _("Belarusian")),
            ("bg", _("Bulgarian")),
            ("bh", _("Bihari")),
            ("bi", _("Bislama")),
            ("bm", _("Bambara")),
            ("bn", _("Bengali")),
            ("bo", _("Tibetan")),
            ("br", _("Breton")),
            ("bs", _("Bosnian")),
            ("ca", _("Catalan")),
            ("ce", _("Chechen")),
            ("ch", _("Chamorro")),
            ("co", _("Corsican")),
            ("cr", _("Cree")),
            ("cs", _("Czech")),
            ("cu", _("Church Slavic")),
            ("cv", _("Chuvash")),
            ("cy", _("Welsh")),
            ("da", _("Danish")),
            # ("de", _("German")),
            ("dv", _("Divehi")),
            ("dz", _("Dzongkha")),
            ("ee", _("Ewe")),
            ("el", _("Greek")),
            # ("en", _("English")),
            ("eo", _("Esperanto")),
            # ("es", _("Spanish")),
            ("et", _("Estonian")),
            ("eu", _("Basque")),
            ("fa", _("Persian")),
            ("ff", _("Fulah")),
            ("fi", _("Finnish")),
            ("fj", _("Fijian")),
            ("fo", _("Faroese")),
            # ("fr", _("French")),
            ("fy", _("Western Frisian")),
            ("ga", _("Irish")),
            ("gd", _("Scottish Gaelic")),
            ("gl", _("Galician")),
            ("gn", _("Guarani")),
            ("gu", _("Gujarati")),
            ("gv", _("Manx")),
            ("ha", _("Hausa")),
            ("he", _("Hebrew")),
            ("hi", _("Hindi")),
            ("ho", _("Hiri Motu")),
            ("hr", _("Croatian")),
            ("ht", _("Haitian")),
            ("hu", _("Hungarian")),
            ("hy", _("Armenian")),
            ("hz", _("Herero")),
            ("ia", _("Interlingua")),
            ("id", _("Indonesian")),
            ("ie", _("Interlingue")),
            ("ig", _("Igbo")),
            ("ii", _("Sichuan Yi")),
            ("ik", _("Inupiaq")),
            ("io", _("Ido")),
            ("is", _("Icelandic")),
            # ("it", _("Italian")),
            ("iu", _("Inuktitut")),
            # ("ja", _("Japanese")),
            ("jv", _("Javanese")),
            ("ka", _("Georgian")),
            ("kg", _("Kongo")),
            ("ki", _("Kikuyu")),
            ("kj", _("Kwanyama")),
            ("kk", _("Kazakh")),
            ("kl", _("Kalaallisut")),
            ("km", _("Central Khmer")),
            ("kn", _("Kannada")),
            ("ko", _("Korean")),
            ("kr", _("Kanuri")),
            ("ks", _("Kashmiri")),
            ("ku", _("Kurdish")),
            ("kv", _("Komi")),
            ("kw", _("Cornish")),
            ("ky", _("Kirghiz")),
            ("la", _("Latin")),
            ("lb", _("Luxembourgish")),
            ("lg", _("Ganda")),
            ("li", _("Limburgan")),
            ("ln", _("Lingala")),
            ("lo", _("Lao")),
            ("lt", _("Lithuanian")),
            ("lu", _("Luba-Katanga")),
            ("lv", _("Latvian")),
            ("mg", _("Malagasy")),
            ("mh", _("Marshallese")),
            ("mi", _("Maori")),
            ("mk", _("Macedonian")),
            ("ml", _("Malayalam")),
            ("mn", _("Mongolian")),
            ("mr", _("Marathi")),
            ("ms", _("Malay")),
            ("mt", _("Maltese")),
            ("my", _("Burmese")),
            ("na", _("Nauru")),
            ("nb", _("Norwegian Bokmål")),
            ("nd", _("North Ndebele")),
            ("ne", _("Nepali")),
            ("ng", _("Ndonga")),
            ("nl", _("Dutch")),
            ("nn", _("Norwegian Nynorsk")),
            ("no", _("Norwegian")),
            ("nr", _("South Ndebele")),
            ("nv", _("Navajo")),
            ("ny", _("Chichewa")),
            ("oc", _("Occitan")),
            ("oj", _("Ojibwa")),
            ("om", _("Oromo")),
            ("or", _("Oriya")),
            ("os", _("Ossetian")),
            ("pa", _("Panjabi")),
            ("pi", _("Pali")),
            ("pl", _("Polish")),
            ("ps", _("Pashto")),
            # ("pt", _("Portuguese")),
            ("qu", _("Quechua")),
            ("rm", _("Romansh")),
            ("rn", _("Rundi")),
            ("ro", _("Romanian")),
            # ("ru", _("Russian")),
            ("rw", _("Kinyarwanda")),
            ("sa", _("Sanskrit")),
            ("sc", _("Sardinian")),
            ("sd", _("Sindhi")),
            ("se", _("Northern Sami")),
            ("sg", _("Sango")),
            ("si", _("Sinhala")),
            ("sk", _("Slovak")),
            ("sl", _("Slovenian")),
            ("sm", _("Samoan")),
            ("sn", _("Shona")),
            ("so", _("Somali")),
            ("sq", _("Albanian")),
            ("sr", _("Serbian")),
            ("ss", _("Swati")),
            ("st", _("Southern So")),
            ("su", _("Sundanese")),
            ("sv", _("Swedish")),
            ("sw", _("Swahili")),
            ("ta", _("Tamil")),
            ("te", _("Telugu")),
            ("tg", _("Tajik")),
            ("th", _("Thai")),
            ("ti", _("Tigrinya")),
            ("tk", _("Turkmen")),
            ("tl", _("Tagalog")),
            ("tn", _("Tswana")),
            ("to", _("Tonga")),
            ("tr", _("Turkish")),
            ("ts", _("Tsonga")),
            ("tt", _("Tatar")),
            ("tw", _("Twi")),
            ("ty", _("Tahitian")),
            ("ug", _("Uighur")),
            ("uk", _("Ukrainian")),
            ("ur", _("Urdu")),
            ("uz", _("Uzbek")),
            ("ve", _("Venda")),
            ("vi", _("Vietnamese")),
            ("vo", _("Volapük")),
            ("wa", _("Walloon")),
            ("wo", _("Wolof")),
            ("xh", _("Xhosa")),
            ("yi", _("Yiddish")),
            ("yo", _("Yoruba")),
            ("za", _("Zhuang")),
            # ("zh", _("Chinese")),
            ("zu", _("Zulu")),
        ],
    ),
]
