#!/usr/bin/env bash

WHITE="\033[0;37m"
RED="\e[1;31m"
GREEN="\e[1;32m"
BLUE="\e[1;34m"
END="\e[0m"

jq(){
    /usr/local/bin/jq "$@"
}

currency(){
    print(){
        name=$1
        changes=$(echo $2 | jq '.YUZDEDEGISIM')
        value=$(echo $2 | jq '.ALIS')

        if [[ ${changes} > 0 ]]; then
            printf "${WHITE}%-30s\t${GREEN}%.2f\t▲️${END}\n" "${name}" $value
        else
            printf "${WHITE}%-30s\t${RED}%.2f\t▼${END}\n" "${name}" $value
        fi
    }

    url="https://api.bigpara.hurriyet.com.tr/doviz/headerlist/anasayfa"
    data=$(curl -s -f -k "${url}" | jq '.data' | jq '.[]')
    usd=$(echo "${data}" | jq 'select(.SEMBOL =="USDTRY")')
    euro=$(echo "${data}" | jq 'select(.SEMBOL =="EURTRY")')
    gold=$(echo "${data}" | jq 'select(.SEMBOL =="GLDGR")')
    print "DOLAR" "${usd}"
    print "EURO" "${euro}"
    print "ALTIN" "${gold}"
}

fuel(){
    response=$(curl -sL "https://api.opet.com.tr/api/fuelprices/prices?ProvinceCode=34")
    products=$(echo $response | jq '.[] | select(.districtCode == "034005") | .prices')
    for row in $(echo "${products}" | jq -r '.[] | @base64') ; do
        row=$(echo "$row" | base64 --decode)
        name=$(echo $row | jq -r '.productName')
        amount=$(echo $row | jq -r '.amount')

        printf "${WHITE}%-20s\t${BLUE}%.2f${END}\n" "${name}" $amount
    done
}


echo "🔘"
echo "---"
echo ":chart_with_upwards_trend: Borsa"
echo "---"
currency
echo "---"
echo ":fuelpump: Akaryakıt Fiyatları"
echo "---"
fuel
echo "---"
echo "↻ Refresh | refresh=true | key=CmdOrCtrl+r"
