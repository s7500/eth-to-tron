def get_last_network_block(network):
    network.network_type == 'tron'
    last_block_networks = {
        'ethereum': (network.w3.eth.block_number - network.confirmation_blocks),
        
        'tron': (
            network.get_block_data('latest')['number'] - network.confirmation_blocks
            )
    }
    return last_block_networks[network.network_type]


def get_event_data(network, last_block_checked, last_block_network, event):
    if network.network_type == 'ethereum':
        event_filter = event.createFilter(
            fromBlock=last_block_checked, toBlock=last_block_network
        )
        events= event_filter.get_all_entries()
        
    elif network.network_type == 'tron':
        url = \
        f'{network.endpoint}/v1/contracts/{network.swap_address}/events?event_name={event}' \
                      f'&min_block_timestamp={last_block_checked["timestamp"]}' \
                      f'&max_block_timestamp={last_block_network["timestamp"]}'
        events = requests.get(url).json()['data']
    return events


def get_block_data(network, identifer):
    if network.network_type == 'tron':
        return network.tron.trx.get_block(identifer)['block_header']['raw_data']
