pokemons = {
    'Charmander': {
        'stage': '1',
        'tipo': 'fogo',
        'evoluções': {
            'charmilion': {
                'stage': '2',
                'tipo': 'fogo',
                'evoluções': {
                    'charizard': {
                        'stage': '3',
                        'tipo': 'fogo/voador',
                    },
                },
            },
        },
    },
}

pesquisa = str(input('Qual pokemon gostaria de saber mais sobre? '))
if pesquisa in pokemons:
   print(f"{pesquisa} é um pokemon no estágio {pokemons[pesquisa]['stage']}")
   for pokemon2, dados_pokemon2 in pokemons[pesquisa]['evoluções'].items():
       print(f"{pokemon2} é evolução de {pesquisa} e é estágio {dados_pokemon2['stage']}")
       for pokemon3, dados_pokemon3 in dados_pokemon2['evoluções'].items():
           print(f"{pokemon3} é evolução de {pokemon2} e é estágio {dados_pokemon3['stage']}")