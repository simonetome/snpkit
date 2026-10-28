from .api_client import BaseAPIClient

import numpy as np
import polars as pl

class ExPhewasClient(BaseAPIClient):

    base_url = "https://exphewas.ca/v1/api/"

    def _repeat_for_list(self, url, repeated_elem_key, repeated_elem, fixed_params={}):
        """
        If the API  call requires a single parameter and the user insert a list, just call 
        the API n times
        """
        results = [
            self._get(
                url, 
                params={repeated_elem_key: x} | fixed_params
            )
            for x in repeated_elem
        ]
        
        temp = [item 
                for raw in results 
                for item in raw['data'] if raw['paging_info']['totalNumberOfItems'] != 0]

        # return only non empty 
        return temp

    def get_assoc_by_gene(self, genes):

        # TODO check the gene is in ENS format 
        # TODO now its a single gene only, extend for a list and return a dictionary of results 
        raw = self._get(
            self.base_url+'gene/'+genes+"/results", 
            params={
            }
        )

        print(raw)
        return self.parse(raw)

    def parse(self, raw):
        return pl.DataFrame(raw)

