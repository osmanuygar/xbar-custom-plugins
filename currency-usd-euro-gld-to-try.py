import warnings
import requests

warnings.filterwarnings("ignore")

GREEN = "\033[0;32m"
RED = "\033[0;31m"
WHITE = "\033[0;37m"
END = "\033[0m"


def _print(name, item):
    value = round(item["ALIS"], 2)

    if item["YUZDEDEGISIM"] > 0:
        icon = "▲️"
        color = GREEN
    else:
        icon = "▼"
        color = RED

    print(f"{WHITE}{name}{END} {color}{icon} {value}{END}|terminal=false refresh=false")


response = requests.get("https://api.bigpara.hurriyet.com.tr/doviz/headerlist/anasayfa", verify=False)
data = response.json().get("data")
dollar = next(filter(lambda it: it["SEMBOL"] == "USDTRY", data))
euro = next(filter(lambda it: it["SEMBOL"] == "EURTRY", data))
gold = next(filter(lambda it: it["SEMBOL"] == "GLDGR", data))

image = "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAA4FJREFUOE+dlG1MU2cUx//3vaWl1Qk2TkAzcIRAlc" \
        "J4UyquxAZpxBEFQfyAQKqLC7CNrVFnhlEDis6okWRDgmIMZkhiZuIisADyYW71y3z5INH4QUFxlQr2hdtb7t1aA7YViXg+3vPc3/Oc8z/n" \
        "T+AD4nClMsmURn6xKoY+ReSPTQQiiHnw0gCkAGjLTaat2k/olaZ05qEhhTlNMuJ54vOXL32s+QB/BnANQGzxWvbLk7sVcSWHHUiLp7E0gh" \
        "yp1TijiXqI8wE2AOgC8E25kVtXnMMt0cVRWLyAxKGLbuR9xm3LqLZ3zAWkshOprYtU5A6Gxgq7E6p/Hk6pPYJE7Nsml+qK5KSvROuQF42X" \
        "3MhLZdw78xTa2YDEQiW5e00iXVWZzyWuW8nQLdcmkatjkBxL4+zvk2i7zqNzfzg+XkTiXDeP7bmcH6pWSiWhQIVGTbacsyj0xlQ2alqwG3" \
        "cEXP1TQHgYAYYCdm2UoabZif1lclzo5e3W+97nw2PSg3uPvDsCgUykmmy3nlEZoiOpxaHqPx0TIUnwv8oXdoeEwh9fIVvLFDZ0uK5Mn58B" \
        "cjTq+k6oKjI+ZRICYb8OeHBryIsFSgIFWSySllMz6e9bXDi2U55FrB+7GQTUxVGVBh373dGqsPhAWNegB26PhPx0FuYTDlywKCHn3hRlOe" \
        "tCU4VsFbHBfjsQqN1bKus/WK74KLTMi3/wiNGQ0CcxOH7Zjc16Dss1r0v2hf+FZsVSwmgbCQQqdLH0b2dqlAkZ8dQSX8LNSzjfw8NskmFP" \
        "qwsbM1ks05CIiiBBBHS9ttnpOaWblPsGOrSHbJmBu9VuUWp9iSc2Ee09PPaWyv1CVP3kQOu3yre2tPjQxFDXoBDUppn7VifS3b1HVOs55v" \
        "Un/dfjaKhUYGE4gWOdbrTVBQMfPxenjJaJ5qGRqepZzSE9js4qyGZ795TKw15MSBi4LWDYJoIXJJQbZYhQB4/s9kbH3Y4+Ph/A43e6zabV" \
        "dOdXBWFbDDpmThPqtgrPypscraPj4g+hB0M3hSjK4fpzk+m1VRtkQQJM/zh4Rxgva3R0D9vEEuCNGG8NduBNNYWyA09sYq0pnVXptTSiIi" \
        "n/ytX94rx7acDT/+yFWAtgarYy3uk29fUgR/+WVdy8L5hNmWyK/ZX4b9t13uzicXWufryPHxKZCfS+0XH89WjE2zNnc/9P/gfD2CiBwhFS" \
        "TwAAAABJRU5ErkJggg=="

print(f"|image={image}")
print("---")
_print("USD    ", dollar)
_print("EUR      ", euro)
_print("GOLD      ", gold)