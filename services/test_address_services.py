from services.district_service import (
    match_district_en
)

from services.commune_service import (
    match_commune_en
)

from services.village_service import (
    match_village_en
)

print(
    match_district_en(
        "DANGKA0"
    )
)

print(
    match_commune_en(
        "CHEUNG AEK"
    )
)

print(
    match_village_en(
        "PREK TA K0NG"
    )
)