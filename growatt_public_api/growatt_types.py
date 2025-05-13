from enum import Enum
from typing import Optional, Self


class DeviceType(Enum):
    GROBOOST = "groboost"
    HPS = "hps"
    INVERTER = "inv"
    MAX = "max"
    MIN = "min"
    NOAH = "noah"
    PBD = "pbd"
    PCS = "pcs"
    SPA = "spa"
    SPH = "sph"
    SPHS = "sph-s"
    STORAGE = "storage"
    WIT = "wit"
    OTHER = "other"

    @classmethod
    def from_device_type_info(cls, device_type: int) -> Optional[Self]:
        """
        Args:
            device_type (int): The device type as returned by device.type_info()
        Returns:
            DeviceType: The mapped enum value.
        """
        mapper = {
            0: cls.OTHER,  # (datalogger / unknown / not existing ...)
            16: cls.INVERTER,
            17: cls.SPH,
            18: cls.MAX,
            19: cls.SPA,
            22: cls.MIN,
            81: cls.PCS,
            82: cls.HPS,
            83: cls.PBD,
            96: cls.STORAGE,
            218: cls.WIT,
            260: cls.SPHS,
        }
        return mapper.get(device_type)

    @classmethod
    def from_device_list(cls, device_type: str) -> Optional[Self]:
        """
        Args:
            device_type (str): The device type as returned by device.list()
        Returns:
            DeviceType: The mapped enum value.
        """
        mapper = {
            "inv": cls.INVERTER,
            "storage": cls.STORAGE,
            "max": cls.MAX,
            "sph": cls.SPH,
            "spa": cls.SPA,
            "min": cls.MIN,
            "wit": cls.WIT,
            "sph-s": cls.SPHS,
            "noah": cls.NOAH,
        }
        return mapper.get(device_type)

    @classmethod
    def from_plant_list_devices(cls, device_type: int) -> Optional[Self]:
        """
        Args:
            device_type (int): The device type as returned by plant.list_devices()
        Returns:
            DeviceType: The mapped enum value.
        """
        mapper = {
            1: cls.INVERTER,
            2: cls.STORAGE,
            3: cls.OTHER,  # (datalogger, smart meter, environmental sensor, ...)
            4: cls.MAX,
            5: cls.SPH,
            6: cls.SPA,
            7: cls.MIN,
            8: cls.PCS,
            9: cls.HPS,
            10: cls.PBD,
            11: cls.GROBOOST,
        }
        return mapper.get(device_type)


class PlantType(Enum):
    """
    to be used for plant.add()
    """

    RESIDENTIAL = 0
    COMMERCIAL = 1
    GROUND_MOUNTED = 2


class GrowattCountry(Enum):
    """
    use for user.register()
    see https://www.showdoc.com.cn/dfsfdf/9187729846853701
    """

    OTHER = "Other"
    AFGHANISTAN = "Afghanistan"
    ALAND_ISLANDS = "Aland Islands"
    ALBANIA = "Albania"
    ALGERIA = "Algeria"
    AMERICAN_SAMOA = "American Samoa"
    ANDORRA = "Andorra"
    ANGOLA = "Angola"
    ANGUILLA = "Anguilla"
    ANTARCTICA = "Antarctica"
    ANTIGUA_AND_BARBUDA = "Antigua And Barbuda"
    ARGENTINA = "Argentina"
    ARMENIA = "Armenia"
    ARUBA = "Aruba"
    AUSTRALIA = "Australia"
    AUSTRIA = "Austria"
    AZERBAIJAN = "Azerbaijan"
    BAHAMAS = "Bahamas"
    BAHRAIN = "Bahrain"
    BANGLADESH = "Bangladesh"
    BARBADOS = "Barbados"
    BELARUS = "Belarus"
    BELGIUM = "Belgium"
    BELIZE = "Belize"
    BENIN = "Benin"
    BERMUDA = "Bermuda"
    BHUTAN = "Bhutan"
    BOLIVIA = "Bolivia"
    BONAIRE = "Bonaire"
    BOSNIA_AND_HERZEGOVINA = "Bosnia And Herzegovina"
    BOTSWANA = "Botswana"
    BOUVET_ISLAND = "Bouvet Island"
    BRAZIL = "Brazil"
    BRITISH_INDIAN_OCEAN_TERRITORY = "British Indian Ocean Territory"
    BRITISHVIRGIN_ISLANDS = "The British Virgin Islands"
    BRUNEI = "Brunei"
    BRUNEI_DARUSSALAM = "Brunei Darussalam"
    BULGARIA = "Bulgaria"
    BURKINA_FASO = "Burkina Faso"
    BURUNDI = "Burundi"
    CABO_VERDE = "Cape Verde"
    CAMBODIA = "Cambodia"
    CAMEROON = "Cameroon"
    CANADA = "Canada"
    CAYMAN_ISLANDS = "Cayman Islands"
    CENTRAL_AFRICAN_REPUBLIC = "Central African Republic"
    CHAD = "Chad"
    CHILE = "Chile"
    CHINA = "China"
    CHRISTMAS_ISLAND = "Christmas Island"
    COCOS_ISLANDS = "Cocos( Keeling) Islands"
    COLOMBIA = "Columbia"
    COMOROS = "Comoros"
    CONGO = "Congo Democratic Republic"
    COOK_ISLANDS = "Cook Islands"
    COSTA_RICA = "Costa Rica"
    COTE_DIVOIRE = "Ivory Coast"
    CROATIA = "Croatia"
    CUBA = "Cuba"
    CURACAO = "Curacao"
    CYPRUS = "Cyprus"
    CZECHIA = "Czech Republic"
    DENMARK = "Denmark"
    DJIBOUTI = "Djibouti"
    DOMINICA = "Dominica"
    DOMINICAN_REPUBLIC = "Dominican Republic"
    DUTCH_CARIBBEAN = "Dutch Caribbean"
    ECUADOR = "Ecuador"
    EGYPT = "Egypt"
    EL_SALVADOR = "Salvador"
    EQUATORIAL_GUINEA = "Equatorial Guinea"
    ERITREA = "Eritrea"
    ESTONIA = "Estonia"
    ESWATINI = "Swaziland"
    ETHIOPIA = "Ethiopia"
    FALKLAND_ISLANDS = "Malvinas Islands( Falkland)"
    FAROE_ISLANDS = "Faroe Islands"
    FIJI = "Fiji"
    FINLAND = "Finland"
    FRANCE = "France"
    FRENCH_GUIANA = "French Guiana"
    FRENCH_POLYNESIA = "French Polynesia"
    FRENCH_SOUTHERN_TERRITORIES = "French Southern Territories"
    GABON = "Gabon"
    GAMBIA = "Gambia"
    GEORGIA = "Georgia"
    GERMANY = "Germany"
    GHANA = "Ghana"
    GIBRALTAR = "Gibraltar"
    GREECE = "Greece"
    GREENLAND = "Greenland"
    GRENADA = "Grenada"
    GUADELOUPE = "Guadeloupe"
    GUAM = "Guam"
    GUATEMALA = "Guatemala"
    GUERNSEY = "Guernsey"
    GUINEA = "Guinea"
    GUINEA_BISSAU = "Guinea Bissau"
    GUYANA = "Guyana"
    HAITI = "Haiti"
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = "Heard Island& Mc Donald Island"
    HONDURAS = "Honduras"
    HONG_KONG = "HongKong(China)"
    HUNGARY = "Hungary"
    ICELAND = "Iceland"
    INDIA = "India"
    INDONESIA = "Indonesia"
    IRAN = " Iran"
    IRAQ = "Iraq"
    IRELAND = "Ireland"
    ISLE_OF_MAN = "Isle Of Man"
    ISRAEL = "Israel"
    ITALY = "Italy"
    JAMAICA = "Jamaica"
    JAN_MAYEN = "Svalbard And Jan Mayen"
    JAPAN = "Japan"
    JERSEY = "Jersey"
    JORDAN = "Jordan"
    KAZAKHSTAN = "Kazakhstan"
    KENYA = "Kenya"
    KIRIBATI = "Kiribati"
    KUWAIT = "Kuwait"
    KYRGYZSTAN = "Kyrgyzstan"
    LAOS = "Laos"
    LATVIA = "Latvia"
    LEBANON = "Lebanon"
    LESOTHO = "Lesotho"
    LIBERIA = "Liberia"
    LIBYA = "Libya"
    LIECHTENSTEIN = "Liechtenstein"
    LITHUANIA = "Lithuania"
    LUXEMBOURG = "Luxembourg"
    MACAO = "Macau(China)"
    MADAGASCAR = "Madagascar"
    MALAWI = "Malawi"
    MALAYSIA = "Malaysia"
    MALDIVES = "Maldives"
    MALI = "Mali"
    MALTA = "Malta"
    MARSHALL_ISLANDS = "Marshall Islands"
    MARTINIQUE = "Martinique"
    MAURITANIA = "Mauritania"
    MAURITIUS = "Mauritius"
    MAYOTTE = "Mayotte"
    MEXICO = "Mexico"
    MICRONESIA = "Federated States Of Micronesia"
    MOLDOVA = "Moldova"
    MONACO = "Monaco"
    MONGOLIA = "Mongolia"
    MONTENEGRO = "Montenegro"
    MONTSERRAT = "Montserrat"
    MOROCCO = "Morocco"
    MOZAMBIQUE = "Mozambique"
    MYANMAR = "Myanmar"
    NAMIBIA = "Namibia"
    NAURU = "Nauru"
    NEPAL = "Nepal"
    NETHERLANDS = "Netherlands"
    NEW_CALEDONIA = "New Caledonia"
    NEW_ZEALAND = "New Zealand"
    NICARAGUA = "Nicaragua"
    NIGER = "Niger"
    NIGERIA = "Nigeria"
    NIUE = "Niue"
    NORFOLK_ISLAND = "Norfolk Island"
    NORTH_KOREA = "North Korea"
    NORTH_MACEDONIA = "Macedonia"
    NORTHERN_MARIANA_ISLANDS = "Northern Mariana Islands"
    NORWAY = "Norway"
    OMAN = "Oman"
    PAKISTAN = "Pakistan"
    PALAU = "Palau"
    PALESTINE = "Palestine"
    PANAMA = "Panama"
    PAPUA_NEW_GUINEA = "Papua New Guinea"
    PARAGUAY = "Paraguay"
    PERU = "Peru"
    PHILIPPINES = "Philippines"
    PITCAIRN = "Pitcairn Islands"
    POLAND = "Poland"
    PORTUGAL = "Portugal"
    PUERTO_RICO = "Puerto Rico"
    QATAR = "Qatar"
    REUNION = "Reunion"
    ROMANIA = "Romania"
    RUSSIAN_FEDERATION = "Russia"
    RWANDA = "Rwanda"
    SABA = "Bonaire"
    SAINT_BARTHELEMY = "Saint Barthelemy"
    SAINT_HELENA = "Saint Helena"
    SAINT_KITTS_AND_NEVIS = "Saint Kitts And Nevis"
    SAINT_LUCIA = "Saint Lucia"
    SAINT_MARTIN = "French Saint Martin"
    SAINT_PIERRE_AND_MIQUELON = "Saint Pierre And Miquelon"
    SAINT_VINCENT_AND_THE_GRENADINES = "Saint Vincent Andthe Grenadines"
    SAMOA = "Samoa"
    SAN_MARINO = "San Marino"
    SAO_TOME_AND_PRINCIPE = "Sao Tome And Principe"
    SAUDI_ARABIA = "Saudi Arabia"
    SENEGAL = "Senegal"
    SERBIA = "Serbia"
    SEYCHELLES = "Seychelles"
    SIERRA_LEONE = "Sierra Leone"
    SINGAPORE = "Singapore"
    SINT_EUSTATIUS = "Bonaire"
    SINT_MAARTEN = "Sint Maarten"
    SLOVAKIA = "Slovakia"
    SLOVENIA = "Slovenia"
    SOLOMON_ISLANDS = "Solomon Islands"
    SOMALIA = "Somalia"
    SOUTH_AFRICA = "South Africa"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "South Georgia And The South Sand"
    SOUTH_KOREA = "South Korea"
    SOUTH_SUDAN = "South Sudan"
    SPAIN = "Spain"
    SRI_LANKA = "Sri Lanka"
    SUDAN = "Sudan"
    SURINAME = "Suriname"
    SVALBARD = "Svalbard And Jan Mayen"
    SWEDEN = "Sweden"
    SWITZERLAND = "Switzerland"
    SYRIA = "Syria"
    TAIWAN = "Taiwan(China)"
    TAJIKISTAN = "Tajikistan"
    TANZANIA = "Tanzania"
    THAILAND = "Thailand"
    TIMOR_LESTE = "East Timor"
    TOGO = "Togo"
    TOKELAU = "Tokelau"
    TONGA = "Tonga"
    TRINIDAD_AND_TOBAGO = "Trinidad And Tobago"
    TUNISIA = "Tunisia"
    TURKEY = "Turkey"
    TURKMENISTAN = "Turkmenistan"
    TURKS_AND_CAICOS_ISLANDS = "Turks And Caicos Islands"
    TUVALU = "Tuvalu"
    UGANDA = "Uganda"
    UKRAINE = "Ukraine"
    UNITED_ARAB_EMIRATES = "United Arab Emirates"
    UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND = "United Kingdom"
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = "U S Minor Outlying Islands"
    UNITED_STATES_OF_AMERICA = "United States"
    UNITED_STATES_VIRGIN_ISLANDS = "United States Virgin Islands"
    URUGUAY = "Uruguay"
    UZBEKISTAN = "Uzbekistan"
    VANUATU = "Vanuatu"
    VATICAN = "Vatican"
    VENEZUELA = "Venezuela"
    VIETNAM = "Vietnam"
    WALLIS_AND_FUTUNA = "Wallis And Futuna"
    WESTERN_SAHARA = "Western Sahara"
    YEMEN = "Yemen"
    ZAMBIA = "Zambia"
    ZIMBABWE = "Zimbabwe"
