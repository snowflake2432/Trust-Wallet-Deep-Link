import qrcode
import tkinter as tk

win = tk.Tk()
##############################################
# Variable
coin = {'Bitcoin': {'coin': '0', 'symbol': 'BTC', 'logo': ''}, 'Litecoin': {'coin': '2', 'symbol': 'LTC', 'logo': ''},
        'Dogecoin': {'coin': '3', 'symbol': 'DOGE', 'logo': ''}, 'Dash': {'coin': '5', 'symbol': 'DASH', 'logo': ''},
        'Viacoin': {'coin': '14', 'symbol': 'VIA', 'logo': ''},
        'Groestlcoin': {'coin': '17', 'symbol': 'GRS', 'logo': ''},
        'DigiByte': {'coin': '20', 'symbol': 'DGB', 'logo': ''},
        'Monacoin': {'coin': '22', 'symbol': 'MONA', 'logo': ''}, 'Decred': {'coin': '42', 'symbol': 'DCR', 'logo': ''},
        'Syscoin': {'coin': '57', 'symbol': 'SYS', 'logo': ''}, 'Ethereum': {'coin': '60', 'symbol': 'ETH', 'logo': ''},
        'Ethereum Classic': {'coin': '61', 'symbol': 'ETC', 'logo': ''},
        'ICON': {'coin': '74', 'symbol': 'ICX', 'logo': ''}, 'Verge': {'coin': '77', 'symbol': 'XVG', 'logo': ''},
        'Cosmos Hub': {'coin': '118', 'symbol': 'ATOM', 'logo': ''},
        'Pivx': {'coin': '119', 'symbol': 'PIVX', 'logo': ''}, 'Zen': {'coin': '121', 'symbol': 'ZEN', 'logo': ''},
        'Zcash': {'coin': '133', 'symbol': 'ZEC', 'logo': ''}, 'Firo': {'coin': '136', 'symbol': 'FIRO', 'logo': ''},
        'Rootstock': {'coin': '137', 'symbol': 'RBTC', 'logo': ''},
        'Komodo': {'coin': '141', 'symbol': 'KMD', 'logo': ''}, 'XRP': {'coin': '144', 'symbol': 'XRP', 'logo': ''},
        'Bitcoin Cash': {'coin': '145', 'symbol': 'BCH', 'logo': ''},
        'Nebl': {'coin': '146', 'symbol': 'NEBL', 'logo': ''}, 'Stellar': {'coin': '148', 'symbol': 'XLM', 'logo': ''},
        'Bitcoin Gold': {'coin': '156', 'symbol': 'BTG', 'logo': ''},
        'Nano': {'coin': '165', 'symbol': 'XNO', 'logo': ''},
        'Manta Pacific': {'coin': '169', 'symbol': 'ETH', 'logo': ''},
        'Ravencoin': {'coin': '175', 'symbol': 'RVN', 'logo': ''},
        'POA Network': {'coin': '178', 'symbol': 'POA', 'logo': ''},
        'EOS': {'coin': '194', 'symbol': 'EOS', 'logo': ''}, 'Tron': {'coin': '195', 'symbol': 'TRX', 'logo': ''},
        'OpBNB': {'coin': '204', 'symbol': 'BNB', 'logo': ''},
        'Internet Computer': {'coin': '223', 'symbol': 'ICP', 'logo': ''},
        'FIO': {'coin': '235', 'symbol': 'FIO', 'logo': ''}, 'Nimiq': {'coin': '242', 'symbol': 'NIM', 'logo': ''},
        'Algorand': {'coin': '283', 'symbol': 'ALGO', 'logo': ''},
        'IOST': {'coin': '291', 'symbol': 'IOST', 'logo': ''}, 'IoTeX': {'coin': '304', 'symbol': 'IOTX', 'logo': ''},
        'Nervos': {'coin': '309', 'symbol': 'CKB', 'logo': ''}, 'Zilliqa': {'coin': '313', 'symbol': 'ZIL', 'logo': ''},
        'Terra Classic': {'coin': '330', 'symbol': 'LUNC', 'logo': ''},
        'Polkadot': {'coin': '354', 'symbol': 'DOT', 'logo': ''},
        'Theta Fuel': {'coin': '361', 'symbol': 'TFUEL', 'logo': ''},
        'Crypto.org': {'coin': '394', 'symbol': 'CRO', 'logo': ''},
        'Everscale': {'coin': '396', 'symbol': 'EVER', 'logo': ''},
        'NEAR': {'coin': '397', 'symbol': 'NEAR', 'logo': ''}, 'Aion': {'coin': '425', 'symbol': 'AION', 'logo': ''},
        'Kusama': {'coin': '434', 'symbol': 'KSM', 'logo': ''},
        'Aeternity': {'coin': '457', 'symbol': 'AE', 'logo': ''}, 'Kava': {'coin': '459', 'symbol': 'KAVA', 'logo': ''},
        'Filecoin': {'coin': '461', 'symbol': 'FIL', 'logo': ''},
        'Oasis': {'coin': '474', 'symbol': 'ROSE', 'logo': ''},
        'Bluzelle': {'coin': '483', 'symbol': 'BLZ', 'logo': ''},
        'BandChain': {'coin': '494', 'symbol': 'BAND', 'logo': ''},
        'Theta': {'coin': '500', 'symbol': 'THETA', 'logo': ''}, 'Solana': {'coin': '501', 'symbol': 'SOL', 'logo': ''},
        'MultiversX': {'coin': '508', 'symbol': 'eGLD', 'logo': ''},
        'Secret': {'coin': '529', 'symbol': 'SCRT', 'logo': ''}, 'Agoric': {'coin': '564', 'symbol': 'BLD', 'logo': ''},
        'TON': {'coin': '607', 'symbol': 'TON', 'logo': ''}, 'Aptos': {'coin': '637', 'symbol': 'APT', 'logo': ''},
        'BNB Beacon Chain': {'coin': '714', 'symbol': 'BNB', 'logo': ''},
        'Sui': {'coin': '784', 'symbol': 'SUI', 'logo': ''}, 'Acala': {'coin': '787', 'symbol': 'ACA', 'logo': ''},
        'VeChain': {'coin': '818', 'symbol': 'VET', 'logo': ''},
        'Callisto': {'coin': '820', 'symbol': 'CLO', 'logo': ''}, 'NEO': {'coin': '888', 'symbol': 'NEO', 'logo': ''},
        'Viction': {'coin': '889', 'symbol': 'VIC', 'logo': ''}, 'eCash': {'coin': '899', 'symbol': 'XEC', 'logo': ''},
        'THORChain': {'coin': '931', 'symbol': 'RUNE', 'logo': ''},
        'Polygon': {'coin': '966', 'symbol': 'MATIC', 'logo': ''},
        'OKX Chain': {'coin': '996', 'symbol': 'OKT', 'logo': ''},
        'Bitcoin Diamond': {'coin': '999', 'symbol': 'BCD', 'logo': ''},
        'ThunderCore': {'coin': '1001', 'symbol': 'TT', 'logo': ''},
        'Harmony': {'coin': '1023', 'symbol': 'ONE', 'logo': ''},
        'Ontology': {'coin': '1024', 'symbol': 'ONT', 'logo': ''},
        'Conflux eSpace': {'coin': '1030', 'symbol': 'CFX', 'logo': ''},
        'Tezos': {'coin': '1729', 'symbol': 'XTZ', 'logo': ''},
        'Cardano': {'coin': '1815', 'symbol': 'ADA', 'logo': ''},
        'Qtum': {'coin': '2301', 'symbol': 'QTUM', 'logo': ''},
        'Nebulas': {'coin': '2718', 'symbol': 'NAS', 'logo': ''},
        'Hedera': {'coin': '3030', 'symbol': 'HBAR', 'logo': ''},
        'Mantle': {'coin': '5000', 'symbol': 'MNT', 'logo': ''},
        'BNB Greenfield': {'coin': '5600', 'symbol': 'BNB', 'logo': ''},
        'GoChain': {'coin': '6060', 'symbol': 'GO', 'logo': ''},
        'Zen EON': {'coin': '7332', 'symbol': 'ZEN', 'logo': ''}, 'Base': {'coin': '8453', 'symbol': 'ETH', 'logo': ''},
        'NULS': {'coin': '8964', 'symbol': 'NULS', 'logo': ''}, 'WAX': {'coin': '14001', 'symbol': 'WAXP', 'logo': ''},
        'Meter': {'coin': '18000', 'symbol': 'MTR', 'logo': ''},
        'Flux': {'coin': '19167', 'symbol': 'FLUX', 'logo': ''},
        'Celo': {'coin': '52752', 'symbol': 'CELO', 'logo': ''},
        'Linea': {'coin': '59144', 'symbol': 'ETH', 'logo': ''},
        'Stratis': {'coin': '105105', 'symbol': 'STRAX', 'logo': ''},
        'Scroll': {'coin': '534352', 'symbol': 'ETH', 'logo': ''},
        'Wanchain': {'coin': '5718350', 'symbol': 'WAN', 'logo': ''},
        'Waves': {'coin': '5741564', 'symbol': 'WAVES', 'logo': ''},
        'Cronos Chain': {'coin': '10000025', 'symbol': 'CRO', 'logo': ''},
        'Native Injective': {'coin': '10000060', 'symbol': 'INJ', 'logo': ''},
        'Optimism Ethereum': {'coin': '10000070', 'symbol': 'ETH', 'logo': ''},
        'Gnosis Chain': {'coin': '10000100', 'symbol': 'xDAI', 'logo': ''},
        'Osmosis': {'coin': '10000118', 'symbol': 'OSMO', 'logo': ''},
        'Smart Bitcoin Cash': {'coin': '10000145', 'symbol': 'BCH', 'logo': ''},
        'Fantom': {'coin': '10000250', 'symbol': 'FTM', 'logo': ''},
        'Boba': {'coin': '10000288', 'symbol': 'BOBAETH', 'logo': ''},
        'KuCoin Community Chain': {'coin': '10000321', 'symbol': 'KCS', 'logo': ''},
        'zkSync Era': {'coin': '10000324', 'symbol': 'ETH', 'logo': ''},
        'Terra': {'coin': '10000330', 'symbol': 'LUNA', 'logo': ''},
        'Huobi ECO Chain': {'coin': '10000553', 'symbol': 'HT', 'logo': ''},
        'Acala EVM': {'coin': '10000787', 'symbol': 'ACA', 'logo': ''},
        'Coreum': {'coin': '10000990', 'symbol': 'CORE', 'logo': ''},
        'Metis': {'coin': '10001088', 'symbol': 'METIS', 'logo': ''},
        'Polygon zkEVM': {'coin': '10001101', 'symbol': 'ETH', 'logo': ''},
        'Moonbeam': {'coin': '10001284', 'symbol': 'GLMR', 'logo': ''},
        'Moonriver': {'coin': '10001285', 'symbol': 'MOVR', 'logo': ''},
        'Ronin': {'coin': '10002020', 'symbol': 'RON', 'logo': ''},
        'KavaEvm': {'coin': '10002222', 'symbol': 'KAVA', 'logo': ''},
        'IoTeX EVM': {'coin': '10004689', 'symbol': 'IOTX', 'logo': ''},
        'NativeZetaChain': {'coin': '10007000', 'symbol': 'ZETA', 'logo': ''},
        'NativeCanto': {'coin': '10007700', 'symbol': 'CANTO', 'logo': ''},
        'Klaytn': {'coin': '10008217', 'symbol': 'KLAY', 'logo': ''},
        'Avalanche C-Chain': {'coin': '10009000', 'symbol': 'AVAX', 'logo': ''},
        'Evmos': {'coin': '10009001', 'symbol': 'EVMOS', 'logo': ''},
        'Arbitrum Nova': {'coin': '10042170', 'symbol': 'ETH', 'logo': ''},
        'Arbitrum': {'coin': '10042221', 'symbol': 'ETH', 'logo': ''},
        'Sommelier': {'coin': '11000118', 'symbol': 'SOMM', 'logo': ''},
        'Fetch AI': {'coin': '12000118', 'symbol': 'FET', 'logo': ''},
        'Mars Hub': {'coin': '13000118', 'symbol': 'MARS', 'logo': ''},
        'Umee': {'coin': '14000118', 'symbol': 'UMEE', 'logo': ''},
        'Quasar': {'coin': '15000118', 'symbol': 'QSR', 'logo': ''},
        'Persistence': {'coin': '16000118', 'symbol': 'XPRT', 'logo': ''},
        'Akash': {'coin': '17000118', 'symbol': 'AKT', 'logo': ''},
        'Noble': {'coin': '18000118', 'symbol': 'USDC', 'logo': ''},
        'Sei': {'coin': '19000118', 'symbol': 'SEI', 'logo': ''},
        'Stargaze': {'coin': '20000118', 'symbol': 'STARS', 'logo': ''},
        'BNB Smart Chain': {'coin': '20000714', 'symbol': 'BNB', 'logo': ''},
        'Zeta EVM': {'coin': '20007000', 'symbol': 'ZETA', 'logo': ''},
        'Native Evmos': {'coin': '20009001', 'symbol': 'EVMOS', 'logo': ''},
        'Celestia': {'coin': '21000118', 'symbol': 'TIA', 'logo': ''},
        'dYdX': {'coin': '22000118', 'symbol': 'DYDX', 'logo': ''},
        'Juno': {'coin': '30000118', 'symbol': 'JUNO', 'logo': ''},
        'TBNB': {'coin': '30000714', 'symbol': 'BNB', 'logo': ''},
        'Stride': {'coin': '40000118', 'symbol': 'STRD', 'logo': ''},
        'Axelar': {'coin': '50000118', 'symbol': 'AXL', 'logo': ''},
        'Crescent': {'coin': '60000118', 'symbol': 'CRE', 'logo': ''},
        'Kujira': {'coin': '70000118', 'symbol': 'KUJI', 'logo': ''},
        'Comdex': {'coin': '80000118', 'symbol': 'CMDX', 'logo': ''},
        'Neutron': {'coin': '90000118', 'symbol': 'NTRN', 'logo': ''},
        'Neon': {'coin': '245022934', 'symbol': 'NEON', 'logo': ''},
        'Aurora': {'coin': '1323161554', 'symbol': 'ETH', 'logo': ''}}


##############################################
##############################################
# Functions
def UAI(network, token):
    if token == "":
        return f"c{network}"
    else:
        return f"c{network}_t{token}"


def generate(asset, addr, amount):
    img = qrcode.make(
        f'trust://send?asset={asset}&address={addr}&amount={amount}')
    type(img)  # qrcode.image.pil.PilImage
    img.save("./some_file.png")


#####################################################


win.geometry("215x260")
label1 = tk.Label(win, text='Trust Wallet Deep Link', font=("Arial", 20)).grid(column=0, row=0)
label2 = tk.Label(win, text='Choose Network:', font=("Arial", 15)).grid(column=0, row=4)

choosed = tk.StringVar()
network_list = (
    'Bitcoin', 'Litecoin', 'Dogecoin', 'Dash', 'Viacoin', 'Groestlcoin', 'DigiByte', 'Monacoin', 'Decred', 'Syscoin',
    'Ethereum', 'Ethereum Classic', 'ICON', 'Verge', 'Cosmos Hub', 'Pivx', 'Zen', 'Zcash', 'Firo', 'Rootstock',
    'Komodo',
    'XRP', 'Bitcoin Cash', 'Nebl', 'Stellar', 'Bitcoin Gold', 'Nano', 'Manta Pacific', 'Ravencoin', 'POA Network',
    'EOS',
    'Tron', 'OpBNB', 'Internet Computer', 'FIO', 'Nimiq', 'Algorand', 'IOST', 'IoTeX', 'Nervos', 'Zilliqa',
    'Terra Classic',
    'Polkadot', 'Theta Fuel', 'Crypto.org', 'Everscale', 'NEAR', 'Aion', 'Kusama', 'Aeternity', 'Kava', 'Filecoin',
    'Oasis',
    'Bluzelle', 'BandChain', 'Theta', 'Solana', 'MultiversX', 'Secret', 'Agoric', 'TON', 'Aptos', 'BNB Beacon Chain',
    'Sui',
    'Acala', 'VeChain', 'Callisto', 'NEO', 'Viction', 'eCash', 'THORChain', 'Polygon', 'OKX Chain', 'Bitcoin Diamond',
    'ThunderCore', 'Harmony', 'Ontology', 'Conflux eSpace', 'Tezos', 'Cardano', 'Qtum', 'Nebulas', 'Hedera', 'Mantle',
    'BNB Greenfield', 'GoChain', 'Zen EON', 'Base', 'NULS', 'WAX', 'Meter', 'Flux', 'Celo', 'Linea', 'Stratis',
    'Scroll',
    'Wanchain', 'Waves', 'Cronos Chain', 'Native Injective', 'Optimism Ethereum', 'Gnosis Chain', 'Osmosis',
    'Smart Bitcoin Cash', 'Fantom', 'Boba', 'KuCoin Community Chain', 'zkSync Era', 'Terra', 'Huobi ECO Chain',
    'Acala EVM',
    'Coreum', 'Metis', 'Polygon zkEVM', 'Moonbeam', 'Moonriver', 'Ronin', 'KavaEvm', 'IoTeX EVM', 'NativeZetaChain',
    'NativeCanto', 'Klaytn', 'Avalanche C-Chain', 'Evmos', 'Arbitrum Nova', 'Arbitrum', 'Sommelier', 'Fetch AI',
    'Mars Hub',
    'Umee', 'Quasar', 'Persistence', 'Akash', 'Noble', 'Sei', 'Stargaze', 'BNB Smart Chain', 'Zeta EVM', 'Native Evmos',
    'Celestia', 'dYdX', 'Juno', 'TBNB', 'Stride', 'Axelar', 'Crescent', 'Kujira', 'Comdex', 'Neutron', 'Neon', 'Aurora')
network = tk.OptionMenu(win, choosed, *network_list)
network.grid(column=0, row=5)
choose_tokens = tk.Label(win, text='Enter Token:', font=("Arial", 15)).grid(column=0, row=6)
toke = tk.Entry(win)
toke.grid(column=0, row=7)

enter_address = tk.Label(win, text='Enter address', font=("Arial", 15)).grid(column=0, row=8)
address = tk.Entry(win)
address.grid(column=0, row=9)

enter_amount = tk.Label(win, text='Enter amount', font=("Arial", 15)).grid(column=0, row=10)
amounts = tk.Entry(win)
amounts.grid(column=0, row=11)


def execute():
    chain = coin[choosed.get()]['coin']
    tok = toke.get()
    asset = UAI(chain, tok)
    addresses = address.get()
    amount = amounts.get()
    generate(asset, addresses, amount)


button = tk.Button(win, text='Generate', command=execute).grid(column=0, row=12)

win.mainloop()
