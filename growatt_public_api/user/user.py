from enum import Enum
from typing import Optional, Union

import truststore

from pydantic_models.user import (
    UserRegistration,
    UserModification,
    UsernameAvailabilityCheck,
    UserList,
)

truststore.inject_into_ssl()
from growatt_public_api.session import GrowattApiSession  # noqa: E402


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


class User:
    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def register(
        self,
        username: str,
        password: str,
        email: str,
        country: Union[GrowattCountry, str],
        installer_code: Optional[str] = None,
        phone_number: Optional[str] = None,
        time_zone: Optional[str] = None,
        user_type: int = 1,
    ) -> UserRegistration:
        """
        1.1 User registration
        User registered interface
        https://www.showdoc.com.cn/262556420217021/1494056540800578

        Specific error codes:
        * 10001: System error
        * 10002: Username or password is empty
        * 10003: Username already exists
        * 10004: User mailbox is empty
        * 10006: User type is empty
        * 10008: Token is empty
        * 10014: Installer coding error

        Args:
            username (str): username
            password (str): Password
            email (str): Register Email
            country (str): User Country
            user_type (int): User Type (1 for end customers)
            installer_code (Optional[str]): Installer code
            phone_number (Optional[str]): User Phone
            time_zone (Optional[str]): User Time Zone

        Returns:
            UserRegistration
            {   'data': {'c_user_id': 54},
                'error_code': 0,
                'error_msg': None}
        """
        if isinstance(country, GrowattCountry):
            country = country.value

        response = self.session.post(
            endpoint="user/user_register",
            data={
                "user_name": username,
                "user_password": password,
                "user_email": email,
                "user_type": user_type,
                "user_country": country,
                "agent_code": installer_code,
                "user_tel": phone_number,
                "time": time_zone,
            },
        )

        return UserRegistration.model_validate(response)

    def modify(
        self,
        user_id: int,
        phone_number: str,
        installer_code: Optional[str] = None,
    ) -> UserModification:
        """
        1.2 Modify user information
        Interface to modify user information
        https://www.showdoc.com.cn/262556420217021/1494057478651903

        Specific error codes:
        * 10001: System error
        * 10002: User ID is empty
        * 10003: User does not exist
        * 10004: User ID does not match token
        * 10014：Installer coding error

        Args:
            user_id (int): User ID ("c_user_id" as returned in register())
            phone_number (str): Phone number
            installer_code (Optional[str]): Installer code

        Returns:
            UserModification
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="user/modify",
            data={
                "c_user_id": user_id,
                "mobile": phone_number,
                "agent_code": installer_code,
            },
        )

        return UserModification.model_validate(response)

    def check_username(
        self,
        username: str,
    ) -> UsernameAvailabilityCheck:
        """
        1.3 Verify that the username is duplicated
        Verify that the username is duplicated
        https://www.showdoc.com.cn/262556420217021/1494057808771611

        Specific error codes:
        * 10001: Server exception
        * 10002: Username is empty
        * 10003: Username already exists

        Args:
            username (str): username

        Returns:
            UserModification
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="user/check_user",
            data={
                "user_name": username,
            },
        )
        if response["error_code"] == 10003:
            response["username_available"] = False
        elif response["error_code"] == 0:
            response["username_available"] = True

        return UsernameAvailabilityCheck.model_validate(response)

    def list(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> UserList:
        """
        1.4 Get a list of end users under the merchant
        Get the interface of the end user list under the merchant
        https://www.showdoc.com.cn/262556420217021/1494058357406324

        Rate limit(s):
        * Get the frequency once every 5 minutes
        * This interface is only allowed to call 10 times a day

        Specific error codes:
        * 10001: System error

        Args:
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            UserList
            {   'data': {   'c_user': [   {   'c_user_email': 'foobar@example.com',
                                              'c_user_id': 1,
                                              'c_user_name': 'admin',
                                              'c_user_regtime': datetime.datetime(2018, 2, 4, 9, 46, 50),
                                              'c_user_tel': None}],
                            'count': 2},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="user/c_user_list",
            params={
                "page": page,
                "perpage": limit,
            },
        )

        return UserList.model_validate(response)
