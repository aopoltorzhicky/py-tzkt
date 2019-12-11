import requests

class TzKTException(Exception):
    pass

class TzKT:
    def __init__(self, base_url='https://api.tzkt.io', version=1):
        self._url = f'{base_url}/v{version}'

    def _request(self, method, **kwargs):
        data = {key: value for key, value in kwargs.items() if value is not None}
        url = "{}/{}".format(self._url, method)

        try:
            response = requests.get(url, params=data, timeout=10)
        except requests.Timeout:
            raise TzKTException('TzKT timeout')
        except requests.ConnectionError:
            raise TzKTException('Seems like dns lookup failed..')
        except requests.HTTPError as err:
            raise TzKTException('HTTP Error occured: {}'.format(err))
        except requests.RequestException as e:
            raise TzKTException(e)

        if response.status_code != 200:
            raise TzKTException('TzKT invalid status code: {}'.format(response.text))

        return response.json()
    
    ### Accounts

    def get_accounts(self, page=None, limit=None):
        return self._request(f'accounts', p=page, n=limit)
    
    def get_account(self, address: str):
        return  self._request(f'accounts/{address}')
    
    def get_account_profile(self, address: str):
        return  self._request(f'accounts/{address}/profile')
    
    def get_account_contracts(self, address: str, page=None, limit=None):
        return  self._request(f'accounts/{address}/contracts', p=page, n=limit)
    
    def get_account_delegators(self, address: str, page=None, limit=None):
        return  self._request(f'accounts/{address}/delegators', p=page, n=limit)
    
    def get_account_operations(self, address: str, operation_type=None, last_id=None, limit=None, sort=1):
        return  self._request(f'accounts/{address}/operations', **{
            'type': operation_type,
            'lastId': last_id,
            'limit': limit,
            'sort': sort
        })
    
    ### Blocks
    
    def get_block(self, level: int, operations=False):
        return  self._request(f'blocks/{level}', operations=operations)
    
    def get_block_by_hash(self, block_hash: int, operations=False):
        return  self._request(f'blocks/{block_hash}', operations=operations)
    
    def get_blocks(self, page=None, limit=None):
        return self._request(f'blocks', p=page, n=limit)
    
    ### Head
    
    def get_head(self):
        return self._request(f'head')
    
    ### Operations
    
    def get_operations(self, operation_type: str, page=None, limit=None):
        return self._request(f'operations/{operation_type}', p=page, n=limit)
    
    def get_operations_count(self, operation_type: str, op_hash: str):
        return self._request(f'operations/{operation_type}/count')
    
    def get_operations_by_hash(self, operation_type: str, op_hash: str):
        return self._request(f'operations/{operation_type}/{op_hash}')

    def get_operations_by_hash_and_counter(self, op_hash: str, counter: int):
        return self._request(f'operations/{op_hash}/{counter}')
    
    def get_operations_by_hash_and_counter_and_nonce(self, op_hash: str, counter: int, nonce: int):
        return self._request(f'operations/{op_hash}/{counter}/{nonce}')
    
    ### Protocols
    
    def get_protocol(self, code: int):
        return self._request(f'protocols/{code}')
    
    def get_protocol_by_hash(self, protocol_hash: str):
        return self._request(f'protocols/{protocol_hash}')
    
    def get_protocols(self, page=None, limit=None):
        return self._request(f'protocols', p=page, n=limit)
    

    ### Voting
    
    def get_voting_proposal(self, proposal_hash: str):
        return self._request(f'voting/proposals/{proposal_hash}')
    
    def get_voting_proposals(self, page=None, limit=None):
        return self._request(f'voting/proposals', p=page, n=limit)
    
    def get_voting_period(self, page=None, limit=None):
        return self._request(f'voting/periods', p=page, n=limit)
