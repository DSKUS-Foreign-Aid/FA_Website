from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    korea_class = 'Korea Data'
    other_country = 'Another Countries Data'
    available_countreis = ["Argentina", "Belize", "Bolivia", "Brazil", "Chile", "Colombia",
                        "Costa Rica", "Cuba", "Ecuador", "El Salvador", "Guatemala", "Guyana",
                        "Honduras", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru",
                        "Puerto Rico", "Uruguay"]
    country_code = {
        "Africa Eastern and Southern": "AFE",
        "Afghanistan": "AFG",
        "Africa Western and Central": "AFW",
        "Angola": "AGO",
        "Albania": "ALB",
        "Arab World": "ARB",
        "United Arab Emirates": "ARE",
        "Argentina": "ARG",
        "Armenia": "ARM",
        "Antigua and Barbuda": "ATG",
        "Australia": "AUS",
        "Austria": "AUT",
        "Azerbaijan": "AZE",
        "Belgium": "BEL",
        "Benin": "BEN",
        "Burkina Faso": "BFA",
        "Bangladesh": "BGD",
        "Bahrain": "BHR",
        "Bahamas, The": "BHS",
        "Bosnia and Herzegovina": "BIH",
        "Belarus": "BLR",
        "Belize": "BLZ",
        "Bolivia": "BOL",
        "Brazil": "BRA",
        "Brunei Darussalam": "BRN",
        "Bhutan": "BTN",
        "Botswana": "BWA",
        "Central African Republic": "CAF",
        "Central Europe and the Baltics": "CEB",
        "Switzerland": "CHE",
        "Chile": "CHL",
        "China": "CHN",
        "Cote d'Ivoire": "CIV",
        "Cameroon": "CMR",
        "Congo, Dem. Rep.": "COD",
        "Colombia": "COL",
        "Cabo Verde": "CPV",
        "Costa Rica": "CRI",
        "Cuba": "CUB",
        "Curacao": "CUW",
        "Cyprus": "CYP",
        "Czech Republic": "CZE",
        "Germany": "DEU",
        "Dominica": "DMA",
        "Denmark": "DNK",
        "Dominican Republic": "DOM",
        "Algeria": "DZA",
        "East Asia & Pacific (excluding high income)": "EAP",
        "Early-demographic dividend": "EAR",
        "East Asia & Pacific": "EAS",
        "Europe & Central Asia (excluding high income)": "ECA",
        "Europe & Central Asia": "ECS",
        "Ecuador": "ECU",
        "Egypt, Arab Rep.": "EGY",
        "Euro area": "EMU",
        "Spain": "ESP",
        "Estonia": "EST",
        "Ethiopia": "ETH",
        "European Union": "EUU",
        "Finland": "FIN",
        "Fiji": "FJI",
        "France": "FRA",
        "Micronesia, Fed. Sts.": "FSM",
        "Gabon": "GAB",
        "United Kingdom": "GBR",
        "Georgia": "GEO",
        "Ghana": "GHA",
        "Guinea": "GIN",
        "Gambia, The": "GMB",
        "Equatorial Guinea": "GNQ",
        "Greece": "GRC",
        "Grenada": "GRD",
        "Guatemala": "GTM",
        "Guyana": "GUY",
        "Hong Kong SAR, China": "HKG",
        "Honduras": "HND",
        "Heavily indebted poor countries (HIPC)": "HPC",
        "Croatia": "HRV",
        "Haiti": "HTI",
        "Hungary": "HUN",
        "IBRD only": "IBD",
        "IDA & IBRD total": "IBT",
        "IDA total": "IDA",
        "IDA blend": "IDB",
        "Indonesia": "IDN",
        "IDA only": "IDX",
        "India": "IND",
        "Ireland": "IRL",
        "Iran, Islamic Rep.": "IRN",
        "Iraq": "IRQ",
        "Iceland": "ISL",
        "Israel": "ISR",
        "Italy": "ITA",
        "Jamaica": "JAM",
        "Jordan": "JOR",
        "Kazakhstan": "KAZ",
        "Kenya": "KEN",
        "Kyrgyz Republic": "KGZ",
        "Cambodia": "KHM",
        "St. Kitts and Nevis": "KNA",
        "Korea, Rep.": "KOR",
        "Kuwait": "KWT",
        "Latin America & Caribbean (excluding high income)": "LAC",
        "Lao PDR": "LAO",
        "Lebanon": "LBN",
        "St. Lucia": "LCA",
        "Latin America & Caribbean": "LCN",
        "Least developed countries: UN classification": "LDC",
        "Low income": "LIC",
        "Sri Lanka": "LKA",
        "Lower middle income": "LMC",
        "Low & middle income": "LMY",
        "Lesotho": "LSO",
        "Late-demographic dividend": "LTE",
        "Lithuania": "LTU",
        "Luxembourg": "LUX",
        "Latvia": "LVA",
        "Morocco": "MAR",
        "Moldova": "MDA",
        "Madagascar": "MDG",
        "Maldives": "MDV",
        "Middle East & North Africa": "MEA",
        "Mexico": "MEX",
        "Marshall Islands": "MHL",
        "Middle income": "MIC",
        "North Macedonia": "MKD",
        "Mali": "MLI",
        "Malta": "MLT",
        "Middle East & North Africa (excluding high income)": "MNA",
        "Montenegro": "MNE",
        "Mongolia": "MNG",
        "Mozambique": "MOZ",
        "Mauritania": "MRT",
        "Mauritius": "MUS",
        "Malaysia": "MYS",
        "Namibia": "NAM",
        "Niger": "NER",
        "Nigeria": "NGA",
        "Nicaragua": "NIC",
        "Netherlands": "NLD",
        "Norway": "NOR",
        "Nepal": "NPL",
        "Oman": "OMN",
        "Other small states": "OSS",
        "Pakistan": "PAK",
        "Panama": "PAN",
        "Peru": "PER",
        "Philippines": "PHL",
        "Palau": "PLW",
        "Poland": "POL",
        "Pre-demographic dividend": "PRE",
        "Puerto Rico": "PRI",
        "Portugal": "PRT",
        "Paraguay": "PRY",
        "Qatar": "QAT",
        "Romania": "ROU",
        "Russian Federation": "RUS",
        "Rwanda": "RWA",
        "South Asia": "SAS",
        "Saudi Arabia": "SAU",
        "Senegal": "SEN",
        "Singapore": "SGP",
        "Sierra Leone": "SLE",
        "El Salvador": "SLV",
        "Serbia": "SRB",
        "Sub-Saharan Africa (excluding high income)": "SSA",
        "Sub-Saharan Africa": "SSF",
        "Small states": "SST",
        "Sao Tome and Principe": "STP",
        "Suriname": "SUR",
        "Slovak Republic": "SVK",
        "Slovenia": "SVN",
        "Sweden": "SWE",
        "Eswatini": "SWZ",
        "Seychelles": "SYC",
        "Turks and Caicos Islands": "TCA",
        "Chad": "TCD",
        "East Asia & Pacific (IDA & IBRD countries)": "TEA",
        "Europe & Central Asia (IDA & IBRD countries)": "TEC",
        "Togo": "TGO",
        "Thailand": "THA",
        "Latin America & the Caribbean (IDA & IBRD countries)": "TLA",
        "Timor-Leste": "TLS",
        "Middle East & North Africa (IDA & IBRD countries)": "TMN",
        "Tonga": "TON",
        "South Asia (IDA & IBRD)": "TSA",
        "Sub-Saharan Africa (IDA & IBRD countries)": "TSS",
        "Tunisia": "TUN",
        "Turkey": "TUR",
        "Tanzania": "TZA",
        "Uganda": "UGA",
        "Ukraine": "UKR",
        "Upper middle income": "UMC",
        "Uruguay": "URY",
        "Uzbekistan": "UZB",
        "St. Vincent and the Grenadines": "VCT",
        "Vietnam": "VNM",
        "Samoa": "WSM",
        "Kosovo": "XKX",
        "South Africa": "ZAF",
        "Zambia": "ZMB",
        "Zimbabwe": "ZWE"}

    
    values = {'Korea': korea_class, 'Country':other_country,
              'Countries': country_code}
    return render(request, 'ClassificationApp/home.html', values)


def country(request):
    # Function to get data for country
    # enter data into classification model
    country_details = {
        "AFE": ["Africa Eastern and Southern", "Class 2", "Class 2"],
        "AFG": ["Afghanistan", "Class 1", "Class 1"],
        "AFW": ["Africa Western and Central", "Class 1", "Class 1"],
        "AGO": ["Angola", "Class 2", "Class 2"],
        "ALB": ["Albania", "Class 1", "Class 1"],
        "ARB": ["Arab World", "Class 4", "Class 3"],
        "ARE": ["United Arab Emirates", "Class 4", "Class 4"],
        "ARG": ["Argentina", "Class 4", "Class 4"],
        "ARM": ["Armenia", "Class 2", "Class 2"],
        "ATG": ["Antigua and Barbuda", "Class 4", "Class 4"],
        "AUS": ["Australia", "Class 4", "Class 4"],
        "AUT": ["Austria", "Class 4", "Class 4"],
        "AZE": ["Azerbaijan", "Class 2", "Class 2"],
        "BEL": ["Belgium", "Class 4", "Class 4"],
        "BEN": ["Benin", "Class 1", "Class 1"],
        "BFA": ["Burkina Faso", "Class 1", "Class 1"],
        "BGD": ["Bangladesh", "Class 2", "Class 2"],
        "BHR": ["Bahrain", "Class 4", "Class 4"],
        "BHS": ["Bahamas, The", "Class 4", "Class 4"],
        "BIH": ["Bosnia and Herzegovina", "Class 4", "Class 4"],
        "BLR": ["Belarus", "Class 3", "Class 3"],
        "BLZ": ["Belize", "Class 4", "Class 4"],
        "BOL": ["Bolivia", "Class 2", "Class 2"],
        "BRA": ["Brazil", "Class 4", "Class 4"],
        "BRN": ["Brunei Darussalam", "Class 3", "Class 3"],
        "BTN": ["Bhutan", "Class 1", "Class 2"],
        "BWA": ["Botswana", "Class 4", "Class 4"],
        "CAF": ["Central African Republic", "Class 1", "Class 1"],
        "CEB": ["Central Europe and the Baltics", "Class 4", "Class 4"],
        "CHE": ["Switzerland", "Class 4", "Class 4"],
        "CHL": ["Chile", "Class 4", "Class 4"],
        "CHN": ["China", "Class 4", "Class 3"],
        "CIV": ["Cote d'Ivoire", "Class 1", "Class 1"],
        "CMR": ["Cameroon", "Class 1", "Class 1"],
        "COD": ["Congo, Dem. Rep.", "Class 1", "Class 2"],
        "COL": ["Colombia", "Class 4", "Class 4"],
        "CPV": ["Cabo Verde", "Class 4", "Class 4"],
        "CRI": ["Costa Rica", "Class 4", "Class 4"],
        "CUB": ["Cuba", "Class 4", "Class 4"],
        "CUW": ["Curacao", "Class 4", "Class 4"],
        "CYP": ["Cyprus", "Class 4", "Class 4"],
        "CZE": ["Czech Republic", "Class 4", "Class 4"],
        "DEU": ["Germany", "Class 4", "Class 4"],
        "DMA": ["Dominica", "Class 1", "Class 1"],
        "DNK": ["Denmark", "Class 4", "Class 4"],
        "DOM": ["Dominican Republic", "Class 4", "Class 4"],
        "DZA": ["Algeria", "Class 2", "Class 2"],
        "EAP": ["East Asia & Pacific (excluding high income)", "Class 3", "Class 3"],
        "EAR": ["Early-demographic dividend", "Class 4", "Class 4"],
        "EAS": ["East Asia & Pacific", "Class 4", "Class 4"],
        "ECA": ["Europe & Central Asia (excluding high income)", "Class 4", "Class 4"],
        "ECS": ["Europe & Central Asia", "Class 4", "Class 4"],
        "ECU": ["Ecuador", "Class 3", "Class 3"],
        "EGY": ["Egypt, Arab Rep.", "Class 2", "Class 2"],
        "EMU": ["Euro area", "Class 4", "Class 4"],
        "ESP": ["Spain", "Class 4", "Class 4"],
        "EST": ["Estonia", "Class 4", "Class 4"],
        "ETH": ["Ethiopia", "Class 1", "Class 1"],
        "EUU": ["European Union", "Class 4", "Class 4"],
        "FIN": ["Finland", "Class 4", "Class 4"],
        "FJI": ["Fiji", "Class 2", "Class 2"],
        "FRA": ["France", "Class 4", "Class 4"],
        "FSM": ["Micronesia, Fed. Sts.", "Class 1", "Class 1"],
        "GAB": ["Gabon", "Class 3", "Class 3"],
        "GBR": ["United Kingdom", "Class 4", "Class 4"],
        "GEO": ["Georgia", "Class 4", "Class 4"],
        "GHA": ["Ghana", "Class 1", "Class 1"],
        "GIN": ["Guinea", "Class 1", "Class 1"],
        "GMB": ["Gambia, The", "Class 1", "Class 1"],
        "GNQ": ["Equatorial Guinea", "Class 3", "Class 3"],
        "GRC": ["Greece", "Class 4", "Class 4"],
        "GRD": ["Grenada", "Class 4", "Class 4"],
        "GTM": ["Guatemala", "Class 4", "Class 4"],
        "GUY": ["Guyana", "Class 1", "Class 1"],
        "HKG": ["Hong Kong SAR, China", "Class 4", "Class 4"],
        "HND": ["Honduras", "Class 4", "Class 4"],
        "HPC": ["Heavily indebted poor countries (HIPC)", "Class 1", "Class 1"],
        "HRV": ["Croatia", "Class 4", "Class 4"],
        "HTI": ["Haiti", "Class 1", "Class 1"],
        "HUN": ["Hungary", "Class 4", "Class 4"],
        "IBD": ["IBRD only", "Class 4", "Class 4"],
        "IBT": ["IDA & IBRD total", "Class 4", "Class 4"],
        "IDA": ["IDA total", "Class 1", "Class 1"],
        "IDB": ["IDA blend", "Class 1", "Class 1"],
        "IDN": ["Indonesia", "Class 2", "Class 2"],
        "IDX": ["IDA only", "Class 1", "Class 1"],
        "IND": ["India", "Class 1", "Class 1"],
        "IRL": ["Ireland", "Class 4", "Class 4"],
        "IRN": ["Iran, Islamic Rep.", "Class 3", "Class 3"],
        "IRQ": ["Iraq", "Class 3", "Class 3"],
        "ISL": ["Iceland", "Class 4", "Class 4"],
        "ISR": ["Israel", "Class 4", "Class 4"],
        "ITA": ["Italy", "Class 4", "Class 4"],
        "JAM": ["Jamaica", "Class 4", "Class 4"],
        "JOR": ["Jordan", "Class 4", "Class 4"],
        "KAZ": ["Kazakhstan", "Class 4", "Class 4"],
        "KEN": ["Kenya", "Class 1", "Class 1"],
        "KGZ": ["Kyrgyz Republic", "Class 2", "Class 2"],
        "KHM": ["Cambodia", "Class 1", "Class 1"],
        "KNA": ["St. Kitts and Nevis", "Class 4", "Class 4"],
        "KOR": ["Korea, Rep.", "Class 4", "Class 4"],
        "KWT": ["Kuwait", "Class 4", "Class 4"],
        "LAC": ["Latin America & Caribbean (excluding high income)", "Class 4", "Class 4"],
        "LAO": ["Lao PDR", "Class 1", "Class 1"],
        "LBN": ["Lebanon", "Class 4", "Class 4"],
        "LCA": ["St. Lucia", "Class 4", "Class 4"],
        "LCN": ["Latin America & Caribbean", "Class 4", "Class 4"],
        "LDC": ["Least developed countries: UN classification", "Class 1", "Class 1"],
        "LIC": ["Low income", "Class 1", "Class 1"],
        "LKA": ["Sri Lanka", "Class 4", "Class 4"],
        "LMC": ["Lower middle income", "Class 2", "Class 2"],
        "LMY": ["Low & middle income", "Class 4", "Class 3"],
        "LSO": ["Lesotho", "Class 4", "Class 4"],
        "LTE": ["Late-demographic dividend", "Class 4", "Class 4"],
        "LTU": ["Lithuania", "Class 4", "Class 4"],
        "LUX": ["Luxembourg", "Class 4", "Class 4"],
        "LVA": ["Latvia", "Class 4", "Class 4"],
        "MAR": ["Morocco", "Class 2", "Class 2"],
        "MDA": ["Moldova", "Class 2", "Class 2"],
        "MDG": ["Madagascar", "Class 1", "Class 1"],
        "MDV": ["Maldives", "Class 4", "Class 4"],
        "MEA": ["Middle East & North Africa", "Class 4", "Class 4"],
        "MEX": ["Mexico", "Class 4", "Class 4"],
        "MHL": ["Marshall Islands", "Class 1", "Class 4"],
        "MIC": ["Middle income", "Class 4", "Class 4"],
        "MKD": ["North Macedonia", "Class 4", "Class 4"],
        "MLI": ["Mali", "Class 1", "Class 1"],
        "MLT": ["Malta", "Class 4", "Class 4"],
        "MNA": ["Middle East & North Africa (excluding high income)", "Class 2", "Class 2"],
        "MNE": ["Montenegro", "Class 4", "Class 4"],
        "MNG": ["Mongolia", "Class 2", "Class 2"],
        "MOZ": ["Mozambique", "Class 1", "Class 1"],
        "MRT": ["Mauritania", "Class 1", "Class 1"],
        "MUS": ["Mauritius", "Class 4", "Class 4"],
        "MYS": ["Malaysia", "Class 4", "Class 3"],
        "NAM": ["Namibia", "Class 4", "Class 4"],
        "NER": ["Niger", "Class 1", "Class 1"],
        "NGA": ["Nigeria", "Class 1", "Class 1"],
        "NIC": ["Nicaragua", "Class 1", "Class 2"],
        "NLD": ["Netherlands", "Class 4", "Class 4"],
        "NOR": ["Norway", "Class 4", "Class 4"],
        "NPL": ["Nepal", "Class 1", "Class 1"],
        "OMN": ["Oman", "Class 3", "Class 3"],
        "OSS": ["Other small states", "Class 4", "Class 4"],
        "PAK": ["Pakistan", "Class 1", "Class 1"],
        "PAN": ["Panama", "Class 4", "Class 4"],
        "PER": ["Peru", "Class 4", "Class 4"],
        "PHL": ["Philippines", "Class 4", "Class 4"],
        "PLW": ["Palau", "Class 4", "Class 4"],
        "POL": ["Poland", "Class 4", "Class 4"],
        "PRE": ["Pre-demographic dividend", "Class 1", "Class 1"],
        "PRI": ["Puerto Rico", "Class 3", "Class 3"],
        "PRT": ["Portugal", "Class 4", "Class 4"],
        "PRY": ["Paraguay", "Class 2", "Class 2"],
        "QAT": ["Qatar", "Class 3", "Class 3"],
        "ROU": ["Romania", "Class 4", "Class 4"],
        "RUS": ["Russian Federation", "Class 4", "Class 4"],
        "RWA": ["Rwanda", "Class 1", "Class 1"],
        "SAS": ["South Asia", "Class 1", "Class 1"],
        "SAU": ["Saudi Arabia", "Class 4", "Class 3"],
        "SEN": ["Senegal", "Class 1", "Class 2"],
        "SGP": ["Singapore", "Class 4", "Class 4"],
        "SLE": ["Sierra Leone", "Class 1", "Class 1"],
        "SLV": ["El Salvador", "Class 4", "Class 4"],
        "SRB": ["Serbia", "Class 4", "Class 4"],
        "SSA": ["Sub-Saharan Africa (excluding high income)", "Class 1", "Class 1"],
        "SSF": ["Sub-Saharan Africa", "Class 1", "Class 1"],
        "SST": ["Small states", "Class 4", "Class 4"],
        "STP": ["Sao Tome and Principe", "Class 4", "Class 4"],
        "SUR": ["Suriname", "Class 3", "Class 3"],
        "SVK": ["Slovak Republic", "Class 4", "Class 4"],
        "SVN": ["Slovenia", "Class 4", "Class 4"],
        "SWE": ["Sweden", "Class 4", "Class 4"],
        "SWZ": ["Eswatini", "Class 4", "Class 3"],
        "SYC": ["Seychelles", "Class 4", "Class 4"],
        "TCA": ["Turks and Caicos Islands", "Class 4", "Class 4"],
        "TCD": ["Chad", "Class 1", "Class 1"],
        "TEA": ["East Asia & Pacific (IDA & IBRD countries)", "Class 3", "Class 3"],
        "TEC": ["Europe & Central Asia (IDA & IBRD countries)", "Class 4", "Class 4"],
        "TGO": ["Togo", "Class 1", "Class 1"],
        "THA": ["Thailand", "Class 4", "Class 4"],
        "TLA": ["Latin America & the Caribbean (IDA & IBRD countries)", "Class 4", "Class 4"],
        "TLS": ["Timor-Leste", "Class 1", "Class 1"],
        "TMN": ["Middle East & North Africa (IDA & IBRD countries)", "Class 2", "Class 2"],
        "TON": ["Tonga", "Class 1", "Class 1"],
        "TSA": ["South Asia (IDA & IBRD)", "Class 1", "Class 1"],
        "TSS": ["Sub-Saharan Africa (IDA & IBRD countries)", "Class 1", "Class 1"],
        "TUN": ["Tunisia", "Class 4", "Class 4"],
        "TUR": ["Turkey", "Class 4", "Class 4"],
        "TZA": ["Tanzania", "Class 1", "Class 1"],
        "UGA": ["Uganda", "Class 1", "Class 1"],
        "UKR": ["Ukraine", "Class 4", "Class 2"],
        "UMC": ["Upper middle income", "Class 4", "Class 4"],
        "URY": ["Uruguay", "Class 4", "Class 4"],
        "UZB": ["Uzbekistan", "Class 1", "Class 1"],
        "VCT": ["St. Vincent and the Grenadines", "Class 4", "Class 4"],
        "VNM": ["Vietnam", "Class 2", "Class 2"],
        "WSM": ["Samoa", "Class 4", "Class 4"],
        "XKX": ["Kosovo", "Class 2", "Class 2"],
        "ZAF": ["South Africa", "Class 4", "Class 4"],
        "ZMB": ["Zambia", "Class 4", "Class 4"],
        "ZWE": ["Zimbabwe", "Class 3", "Class 4"],
    }
    # this line is for me to change what page is returned when I'm working on templates.
    selected_country_code = str(request.GET.get('Country'))
    selected_country = country_details[selected_country_code][0]
    year1 = country_details[selected_country_code][1]
    year5 = country_details[selected_country_code][2]
    choice = 1
    if choice:
        return render(request,
                      'ClassificationApp/country_classification.html',
                      {'selected_country': selected_country,
                       'year1': year1,
                       'year5': year5})
    else:
        return render(request,
                      'ClassificationApp/country_classification.html',
                      {'selected_country': selected_country})