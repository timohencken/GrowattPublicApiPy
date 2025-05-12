from typing import Optional

import truststore

truststore.inject_into_ssl()
from growatt_public_api.session import GrowattApiSession  # noqa: E402


class User:
    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def register(
        self,
        username: str,
        password: str,
        email: str,
        country: str,
        user_type: int = 1,
        installer_code: Optional[str] = None,
        phone_number: Optional[int] = None,
        time_zone: Optional[str] = None,
    ):
        """
        Args:
            username (str): username
            password (str): Password
            email (str): Register Email
            country (str): User Country
            user_type (int): User Type (1 for end customers)
            installer_code (Optional[str]): Installer code
            phone_number (Optional[int]): User Phone
            time_zone (Optional[str]): User Time Zone
        Returns:
            Dict[str, Any]: Response
            {
                "data": {
                    "c_user_id": int,   # End User ID
                },
                "error_code": int,      # 0: Normal return
                                        # 10001: System error
                                        # 10002: Username or password is empty
                                        # 10003: Username already exists
                                        # 10004: User mailbox is empty
                                        # 10006: User type is empty
                                        # 10008: Token is empty
                                        # 10014：Installer coding error
                "error_msg": str,       # Error Message Prompt
            }

        Country list:
            see https://www.showdoc.com.cn/dfsfdf/9187729846853701
            Other
            中国   # == China
            China
            Taiwan(China)
            Singapore
            Thailand
            Indonesia
            Malaysia
            Vietnam
            Japan
            Russia
            United States
            Afghanistan
            Albania
            Algeria
            American Samoa
            Andorra
            Angola
            Anguilla
            Antigua And Barbuda
            Argentina
            Armenia
            Aruba
            Australia
            Austria
            Azerbaijan
            Bahamas
            Bahrain
            Bangladesh
            Barbados
            Belarus
            Belgium
            Belize
            Benin
            Bermuda
            Bhutan
            Bolivia
            Bosnia And Herzegovina
            Botswana
            Brazil
            The British Virgin Islands
            Brunei Darussalam
            Bulgaria
            Burkina Faso
            Burundi
            Cambodia
            Cameroon
            Canada
            Cape Verde
            Cayman Islands
            Central African Republic
            Chad
            Chile
            Columbia
            Comoros
            Republic Of The Congo
            Congo Democratic Republic
            Cook Islands
            Costa Rica
            Croatia
            Cuba
            Cyprus
            Czech Republic
            Denmark
            Djibouti
            Dominica
            Dominican Republic
            East Timor
            Ecuador
            Egypt
            Salvador
            Equatorial Guinea
            Eritrea
            Estonia
            Ethiopia
            Malvinas Islands( Falkland)
            Faroe Islands
            Fiji
            Finland
            France
            French Guiana
            French Polynesia
            Gabon
            Gambia
            Georgia
            Germany
            Ghana
            Gibraltar
            Greece
            Greenland
            Grenada
            Guadeloupe
            Guam
            Guatemala
            Guinea
            Guinea Bissau
            Guyana
            Haiti
            Honduras
            HongKong(China)
            Hungary
            Iceland
            India
            M I D E for S I
            Iraq
            Ireland
            Isle Of Man
            Israel
            Italy
            Jamaica
            Jordan
            Kazakhstan
            Kenya
            Kiribati
            Kuwait
            Kyrgyzstan
            Laos
            Latvia
            Lebanon
            Lesotho
            Liberia
            Libya
            Liechtenstein
            Lithuania
            Luxembourg
            Macau(China)
            Macedonia
            Madagascar
            Malawi
            Maldives
            Mali
            Malta
            Marshall Islands
            Martinique
            Mauritania
            Mauritius
            Mexico
            Federated States Of Micronesia
            Moldova
            Monaco
            Mongolia
            Montenegro
            Montserrat
            Morocco
            Mozambique
            Myanmar
            Namibia
            Nauru
            Nepal
            Netherlands
            New Caledonia
            New Zealand
            Nicaragua
            Niger
            Nigeria
            Niue
            Norfolk Island
            North Korea
            Northern Mariana Islands
            Norway
            Oman
            Pakistan
            Palau
            Palestine
            Panama
            Papua New Guinea
            Paraguay
            Peru
            Philippines
            Pitcairn Islands
            Poland
            Portugal
            Puerto Rico
            Qatar
            Romania
            Rwanda
            Saint Helena
            Saint Kitts And Nevis
            Saint Lucia
            Saint Pierre And Miquelon
            Saint Vincent Andthe Grenadines
            Samoa
            San Marino
            Saudi Arabia
            Senegal
            Serbia
            Seychelles
            Sierra Leone
            Sint Maarten
            Slovakia
            Slovenia
            Solomon Islands
            Somalia
            South Africa
            South Korea
            South Sudan
            Spain
            Sri Lanka
            Sudan
            Suriname
            Svalbard And Jan Mayen
            Swaziland
            Sweden
            Switzerland
            Syria
            Tajikistan
            Tanzania
            Togo
            Tokelau
            Tonga
            Trinidad And Tobago
            Tunisia
            Turkey
            Turkmenistan
            Turks And Caicos Islands
            Tuvalu
            United States Virgin Islands
            Uganda
            Ukraine
            United Arab Emirates
            United Kingdom
            Uruguay
            Uzbekistan
            Vanuatu
            Venezuela
            Wallis And Futuna
            Yemen
            Zambia
            Zimbabwe
            Ivory Coast
            Dutch Caribbean
            Western Sahara
            Christmas Island
            Brunei
            Cocos( Keeling) Islands
            Saint Barthelemy
            Curacao
            French Saint Martin
            U S Minor Outlying Islands
            South Georgia And The South Sand
            Antarctica
            Bouvet Island
            French Southern Territories
            Heard Island& Mc Donald Island
            Aland Islands
            Guernsey
            Vatican
            Jersey
            Sao Tome And Principe
            Reunion
            British Indian Ocean Territory
            Mayotte
            Bonaire
        """
        return self.session.post(
            endpoint="user/user_register",
            data={
                "user_name": username,
                "user_password": password,
                "user_email": email,
                "user_type": user_type,
                "user_country": country,
                "agentCode": installer_code,
                "user_tel": phone_number,
                "time": time_zone,
            },
        )
