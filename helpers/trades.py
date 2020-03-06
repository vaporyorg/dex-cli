import click

from constants import SEPARATOR

# Trade entity fields
#   See https://thegraph.com/explorer/subgraph/gnosis/dfusion
TRADE_FIELDS = '''\
  owner { id}
  order { orderId }
  sellVolume
  buyVolume
  txHash
  tradeBatchId\
'''

def toTradeDto(trade):
  return {
    "owner_address": trade['owner']['id'],
    "order_id": trade['order']['orderId'],
    "tradeBatchId": trade['tradeBatchId'],
    "sellVolume": trade['sellVolume'],
    "buyVolume": trade['buyVolume'],
    "txHash": trade['txHash']
  }

def print_trades_pretty(trades):
  click.echo(click.style(SEPARATOR, fg='red'))

  for trade in trades:
    click.echo(
      click.style('  Trader', fg='green') + ':' + 
      trade['owner_address'] + '\n' + 

      click.style('  Order Id', fg='green') + ': ' + 
      str(trade['order_id']) + '\n' + 

      click.style('  Batch Id', fg='green') + ': ' + 
      str(trade['tradeBatchId']) + '\n' + 

      click.style('  Batch Id', fg='green') + ': ' + 
      str(trade['tradeBatchId']) + '\n' + 

      click.style('  Sell volume', fg='green') + ': ' + 
      str(trade['sellVolume']) + '\n' + 

      click.style('  Buy volume', fg='green') + ': ' + 
      str(trade['sellVolume']) + '\n' + 

      click.style(SEPARATOR, fg='red')
    )

def print_trades_csv(trade):
  click.echo("Not implemented yet")