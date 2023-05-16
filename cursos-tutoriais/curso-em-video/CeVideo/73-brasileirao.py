
times = "inter", "gremio", "flamengo", "flminense", "cruzeiro", "palmeiras", "sao paulo",\
    "santos", "goias", 'parana', "atleticoMg", "botafogo", "bragantino", "coritiba",\
    "ceara", "juventude", "AVAI", "atloticoGo", "CUIABA", "corintians"

print(f"Os cinco primeiros são: {times[:6]}")
print(f"Os quatro ultimos sao : {times[-4:]}")
print(sorted(times))
print(f' o time inter esta na posiçao {times.index("inter")+1}')
