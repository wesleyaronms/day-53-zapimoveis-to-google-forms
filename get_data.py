import requests
from bs4 import BeautifulSoup


# A página de busca do ZapImóveis da qual irá coletar os dados.
URL = "https://www.zapimoveis.com.br/aluguel/casas-de-condominio/sp+sao-paulo+zona-norte/?onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Paulo,Zona%20Norte,,,,,BR%3ESao%20Paulo%3ENULL%3ESao%20Paulo%3EZona%20Norte,-23.555771,-46.639557,&transacao=Aluguel&tipoUnidade=Residencial,Casa%20de%20Condom%C3%ADnio&tipo=Im%C3%B3vel%20usado&pagina=1"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}


class GetData:
    def __init__(self):
        """Contém quatro atributos, cada qual com uma lista de preços, detalhes,
        endereços e links de cada imóvel para alugar encontrado."""
        response = requests.get(url=URL, headers=header)
        response.raise_for_status()
        soup = BeautifulSoup(markup=response.text, features="html.parser")
        self.prices = [" ".join(price.text.split()) for price in
                       soup.find_all(name="p", class_="simple-card__price")]

        self.details = [" ".join(detail.text.split()[:-1]) for detail in
                        soup.find_all(name="div", class_="simple-card__description")]

        self.address = [" ".join(address.text.split()).split("m²")[0] + "m²" for address in
                        soup.find_all(name="div", class_="simple-card__actions")]

        self.links = [f"https://www.zapimoveis.com.br/imovel/{ids['data-id']}/" for ids in
                      soup.find_all(name="div", class_="card-container")]
