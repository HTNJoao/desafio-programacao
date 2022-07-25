import json


pessoas=[   
	{
		"nome": "Victor Bento Bryan Caldeira",
		"idade": 71,
		"cpf": "461.002.215-00",
		"rg": "15.195.291-7",
		"data_nasc": "10/02/1951",
		"sexo": "Masculino",
		"signo": "Aquário",
		"mae": "Jennifer Marlene Nina",
		"pai": "Leandro Daniel Noah Caldeira",
		"email": "victorbentocaldeira@tasaut.com.br",
		"senha": "bumGNkkg9U",
		"cep": "72503-511",
		"endereco": "Quadra QR 203 Conjunto K",
		"numero": 777,
		"bairro": "Santa Maria",
		"cidade": "Brasília",
		"estado": "DF",
		"telefone_fixo": "(61) 2601-0841",
		"celular": "(61) 99368-8932",
		"altura": "1,83",
		"peso": 77,
		"tipo_sanguineo": "O+",
		"cor": "roxo"
	},
	{
		"nome": "Elaine Rafaela da Cunha",
		"idade": 44,
		"cpf": "139.266.781-00",
		"rg": "30.566.211-9",
		"data_nasc": "08/04/1978",
		"sexo": "Feminino",
		"signo": "Áries",
		"mae": "Evelyn Tereza Fátima",
		"pai": "Heitor Enzo da Cunha",
		"email": "elaine_rafaela_dacunha@manjubinhafilmes.com.br",
		"senha": "QmfNwmA6w2",
		"cep": "79093-100",
		"endereco": "Rua Ceará",
		"numero": 810,
		"bairro": "Jardim São Conrado",
		"cidade": "Campo Grande",
		"estado": "MS",
		"telefone_fixo": "(67) 3699-8137",
		"celular": "(67) 98276-0504",
		"altura": "1,79",
		"peso": 70,
		"tipo_sanguineo": "B+",
		"cor": "preto"
	},
	{
		"nome": "Agatha Alícia Rosângela da Conceição",
		"idade": 52,
		"cpf": "683.530.916-40",
		"rg": "30.386.165-4",
		"data_nasc": "20/04/1970",
		"sexo": "Feminino",
		"signo": "Áries",
		"mae": "Fabiana Rebeca",
		"pai": "Mário Mário Cauã da Conceição",
		"email": "agatha-daconceicao91@teadit.com.br",
		"senha": "HGOeKtsMem",
		"cep": "69317-561",
		"endereco": "Rua R-24",
		"numero": 112,
		"bairro": "Cidade Satélite",
		"cidade": "Boa Vista",
		"estado": "RR",
		"telefone_fixo": "(95) 2682-9712",
		"celular": "(95) 98405-0435",
		"altura": "1,75",
		"peso": 48,
		"tipo_sanguineo": "AB-",
		"cor": "amarelo"
	},
	{
		"nome": "Jaqueline Tânia Vanessa Viana",
		"idade": 74,
		"cpf": "032.191.202-02",
		"rg": "20.277.663-3",
		"data_nasc": "08/01/1948",
		"sexo": "Feminino",
		"signo": "Capricórnio",
		"mae": "Beatriz Nair Liz",
		"pai": "Diogo Kauê Luiz Viana",
		"email": "jaqueline.tania.viana@folha.com.br",
		"senha": "nTA9tJXfaa",
		"cep": "29312-095",
		"endereco": "Rua Raul Luiz de Souza",
		"numero": 376,
		"bairro": "Monte Cristo",
		"cidade": "Cachoeiro de Itapemirim",
		"estado": "ES",
		"telefone_fixo": "(28) 2512-9680",
		"celular": "(28) 98698-5356",
		"altura": "1,75",
		"peso": 74,
		"tipo_sanguineo": "AB+",
		"cor": "verde"
	},
	{
		"nome": "Luzia Sueli Luiza da Mata",
		"idade": 28,
		"cpf": "610.945.493-12",
		"rg": "18.130.943-9",
		"data_nasc": "19/01/1994",
		"sexo": "Feminino",
		"signo": "Capricórnio",
		"mae": "Luana Priscila",
		"pai": "Giovanni Renato Heitor da Mata",
		"email": "luzia.sueli.damata@kascher.com.br",
		"senha": "njGkXyd5Ck",
		"cep": "78068-435",
		"endereco": "Rua Dezesseis",
		"numero": 684,
		"bairro": "Boa Esperança",
		"cidade": "Cuiabá",
		"estado": "MT",
		"telefone_fixo": "(65) 2656-0213",
		"celular": "(65) 98758-1907",
		"altura": "1,60",
		"peso": 57,
		"tipo_sanguineo": "A+",
		"cor": "vermelho"
	},
	{
		"nome": "Luís Levi Pedro Mendes",
		"idade": 52,
		"cpf": "105.633.991-80",
		"rg": "44.814.459-1",
		"data_nasc": "06/05/1970",
		"sexo": "Masculino",
		"signo": "Touro",
		"mae": "Clarice Helena",
		"pai": "Gabriel Ricardo Henrique Mendes",
		"email": "luis.levi.mendes@jci.com",
		"senha": "cFH39mwIFR",
		"cep": "55194-100",
		"endereco": "Rua Capitão Pedrosa",
		"numero": 334,
		"bairro": "São Cristovão",
		"cidade": "Santa Cruz do Capibaribe",
		"estado": "PE",
		"telefone_fixo": "(81) 3832-1382",
		"celular": "(81) 98222-8624",
		"altura": "1,66",
		"peso": 67,
		"tipo_sanguineo": "AB+",
		"cor": "vermelho"
	},
	{
		"nome": "Maria Mariana Adriana da Luz",
		"idade": 56,
		"cpf": "397.153.990-45",
		"rg": "46.339.758-7",
		"data_nasc": "27/03/1966",
		"sexo": "Feminino",
		"signo": "Áries",
		"mae": "Heloisa Letícia Sophie",
		"pai": "Alexandre Sérgio da Luz",
		"email": "mariamarianadaluz@arecocomercial.com.br",
		"senha": "aCF3WWiL4i",
		"cep": "58801-670",
		"endereco": "Avenida Angelim",
		"numero": 333,
		"bairro": "Angelim",
		"cidade": "Sousa",
		"estado": "PB",
		"telefone_fixo": "(83) 3999-3800",
		"celular": "(83) 99254-3539",
		"altura": "1,85",
		"peso": 54,
		"tipo_sanguineo": "A-",
		"cor": "azul"
	},
	{
		"nome": "Augusto Rodrigo Assunção",
		"idade": 78,
		"cpf": "685.654.735-89",
		"rg": "48.408.164-0",
		"data_nasc": "01/06/1944",
		"sexo": "Masculino",
		"signo": "Gêmeos",
		"mae": "Mariana Julia Eliane",
		"pai": "Mateus Enrico Elias Assunção",
		"email": "augusto.rodrigo.assuncao@daou.com.br",
		"senha": "uLsJS3DZwy",
		"cep": "31842-683",
		"endereco": "Rua Flor Azul",
		"numero": 881,
		"bairro": "Tupi B",
		"cidade": "Belo Horizonte",
		"estado": "MG",
		"telefone_fixo": "(31) 2891-5659",
		"celular": "(31) 99298-2569",
		"altura": "1,63",
		"peso": 101,
		"tipo_sanguineo": "AB-",
		"cor": "vermelho"
	},
	{
		"nome": "Rafaela Josefa Simone Sales",
		"idade": 24,
		"cpf": "279.304.710-47",
		"rg": "20.579.684-9",
		"data_nasc": "07/07/1998",
		"sexo": "Feminino",
		"signo": "Câncer",
		"mae": "Márcia Rayssa",
		"pai": "Tomás Erick Breno Sales",
		"email": "rafaela_sales@montcalm.com.br",
		"senha": "PgR2de9P44",
		"cep": "12232-869",
		"endereco": "Avenida Sete",
		"numero": 413,
		"bairro": "Conjunto Residencial Dom Pedro II",
		"cidade": "São José dos Campos",
		"estado": "SP",
		"telefone_fixo": "(12) 3917-3522",
		"celular": "(12) 98420-2774",
		"altura": "1,57",
		"peso": 72,
		"tipo_sanguineo": "A+",
		"cor": "laranja"
	},
	{
		"nome": "Nair Lorena Analu Cavalcanti",
		"idade": 44,
		"cpf": "141.824.673-53",
		"rg": "16.913.291-2",
		"data_nasc": "13/07/1978",
		"sexo": "Feminino",
		"signo": "Câncer",
		"mae": "Stefany Carla Bruna",
		"pai": "Caio Elias Breno Cavalcanti",
		"email": "nair_lorena_cavalcanti@dc4.com.br",
		"senha": "K07X6QAZjc",
		"cep": "49032-060",
		"endereco": "Rua Tenente Aragão",
		"numero": 711,
		"bairro": "Farolândia",
		"cidade": "Aracaju",
		"estado": "SE",
		"telefone_fixo": "(79) 3872-6478",
		"celular": "(79) 99402-2198",
		"altura": "1,77",
		"peso": 50,
		"tipo_sanguineo": "AB-",
		"cor": "preto"
	},
	{
		"nome": "Anderson Juan Rodrigo Barros",
		"idade": 36,
		"cpf": "359.100.371-96",
		"rg": "29.787.865-7",
		"data_nasc": "20/02/1986",
		"sexo": "Masculino",
		"signo": "Peixes",
		"mae": "Marli Hadassa Sophia",
		"pai": "Leandro Igor Fábio Barros",
		"email": "andersonjuanbarros@openlink.com.br",
		"senha": "ljFi6UzwXx",
		"cep": "76813-431",
		"endereco": "Rua Anchieta",
		"numero": 561,
		"bairro": "São Francisco",
		"cidade": "Porto Velho",
		"estado": "RO",
		"telefone_fixo": "(69) 3664-3646",
		"celular": "(69) 99575-2110",
		"altura": "1,85",
		"peso": 68,
		"tipo_sanguineo": "AB+",
		"cor": "vermelho"
	},
	{
		"nome": "Camila Francisca Rocha",
		"idade": 77,
		"cpf": "546.502.409-72",
		"rg": "50.720.771-3",
		"data_nasc": "12/01/1945",
		"sexo": "Feminino",
		"signo": "Capricórnio",
		"mae": "Clarice Eduarda Sônia",
		"pai": "Nathan Luiz Rocha",
		"email": "camila_francisca_rocha@lta-am.com.br",
		"senha": "TuzxjKxn4D",
		"cep": "77817-170",
		"endereco": "Alameda das Perdizes",
		"numero": 748,
		"bairro": "Jardim Esplanada",
		"cidade": "Araguaína",
		"estado": "TO",
		"telefone_fixo": "(63) 3950-2123",
		"celular": "(63) 98669-3030",
		"altura": "1,58",
		"peso": 48,
		"tipo_sanguineo": "AB+",
		"cor": "amarelo"
	},
	{
		"nome": "Evelyn Stefany Mariah Drumond",
		"idade": 53,
		"cpf": "425.951.786-44",
		"rg": "31.658.456-3",
		"data_nasc": "12/02/1969",
		"sexo": "Feminino",
		"signo": "Aquário",
		"mae": "Alícia Emanuelly",
		"pai": "Caleb Fernando Bernardo Drumond",
		"email": "evelyn.stefany.drumond@termakui.com.br",
		"senha": "6oJaniLBjG",
		"cep": "70686-450",
		"endereco": "Quadra SQNW 109 Bloco J",
		"numero": 783,
		"bairro": "Setor Noroeste",
		"cidade": "Brasília",
		"estado": "DF",
		"telefone_fixo": "(61) 2953-4869",
		"celular": "(61) 99984-3703",
		"altura": "1,61",
		"peso": 61,
		"tipo_sanguineo": "O-",
		"cor": "azul"
	},
	{
		"nome": "Alícia Bruna Teixeira",
		"idade": 80,
		"cpf": "436.472.707-50",
		"rg": "22.029.540-2",
		"data_nasc": "06/02/1942",
		"sexo": "Feminino",
		"signo": "Aquário",
		"mae": "Carolina Simone",
		"pai": "Benjamin Calebe Teixeira",
		"email": "alicia_bruna_teixeira@kaynak.com.br",
		"senha": "XhnCDDMYLu",
		"cep": "88706-216",
		"endereco": "Rua Manoel Jovito Cardoso",
		"numero": 710,
		"bairro": "Passo do Gado",
		"cidade": "Tubarão",
		"estado": "SC",
		"telefone_fixo": "(48) 2795-2919",
		"celular": "(48) 98888-5706",
		"altura": "1,85",
		"peso": 84,
		"tipo_sanguineo": "AB+",
		"cor": "amarelo"
	},
	{
		"nome": "Pietro Guilherme Isaac Cardoso",
		"idade": 75,
		"cpf": "851.476.975-86",
		"rg": "40.746.843-2",
		"data_nasc": "11/07/1947",
		"sexo": "Masculino",
		"signo": "Câncer",
		"mae": "Gabrielly Heloisa Manuela",
		"pai": "César Danilo Cardoso",
		"email": "pietro-cardoso81@mpcnet.com.br",
		"senha": "kc67bK65J9",
		"cep": "64010-380",
		"endereco": "Quadra Mocambinho - Setor E",
		"numero": 752,
		"bairro": "Mocambinho",
		"cidade": "Teresina",
		"estado": "PI",
		"telefone_fixo": "(86) 3812-9551",
		"celular": "(86) 98404-2867",
		"altura": "1,88",
		"peso": 57,
		"tipo_sanguineo": "A+",
		"cor": "azul"
	},
	{
		"nome": "Tereza Luzia Gomes",
		"idade": 44,
		"cpf": "799.079.114-53",
		"rg": "30.157.525-3",
		"data_nasc": "04/07/1978",
		"sexo": "Feminino",
		"signo": "Câncer",
		"mae": "Eliane Yasmin Raquel",
		"pai": "Nicolas Fernando Jorge Gomes",
		"email": "tereza_gomes@ohms.com.br",
		"senha": "wcusgqI4mM",
		"cep": "78158-181",
		"endereco": "Rua São Fábio",
		"numero": 186,
		"bairro": "Jardim dos Estados",
		"cidade": "Várzea Grande",
		"estado": "MT",
		"telefone_fixo": "(65) 3595-5302",
		"celular": "(65) 99490-7807",
		"altura": "1,77",
		"peso": 78,
		"tipo_sanguineo": "B-",
		"cor": "azul"
	},
	{
		"nome": "Nina Sônia Campos",
		"idade": 24,
		"cpf": "485.327.812-50",
		"rg": "48.367.603-2",
		"data_nasc": "22/01/1998",
		"sexo": "Feminino",
		"signo": "Aquário",
		"mae": "Andrea Caroline Sophia",
		"pai": "Giovanni Lorenzo Martin Campos",
		"email": "nina_sonia_campos@ipk.org.br",
		"senha": "uRds3swA1k",
		"cep": "49025-310",
		"endereco": "Rua Humberto Pinto do Valle",
		"numero": 536,
		"bairro": "Grageru",
		"cidade": "Aracaju",
		"estado": "SE",
		"telefone_fixo": "(79) 2807-4377",
		"celular": "(79) 98712-3262",
		"altura": "1,63",
		"peso": 84,
		"tipo_sanguineo": "O+",
		"cor": "azul"
	},
	{
		"nome": "Sueli Eliane Baptista",
		"idade": 45,
		"cpf": "665.268.851-44",
		"rg": "38.551.909-6",
		"data_nasc": "26/03/1977",
		"sexo": "Feminino",
		"signo": "Áries",
		"mae": "Rita Emanuelly Raimunda",
		"pai": "Benício Cláudio Renan Baptista",
		"email": "sueli.eliane.baptista@papayacomunicacao.com.br",
		"senha": "MsNpToGBwt",
		"cep": "59150-660",
		"endereco": "Rua Pau-Brasil",
		"numero": 674,
		"bairro": "Nova Parnamirim",
		"cidade": "Parnamirim",
		"estado": "RN",
		"telefone_fixo": "(84) 2536-2888",
		"celular": "(84) 98562-7733",
		"altura": "1,71",
		"peso": 50,
		"tipo_sanguineo": "A-",
		"cor": "amarelo"
	},
	{
		"nome": "Martin Kauê Daniel da Silva",
		"idade": 68,
		"cpf": "979.875.325-92",
		"rg": "47.450.002-0",
		"data_nasc": "22/02/1954",
		"sexo": "Masculino",
		"signo": "Peixes",
		"mae": "Pietra Stella Julia",
		"pai": "Luiz Davi da Silva",
		"email": "martinkauedasilva@tita.com.br",
		"senha": "MMrQ6WIpjp",
		"cep": "77826-662",
		"endereco": "Rua D",
		"numero": 518,
		"bairro": "Morada do Sol 3",
		"cidade": "Araguaína",
		"estado": "TO",
		"telefone_fixo": "(63) 3516-7511",
		"celular": "(63) 98534-9385",
		"altura": "1,68",
		"peso": 60,
		"tipo_sanguineo": "A-",
		"cor": "azul"
	},
	{
		"nome": "Luan Sebastião Antonio Lima",
		"idade": 31,
		"cpf": "567.485.621-47",
		"rg": "20.729.239-5",
		"data_nasc": "08/05/1991",
		"sexo": "Masculino",
		"signo": "Touro",
		"mae": "Sara Valentina Marli",
		"pai": "Benício Bruno Emanuel Lima",
		"email": "luan.sebastiao.lima@senioraereo.com.br",
		"senha": "5SayAWaJBJ",
		"cep": "08625-585",
		"endereco": "Rua Cosmo Vieira da Silva",
		"numero": 131,
		"bairro": "Vila Rica",
		"cidade": "Suzano",
		"estado": "SP",
		"telefone_fixo": "(11) 2719-0758",
		"celular": "(11) 99428-9190",
		"altura": "1,82",
		"peso": 92,
		"tipo_sanguineo": "O-",
		"cor": "vermelho"
	},
	{
		"nome": "Ruan Tomás Almeida",
		"idade": 64,
		"cpf": "244.049.030-06",
		"rg": "20.218.574-6",
		"data_nasc": "02/04/1958",
		"sexo": "Masculino",
		"signo": "Áries",
		"mae": "Antonella Heloisa",
		"pai": "Gustavo Danilo Almeida",
		"email": "ruan.tomas.almeida@avantii.com.br",
		"senha": "xjAEcYqdAs",
		"cep": "76804-330",
		"endereco": "Rua Tenreiro Aranha",
		"numero": 236,
		"bairro": "Areal",
		"cidade": "Porto Velho",
		"estado": "RO",
		"telefone_fixo": "(69) 2965-6256",
		"celular": "(69) 98309-8591",
		"altura": "1,92",
		"peso": 88,
		"tipo_sanguineo": "B+",
		"cor": "laranja"
	},
	{
		"nome": "Ruan Caleb Nicolas Oliveira",
		"idade": 38,
		"cpf": "594.534.566-08",
		"rg": "18.787.298-3",
		"data_nasc": "11/04/1984",
		"sexo": "Masculino",
		"signo": "Áries",
		"mae": "Beatriz Elisa",
		"pai": "Marcos Anderson Filipe Oliveira",
		"email": "ruancaleboliveira@coeducar.com.br",
		"senha": "fF5jKhWmLW",
		"cep": "75709-652",
		"endereco": "Rua VB 8",
		"numero": 469,
		"bairro": "Residencial Vereda dos Buritis",
		"cidade": "Catalão",
		"estado": "GO",
		"telefone_fixo": "(64) 2949-7824",
		"celular": "(64) 98792-2037",
		"altura": "1,75",
		"peso": 52,
		"tipo_sanguineo": "O-",
		"cor": "laranja"
	},
	{
		"nome": "Gabriela Jennifer Fátima Duarte",
		"idade": 39,
		"cpf": "017.124.028-62",
		"rg": "28.625.449-9",
		"data_nasc": "02/05/1983",
		"sexo": "Feminino",
		"signo": "Touro",
		"mae": "Luiza Maitê Eliane",
		"pai": "Diego Julio Duarte",
		"email": "gabriela_duarte@megapremiumvip.com",
		"senha": "1kDEE11Y7z",
		"cep": "58433-175",
		"endereco": "Rua Vila Velha",
		"numero": 591,
		"bairro": "Malvinas",
		"cidade": "Campina Grande",
		"estado": "PB",
		"telefone_fixo": "(83) 2904-4228",
		"celular": "(83) 99576-9722",
		"altura": "1,65",
		"peso": 82,
		"tipo_sanguineo": "AB+",
		"cor": "roxo"
	},
	{
		"nome": "César Kevin Raul da Rosa",
		"idade": 80,
		"cpf": "512.709.092-90",
		"rg": "22.249.267-3",
		"data_nasc": "18/02/1942",
		"sexo": "Masculino",
		"signo": "Aquário",
		"mae": "Rosa Helena Sarah",
		"pai": "Calebe Carlos Lorenzo da Rosa",
		"email": "cesar.kevin.darosa@kof.com.mx",
		"senha": "xRr1HNc8iW",
		"cep": "58394-970",
		"endereco": "Praça José Amâncio Ramalho 06",
		"numero": 663,
		"bairro": "Centro",
		"cidade": "Borborema",
		"estado": "PB",
		"telefone_fixo": "(83) 3517-8693",
		"celular": "(83) 98424-7033",
		"altura": "1,95",
		"peso": 90,
		"tipo_sanguineo": "B+",
		"cor": "azul"
	},
	{
		"nome": "Hadassa Alessandra Louise Melo",
		"idade": 21,
		"cpf": "207.676.355-40",
		"rg": "38.479.692-8",
		"data_nasc": "10/06/2001",
		"sexo": "Feminino",
		"signo": "Gêmeos",
		"mae": "Malu Jéssica",
		"pai": "Bryan Bruno Melo",
		"email": "hadassa-melo79@akaer.com.br",
		"senha": "et5FcUhKGw",
		"cep": "64845-970",
		"endereco": "Praça Dirno Pires Ferreira 261",
		"numero": 270,
		"bairro": "Centro",
		"cidade": "Marcos Parente",
		"estado": "PI",
		"telefone_fixo": "(89) 3523-6829",
		"celular": "(89) 98764-2132",
		"altura": "1,73",
		"peso": 49,
		"tipo_sanguineo": "B+",
		"cor": "amarelo"
	},
	{
		"nome": "Fátima Sabrina Martins",
		"idade": 33,
		"cpf": "357.527.993-41",
		"rg": "16.330.991-7",
		"data_nasc": "22/05/1989",
		"sexo": "Feminino",
		"signo": "Gêmeos",
		"mae": "Luna Agatha Mariah",
		"pai": "Gael Gustavo Pietro Martins",
		"email": "fatima_sabrina_martins@amure.com.br",
		"senha": "z3mKJYno47",
		"cep": "89202-201",
		"endereco": "Rua Rio do Sul",
		"numero": 296,
		"bairro": "Bucarein",
		"cidade": "Joinville",
		"estado": "SC",
		"telefone_fixo": "(47) 3501-8228",
		"celular": "(47) 99854-5079",
		"altura": "1,65",
		"peso": 55,
		"tipo_sanguineo": "O-",
		"cor": "verde"
	},
	{
		"nome": "Luna Laís Manuela Moraes",
		"idade": 30,
		"cpf": "578.089.994-07",
		"rg": "50.073.718-6",
		"data_nasc": "04/07/1992",
		"sexo": "Feminino",
		"signo": "Câncer",
		"mae": "Marli Malu Giovanna",
		"pai": "Raul José Moraes",
		"email": "luna_lais_moraes@plaman.com.br",
		"senha": "jALJULXj8r",
		"cep": "79062-222",
		"endereco": "Rua Marcílio Gasparine",
		"numero": 103,
		"bairro": "Jardim Indianápolis",
		"cidade": "Campo Grande",
		"estado": "MS",
		"telefone_fixo": "(67) 2613-5958",
		"celular": "(67) 98158-4191",
		"altura": "1,66",
		"peso": 69,
		"tipo_sanguineo": "A-",
		"cor": "vermelho"
	},
	{
		"nome": "Fabiana Amanda Clarice da Mota",
		"idade": 52,
		"cpf": "684.242.150-01",
		"rg": "27.758.522-3",
		"data_nasc": "17/02/1970",
		"sexo": "Feminino",
		"signo": "Aquário",
		"mae": "Elaine Ana Luna",
		"pai": "Marcelo João Gael da Mota",
		"email": "fabiana-damota86@rebecacometerra.com.br",
		"senha": "YZu3E3t6lm",
		"cep": "65908-701",
		"endereco": "Rua Poços de Caldas",
		"numero": 953,
		"bairro": "Jardim Camboriú",
		"cidade": "Imperatriz",
		"estado": "MA",
		"telefone_fixo": "(98) 2822-2368",
		"celular": "(98) 98593-4682",
		"altura": "1,72",
		"peso": 78,
		"tipo_sanguineo": "O+",
		"cor": "azul"
	},
	{
		"nome": "Allana Evelyn Betina Silveira",
		"idade": 54,
		"cpf": "907.244.082-07",
		"rg": "23.924.390-0",
		"data_nasc": "22/04/1968",
		"sexo": "Feminino",
		"signo": "Touro",
		"mae": "Stefany Marina",
		"pai": "Victor João Caleb Silveira",
		"email": "allana_evelyn_silveira@reginfo.com.br",
		"senha": "wQRitHFgfA",
		"cep": "40325-825",
		"endereco": "Vila Brasil",
		"numero": 876,
		"bairro": "Liberdade",
		"cidade": "Salvador",
		"estado": "BA",
		"telefone_fixo": "(71) 2854-0761",
		"celular": "(71) 99608-7128",
		"altura": "1,81",
		"peso": 69,
		"tipo_sanguineo": "B+",
		"cor": "vermelho"
	},
	{
		"nome": "Márcio Henry da Cruz",
		"idade": 52,
		"cpf": "383.394.382-39",
		"rg": "36.151.318-5",
		"data_nasc": "08/06/1970",
		"sexo": "Masculino",
		"signo": "Gêmeos",
		"mae": "Flávia Eduarda",
		"pai": "Erick Lorenzo Fernando da Cruz",
		"email": "marcio.henry.dacruz@fk1.com.br",
		"senha": "KDGzRDABce",
		"cep": "87055-490",
		"endereco": "Rua Pioneiro Elias Martins",
		"numero": 928,
		"bairro": "Conjunto Habitacional Sol Nascente",
		"cidade": "Maringá",
		"estado": "PR",
		"telefone_fixo": "(44) 3616-2156",
		"celular": "(44) 99514-9123",
		"altura": "1,75",
		"peso": 105,
		"tipo_sanguineo": "A-",
		"cor": "amarelo"
	}
]

gentes=json.loads(pessoas)
print(type(pessoas))
print(type(gentes))
print(gentes)
